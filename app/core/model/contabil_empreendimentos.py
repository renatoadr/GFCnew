from core.db_connect import db
from utils import logger


class ContabilEmpreendimentos(db.Model):
    __tablename__ = "tb_contabil_empreendimentos"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_empreendimento = db.Column(db.Integer, nullable=False)
    id_empreendimento_elonet = db.Column(db.Integer, nullable=True)
    dt_criado = db.Column(
        db.DateTime,
        nullable=False,
        server_default=db.func.current_timestamp()
    )
    dt_vigencia = db.Column(db.Date, nullable=False)
    vlr_liberado = db.Column(db.Numeric(15, 2), nullable=False)
    vlr_a_liberar = db.Column(db.Numeric(15, 2), nullable=False)
    vlr_estoque = db.Column(db.Numeric(15, 2), nullable=False)
    vlr_recebivel = db.Column(db.Numeric(15, 2), nullable=False)

    def save(self):
        try:
            item = ContabilEmpreendimentos.query.get(self.id)
            if self.id is None or item is None:
                db.session.add(self)
                db.session.flush()
            else:
                db.session.merge(self)
            db.session.commit()
        except Exception as e:
            logger.exception(f'Erro ao salvar entidade: {e}')
            db.session.rollback()
