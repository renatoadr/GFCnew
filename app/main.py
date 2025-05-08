#!python3

from flask import Flask
import configparser
import os
from utils.logger import logger

from router.gerar_relatorios import gerar_relatorio_bp
from router.contas_corrente import contas_corrente_bp
from router.consideracoes import consideracoes_bp
from router.emprendimento import empreend_bp
from router.relatorios import relatorio_bp
from router.medicoes import medicoes_bp
from router.garantia import garantia_bp
from router.usuarios import usuarios_bp
from router.unidades import unidade_bp
from router.graficos import grafico_bp
from router.clientes import cliente_bp
from router.orcamentos import orca_bp
from router.certidoes import cert_bp
from router.tabelas import tabela_bp
from router.agenda import agenda_bp
from router.bancos import bancos_bp
from router.torres import torre_bp
from router.inicio import init_bp
from router.notas import nota_bp
from router.fotos import foto_bp
from router.api import api_bp

from filters import filtros_bp

app = Flask(__name__)
app.secret_key = "gfc001"

app.register_blueprint(gerar_relatorio_bp)
app.register_blueprint(contas_corrente_bp)
app.register_blueprint(consideracoes_bp)
app.register_blueprint(relatorio_bp)
app.register_blueprint(empreend_bp)
app.register_blueprint(medicoes_bp)
app.register_blueprint(garantia_bp)
app.register_blueprint(usuarios_bp)
app.register_blueprint(grafico_bp)
app.register_blueprint(unidade_bp)
app.register_blueprint(cliente_bp)
app.register_blueprint(filtros_bp)
app.register_blueprint(tabela_bp)
app.register_blueprint(agenda_bp)
app.register_blueprint(bancos_bp)
app.register_blueprint(torre_bp)
app.register_blueprint(cert_bp)
app.register_blueprint(orca_bp)
app.register_blueprint(init_bp)
app.register_blueprint(nota_bp)
app.register_blueprint(foto_bp)
app.register_blueprint(api_bp)

app.permanent_session_lifetime.seconds


def init(app):
    config = configparser.ConfigParser()
    try:
        config_location = "gfc.cfg"
        config.read(config_location)
        app.config['UPLOAD_FOLDER'] = config.get("config", "UPLOAD_FOLDER")
        app.config['ALLOWED_EXTENSIONS'] = config.get(
            "config", "ALLOWED_EXTENSIONS")
        app.config['BARRADIR'] = config.get("config", "BARRADIR")
        app.config['DIRSYS'] = config.get("config", "DIRSYS")

        if not os.path.exists(app.config['DIRSYS']):
            os.makedirs(app.config['DIRSYS'])

        logger.info("Configurações carregadas com sucesso: ", config_location)
    except Exception as error:
        logger.error("Não foi possível carregar as configurações: ", error)


init(app)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
    # app.run(host="192.168.0.11",port=5000)
    # app.run(host="177.195.148.38",port=80)
    # app.run(host='2804:14d:32a2:8564:a16e:bd9f:ad8b:9c76',port=80)
