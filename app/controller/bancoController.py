# controller or business logic
# Trata base de bancoS

from utils.dbContext import MySql
from dto.banco import banco


class bancoController:

    def lista_bancos(self) -> list[banco]:
        query = f"SELECT ispb, descricao, codigo, descricao_completa FROM {MySql.DB_NAME}.tb_bancos ORDER BY codigo"
        bancos = MySql.getAll(query)
        list = []
        for row in bancos:
            bank = banco()
            bank.setIspb(row.get('ispb'))
            bank.setCodigo(row.get('codigo'))
            bank.setDescricao(row.get('descricao'))
            bank.setDescricaoCompleta(row.get('descricao_completa'))
            list.append(bank)
        return list

    def cadastrar_banco(self, bank: banco):
        query = f"""INSERT INTO {MySql.DB_NAME}.tb_bancos(ispb, descricao, codigo, descricao_completa) VALUE (%s, %s, %s, %s)"""
        MySql.exec(query, (
            bank.getIspb(),
            bank.getDescricao(),
            bank.getCodigo(),
            bank.getDescricaoCompleta()
        ))

    def get_banco_pelo_id(self, cod: str) -> banco:
        query = f"SELECT ispb, descricao, codigo, descricao_completa FROM {MySql.DB_NAME}.tb_bancos WHERE codigo = %s"

        linha = MySql.getOne(query, (cod,))

        if linha:
            bank = banco()
            bank.setIspb(linha.get('ispb'))
            bank.setCodigo(linha.get('codigo'))
            bank.setDescricao(linha.get('descricao'))
            bank.setDescricaoCompleta(linha.get('descricao_completa'))
            return bank

        return None

    def atulizar_banco(self, bank: banco):
        query = f"UPDATE {MySql.DB_NAME}.tb_bancos SET ispb = %s, descricao = %s, descricao_completa = %s WHERE codigo = %s"
        MySql.exec(query, (
            bank.getIspb(),
            bank.getDescricao(),
            bank.getDescricaoCompleta(),
            bank.getCodigo(),
        ))

    def excluir_banco(self, cod: int):
        query = f'DELETE FROM {MySql.DB_NAME}.tb_bancos WHERE codigo = %s'
        MySql.exec(query, (cod,))
