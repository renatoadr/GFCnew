#controller or business logic
# Trata base de PONTOS DE ATENÇÃO

from dto.ponto import ponto
from utils.dbContext import MySql

class pontoController:
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

    def consultarPontosPelaData(self, idEmpreend, dtCarga, tipo):
        self.__connection = MySql.connect()
        cursor = self.__connection.cursor(dictionary=True)   

#        query =  "select id_empreendimento, mes_vigencia, ano_vigencia, dt_carga, item, vl_nota_fiscal, vl_estoque from " + MySql.DB_NAME + ".tb_notas where id_empreendimento = '" + idEmpreend + "' and dt_carga = '" + dtCarga + "'"
        query =  "select id_empreendimento, mes_vigencia, ano_vigencia, tipo, historico, status, observacao from " + MySql.DB_NAME + ".tb_pontos_atencao where id_empreendimento = '" + str(idEmpreend) + "' and tipo = '" + tipo + "'"
    
        print(query)

        cursor.execute(query)

#        linha = cursor.fetchone()
        print('++++++++++++ consultarPontosPelaData +++++++++++++++')
#        print (linha)
#        print('+++++++++++++++++++++++++++')

        lista = cursor.fetchall()
        
        listaItens = []

        for x in lista:
            p = ponto()
            p.setHistorico(x['historico'])
            p.setStatus(x['status'])
            p.setObservacao(x['observacao'])
            listaItens.append(p)

#        dados = [list(linha) for linha in listaItens()]

        print('------------------------')       
        print('------------------------')
        cursor.close()
        MySql.close(self.__connection)
#        print ('-----------------> ', dados)
        print ('-----------------> ', listaItens)

        return listaItens
