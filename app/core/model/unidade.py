from core.db_connect import db
from utils.logger import logger


class Unidade(db.Model):
    __tablename__ = "tb_unidades"
    id_unidade = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_empreendimento = db.Column(db.Integer, nullable=False)
    id_torre = db.Column(db.Integer, nullable=False)
    id_unidade_elonet = db.Column(db.Integer, nullable=True)
    id_torre_elonet = db.Column(db.Integer, nullable=True)
    id_empreed_elonet = db.Column(db.Integer, nullable=True)
    unidade = db.Column(db.String(15), nullable=False)
    mes_vigencia = db.Column(db.String(2), nullable=False)
    ano_vigencia = db.Column(db.String(4), nullable=False)
    vl_unidade = db.Column(db.Numeric(10, 2), nullable=True)
    status = db.Column(db.String(8), nullable=False)
    cpf_cnpj_comprador = db.Column(db.String(15), nullable=True)
    vl_receber = db.Column(db.Numeric(10, 2), nullable=True)
    dt_ocorrencia = db.Column(
        db.DateTime,
        nullable=True,
        server_default=db.text('CURRENT_TIMESTAMP')
    )
    financiado = db.Column(db.String(3), nullable=True)
    vl_chaves = db.Column(db.Numeric(15, 2), nullable=True)
    vl_pre_chaves = db.Column(db.Numeric(15, 2), nullable=True)
    vl_pos_chaves = db.Column(db.Numeric(15, 2), nullable=True)
    ac_historico = db.Column(db.String(15), nullable=True)

    def save(self):
        try:
            item = Unidade.query.get(self.id_unidade)
            if self.id_unidade is None or item is None:
                db.session.add(self)
                db.session.flush()
            else:
                db.session.merge(self)
            db.session.commit()
        except Exception as e:
            logger.exception(f'Erro ao salvar entidade: {e}')
            db.session.rollback()
