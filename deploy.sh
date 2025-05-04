#! /bin/bash

pasta_servidor=/home/ec2-user/gfc_app
nome_image=gfcapp

log() {
  echo -e "\033[0;34m[GFC_DEPLOY]\033[0m $1"
}


try
  log "Iniciando deploy...."

  log "Removendo arqivos de builds anteriores..."
  rm -f *.tar *.gz

  log "Verificando se tem arquivo pendente..."
  arquivos_mod=$(git status -s)
  if [ -n "$arquivos_mod" ]; then
    log "O deploy foi finalizado com erro. Existe modificações não comitadas"
    exit
  fi

  log "Verificando se está na branch main..."
  current_branch=$(git branch --show-current)
  if [ "$current_branch" != "main" ]; then
    log "Alterando para branch principal"
    git checkout main
  fi

  log "Baixando versão mais recente do repositório"
  git pull

  log "Verificando se tem conflitos..."
  arquivos_mod=$(git status -s)
  if [ -n "$arquivos_mod" ]; then
    log "O deploy foi finalizado. Existem conflitos para resolver ou arquivos para comitar"
    exit
  fi

  log "Preparando versão..."
  imagem_atual=$(cat docker-compose.yml | grep "image: ${nome_image}" | awk '{print $2}')
  IFS=':' read -r -a imgVersao <<< "$imagem_atual"
  versao_atual=${imgVersao[1]}
  IFS='.' read -r -a semver <<< "$versao_atual"
  versao_build=$(( semver[3] + 1))
  semver[3]=$versao_build
  nova_versao=$(IFS=. ; echo "${semver[*]}")
  nome_arquivo="${nome_image}_${nova_versao}.tar"

  log "Alterando versão do deploy no docker-compose"
  sed -i "s/image: ${imagem_atual}/image: gfcapp:${nova_versao}/" docker-compose.yml

  log "Alterado Versao Atual: ${versao_atual} para Nova versão: ${nova_versao}"

  log "Removendo imagem antiga"
  docker rmi "${imagem_atual}"

  log "Iniciando build da aplicação"
  docker-compose build app

  log "Salvando cópia da imagem... Aguarde alguns minutos..."
  docker save gfcapp -o "${nome_arquivo}"

  log "Tamanho da imagem antes da compactação..."
  du -hs "${nome_arquivo}"

  log "Aguarde, comprimindo o arquivo..."
  gzip -v "${nome_arquivo}"

  log "Tamanho da imagem após a compactação..."
  du -hs "${nome_arquivo}.gz"

  log "Enviando imagem para o servidor"
  scp -i "chavegfc.pem" "${nome_arquivo}.gz" ec2-user@ec2-100-28-173-23.compute-1.amazonaws.com:${pasta_servidor}

  log "Descompactando imagem no servidor...."
  ssh -i "chavegfc.pem" ec2-user@ec2-100-28-173-23.compute-1.amazonaws.com "cd ${pasta_servidor} && gzip -vd ${nome_arquivo}.gz"

  log "Carregando para o docker do servidor a nova imagem. Aguarde alguns minutos..."
  ssh -i "chavegfc.pem" ec2-user@ec2-100-28-173-23.compute-1.amazonaws.com "cd ${pasta_servidor} && docker load < ${nome_arquivo}"

  log "Removendo imagem antiga da aplicação no servidor"
  ssh -i "chavegfc.pem" ec2-user@ec2-100-28-173-23.compute-1.amazonaws.com "docker rmi ${imagem_atual}"

  log "Removendo arquivos de configuração do servidor"
  ssh -i "chavegfc.pem" ec2-user@ec2-100-28-173-23.compute-1.amazonaws.com "cd ${pasta_servidor} && rm -f docker-compose.yml gunicorn_config.py nginx.conf"

  log "Enviando novos arquivos de configuração para o servidor"
  scp -i "chavegfc.pem" docker-compose.yml gunicorn_config.py nginx.conf ec2-user@ec2-100-28-173-23.compute-1.amazonaws.com:${pasta_servidor}

  log "Parando os containers no servidor"
  ssh -i "chavegfc.pem" ec2-user@ec2-100-28-173-23.compute-1.amazonaws.com "cd ${pasta_servidor} && docker-compose down"

  log "Recriando os containers no servidor"
  ssh -i "chavegfc.pem" ec2-user@ec2-100-28-173-23.compute-1.amazonaws.com "cd ${pasta_servidor} && docker-compose up -d"

  log "Deletando imagem do diretório do servidor"
  ssh -i "chavegfc.pem" ec2-user@ec2-100-28-173-23.compute-1.amazonaws.com "cd ${pasta_servidor} && rm -f ${nome_arquivo} ${nome_arquivo}.gz"

  log "Deletando imagem salva no diretório local"
  rm -f "${nome_arquivo}" "${nome_arquivo}.gz"

  log "Removendo imagem nova do docker local"
  docker rmi "${nome_image}:${nova_versao}"

  log "Enviando alteração da versão da aplicação para o repositório"
  git add docker-compose.yml
  git commit -m "Novo deploy versao: ${nova_versao}"
  git push

  log "Criando tag da versão..."
  git tag -a v"${nova_versao}" -m "Nova versão da aplicação v${nova_versao}"
  git push --tags

  log "Deploy concluído!"
catch
  log "Erro no processo de deploy. Desfazendo processo..."

  log "Removendo arquivos compactados da imagem..."
  rm -f "${nome_arquivo}" "${nome_arquivo}.gz"

  log "Removendo imagem nova do docker..."
  docker rmi "${nome_image}:${nova_versao}"

  log "Desfazendo versão do compose..."
  git checkout docker-compose.yml

  log "Deploy desfeito!"
