from flask_sqlalchemy import SQLAlchemy
import os

db = SQLAlchemy()

Model = db.Model

PORT = os.getenv('PORT', '3306')
USER = os.getenv('DB_USER')
HOST = os.getenv('DB_HOST')
DB_NAME = os.getenv('DB_NAME')
PLUGIN = os.getenv('DB_PLUGIN', 'mysqlconnector')

try:
    filePass = open('/run/secrets/db-password', 'r')
    PASSWORD = filePass.read()
except:
    PASSWORD = os.getenv('DB_PASS')

CONEXAO = f'mysql+{PLUGIN}://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB_NAME}'
