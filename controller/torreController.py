#controller or business logic
# Trata base de TORRES

from dto.torre import torre
from utils.dbContext import MySql

class torreController:
    __connection = None

    def __init__(self):
        pass

    def inserirTorre(self, torre):
        self.__connection = MySql.connect()
        cursor = self.__connection.cursor()       
   
        query =  "INSERT INTO " + MySql.DB_NAME + ".tb_torres ( id_empreendimento, nm_torre, qt_unidade ) VALUES (" + str(torre.getIdEmpreend()) + ", '" + torre.getNmTorre() + "', " + torre.getQtUnidade() + ")"
                                                                                                                                                          
        print('++++++++++++++++++++++')
        print(query)
        print('++++++++++++++++++++++')

        cursor.execute(query)

        self.__connection.commit()     
        print(cursor.rowcount,"Torre cadastrada com sucesso")     
        cursor.close()
        MySql.close(self.__connection)


    def consultarTorres(self, idEmpreend):
        self.__connection = MySql.connect()
        cursor = self.__connection.cursor()   

        print('---consultarTorres--')
        print(idEmpreend)

        query =  "select * from " + MySql.DB_NAME + ".tb_torres where id_empreendimento = " +  str (idEmpreend) + " order by nm_torre"

        print('-----------------')
        print(query)
        print('-----------------')
        
        cursor.execute(query)

        lista = cursor.fetchall()
        
        listatorres = []

        for x in lista:
            t = torre()
            t.setIdTorre(x[0])
            t.setIdEmpreend(x[1])
            t.setNmTorre(x[2])
            t.setQtUnidade(x[3])
            listatorres.append(t)
            
        cursor.close()
        MySql.close(self.__connection)
        return listatorres

    def consultarTorrePeloId(self, idTorre):
        self.__connection = MySql.connect()
        cursor = self.__connection.cursor(dictionary=True)   

        query =  "select id_torre, id_empreendimento, nm_torre, qt_unidade from " + MySql.DB_NAME + ".tb_torres where id_torre = " + str(idTorre) 
    
        print(query)

        cursor.execute(query)

        linha = cursor.fetchone()
        print('+++++++++++++++++++++++++++')
        print (linha)
        print(linha['id_torre'])
        print('+++++++++++++++++++++++++++')

        linhaT = torre()
        linhaT.setIdTorre(linha['id_torre'])
        linhaT.setIdEmpreend(linha['id_empreendimento'])
        linhaT.setNmTorre(linha['nm_torre'])
        linhaT.setQtUnidade(linha['qt_unidade'])
    
        print('------------------------')       
        print(linhaT.getIdTorre())
        print('------------------------')
        cursor.close()
        MySql.close(self.__connection)

        return linhaT

    def consultarNomeTorre(self, idTorre):
        self.__connection = MySql.connect()
        cursor = self.__connection.cursor(dictionary=True)   

        query =  "select nm_torre from " + MySql.DB_NAME + ".tb_torres where id_torre = " + str(idTorre) 
    
        print('-----------consultarNomeTorre----------')
        print(query)

        cursor.execute(query)

        linha = cursor.fetchone()
    #    print('+++++++++++++++++++++++++++')
    #    print (linha)

        linhaT = torre()
        linhaT.setNmTorre(linha['nm_torre'])
        nmTorre = linha['nm_torre']
     #   print('------------------------')   
     #   print(nmTorre)
     #   print('-----------fim consultarNomeTorre----------')
        cursor.close()
        MySql.close(self.__connection)

        return nmTorre

    def salvarTorre(self,torre):
        self.__connection = MySql.connect()
        cursor = self.__connection.cursor()   

        query =  "update " + MySql.DB_NAME + ".tb_torres set " + \
        "nm_torre = '" + torre.getNmTorre() + "', " + "qt_unidade = '" + torre.getQtUnidade() + "' " + " where id_torre = " + str(torre.getIdTorre())

        print (query)
        cursor.execute(query)

        self.__connection.commit()     
        print(cursor.rowcount,"Torre atualizada com sucesso")     
        cursor.close()
        MySql.close(self.__connection)

    def excluirTorre(self,idTorre):
        self.__connection = MySql.connect()
        cursor = self.__connection.cursor()   

#        print (emp)

        query =  "delete from " + MySql.DB_NAME + ".tb_torres" + " where id_torre = " + str(idTorre) 
        print (query)

        cursor.execute(query)
        self.__connection.commit()   
        cursor.close()
        MySql.close(self.__connection)
     
 