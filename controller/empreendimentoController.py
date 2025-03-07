#controller or business logic
# Trata base de EMPREENDIMENTO


from dto.empreendimento import empreendimento
from utils.dbContext import MySql

class empreendimentoController:
    __connection = None

    def __init__(self):
        pass

    def inserirEmpreendimento(self, empreend):
        self.__connection = MySql.connect()
        cursor = self.__connection.cursor()   

        query =  "INSERT INTO " + MySql.DB_NAME + ".tb_empreendimentos (nm_empreendimento, logradouro, bairro, cidade, estado, cep, nm_incorporador, nm_construtor, nm_banco, nm_engenheiro, vl_plano_empresario, indice_garantia, previsao_entrega) VALUES ('" +  empreend.getNmEmpreend() + "', '" + empreend.getLogradouro() + "', '" +  empreend.getBairro() + "', '" + empreend.getCidade() + "', '" +  empreend.getEstado() + "', '" +  empreend.getCep() + "', '" + empreend.getNmIncorp() + "', '" +  empreend.getNmConstrutor() + "', '" + empreend.getNmBanco() + "', '" + empreend.getNmEngenheiro() + "', " +  empreend.getVlPlanoEmp() + " ," + empreend.getIndiceGarantia() + ",'" + empreend.getPrevisaoEntrega() + "')"
    
        print (query)
        cursor.execute(query)

        self.__connection.commit()     
        print(cursor.rowcount,"Empreendimento cadastrado com sucesso")     
        cursor.close()
        MySql.close(self.__connection)


    def consultarEmpreendimentos(self):
        self.__connection = MySql.connect()
        cursor = self.__connection.cursor()   

        query =  "select * from " + MySql.DB_NAME + ".tb_empreendimentos"  
    
        cursor.execute(query)

        lista = cursor.fetchall()
        
        listaEmps = []

        for x in lista:
            e = empreendimento()
            e.setIdEmpreend(x[0])
            e.setNmEmpreend(x[1])
            listaEmps.append(e)
            
        cursor.close()
        MySql.close(self.__connection)
        return listaEmps

    def consultarEmpreendimentoPeloId(self, idEmpreend):
        self.__connection = MySql.connect()
        cursor = self.__connection.cursor(dictionary=True)   

        query =  "select id_empreendimento, nm_empreendimento, logradouro, bairro, cidade, estado, cep,\
              nm_incorporador, nm_construtor, nm_banco, nm_engenheiro, vl_plano_empresario, indice_garantia, previsao_entrega\
              from " + MySql.DB_NAME + ".tb_empreendimentos where id_empreendimento = " + idEmpreend 
    
        print(query)

        cursor.execute(query)

        linha = cursor.fetchone()
        print('+++++++++++++++++++++++++++')
        print (linha)
        print(linha['id_empreendimento'])
        print(linha['nm_empreendimento'])
        print('+++++++++++++++++++++++++++')

        linhaE = empreendimento()
        linhaE.setIdEmpreend(linha['id_empreendimento'])
        linhaE.setNmEmpreend(linha['nm_empreendimento'])
        linhaE.setNmBanco(linha['nm_banco'])
        linhaE.setNmIncorp(linha['nm_incorporador'])
        linhaE.setNmConstrutor(linha['nm_construtor'])
        linhaE.setLogradouro(linha['logradouro'])
        linhaE.setBairro(linha['bairro'])
        linhaE.setCidade(linha['cidade'])
        linhaE.setEstado(linha['estado'])
        linhaE.setCep(linha['cep'])
        linhaE.setNmEngenheiro(linha['nm_engenheiro'])
        linhaE.setVlPlanoEmp(linha['vl_plano_empresario'])
        linhaE.setIndiceGarantia(linha['indice_garantia'])
        linhaE.setPrevisaoEntrega(linha['previsao_entrega'])

        print('------------------------')       
        print(linhaE.getIdEmpreend())
        print('------------------------')
        cursor.close()
        MySql.close(self.__connection)

        return linhaE

    def excluirEmpreendimento(self,idEmpreend):
        self.__connection = MySql.connect()
        cursor = self.__connection.cursor()   

#        print (emp)

        query =  "delete from " + MySql.DB_NAME + ".tb_empreendimentos" + " where id_empreendimento = " + str(idEmpreend) 
        print (query)

        cursor.execute(query)
        self.__connection.commit()   
        cursor.close()
        MySql.close(self.__connection)
     
    def salvarEmpreendimento(self,empreend):
        self.__connection = MySql.connect()
        cursor = self.__connection.cursor()   

        query =  "update " + MySql.DB_NAME + ".tb_empreendimentos set " + \
        "nm_empreendimento = '" + empreend.getNmEmpreend() + "', " + \
        "logradouro = '" + empreend.getLogradouro() + "', " + \
        "bairro = '" + empreend.getBairro() + "', " + \
        "cidade = '" + empreend.getCidade() + "', " + \
        "estado = '" + empreend.getEstado() + "', " + \
        "cep = '" + empreend.getCep() + "', " + \
        "nm_incorporador = '" + empreend.getNmIncorp() + "', " + \
        "nm_construtor = '" + empreend.getNmConstrutor() + "', " + \
        "nm_banco = '" + empreend.getNmBanco() + "', " + \
        "nm_engenheiro = '" + empreend.getNmEngenheiro() + "', " + \
        "vl_plano_empresario = " + empreend.getVlPlanoEmp() + ", " + \
        "indice_garantia = " + empreend.getIndiceGarantia() + ", " + \
        "previsao_entrega = '" + empreend.getPrevisaoEntrega() + "' " + \
        "where id_empreendimento = " + str(empreend.getIdEmpreend())

        print (query)
        cursor.execute(query)

        self.__connection.commit()     
        print(cursor.rowcount,"Empreendimento atualizado com sucesso")     
        cursor.close()
        MySql.close(self.__connection)
