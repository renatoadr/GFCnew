#! /bin/bash

pasta_servidor=/home/ec2-user/gfc_app
nome_image=gfcapp
server_connect=ec2-user@100.28.173.23
path_chave=chavegfc.pem

log() {
  echo -e "\033[0;34m[GFC_DEPLOY]\033[0m $1"
}

ecSrCom() {
  ssh -i "${path_chave}" "${server_connect}" "$1"
}

clear_stage() {
  log "Removendo arquivos compactados da imagem..."
  rm -f *.tar *.gz

  log "Desfazendo versão do compose..."
  git checkout docker-compose.yml

  log "Removendo imagem local"
  images=$(docker images -q "$nome_image")
  if [ -z "$images" ]; then
    log "Não há imagens para remover"
  else
    docker rmi -f "$images"
  fi
}

handle_error() {
  local exit_code=$?
  log "Erro no processo de deploy. Desfazendo processo..."
  log "Removendo arquivos compactados da imagem..."
  rm -f *.tar *.gz

  clear_stage

  log "Deploy desfeito!"
  exit $exit_code
}

if [ "$1" == "-r" ]; then
  log "Realizando a limpeza do stage...."

  clear_stage

  log "Reiniciado o fluxo de deploy!"
  exit 0
fi

trap 'handle_error' ERR

log "Iniciando deploy...."

log "Verificando se tem arquivo pendente..."
arquivos_mod=$(git status -s)
if [ -n "$arquivos_mod" ]; then
  log "O deploy foi finalizado com erro. Existe modificações não comitadas"
  exit 1
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
  exit 1
fi

log "Preparando versão..."
imagem_atual=$(cat docker-compose.yml | grep "image: ${nome_image}" | awk '{print $2}')
IFS=':' read -r -a imgVersao <<< "$imagem_atual"
versao_atual=${imgVersao[1]}
IFS='.' read -r -a semver <<< "$versao_atual"

if [ "$1" == "-v" ] && [ -n "$2" ]; then
  nova_versao="$2.0"
else
  versao_build=$(( semver[3] + 1))
  semver[3]=$versao_build
  nova_versao=$(IFS=. ; echo "${semver[*]}")
fi

nome_arquivo="${nome_image}_${nova_versao}.tar"

log "Alterando versão do deploy no docker-compose"
sed -i "s/image: ${imagem_atual}/image: ${nome_image}:${nova_versao}/" docker-compose.yml

log "Alterando versão do projeto"
sed -i "s/version = \".*\"/version = \"${nova_versao}\"/" pyproject.toml

log "Alterado Versao Atual: ${versao_atual} para Nova versão: ${nova_versao}"

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

log "Enviando imagem para o servidor via scp"
retry_attempts=5
delay_seconds=2

while true;
do
scp -i "${path_chave}" "${nome_arquivo}.gz" "${server_connect}":${pasta_servidor} || {
  retry_attempts=$((retry_attempts - 1))
  if [ "$retry_attempts" -gt 0 ]; then
      log "Reenvio em $delay_seconds segundos..."
      sleep "$delay_seconds"
      continue
  else
      log "Erro ao tentar enviar após 5 tentativas."
      clear_stage
      log "Deploy desfeito!"
      exit 1
  fi
}
break
done

log "Carregando para o docker do servidor a nova imagem. Aguarde alguns minutos..."
ecSrCom "cd ${pasta_servidor} && docker load < ${nome_arquivo}.gz"

log "Removendo arquivos de configuração do servidor"
ecSrCom "cd ${pasta_servidor} && rm -f docker-compose.yml nginx.conf"

log "Enviando novos arquivos de configuração para o servidor"
scp -i "${path_chave}" docker-compose.yml nginx.conf "${server_connect}":${pasta_servidor}

log "Parando os containers no servidor"
ecSrCom "cd ${pasta_servidor} && docker-compose down"

log "Recriando os containers no servidor"
ecSrCom "cd ${pasta_servidor} && docker-compose up -d"

log "Removendo imagem antiga da aplicação no servidor"
images=$(ecSrCom "docker images -q ${imagem_atual}")
if [ -n "$images" ]; then
  log "Imagem removida do servidor"
  ecSrCom "docker rmi ${imagem_atual}"
fi

log "Deletando imagem do diretório do servidor"
ecSrCom "cd ${pasta_servidor} && rm -f ${nome_arquivo} ${nome_arquivo}.gz"

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
