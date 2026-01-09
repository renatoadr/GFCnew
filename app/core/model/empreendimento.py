from utils import logger
from core.db_connect import db


class Empreendimento(db.Model):
    __tablename__ = "tb_empreendimentos"

    id_empreendimento = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True
    )
    id_empreed_elonet = db.Column(db.Integer, nullable=True)
    nm_empreendimento = db.Column(db.String(100), nullable=False)
    apelido = db.Column(db.String(10), nullable=False)
    nm_incorporador = db.Column(db.String(100), nullable=False)
    nm_construtor = db.Column(db.String(100), nullable=False)
    logradouro = db.Column(db.String(100), nullable=False)
    bairro = db.Column(db.String(50), nullable=False)
    cidade = db.Column(db.String(50), nullable=False)
    estado = db.Column(db.String(2), nullable=False)
    cep = db.Column(db.String(8), nullable=False)
    cpf_cnpj_engenheiro = db.Column(
        db.String(15),
        db.ForeignKey('tb_clientes.cpf_cnpj'),
        nullable=False
    )
    vl_plano_empresario = db.Column(db.Numeric(15, 2), nullable=False)
    indice_garantia = db.Column(db.Numeric(3, 2), nullable=False)
    previsao_entrega = db.Column(db.Date, nullable=False)
    cod_banco = db.Column(db.Integer, nullable=True)
    id_empreed_elonet = db.Column(db.Integer, nullable=True)

    def save(self):
        try:
            item = Empreendimento.query.get(self.id_empreendimento)
            if self.id_empreendimento is None or item is None:
                db.session.add(self)
                db.session.flush()
            else:
                db.session.merge(self)
            db.session.commit()
        except Exception as e:
            logger.exception(f'Erro ao salvar entidade: {e}')
            db.session.rollback()
