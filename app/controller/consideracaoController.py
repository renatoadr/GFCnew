from utils.dbContext import MySql
from html import escape
from dto.consideracoes import consideracoes


class consideracaoController:

    def insert_registros(self, registros: dict, idEmpreend: int, mes: str, ano: int) -> None:
        querySelect = f"SELECT COUNT(1) existe FROM {MySql.DB_NAME}.tb_consideracoes WHERE campo = %s AND texto = %s AND id_empreendimento = %s AND mes_vigencia = %s AND ano_vigencia = %s AND ac_historico IS NULL;"
        queryInsert = f"INSERT INTO {MySql.DB_NAME}.tb_consideracoes (campo, texto, id_empreendimento, mes_vigencia, ano_vigencia) VALUES (%s, %s, %s, %s, %s);"
        queryUpdate = f"UPDATE {MySql.DB_NAME}.tb_consideracoes SET ac_historico = 'EDITADO', dt_editado = CURRENT_TIMESTAMP WHERE campo = %s AND texto != %s AND id_empreendimento = %s AND mes_vigencia = %s AND ano_vigencia = %s ;"

        for campo, texto in registros.items():
            data = (campo, escape(texto), idEmpreend, mes, ano)
            select = MySql.getOne(querySelect, data)
            if select['existe'] == 0:
                MySql.exec(queryUpdate, data)
                MySql.exec(queryInsert, data)

    def listar_campos(self, idEmpreend: int, mes: str, ano: int) -> consideracoes:
        query = f"SELECT campo, texto FROM {MySql.DB_NAME}.tb_consideracoes WHERE id_empreendimento = %s AND mes_vigencia = %s AND ano_vigencia = %s AND ac_historico IS NULL ORDER BY 1;"
        result = MySql.getAll(query, (idEmpreend, mes, ano))
        return self.mapeamento(result)

    def mapeamento(self, lista) -> consideracoes:
        consid = consideracoes()
        map = {
            'gp_conclusao_1': 'setConclusao1',
            'gp_conclusao_2': 'setConclusao2',
            'gp_conclusao_3': 'setConclusao3',
            'gp_consideracao_1': 'setConsideracao1',
            'gp_consideracao_2': 'setConsideracao2',
            'gp_consideracao_3': 'setConsideracao3',
            'gp_efetivoEstoque_1': 'setEfetivoEstoque1',
            'gp_efetivoEstoque_2': 'setEfetivoEstoque2',
            'gp_efetivoEstoque_3': 'setEfetivoEstoque3',
            'gp_empreiteiro_1': 'setEmpreiteiro1',
            'gp_empreiteiro_2': 'setEmpreiteiro2',
            'gp_empreiteiro_3': 'setEmpreiteiro3',
            'gp_estoque_1': 'setEstoque1',
            'gp_estoque_2': 'setEstoque2',
            'gp_estoque_3': 'setEstoque3',
            'gp_qualidade_1': 'setQualidade1',
            'gp_qualidade_2': 'setQualidade2',
            'gp_qualidade_3': 'setQualidade3',
            'gp_servico_1': 'setServico1',
            'gp_servico_2': 'setServico2',
            'gp_servico_3': 'setServico3',
            'responsavel': 'setResponsavel',
            'crea': 'setCREA',
        }
        for linha in lista:
            campo = linha['campo']
            texto = linha['texto']
            if campo in map:
                metodo = getattr(consid, map[campo])
                metodo(texto)
        return consid
