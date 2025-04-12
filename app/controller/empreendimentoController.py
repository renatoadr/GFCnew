# controller or business logic
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

        query = "INSERT INTO " + MySql.DB_NAME + \
            """.tb_empreendimentos (apelido, nm_empreendimento, logradouro, bairro, cidade, estado, cep, nm_incorporador, nm_construtor, nm_banco, cpf_cnpj_engenheiro, vl_plano_empresario, indice_garantia, previsao_entrega) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""

        print(query)
        cursor.execute(query, (
            empreend.getApelido(),
            empreend.getNmEmpreend(),
            empreend.getLogradouro(),
            empreend.getBairro(),
            empreend.getCidade(),
            empreend.getEstado(),
            empreend.getCep(),
            empreend.getNmIncorp(),
            empreend.getNmConstrutor(),
            empreend.getNmBanco(),
            empreend.getCpfCnpjEngenheiro(),
            empreend.getVlPlanoEmp(),
            empreend.getIndiceGarantia(),
            empreend.getPrevisaoEntrega()
        ))

        self.__connection.commit()
        print(cursor.rowcount, "Empreendimento cadastrado com sucesso")
        cursor.close()
        MySql.close(self.__connection)

    def consultarEmpreendimentos(self):
        self.__connection = MySql.connect()
        print(self.__connection)
        cursor = self.__connection.cursor()

        query = "select * from " + MySql.DB_NAME + ".tb_empreendimentos"

        cursor.execute(query)

        lista = cursor.fetchall()

        listaEmps = []

        for x in lista:
            e = empreendimento()
            e.setIdEmpreend(x[0])
            e.setNmEmpreend(x[1])
            e.setApelido(x[2])
            listaEmps.append(e)

        cursor.close()
        MySql.close(self.__connection)
        return listaEmps

    def consultarEmpreendimentoPeloId(self, idEmpreend):
        self.__connection = MySql.connect()
        cursor = self.__connection.cursor(dictionary=True)

        query = """SELECT emp.*, cli.nm_cliente  FROM """ + MySql.DB_NAME + \
            """.tb_empreendimentos emp LEFT JOIN  db_gfc.tb_clientes cli ON emp.cpf_cnpj_engenheiro = cli.cpf_cnpj WHERE emp.id_empreendimento = %s;"""
        print(query)

        cursor.execute(query, (idEmpreend,))

        linha = cursor.fetchone()
        print('+++++++++++++++++++++++++++')
        print(linha)
        print(linha['id_empreendimento'])
        print(linha['nm_empreendimento'])
        print('+++++++++++++++++++++++++++')

        linhaE = empreendimento()
        linhaE.setApelido('' if linha['apelido'] is None else linha['apelido'])
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
        linhaE.setNmEngenheiro(linha['nm_cliente'])
        linhaE.setCpfCnpjEngenheiro(linha['cpf_cnpj_engenheiro'])
        linhaE.setVlPlanoEmp(linha['vl_plano_empresario'])
        linhaE.setIndiceGarantia(linha['indice_garantia'])
        linhaE.setPrevisaoEntrega(linha['previsao_entrega'])

        print('------------------------')
        print(linhaE.getIdEmpreend())
        print('------------------------')
        cursor.close()
        MySql.close(self.__connection)

        return linhaE

    def excluirEmpreendimento(self, idEmpreend):
        self.__connection = MySql.connect()
        cursor = self.__connection.cursor()

#        print (emp)

        query = "delete from " + MySql.DB_NAME + ".tb_empreendimentos" + \
            " where id_empreendimento = " + str(idEmpreend)
        print(query)

        cursor.execute(query)
        self.__connection.commit()
        cursor.close()
        MySql.close(self.__connection)

    def salvarEmpreendimento(self, empreend):
        self.__connection = MySql.connect()
        cursor = self.__connection.cursor()

        query = """update """ + MySql.DB_NAME + """.tb_empreendimentos set
         apelido = %s,
         nm_empreendimento = %s,
         logradouro = %s,
         bairro = %s,
         cidade = %s,
         estado = %s,
         cep = %s,
         nm_incorporador = %s,
         nm_construtor = %s,
         nm_banco = %s,
         cpf_cnpj_engenheiro = %s,
         vl_plano_empresario = %s,
         indice_garantia = %s,
         previsao_entrega = %s
         where id_empreendimento = %s ;"""

        print(query)
        cursor.execute(query, (
            empreend.getApelido(),
            empreend.getNmEmpreend(),
            empreend.getLogradouro(),
            empreend.getBairro(),
            empreend.getCidade(),
            empreend.getEstado(),
            empreend.getCep(),
            empreend.getNmIncorp(),
            empreend.getNmConstrutor(),
            empreend.getNmBanco(),
            empreend.getCpfCnpjEngenheiro(),
            empreend.getVlPlanoEmp(),
            empreend.getIndiceGarantia(),
            empreend.getPrevisaoEntrega(),
            empreend.getIdEmpreend()
        ))

        self.__connection.commit()
        print(cursor.rowcount, "Empreendimento atualizado com sucesso")
        cursor.close()
        MySql.close(self.__connection)
