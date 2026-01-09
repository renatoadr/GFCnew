from core.db_connect import db, CONEXAO
from flask import Flask, request
from utils.logger import logger
from filters import filtros_bp
import configparser
import os

app = Flask(__name__)


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


def generate_routes():
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
            logger.exception(
                f"Não foi possível carregar o módulo: {route}. Erro: {error}")


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

        logger.info(f"Configurações carregadas com sucesso: {config_location}")
    except Exception as error:
        logger.exception(
            f"Não foi possível carregar as configurações: {error}")


if __name__ == "main":

    try:
        app.config['SQLALCHEMY_DATABASE_URI'] = CONEXAO
        db.init_app(app)
        with app.app_context():
            db.create_all()
        logger.info('Banco de dados inicializado com sucesso.')
    except Exception as e:
        logger.exception(f'Erro ao inicializar o banco de dados: {e}')

    try:
        app.permanent_session_lifetime = 3600
        app.secret_key = os.urandom(24)
        init(app)
        generate_routes()
        app.register_blueprint(filtros_bp)
        app.run(
            port=os.getenv("FLASK_APP_PORT", 5000),
            use_reloader=os.getenv("FLASK_USE_RELOADER", True),
            host=os.getenv("FLASK_APP_HOST", "0.0.0.0")
        )
        logger.info('Aplicação rodando...')
        logger.info(f'=== SERVIDOR GFC INICIADO ===')
        logger.info(f'URL: http://{os.getenv("FLASK_APP_HOST", "0.0.0.0")
                                   }:{os.getenv("FLASK_APP_PORT", 5000)}')
        logger.info(f'==============================')
    except Exception as e:
        logger.exception(f'Erro ao iniciar a aplicação: {e}')
