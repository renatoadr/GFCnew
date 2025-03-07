#controller or business logic
# Trata base de NOTAS

from dto.medicao import medicao
from utils.dbContext import MySql

class medicaoController:
    __connection = None

    def __init__(self):
        pass

    def consultarMedicoes(self, idEmpreend):
        self.__connection = MySql.connect()
        cursor = self.__connection.cursor(dictionary=True)   

        query =  "select id_empreendimento, nr_medicao, mes_vigencia, ano_vigencia, perc_previsto_acumulado, perc_realizado_acumulado, perc_previsto_periodo from " + MySql.DB_NAME + ".tb_medicoes where id_empreendimento = '" + str(idEmpreend) + "'"
    
        print(query)

        cursor.execute(query)

#        linha = cursor.fetchone()
#        print('++++++++++++ consultarNotaPelaData +++++++++++++++')
#        print (linha)
#        print('+++++++++++++++++++++++++++')

        lista = cursor.fetchall()
        
        listaItens = []

        for x in lista:
            m = medicao()
            m.setNrMedicao(x['nr_medicao'])
            m.setMesVigencia(x['mes_vigencia'])
            m.setAnoVigencia(x['ano_vigencia'])
            m.setPercPrevistoAcumulado(x['perc_previsto_acumulado'])
            m.setPercRealizadoAcumulado(x['perc_realizado_acumulado'])
            m.setPercPrevistoPeriodo(x['perc_previsto_periodo'])
            listaItens.append(m)

#        dados = [list(linha) for linha in listaItens()]

#        print('------------------------')       
#        print('------------------------')
        cursor.close()
        MySql.close(self.__connection)
#        print ('-----------------> ', dados)
#        print ('-----------------> ', listaItens)

        return listaItens

    def consultarMedicoesPorPeriodo(self, idEmpreend, mesVigenciaIni, anoVigenciaIni, mesVigenciaFim, anoVigenciaFim):
        self.__connection = MySql.connect()
        cursor = self.__connection.cursor(dictionary=True)   

        if anoVigenciaIni == anoVigenciaFim:
            query =  "select id_empreendimento, nr_medicao, mes_vigencia, ano_vigencia, perc_previsto_acumulado, perc_realizado_acumulado, perc_previsto_periodo from " + MySql.DB_NAME + ".tb_medicoes where id_empreendimento = '" + str(idEmpreend) + "' and (mes_vigencia >= '" + mesVigenciaIni + "' and ano_vigencia = '" + anoVigenciaIni + "') and (mes_vigencia <= '" + mesVigenciaFim + "' and ano_vigencia = '" + anoVigenciaFim + "')"
        else:
            query =  "select id_empreendimento, nr_medicao, mes_vigencia, ano_vigencia, perc_previsto_acumulado, perc_realizado_acumulado, perc_previsto_periodo from " + MySql.DB_NAME + ".tb_medicoes where id_empreendimento = '" + str(idEmpreend) + "' and (mes_vigencia >= '" + mesVigenciaIni + "' and ano_vigencia = '" + anoVigenciaIni + "') or (mes_vigencia <= '" + mesVigenciaFim + "' and ano_vigencia = '" + anoVigenciaFim + "')"
    
        print(query)

        cursor.execute(query)

        lista = cursor.fetchall()
        
        listaItens = []

        for x in lista:
            m = medicao()
            m.setNrMedicao(x['nr_medicao'])
            m.setMesVigencia(x['mes_vigencia'])
            m.setAnoVigencia(x['ano_vigencia'])
            m.setPercPrevistoAcumulado(x['perc_previsto_acumulado'])
            m.setPercRealizadoAcumulado(x['perc_realizado_acumulado'])
            m.setPercPrevistoPeriodo(x['perc_previsto_periodo'])
            listaItens.append(m)

#        dados = [list(linha) for linha in listaItens()]

#        print('------------------------')       
#        print('------------------------')
        cursor.close()
        MySql.close(self.__connection)
#        print ('-----------------> ', dados)
#        print ('-----------------> ', listaItens)

        return listaItens
