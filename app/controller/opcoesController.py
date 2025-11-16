from utils.dbContext import MySql
import json


class OpcoesController:
    def buscar(self, chave):
        query = f"SELECT valor FROM {MySql.DB_NAME}.tb_opcoes WHERE chave = %s"
        dados = MySql.getOne(query, (chave,))

        if dados is None:
            return None

        try:
            return json.loads(dados['valor'])
        except:
            return dados['valor']

    def salvar(self, chave, valor):
        query = f"INSERT INTO {MySql.DB_NAME}.tb_opcoes (chave, valor) VALUES (%s, %s) ON DUPLICATE KEY UPDATE valor = %s"

        if isinstance(valor, dict):
            valor = json.dumps(valor)

        MySql.exec(query, (chave, valor, valor))

    def deletar(self, chave):
        query = f"DELETE FROM {MySql.DB_NAME}.tb_opcoes WHERE chave = %s"
        MySql.exec(query, (chave,))
