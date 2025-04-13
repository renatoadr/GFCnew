# controller or business logic
# Trata base de UNIDADES

from controller.torreController import torreController
from dto.unidade import unidade
from utils.dbContext import MySql


class unidadeController:
    __connection = None

    def inserirUnidade(self, unidade):
        self.__connection = MySql.connect()
        cursor = self.__connection.cursor()

        query = f"""INSERT INTO {MySql.DB_NAME}.tb_unidades (id_empreendimento, id_torre, unidade, mes_vigencia, ano_vigencia, vl_unidade, status, cpf_cnpj_comprador, vl_pago, financiado, vl_chaves, vl_pre_chaves, vl_pos_chaves) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""

        print('++++++++++++++++++++++')
        print(query)
        print('++++++++++++++++++++++')

        cursor.execute(query, (
            unidade.getIdEmpreend(),
            unidade.getIdTorre(),
            unidade.getUnidade(),
            unidade.getMesVigencia(),
            unidade.getAnoVigencia(),
            unidade.getVlUnidade(),
            unidade.getStatus(),
            unidade.getCpfComprador(),
            unidade.getVlPago(),
            unidade.getFinanciado(),
            unidade.getVlChaves(),
            unidade.getVlPreChaves(),
            unidade.getVlPosChaves(),
        )
        )

        self.__connection.commit()
        print(cursor.rowcount, "Unidade cadastrada com sucesso")
        cursor.close()
        MySql.close(self.__connection)

    def consultarUnidades(self, idEmpreend):
        self.__connection = MySql.connect()
        cursor = self.__connection.cursor(dictionary=True)

        print('---consultarUnidades--')
        print(idEmpreend)

        query = f"""SELECT uni.id_unidade, uni.id_empreendimento, uni.id_torre, uni.unidade, uni.status, tor.nm_torre
        FROM {MySql.DB_NAME}.tb_unidades uni
        INNER JOIN {MySql.DB_NAME}.tb_torres tor
        ON uni.id_torre = tor.id_torre
        WHERE uni.id_empreendimento = %s
        AND uni.ac_historico IS NULL
        ORDER by tor.nm_torre, uni.unidade;"""

        print('-----------------')
        print(query)
        print('-----------------')

        cursor.execute(query, (idEmpreend,))

        lista = cursor.fetchall()
        listaunids = []

        for x in lista:
            u = unidade()
            u.setIdUnidade(x['id_unidade'])
            u.setIdEmpreend(x['id_empreendimento'])
            u.setIdTorre(x['id_torre'])
            u.setNmTorre(x['nm_torre'])
            u.setUnidade(x['unidade'])
            u.setStatus(x['status'])
            listaunids.append(u)

        cursor.close()
        MySql.close(self.__connection)
        return listaunids

    def consultarUnidadePeloId(self, idUnidade):
        self.__connection = MySql.connect()
        cursor = self.__connection.cursor(dictionary=True)

        print('+++++++++ consultarUnidadePeloId ++++++++++++++++++')

        query = """SELECT und.*, cli.nm_cliente  FROM """ + MySql.DB_NAME + \
            """.tb_unidades und LEFT JOIN  db_gfc.tb_clientes cli ON und.cpf_cnpj_comprador = cli.cpf_cnpj WHERE id_unidade = %s """

        print(query)

        cursor.execute(query, (idUnidade,))

        linha = cursor.fetchone()
        print('+++++++++++++++++++++++++++')
        print(linha)
        print(linha['id_torre'])
        print(linha['id_unidade'])
        print('+++++++++++++++++++++++++++')

        linhaU = unidade()
        linhaU.setIdUnidade(linha['id_unidade'])
        linhaU.setNmComprador(linha['nm_cliente'])
        linhaU.setIdTorre(linha['id_torre'])
        linhaU.setIdEmpreend(linha['id_empreendimento'])
        linhaU.setUnidade(linha['unidade'])
        linhaU.setMesVigencia(linha['mes_vigencia'])
        linhaU.setAnoVigencia(linha['ano_vigencia'])
        linhaU.setVlUnidade(linha['vl_unidade'])
        linhaU.setStatus(linha['status'])
        linhaU.setCpfComprador(linha['cpf_cnpj_comprador'])
        linhaU.setVlPago(linha['vl_pago'])
        linhaU.setDtOcorrencia(linha['dt_ocorrencia'])
        linhaU.setFinanciado(linha['financiado'])
        linhaU.setVlChaves(linha['vl_chaves'])
        linhaU.setVlPreChaves(linha['vl_pre_chaves'])
        linhaU.setVlPosChaves(linha['vl_pos_chaves'])

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

        query = "select count(id_unidade), sum(vl_chaves), sum(vl_pre_chaves), sum(vl_pos_chaves) from " + \
            MySql.DB_NAME + ".tb_unidades where id_empreendimento = " + \
                idEmpreend + " and status != 'distrato'"

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
        print(linhaU.getQtUnidade(), linhaU.getTtChaves(),
              linhaU.getTtPreChaves(), linhaU.getTtPosChaves())
        print('------------------------')
        cursor.close()
        MySql.close(self.__connection)

        return linhaU

    def consultarUnidadeVendas(self, idEmpreend):
        self.__connection = MySql.connect()
        cursor = self.__connection.cursor()

        print('+++++++++ consultarUnidadeVendas ++++++++++++++++++')

        query = "select status, count(id_unidade) from " + MySql.DB_NAME + ".tb_unidades where id_empreendimento = " + str(
            idEmpreend) + " and status != 'distrato' group by status"
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

        query = "select status, sum(vl_pago), sum(vl_unidade) from " + MySql.DB_NAME + ".tb_unidades where id_empreendimento = " + str(
            idEmpreend) + " and status in ('vendido', 'estoque') group  by status"

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

    def salvarUnidade(self, unidade):
        self.__connection = MySql.connect()
        cursor = self.__connection.cursor()

        query = "UPDATE " + MySql.DB_NAME + """.tb_unidades SET
      id_torre = %s,
      id_empreendimento = %s,
      unidade = %s,
      mes_vigencia = %s,
      ano_vigencia = %s,
      vl_unidade = %s,
      status = %s,
      cpf_cnpj_comprador = %s,
      vl_pago = %s,
      dt_ocorrencia = %s,
      financiado = %s,
      vl_chaves = %s,
      vl_pre_chaves = %s,
      vl_pos_chaves = %s
      WHERE id_unidade = %s; """

        print(query)
        cursor.execute(query, (
            unidade.getIdTorre(),
            unidade.getIdEmpreend(),
            unidade.getUnidade(),
            unidade.getMesVigencia(),
            unidade.getAnoVigencia(),
            unidade.getVlUnidade(),
            unidade.getStatus(),
            unidade.getCpfComprador(),
            unidade.getVlPago(),
            unidade.getDtOcorrencia(),
            unidade.getFinanciado(),
            unidade.getVlChaves(),
            unidade.getVlPreChaves(),
            unidade.getVlPosChaves(),
            unidade.getIdUnidade()
        ))

        self.__connection.commit()
        print(cursor.rowcount, "Unidade atualizada com sucesso")
        cursor.close()
        MySql.close(self.__connection)

    def excluirUnidade(self, idUnidade):
        query = f"UPDATE {MySql.DB_NAME}.tb_unidades SET ac_historico = 'DELETADO' where id_unidade = %s"
        MySql.exec(query, (idUnidade,))

    def existeUnidadesPorTorre(self, idTorre):
        query = "SELECT COUNT(id_unidade) total FROM " + MySql.DB_NAME + \
            """.tb_unidades WHERE id_torre = %s;"""
        ret = MySql.getAll(query, (idTorre,))
        return ret[0]['total'] > 0

    def mudarHistoricoEditado(self, idUnidade):
        query = f"UPDATE {MySql.DB_NAME}.tb_unidades SET ac_historico = 'EDITADO' where id_unidade = %s"
        MySql.exec(query, (idUnidade,))
