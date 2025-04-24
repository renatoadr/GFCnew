#! /bin/bash

pasta_servidor=gfc_app
nome_image=gfcapp

echo "[GFC_DEPLOY] Iniciando deploy...."

echo "[GFC_DEPLOY] Preparando versão..."
imagem_atual=$(cat docker-compose.yml | grep "image: ${nome_image}" | awk '{print $2}')
IFS=':' read -r -a imgVersao <<< "$imagem_atual"
versao_atual=${imgVersao[1]}
IFS='.' read -r -a semver <<< "$versao_atual"
versao_build=$(( semver[3] + 1))
semver[3]=$versao_build
nova_versao=$(IFS=. ; echo "${semver[*]}")
nome_arquivo="gfcapp_${nova_versao}.tar"

echo "[GFC_DEPLOY] Alterando versão do deploy no docker-compose"
sed -i "s/image: ${imagem_atual}/image: gfcapp:${nova_versao}/" docker-compose.yml

echo "[GFC_DEPLOY] Alterado Versao Atual: ${versao_atual} para Nova versão: ${nova_versao}"

echo "[GFC_DEPLOY] Removendo imagem antiga"
docker rmi "${imagem_atual}"

echo "[GFC_DEPLOY] Iniciando build da aplicação"
docker-compose build app

echo "[GFC_DEPLOY] Salvando cópia da imagem... Aguarde alguns minutos..."
docker save gfcapp -o "${nome_arquivo}"

echo "[GFC_DEPLOY] Aguarde, comprimindo o arquivo..."
gzip -v "${nome_arquivo}"

echo "[GFC_DEPLOY] Enviando imagem para o servidor"
scp -i "chavegfc.pem" "${nome_arquivo}.gz" ec2-user@ec2-100-28-173-23.compute-1.amazonaws.com:~/${pasta_servidor}

echo "[GFC_DEPLOY] Removendo arquivos de configuração do servidor"
ssh -i "chavegfc.pem" ec2-user@ec2-100-28-173-23.compute-1.amazonaws.com "cd ${pasta_servidor} && rm -f docker-compose.yml gunicorn_config.py nginx.conf"

echo "[GFC_DEPLOY] Enviando novos arquivos de configuração para o servidor"
scp -i "chavegfc.pem" docker-compose.yml gunicorn_config.py nginx.conf ec2-user@ec2-100-28-173-23.compute-1.amazonaws.com:~/${pasta_servidor}

echo "[GFC_DEPLOY] Parando os containers no servidor"
ssh -i "chavegfc.pem" ec2-user@ec2-100-28-173-23.compute-1.amazonaws.com "cd ${pasta_servidor} && docker-compose down"

echo "[GFC_DEPLOY] Removendo imagem antiga da aplicação no servidor"
ssh -i "chavegfc.pem" ec2-user@ec2-100-28-173-23.compute-1.amazonaws.com "docker rmi ${imagem_atual}"

echo "[GFC_DEPLOY] Descompactando imagem no servidor...."
ssh -i "chavegfc.pem" ec2-user@ec2-100-28-173-23.compute-1.amazonaws.com "cd ${pasta_servidor} && gzip -vd ${nome_arquivo}.gz"

echo "[GFC_DEPLOY] Carregando para o docker do servidor a nova imagem. Aguarde alguns minutos..."
ssh -i "chavegfc.pem" ec2-user@ec2-100-28-173-23.compute-1.amazonaws.com "cd ${pasta_servidor} && docker load < ${nome_arquivo}"

echo "[GFC_DEPLOY] Recriando os containers no servidor"
ssh -i "chavegfc.pem" ec2-user@ec2-100-28-173-23.compute-1.amazonaws.com "cd ${pasta_servidor} && docker-compose up -d"

echo "[GFC_DEPLOY] Deletando imagem do diretório do servidor"
ssh -i "chavegfc.pem" ec2-user@ec2-100-28-173-23.compute-1.amazonaws.com "cd ${pasta_servidor} && rm -f ${nome_arquivo} ${nome_arquivo}.gz"

echo "[GFC_DEPLOY] Deletando imagem salva no diretório local"
rm -f "${nome_arquivo}" "${nome_arquivo}.gz"

echo "[GFC_DEPLOY] Deploy concluído!"
