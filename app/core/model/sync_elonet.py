from core.db_connect import db
from utils.logger import logger


class SyncElonet(db.Model):
    __tablename__ = "tb_sync_elonet"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    chave_dominio = db.Column(db.Text, nullable=False)
    nm_campo = db.Column(db.Text, nullable=False)
    valor_antigo = db.Column(db.Text, nullable=True)
    novo_valor = db.Column(db.Text, nullable=True)
    ts_sync = db.Column(
        db.DateTime,
        nullable=False,
        server_default=db.text('CURRENT_TIMESTAMP')
    )

    def save(self):
        try:
            db.session.add(self)
            db.session.commit()
        except Exception as e:
            logger.exception(f'Erro ao salvar entidade: {e}')
            db.session.rollback()
