#controller or business logic
# Trata base de UNIDADES

from controller.torreController import torreController
from dto.unidade import unidade
from dto.torre import torre
from utils.dbContext import MySql

class unidadeController:
    __connection = None

    def __init__(self):
        pass

    def inserirUnidade(self, unidade):
        self.__connection = MySql.connect()
        cursor = self.__connection.cursor()       
   
#        query =  "INSERT INTO " + MySql.DB_NAME + ".tb_unidades ( id_empreendimento, id_torre, unidade, mes_vigencia, ano_vigencia, vl_unidade, status, nm_comprador, vl_pago,  dt_ocorrencia, financiado, vl_chaves ) VALUES (" +  str(unidade.getIdEmpreend()) + ", " + str(unidade.getIdTorre()) + ", '" +  unidade.getUnidade() + "', '" +  unidade.getMesVigencia() + "', '" +  unidade.getAnoVigencia() + "', " +   str(unidade.getVlUnidade()) + ", '" + unidade.getStatus() + "', '" +  unidade.getNmComprador() + "', " + str(unidade.getVlPago()) + ", '" + unidade.getDtOcorrencia() + "', '" +  unidade.getFinanciado() + "', " + str(unidade.getVlChaves()) + ")"

        query =  "INSERT INTO " + MySql.DB_NAME + ".tb_unidades ( id_empreendimento, id_torre, unidade, mes_vigencia, ano_vigencia, vl_unidade, status, nm_comprador, vl_pago, dt_ocorrencia, financiado, vl_chaves) VALUES (" + str(unidade.getIdEmpreend()) + ", " + str(unidade.getIdTorre()) + ", '" +  unidade.getUnidade() + "', '" + unidade.getMesVigencia() + "', '" +  unidade.getAnoVigencia() +  "', " + unidade.getVlUnidade()  + ", '" + unidade.getStatus() + "', '" + unidade.getNmComprador() + "', " + unidade.getVlPago()  + ", '" + unidade.getDtOcorrencia() + "', '" +  unidade.getFinanciado() + "', " + unidade.getVlChaves() + ")"
                                                                                                                                                          
        print('++++++++++++++++++++++')
        print(query)
        print('++++++++++++++++++++++')

        cursor.execute(query)

        self.__connection.commit()     
        print(cursor.rowcount,"Unidade cadastrada com sucesso")     
        cursor.close()
        MySql.close(self.__connection)


    def consultarUnidades(self, idEmpreend):
        self.__connection = MySql.connect()
        cursor = self.__connection.cursor(dictionary=True)   

        print('---consultarUnidades--')
        print(idEmpreend)

        query = "select U.id_unidade, U.id_empreendimento, U.id_torre, U.unidade, T.nm_torre from " + MySql.DB_NAME + ".tb_unidades U inner join  " + MySql.DB_NAME + ".tb_torres T on U.id_torre = T.id_torre where U.id_empreendimento= " +  str (idEmpreend) + " order by T.nm_torre, U.unidade"

        print('-----------------')
        print(query)
        print('-----------------')
      
        cursor.execute(query)

        lista = cursor.fetchall()
        listaunids = []
        
#        idTorreAnterior = -1
#        torreC = torreController ()

        for x in lista:
            u = unidade()
            u.setIdUnidade(x['id_unidade'])
            u.setIdEmpreend(x['id_empreendimento'])
            u.setIdTorre(x['id_torre'])
#            idTorreAtual = u.getIdTorre()
#            print ('----> ', idTorreAnterior, idTorreAtual)
 
