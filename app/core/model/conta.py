from core.db_connect import db
from utils.logger import logger


class Conta(db.Model):
    __tablename__ = "tb_contas"

    id_conta = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_empreendimento = db.Column(db.Integer, nullable=False)
    id_empreed_elonet = db.Column(db.Integer, nullable=True)
    mes_vigencia = db.Column(db.String(2), nullable=False)
    ano_vigencia = db.Column(db.String(4), nullable=False)
    dt_carga = db.Column(
        db.DateTime,
        nullable=True,
        server_default=db.text('CURRENT_TIMESTAMP')
    )
    vl_liberacao = db.Column(db.Numeric(15, 2), nullable=True)
    vl_aporte_construtora = db.Column(db.Numeric(15, 2), nullable=True)
    vl_receita_recebiveis = db.Column(db.Numeric(15, 2), nullable=True)
    vl_pagto_obra = db.Column(db.Numeric(15, 2), nullable=True)
    vl_pagto_rh = db.Column(db.Numeric(15, 2), nullable=True)
    vl_diferenca = db.Column(db.Numeric(15, 2), nullable=True)
    vl_saldo = db.Column(db.Numeric(15, 2), nullable=True)

    def save(self):
        try:
            item = Conta.query.get(self.id_conta)
            if self.id_conta is None or item is None:
                db.session.add(self)
                db.session.flush()
            else:
                db.session.merge(self)
            db.session.commit()
        except Exception as e:
            logger.exception(f'Erro ao salvar entidade: {e}')
            db.session.rollback()
