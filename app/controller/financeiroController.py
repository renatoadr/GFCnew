#controller or business logic
# Trata base FINANCEIRO

from dto.financeiro import financeiro
from utils.dbContext import MySql

class financeiroController:
    __connection = None

    def __init__(self):
        pass

    def consultarNotas(self, idEmpreend):
        self.__connection = MySql.connect()
        cursor = self.__connection.cursor()   

        print('---consultarn notas---')
        print(idEmpreend)  

        query =  "select mes_vigencia, ano_vigencia, dt_carga from " + MySql.DB_NAME + ".tb_notas where id_empreendimento = " +  str (idEmpreend) + " group by mes_vigencia, ano_vigencia, dt_carga"

        print('-----------------')
        print(query)
        print('-----------------')
        
        cursor.execute(query)

        lista = cursor.fetchall()
        
        listaNotas = []

        for x in lista:
            n = nota()
            n.setMesVigencia(x[0])
            n.setAnoVigencia(x[1])
            n.setDtCarga(x[2])
            listaNotas.append(n)

        cursor.close()
        MySql.close(self.__connection)
        return listaNotas

    def consultarFinanceiroPelaData(self, idEmpreend, dtCarga):
        self.__connection = MySql.connect()
        cursor = self.__connection.cursor(dictionary=True)   

#        query =  "select id_empreendimento, mes_vigencia, ano_vigencia, dt_carga, item, vl_nota_fiscal, vl_estoque from " + MySql.DB_NAME + ".tb_notas where id_empreendimento = '" + idEmpreend + "' and dt_carga = '" + dtCarga + "'"
        query =  "select id_empreendimento, mes_vigencia, ano_vigencia, historico, perc_financeiro, vl_financeiro from " + MySql.DB_NAME + ".tb_financeiro where id_empreendimento = '" + str(idEmpreend) + "'"
    
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
        print ('-----------------> ', listaItens)

        return listaItens
