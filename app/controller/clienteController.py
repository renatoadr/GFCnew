# controller or business logic
# Trata base de CLIENTES

from dto.cliente import cliente
from utils.dbContext import MySql


class clienteController:
    __connection = None

    def __init__(self):
        pass

    @staticmethod
    def getCliente(cpfCnpj: str) -> str:
        cliC = clienteController()
        return cliC.consultaClientePorCpf(cpfCnpj)

    def inserirCliente(self, cliente):
        self.__connection = MySql.connect()
        cursor = self.__connection.cursor()

        query = "INSERT INTO " + MySql.DB_NAME + ".tb_clientes ( cpf_cnpj, tp_cpf_cnpj, nm_cliente, ddd, tel, email ) VALUES ('" + cliente.getCpfCnpj(
        ) + "', '" + cliente.getTpCpfCnpj() + "', '" + cliente.getNmCliente() + "', '" + cliente.getDdd() + "', '" + cliente.getTel() + "', '" + cliente.getEmail() + "')"

        print('++++++++++++++++++++++')
        print(query)
        print('++++++++++++++++++++++')

        cursor.execute(query)

        self.__connection.commit()
        print(cursor.rowcount, "Cliente cadastrado com sucesso")
        cursor.close()
        MySql.close(self.__connection)

    def consultarClientes(self, search=None):
        self.__connection = MySql.connect()
        cursor = self.__connection.cursor()

        print('---consultarTorres--')

        if search is None:
            query = "select * from " + MySql.DB_NAME + ".tb_clientes"
        else:
            query = "select * from " + MySql.DB_NAME + \
                ".tb_clientes where lower(nm_cliente) like '%" + search + "%' "
        print('-----------------')
        print(query)
        print('-----------------')

        cursor.execute(query)

        lista = cursor.fetchall()

        listaClientes = []

        for x in lista:
            t = cliente()
            t.setCpfCnpj(x[0])
            t.setTpCpfCnpj(x[1])
            t.setNmCliente(x[2])
            t.setDdd(x[3])
            t.setTel(x[4])
            t.setEmail(x[5])
            listaClientes.append(t)

        cursor.close()
        MySql.close(self.__connection)
        return listaClientes

    def consultarClientePeloId(self, idCli):
        self.__connection = MySql.connect()
        cursor = self.__connection.cursor(dictionary=True)

        query = "select cpf_cnpj, tp_cpf_cnpj, nm_cliente, ddd, tel, email from " + \
            MySql.DB_NAME + ".tb_clientes where cpf_cnpj = '" + idCli + "'"

        print(query)

        cursor.execute(query)

        linha = cursor.fetchone()

        if linha is None:
            return None

        print('+++++++++++++++++++++++++++')
        print(linha)
        print(linha['cpf_cnpj'])
        print('+++++++++++++++++++++++++++')

        linhaC = cliente()
        linhaC.setCpfCnpj(linha['cpf_cnpj'])
        linhaC.setTpCpfCnpj(linha['tp_cpf_cnpj'])
        linhaC.setNmCliente(linha['nm_cliente'])
        linhaC.setDdd(linha['ddd'])
        linhaC.setTel(linha['tel'])
        linhaC.setEmail(linha['email'])

        print('------------------------')
        print(linhaC.getCpfCnpj())
        print('------------------------')
        cursor.close()
        MySql.close(self.__connection)

        return linhaC

    def salvarCliente(self, cliente):
        self.__connection = MySql.connect()
        cursor = self.__connection.cursor()

        query = "UPDATE " + MySql.DB_NAME + \
            """.tb_clientes SET cpf_cnpj = %s, tp_cpf_cnpj = %s, nm_cliente = %s, ddd = %s, tel = %s, email = %s WHERE cpf_cnpj = %s """

        print(query)
        cursor.execute(query, (
            cliente.getCpfCnpj(),
            cliente.getTpCpfCnpj(),
            cliente.getNmCliente(),
            cliente.getDdd(),
            cliente.getTel(),
            cliente.getEmail(),
            cliente.getCpfCnpj()
        )
        )

        self.__connection.commit()
        print(cursor.rowcount, "Torre atualizada com sucesso")
        cursor.close()
        MySql.close(self.__connection)

    def excluirCliente(self, cliente):
        self.__connection = MySql.connect()
        cursor = self.__connection.cursor()

        query = "delete from " + MySql.DB_NAME + \
            ".tb_clientes" + " where cpf_cnpj = " + str(cliente)
        print(query)

        cursor.execute(query)
        self.__connection.commit()
        cursor.close()
        MySql.close(self.__connection)

    def existeCliente(self, doc):
        self.__connection = MySql.connect()
        cursor = self.__connection.cursor()
        query = "SELECT COUNT(*) FROM " + MySql.DB_NAME + \
            """.tb_clientes WHERE cpf_cnpj = %s"""
        cursor.execute(query, (doc,))
        result = cursor.fetchone()
        cursor.close()
        MySql.close(self.__connection)
        return result[0] > 0

    def consultaClientePorCpf(self, nrCpf):
        self.__connection = MySql.connect()
        cursor = self.__connection.cursor()
        query = "SELECT nm_cliente FROM " + MySql.DB_NAME + \
            """.tb_clientes WHERE cpf_cnpj = %s"""
        cursor.execute(query, (nrCpf,))
        result = cursor.fetchone()
        cursor.close()
        MySql.close(self.__connection)
        return result[0]
