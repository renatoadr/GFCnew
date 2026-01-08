from utils.logger import logger
from core.db_connect import db


class Cliente(db.Model):
    __tablename__ = "tb_clientes"

    cpf_cnpj = db.Column(db.String(15), primary_key=True, nullable=False)
    tp_cpf_cnpj = db.Column(db.String(4), nullable=False)
    nm_cliente = db.Column(db.String(100), nullable=False)
    ddd = db.Column(db.String(3), nullable=False)
    tel = db.Column(db.String(9), nullable=False)
    email = db.Column(db.String(50), nullable=False)

    def save(self):
        try:
            item = Cliente.query.get(self.cpf_cnpj)
            if self.cpf_cnpj is None or item is None:
                db.session.add(self)
                db.session.flush()
            else:
                db.session.merge(self)
            db.session.commit()
        except Exception as e:
            logger.exception(f'Erro ao salvar entidade: {e}')
            db.session.rollback()
