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


### FrontEnd
Por ser um monolito, foi adicionado as bibliotecas abaixo para layout e comportamentos do projeto
- [jQuery *(Manipulação do DOM)*](https://api.jquery.com)
- [Bootstrap *(layout e comportamentos)*](https://getbootstrap.com/docs/5.3)
- [jQuery Validate *(Validaçao dos formulários)*](https://jqueryvalidation.org/validate/)
- [Fonte Ubuntu *(google fontes)*](https://fonts.google.com/specimen/Ubuntu)
- [Fontawesome *(galeria de ícones)*](https://fontawesome.com/icons)
