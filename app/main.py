#!python3

from flask import Flask, request
from utils.logger import logger
from filters import filtros_bp
import configparser
import os


app = Flask(__name__)
app.secret_key = "gfc001"


@app.context_processor
def utility_processor():
    def update_query_string(**updates):
        from urllib.parse import parse_qs, urlencode
        current_params = parse_qs(request.query_string.decode('utf-8'))
        for key, value in updates.items():
            if value is None:
                if key in current_params:
                    del current_params[key]
            else:
                current_params[key] = [str(value)]
        return urlencode(current_params, doseq=True)
    return dict(update_query_string=update_query_string)


path = os.path.abspath(__file__).replace(f"{__name__}.py", '')
for route in os.listdir(os.path.join(path, 'router')):
    if route == '__pycache__':
        continue
    try:
        nameModule = route.replace('.py', '')
        module = __import__(f'router.{nameModule}')
        bp = getattr(getattr(module, f"{nameModule}"), f"{nameModule}_bp")
        app.register_blueprint(bp)
    except Exception as error:
        logger.error("Não foi possível carregar o módulo: " + route, error)

app.register_blueprint(filtros_bp)
app.permanent_session_lifetime.seconds


def init(app):
    config = configparser.ConfigParser()
    try:
        config_location = "gfc.cfg"
        config.read(config_location)
        app.config['UPLOAD_FOLDER'] = config.get("config", "UPLOAD_FOLDER")
        app.config['ALLOWED_EXTENSIONS'] = config.get(
            "config",
            "ALLOWED_EXTENSIONS"
        )
        app.config['BARRADIR'] = config.get("config", "BARRADIR")
        app.config['DIRSYS'] = config.get("config", "DIRSYS")

        if not os.path.exists(app.config['DIRSYS']):
            os.makedirs(app.config['DIRSYS'])

        logger.info("Configurações carregadas com sucesso: ", config_location)
    except Exception as error:
        logger.error("Não foi possível carregar as configurações: ", error)


if __name__ == "__main__" or __name__ == "main":
    init(app)
    app.run(host="0.0.0.0", port=5000)
    logger.info('Aplicação rodando...')
