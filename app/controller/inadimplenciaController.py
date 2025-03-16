#controller or business logic
# Trata base de INADIMPLENCIA

from dto.inadimpencia import inadimpencia
from utils.dbContext import MySql

class inadimplenciaController:
    __connection = None

    def __init__(self):
        pass

    def consultarInadimplenciaPelaData(self, idEmpreend, mesIni, anoIni, mesFim, anoFim):
        self.__connection = MySql.connect()
        cursor = self.__connection.cursor(dictionary=True)   

        if anoIni == anoFim:
                query =  "select id_empreendimento, mes_vigencia, ano_vigencia, ordem, periodo, qt_unidades from " + MySql.DB_NAME + ".tb_inadimplencias where id_empreendimento = '" + str(idEmpreend) + "' and (mes_vigencia >= '" + mesIni + "' and ano_vigencia = '" + anoIni + "') and (mes_vigencia <= '" + mesFim + "' and ano_vigencia = '" + anoFim + "') order by ordem, ano_vigencia, mes_vigencia"
                print('===========> com and')
        else:
                query =  "select id_empreendimento, mes_vigencia, ano_vigencia, ordem, periodo, qt_unidades from " + MySql.DB_NAME + ".tb_inadimplencias where id_empreendimento = '" + str(idEmpreend) + "' and (mes_vigencia >= '" + mesIni + "' and ano_vigencia = '" + anoIni + "') or  (mes_vigencia <= '" + mesFim + "' and ano_vigencia = '" + anoFim + "') order by ordem, ano_vigencia, mes_vigencia"
                print('===========> com or')

        print(query)

        cursor.execute(query)

#        linha = cursor.fetchone()
        print('++++++++++++ consultarInadimplenciaPelaData +++++++++++++++')
#        print (linha)
#        print('+++++++++++++++++++++++++++')

        lista = cursor.fetchall()
        
        listaItens = []

        for x in lista:
            i = inadimpencia()
            i.setMesVigencia(x['mes_vigencia'])
            i.setAnoVigencia(x['ano_vigencia'])
            i.setOrdem(x['ordem'])
            i.setPeriodo(x['periodo'])
            i.setQtUnidades(x['qt_unidades'])
            listaItens.append(i)

#        dados = [list(linha) for linha in listaItens()]

        print('------------------------')       
        print('------------------------')
        cursor.close()
        MySql.close(self.__connection)
#        print ('-----------------> ', dados)
        print ('-----------------> ', listaItens)

        return listaItens
