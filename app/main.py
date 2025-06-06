#!python3

from flask import Flask
from utils.logger import logger
from filters import filtros_bp
import configparser
import os


app = Flask(__name__)
app.secret_key = "gfc001"

path = os.path.abspath(__file__).replace(f"{__name__}.py", '')
for route in os.listdir(os.path.join(path, 'router')):
    try:
        nameModule = route.replace('.py', '')
        module = __import__(f'router.{nameModule}')
        bp = getattr(getattr(module, f"{nameModule}"), f"{nameModule}_bp")
        app.register_blueprint(bp)
    except:
        pass

app.register_blueprint(filtros_bp)
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

if __name__ == "__main__" or __name__ == "main":
    app.run(host="0.0.0.0", port=5000)
