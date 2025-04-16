# GFC
Este projeto tem como objetivo gerar relatórios do andamento de construções prediais para acompanhamento da evolução das obras.

## Tecnologia

### Backend
É um proejeto monolítico que tem como base os seguintes ferramentas:
- Python 3
- PIP 24
- Flask 3 *(Framework web)*
- Pandas *(IA)*
- ReportLab *(Gerar relatórios)*
- Matplotlib *(Gerador de gráficos)*

#### Iniciar projeto
Use o terminal powershell para criar um ambiente virtual no python
```sh
py -3 -m venv .venv
```
Inicie o ambiente virtual com o comando
```sh
.venv\Scripts\activate
```

#### Pacotes
Para instalar os pacotes rode o mando abaixo em um terminal powershell
```sh
pip install -r requirements.txt
```

#### Rodar projeto
Após criar o ambiente e instalar os pacotes pode executar o comando abaixo para rodar a aplicação em modo de desenvolvimento
```sh
flask --app main.py --debug run
```
Ou para apenas visualizar o projeto rode
```sh
flask --app main.py
```
### Deploy
O projeto roda no EC2 usando docker. Para subir uma imagem da aplicação, necessário subir a versão da imagem no docker compose e depois realizar os comandos abaixo:

#### Gerar Imagem Atualizada
Depois de alterar a versão no docker compose:
```docker
 app:
    image: gfcapp:1.0.1
```

Realize o comando de build
```sh
docker-compose build app
```

#### Salvar praparar a imagem
Após realizar o build, salva a cópia da imagem buildada
```sh
docker save > gfcapp_1.0.1.tar
```

Depois suba a imagem que foi gerada para o EC2 e carregue no docker com o comando
```sh
docker load < gfcapp_1.0.1.tar
```

Altere a versão da imagem do app no docker compose no EC2 e rode o comando para atualizar o container
```sh
docker-compose up -d
```

**Obs: Vale lembrar que deletar a imagem antiga bem como o seu container, funcionará melhor o fluxo de atualização no EC2**

### Comandos para gerenciamento do Docker
Para visualizar os logs
```sh
docker logs {id_container}
```

Para acessar o terminal interno do container
```sh
docker exec -it {nome_container} /bin/bash
```

### FrontEnd
Por ser um monolito, foi adicionado as bibliotecas abaixo para layout e comportamentos do projeto
- [jQuery *(Manipulação do DOM)*](https://api.jquery.com)
- [Bootstrap *(layout e comportamentos)*](https://getbootstrap.com/docs/5.3)
- [jQuery Validate *(Validaçao dos formulários)*](https://jqueryvalidation.org/validate/)
- [Fonte Ubuntu *(google fontes)*](https://fonts.google.com/specimen/Ubuntu)
- [Fontawesome *(galeria de ícones)*](https://fontawesome.com/icons)
- [Jquery Mask *(Para manipular os inputs adicionando padrão)*](https://igorescobar.github.io/jQuery-Mask-Plugin/docs.html)
- [Jquery Toast *(Para adicionar mensagens informativas para o usuário)*](https://kamranahmed.info/toast)
