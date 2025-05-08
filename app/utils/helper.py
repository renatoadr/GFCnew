from flask import current_app
import os


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in current_app.config['ALLOWED_EXTENSIONS']


def criaPastas(diretorio) -> bool:
    try:
        if not os.path.exists(diretorio):
            os.makedirs(diretorio)
        return os.path.exists(diretorio)
    except:
        return False
