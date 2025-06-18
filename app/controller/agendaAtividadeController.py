# controller or business logic
# Trata base de AGENDAS

from utils.dbContext import MySql
from dto.agenda_atividade import agenda_atividade


class agendaAtividadeController:

    def buscar_pelo_id(self, id: str) -> agenda_atividade:
        query = f"SELECT id_atividade, descr_atividade FROM {MySql.DB_NAME}.tb_agendas_atividades WHERE id_atividade = %s"
        item = MySql.getOne(query, (id,))

        if item:
            return agenda_atividade(
                item['id_atividade'],
                item['descr_atividade']
            )
        return None

    def lista_atividades(self) -> list[agenda_atividade]:
        query = f"SELECT id_atividade, descr_atividade FROM {MySql.DB_NAME}.tb_agendas_atividades"
        result = MySql.getAll(query)
        list = []

        for linha in result:
            list.append(agenda_atividade(
                linha['id_atividade'],
                linha['descr_atividade']
            ))

        return list

    def cadastrar_atividade(self, id: str, desc: str):
        query = f"INSERT INTO {MySql.DB_NAME}.tb_agendas_atividades (id_atividade, descr_atividade) VALUES (%s, %s)"
        MySql.exec(query, (id, desc))

    def salvar_atividade(self, id: str, desc: str, idAntiga: str):
        query = f"UPDATE {MySql.DB_NAME}.tb_agendas_atividades SET id_atividade = %s, descr_atividade = %s WHERE id_atividade = %s"
        MySql.exec(query, (id, desc, idAntiga))

    def existe(self, id: str) -> bool:
        return True if self.buscar_pelo_id(id) is not None else False

    def apagar(self, id: str):
        query = f"DELETE FROM {MySql.DB_NAME}.tb_agendas_atividades WHERE id_atividade = %s"
        MySql.exec(query, (id,))
