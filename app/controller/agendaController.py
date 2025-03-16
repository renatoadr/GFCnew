#controller or business logic
# Trata base de AGENDAS

from dto.agenda import agenda
from utils.dbContext import MySql

class agendaController:
    __connection = None

    def __init__(self):
        pass

    def inserirAgenda(self, agenda):
        self.__connection = MySql.connect()
        cursor = self.__connection.cursor()         
   
        query =  "INSERT INTO " + MySql.DB_NAME + ".tb_agendas ( id_empreendimento, nm_agenda, qt_unidade ) VALUES (" + str(agenda.getIdEmpreend()) + ", '" + agenda.getNmAgenda() + "', " + agenda.getQtUnidade() + ")"
                                                                                                                                                          
        print('++++++++++++++++++++++')
        print(query)
        print('++++++++++++++++++++++')

        cursor.execute(query)

        self.__connection.commit()     
        print(cursor.rowcount,"Agenda cadastrada com sucesso")     
        cursor.close()
        MySql.close(self.__connection)


    def consultarAgendas(self, idEmpreend):
        self.__connection = MySql.connect()
        cursor = self.__connection.cursor(dictionary=True)   

        print('---consultarAgendas--')
        print(idEmpreend)

    #    query =  "select * from " + MySql.DB_NAME + ".tb_agendas where id_empreendimento = " +  str (idEmpreend) + " order by dt_atividade"
        query = "select A.id_empreendimento, A.mes_vigencia, A.ano_vigencia, A.id_atividade, AT.descr_atividade, A.status, A.dt_atividade, A.nm_resp_atividade, A.dt_baixa, A.nm_resp_baixa from " + MySql.DB_NAME + ".tb_agendas A inner join  " + MySql.DB_NAME + ".tb_agendas_atividades AT on A.id_atividade = AT.id_atividade where A.id_empreendimento= " +  str (idEmpreend) + " order by A.dt_atividade"

        print('-----------------')
        print(query)
        print('-----------------')
        
        cursor.execute(query)

        lista = cursor.fetchall()
        
        listaAgendas = []

        for x in lista:
            a = agenda()
            a.setIdEmpreend(x['id_empreendimento'])
            a.setMesVigencia(x['mes_vigencia'])
            a.setAnoVigencia(x['ano_vigencia'])
            a.setIdAtividade(x['id_atividade'])
            a.setDescrAtividade(x['descr_atividade'])                    
            a.setStatus(x['status'])
            a.setDtAtividade(x['dt_atividade'])
            a.setNmRespAtividade(x['nm_resp_atividade'])
            a.setDtBaixa(x['dt_baixa'])
            a.setNmRespBaixa(x['nm_resp_baixa'])
            listaAgendas.append(a)
            
        cursor.close()
        MySql.close(self.__connection)
        return listaAgendas

    def consultarAgendaPeloId(self, idAgenda):
        self.__connection = MySql.connect()
        cursor = self.__connection.cursor(dictionary=True)   

        query =  "select id_agenda, id_empreendimento, nm_agenda, qt_unidade from " + MySql.DB_NAME + ".tb_agendas where id_agenda = " + str(idAgenda) 
    
        print(query)

        cursor.execute(query)

        linha = cursor.fetchone()
        print('+++++++++++++++++++++++++++')
        print (linha)
        print(linha['id_agenda'])
        print('+++++++++++++++++++++++++++')

        linhaT = agenda()
        linhaT.setIdAgenda(linha['id_agenda'])
        linhaT.setIdEmpreend(linha['id_empreendimento'])
        linhaT.setNmAgenda(linha['nm_agenda'])
        linhaT.setQtUnidade(linha['qt_unidade'])
    
        print('------------------------')       
        print(linhaT.getIdAgenda())
        print('------------------------')
        cursor.close()
        MySql.close(self.__connection)

        return linhaT

    def consultarNomeAgenda(self, idAgenda):
        self.__connection = MySql.connect()
        cursor = self.__connection.cursor(dictionary=True)   

        query =  "select nm_agenda from " + MySql.DB_NAME + ".tb_agendas where id_agenda = " + str(idAgenda) 
    
        print('-----------consultarNomeAgenda----------')
        print(query)

        cursor.execute(query)

        linha = cursor.fetchone()
    #    print('+++++++++++++++++++++++++++')
    #    print (linha)

        linhaT = agenda()
        linhaT.setNmAgenda(linha['nm_agenda'])
        nmAgenda = linha['nm_agenda']
     #   print('------------------------')   
     #   print(nmAgenda)
     #   print('-----------fim consultarNomeAgenda----------')
        cursor.close()
        MySql.close(self.__connection)

        return nmAgenda

    def salvarAgenda(self,agenda):
        self.__connection = MySql.connect()
        cursor = self.__connection.cursor()   

        query =  "update " + MySql.DB_NAME + ".tb_agendas set " + \
        "nm_agenda = '" + agenda.getNmAgenda() + "', " + "qt_unidade = '" + agenda.getQtUnidade() + "' " + " where id_agenda = " + str(agenda.getIdAgenda())

        print (query)
        cursor.execute(query)

        self.__connection.commit()     
        print(cursor.rowcount,"Agenda atualizada com sucesso")     
        cursor.close()
        MySql.close(self.__connection)

    def excluirAgenda(self,idAgenda):
        self.__connection = MySql.connect()
        cursor = self.__connection.cursor()   

#        print (emp)

        query =  "delete from " + MySql.DB_NAME + ".tb_Agendas" + " where id_agenda = " + str(idAgenda) 
        print (query)

        cursor.execute(query)
        self.__connection.commit()   
        cursor.close()
        MySql.close(self.__connection)
     
 