#            if idTorreAnterior != idTorreAtual:
#               print('entrei para consultar o id_torre== ', idTorreAtual )
#               nmTorre = torreC.consultarNomeTorre (idTorreAtual)
#               print (idTorreAnterior, idTorreAtual, nmTorre)
#               idTorreAnterior = idTorreAtual
            u.setNmTorre(x['nm_torre'])
            u.setUnidade(x['unidade'])
            listaunids.append(u)
                
        cursor.close()
        MySql.close(self.__connection)
        return listaunids

    def consultarUnidadePeloId(self, idUnidade):
        self.__connection = MySql.connect()
        cursor = self.__connection.cursor(dictionary=True)   

        print('+++++++++ consultarUnidadePeloId ++++++++++++++++++')
        
        query =  "select id_unidade, id_empreendimento, id_torre, unidade, mes_vigencia, ano_vigencia, vl_unidade, status, cpf_comprador, vl_pago, dt_ocorrencia, financiado, vl_chaves, vl_pre_chaves, vl_pos_chaves from " + MySql.DB_NAME + ".tb_unidades where id_unidade = " + str(idUnidade)
    
        print(query)

        cursor.execute(query)
       
        linha = cursor.fetchone()
        print('+++++++++++++++++++++++++++')
        print (linha)
        print(linha['id_torre'])
        print(linha['id_unidade'])
        print('+++++++++++++++++++++++++++')

        linhaU = unidade()
        linhaU.setIdUnidade(linha['id_unidade'])
        linhaU.setIdTorre(linha['id_torre'])
        linhaU.setIdEmpreend(linha['id_empreendimento'])
        linhaU.setUnidade(linha['unidade'])
        linhaU.setMesVigencia(linha['mes_vigencia'])
        linhaU.setAnoVigencia(linha['ano_vigencia'])
        linhaU.setVlUnidade(linha['vl_unidade'])
        linhaU.setStatus(linha['status'])
        linhaU.setNmComprador(linha['cpf_comprador'])
        linhaU.setVlPago(linha['vl_pago'])
        linhaU.setDtOcorrencia(linha['dt_ocorrencia'])
        linhaU.setFinanciado(linha['financiado'])
        linhaU.setVlChaves(linha['vl_chaves'])
        linhaU.setVlChaves(linha['vl_pre_chaves'])
        linhaU.setVlChaves(linha['vl_pos_chaves'])

        print('------------------------')       
        print(linhaU.getIdUnidade())
        print('------------------------')
        cursor.close()
        MySql.close(self.__connection)

        return linhaU

    def consultarUnidadeChaves(self, idEmpreend):
        self.__connection = MySql.connect()
        cursor = self.__connection.cursor()   

        print('+++++++++ consultarUnidadeChaves ++++++++++++++++++')
        
        query = "select count(id_unidade), sum(vl_chaves), sum(vl_pre_chaves), sum(vl_pos_chaves) from " + MySql.DB_NAME + ".tb_unidades where id_empreendimento = " + idEmpreend + " and status != 'distrato'"
    
        print(query)

        cursor.execute(query)
       
        linha = cursor.fetchone()
        print('+++++++++++++++++++++++++++')

        print('+++++++++++++++++++++++++++')

        linhaU = unidade()
        linhaU.setQtUnidade(linha[0])
        linhaU.setTtChaves(linha[1])
        linhaU.setTtPreChaves(linha[2])
        linhaU.setTtPosChaves(linha[3])

        print('------------------------')       
        print(linhaU.getQtUnidade(), linhaU.getTtChaves(), linhaU.getTtPreChaves(), linhaU.getTtPosChaves())
        print('------------------------')
        cursor.close()
        MySql.close(self.__connection)

        return linhaU

    def consultarUnidadeVendas(self, idEmpreend):
        self.__connection = MySql.connect()
        cursor = self.__connection.cursor()   

        print('+++++++++ consultarUnidadeVendas ++++++++++++++++++')
        
        query =  "select status, count(id_unidade) from " + MySql.DB_NAME + ".tb_unidades where id_empreendimento = " + str(idEmpreend) + " and status != 'distrato' group by status" 
        print(query)
        
        cursor.execute(query)

        lista = cursor.fetchall()
        listaVendas = []
        
        for x in lista:
            u = unidade()
            u.setStatus(x[0])
            u.setTtStatus(x[1])
            listaVendas.append(u)
                
        cursor.close()

        MySql.close(self.__connection)

        return listaVendas

    def consultarUnidadeRecebibeis(self, idEmpreend):
        self.__connection = MySql.connect()
        cursor = self.__connection.cursor()   

        print('+++++++++ consultarUnidadeRecebibeis ++++++++++++++++++')
        
        query = "select status, sum(vl_pago), sum(vl_unidade) from " + MySql.DB_NAME + ".tb_unidades where id_empreendimento = " + str(idEmpreend) + " and status in ('vendido', 'estoque') group  by status"

        print(query)
        
        cursor.execute(query)

        lista = cursor.fetchall()
        listaVendas = []
        
        for x in lista:
            u = unidade()
            u.setStatus(x[0])
            u.setTtVenda(x[1])
            u.setTtEstoque(x[2])
            listaVendas.append(u)
                
        cursor.close()

        MySql.close(self.__connection)

        return listaVendas

    def salvarUnidade(self,unidade):
        self.__connection = MySql.connect()
        cursor = self.__connection.cursor()   

        query =  "update " + MySql.DB_NAME + ".tb_unidades set " + \
        "id_torre = '" + unidade.getIdTorre() + "', " + \
        "id_empreendimento = '" + unidade.getIdEmpreend() + \
        "', " + "unidade = '" + unidade.getUnidade() + "', " + \
        "mes_vigencia = '" + unidade.getMesVigencia() + "', " + \
        "ano_vigencia = '" + unidade.getAnoVigencia() + "', " + \
        "vl_unidade = '" + unidade.getVlUnidade() + "', " + \
        "status = '" + unidade.getStatus() + "', " + \
        "cpf_comprador = '" + unidade.getCpfComprador() + "', " + \
        "vl_pago = '" + unidade.getVlPago() + "', " + \
        "dt_ocorrencia = '" + unidade.getDtOcorrencia() + "', " + \
        "financiado = '" + unidade.getFinanciado() + "', " + \
        "vl_chaves = '" + unidade.getVlChaves() + "' " + \
        "vl_pre_chaves = '" + unidade.getVlPreChaves() + "' " + \
        "vl_pos_chaves = '" + unidade.getVlPosChaves() + "' " + \
        "where id_unidade = " + str(unidade.getIdUnidade())

        print (query)
        cursor.execute(query)

        self.__connection.commit()     
        print(cursor.rowcount,"Unidade atualizada com sucesso")     
        cursor.close()
        MySql.close(self.__connection)

    def excluirUnidade(self,idUnidade):
        self.__connection = MySql.connect()
        cursor = self.__connection.cursor()   

#        print (emp)

        query =  "delete from " + MySql.DB_NAME + ".tb_unidades" + " where id_unidade = " + str(idUnidade) 
        print (query)

        cursor.execute(query)
        self.__connection.commit()   
        cursor.close()
        MySql.close(self.__connection)
     
 