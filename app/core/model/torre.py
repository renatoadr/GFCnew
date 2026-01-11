from core.db_connect import db
from utils.logger import logger


class Torre(db.Model):
    __tablename__ = "tb_torres"

    id_torre = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_empreendimento = db.Column(db.Integer, nullable=False)
    id_torre_elonet = db.Column(db.Integer, nullable=True)
    id_empreed_elonet = db.Column(db.Integer, nullable=True)
    nm_torre = db.Column(db.String(20), nullable=False)
    qt_unidade = db.Column(db.Integer, nullable=False)
    qt_andar = db.Column(db.Integer, nullable=False)
    qt_coberturas = db.Column(db.Integer, nullable=True)
    prefix_cobertura = db.Column(db.String(20), nullable=True)
    num_apt_um_andar_um = db.Column(db.Integer, nullable=False)
    vl_unidade = db.Column(db.Numeric(15, 2), nullable=True)
    vl_cobertura = db.Column(db.Numeric(15, 2), nullable=True)

    def save(self):
        try:
            item = Torre.query.get(self.id_torre)
            if self.id_torre is None or item is None:
                db.session.add(self)
                db.session.flush()
            else:
                db.session.merge(self)
            db.session.commit()
        except Exception as e:
            logger.exception(f'Erro ao salvar entidade: {e}')
            db.session.rollback()
