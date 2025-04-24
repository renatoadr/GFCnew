# controller or business logic
# Trata base FINANCEIRO

from utils.dbContext import MySql
from dto.financeiro import financeiro


class financeiroController:
    __connection = None

    def consultarFinanceiroPelaData(self, idEmpreend, dtCarga):
        self.__connection = MySql.connect()
        cursor = self.__connection.cursor(dictionary=True)

#        query =  "select id_empreendimento, mes_vigencia, ano_vigencia, dt_carga, item, vl_nota_fiscal, vl_estoque from " + MySql.DB_NAME + ".tb_notas where id_empreendimento = '" + idEmpreend + "' and dt_carga = '" + dtCarga + "'"
        query = "select id_empreendimento, mes_vigencia, ano_vigencia, historico, perc_financeiro, vl_financeiro from " + \
            MySql.DB_NAME + ".tb_financeiro where id_empreendimento = '" + \
                str(idEmpreend) + "'"

        print(query)

        cursor.execute(query)

#        linha = cursor.fetchone()
        print('++++++++++++ consultarFinanceiroPelaData +++++++++++++++')
#        print (linha)
#        print('+++++++++++++++++++++++++++')

        lista = cursor.fetchall()

        listaItens = []

        for x in lista:
            f = financeiro()
            f.setHistorico(x['historico'])
            f.setPercFinanceiro(x['perc_financeiro'])
            f.setVlFinanceiro(x['vl_financeiro'])
            listaItens.append(f)

#        dados = [list(linha) for linha in listaItens()]

        print('------------------------')
        print('------------------------')
        cursor.close()
        MySql.close(self.__connection)
#        print ('-----------------> ', dados)
        print('-----------------> ', listaItens)

        return listaItens

    def consultarFinanceiroPelaVigencia(self, idEmpreend, mes, ano):
        query = f"SELECT id_empreendimento, mes_vigencia, ano_vigencia, historico, perc_financeiro, vl_financeiro FROM {MySql.DB_NAME}.tb_financeiro WHERE id_empreendimento = %s AND mes_vigencia = %s AND ano_vigencia = %s;"
        lista = MySql.getAll(query, (idEmpreend, mes, ano))
        listaItens = []
        for x in lista:
            f = financeiro()
            f.setHistorico(x['historico'])
            f.setPercFinanceiro(x['perc_financeiro'])
            f.setVlFinanceiro(x['vl_financeiro'])
            listaItens.append(f)

        return listaItens
