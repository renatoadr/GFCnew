# controller or business logic
# Trata base de UNIDADES

from dto.unidade import unidade
from utils.dbContext import MySql
from datetime import datetime
from copy import deepcopy
from dateutil import relativedelta
from utils.helper import diff_mes


class unidadeController:
    __connection = None

    def inserirUnidade(self, unidade):
        self.__connection = MySql.connect()
        cursor = self.__connection.cursor()

        query = f"""INSERT INTO {MySql.DB_NAME}.tb_unidades (id_empreendimento, id_torre, unidade, mes_vigencia, ano_vigencia, vl_unidade, status, cpf_cnpj_comprador, vl_receber, financiado, vl_chaves, vl_pre_chaves, vl_pos_chaves) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""

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
            unidade.getVlReceber(),
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

        query = f"""SELECT uni.id_unidade, uni.id_empreendimento, uni.id_torre, uni.unidade, uni.status, tor.nm_torre, uni.vl_unidade, cli.nm_cliente, mes_vigencia, ano_vigencia, uni.cpf_cnpj_comprador
        FROM {MySql.DB_NAME}.tb_unidades uni
        INNER JOIN {MySql.DB_NAME}.tb_torres tor
        ON uni.id_torre = tor.id_torre
        LEFT JOIN {MySql.DB_NAME}.tb_clientes cli
        ON uni.cpf_cnpj_comprador = cli.cpf_cnpj
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
            u.setCpfComprador(x['cpf_cnpj_comprador'])
            u.setMesVigencia(x['mes_vigencia'])
            u.setAnoVigencia(x['ano_vigencia'])
            if x['vl_unidade'] == None:
                u.setVlUnidade(0.00)
            else:
                ValorUnidade = x['vl_unidade']
                ValorUnidadeFormatado = f"{ValorUnidade:,.2f}".replace(
                    ",", "X").replace(".", ",").replace("X", ".")
                u.setVlUnidade(ValorUnidadeFormatado)
            nmCliente = x['nm_cliente']
            if nmCliente == None or nmCliente == 'None':
                u.setNmComprador('')
            else:
                u.setNmComprador(nmCliente)
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
        linhaU.setVlReceber(linha['vl_receber'])
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

    def consultarUnidadeChaves(self, idEmpreend, tipo):
        self.__connection = MySql.connect()
        cursor = self.__connection.cursor()

        print('+++++++++ consultarUnidadeChaves ++++++++++++++++++')

        if tipo == 'valor':
            query = f"SELECT COUNT(id_unidade) AS total_unidades, sum(vl_chaves) AS total_chaves, sum(vl_pre_chaves) AS total_pre_chaves, sum(vl_pos_chaves) AS total_pos_chaves FROM {MySql.DB_NAME}.tb_unidades WHERE id_empreendimento = %s AND (vl_chaves > 0 or vl_pre_chaves > 0 or vl_pos_chaves > 0 ) AND status != 'distrato' AND ac_historico IS NULL"
        else:
            query = f"SELECT COUNT(id_unidade) AS total_unidades, COUNT(CASE WHEN vl_chaves > 0 THEN 1 END) AS total_chaves, COUNT(CASE WHEN vl_pre_chaves > 0 THEN 1 END) AS total_pre_chaves, COUNT(CASE WHEN vl_pos_chaves > 0 THEN 1 END) AS total_pos_chaves FROM {MySql.DB_NAME}.tb_unidades WHERE id_empreendimento = %s AND (vl_chaves > 0 or vl_pre_chaves > 0 or vl_pos_chaves > 0 ) AND status != 'distrato' AND ac_historico IS NULL"

        cursor.execute(query, (idEmpreend,))
        linha = cursor.fetchone()

        linhaU = unidade()
        linhaU.setQtUnidade(linha[0])
        linhaU.setTtChaves(linha[1])
        linhaU.setTtPreChaves(linha[2])
        linhaU.setTtPosChaves(linha[3])

        cursor.close()
        MySql.close(self.__connection)

        return linhaU

    def consultarUnidadeVendas(self, idEmpreend, tipo):
        self.__connection = MySql.connect()
        cursor = self.__connection.cursor()

        print('+++++++++ consultarUnidadeVendas ++++++++++++++++++')

        if tipo == 'valor':
            query = "select status, sum(vl_unidade) from " + MySql.DB_NAME + ".tb_unidades where id_empreendimento = " + str(
                idEmpreend) + " and status != 'distrato' and ac_historico is null group by status"
        else:
            query = "select status, count(id_unidade) from " + MySql.DB_NAME + ".tb_unidades where id_empreendimento = " + str(
                idEmpreend) + " and status != 'distrato' and ac_historico is null group by status"
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

    def consultarUnidadeRecebibeis(self, idEmpreend, mesIni, anoIni, mesFim, anoFim):
        self.__connection = MySql.connect()
        cursor = self.__connection.cursor()

        print('+++++++++ consultarUnidadeRecebibeis ++++++++++++++++++')

#        query = "select vl_receber from " + MySql.DB_NAME + ".tb_unidades where id_empreendimento = " + str(idEmpreend) + " and status = 'Vendido' " + " and ac_historico is null"
#
#        if anoIni == anoFim:
#                query =  "select mes_vigencia, ano_vigencia, sum(vl_receber) from " + MySql.DB_NAME + ".tb_unidades where id_empreendimento = " + str(idEmpreend) + " and status = 'Vendido' and ac_historico is null and ((mes_vigencia >= '" + mesIni + "' and ano_vigencia = '" + anoIni + "') and (mes_vigencia <= '" + mesFim + "' and ano_vigencia = '" + anoFim + "')) group by ano_vigencia, mes_vigencia"
#                print('===========> com and')
#        else:
#                query =  "select mes_vigencia, ano_vigencia, sum(vl_receber) from " + MySql.DB_NAME + ".tb_unidades where id_empreendimento = " + str(idEmpreend) + " and status = 'Vendido' and ac_historico is null and ((mes_vigencia >= '" + mesIni + "' and ano_vigencia = '" + anoIni + "') or  (mes_vigencia <= '" + mesFim + "' and ano_vigencia = '" + anoFim + "')) group by ano_vigencia, mes_vigencia"
#                print('===========> com or')

        query = "select mes_vigencia, ano_vigencia, SUM(CASE WHEN status = 'Estoque' THEN vl_unidade ELSE 0 END) AS total_unidade, SUM(CASE WHEN status = 'Vendido' THEN vl_receber ELSE 0 END) AS total_pago from " + MySql.DB_NAME + ".tb_unidades where id_empreendimento = " + str(
            idEmpreend) + " and ac_historico is null and (ano_vigencia > '" + anoIni + "' OR (ano_vigencia = '" + anoIni + "' AND mes_vigencia >= '" + mesIni + "')) AND (ano_vigencia < '" + anoFim + "' OR (ano_vigencia = '" + anoFim + "' AND mes_vigencia <= '" + mesFim + "')) group by ano_vigencia, mes_vigencia order by ano_vigencia, mes_vigencia"

        print(query)

        cursor.execute(query)

        lista = cursor.fetchall()
        listaVendas = []

        for x in lista:
            u = unidade()
            u.setMesVigencia(x[0])
            u.setAnoVigencia(x[1])
            u.setTtUnidade(x[2])
            u.setTtPago(x[3])
            listaVendas.append(u)

        cursor.close()

        MySql.close(self.__connection)

        return listaVendas

    def consultarUnidadeRecebibeisNOVA(self, idEmpreend, mesIni, anoIni, mesFim, anoFim):
        self.__connection = MySql.connect()
        cursor = self.__connection.cursor()

        print('+++++++++ consultarUnidadeRecebibeis ++++++++++++++++++')

        query = "select mes_vigencia, ano_vigencia, SUM(CASE WHEN status = 'Estoque' THEN vl_unidade ELSE 0 END) AS total_unidade, SUM(CASE WHEN status = 'Vendido' THEN vl_receber ELSE 0 END) AS total_pago from " + MySql.DB_NAME + ".tb_unidades where id_empreendimento = " + str(
            idEmpreend) + " and ac_historico is null and (ano_vigencia > '" + anoIni + "' OR (ano_vigencia = '" + anoIni + "' AND mes_vigencia >= '" + mesIni + "')) AND (ano_vigencia < '" + anoFim + "' OR (ano_vigencia = '" + anoFim + "' AND mes_vigencia <= '" + mesFim + "')) group by ano_vigencia, mes_vigencia order by ano_vigencia, mes_vigencia"

        print(query)

        cursor.execute(query)

        lista = cursor.fetchall()
        listaVendas = []

        for x in lista:
            u = unidade()
            u.setMesVigencia(x[0])
            u.setAnoVigencia(x[1])
            u.setTtUnidade(x[2])
            u.setTtPago(x[3])
            listaVendas.append(u)

        cursor.close()

        MySql.close(self.__connection)

        return listaVendas

    def consultarUnidadeEstoque(self, idEmpreend, mesIni, anoIni, mesFim, anoFim):
        self.__connection = MySql.connect()
        cursor = self.__connection.cursor()

        print('+++++++++ consultarUnidadeRecebibeis ++++++++++++++++++')

#        query = "select vl_receber from " + MySql.DB_NAME + ".tb_unidades where id_empreendimento = " + str(idEmpreend) + " and status = 'Vendido' " + " and ac_historico is null"

        if anoIni == anoFim:
            query = "select mes_vigencia, ano_vigencia, sum(vl_unidade) from " + MySql.DB_NAME + ".tb_unidades where id_empreendimento = " + str(idEmpreend) + " and status = 'Estoque' and ac_historico is null and ((mes_vigencia >= '" + \
                mesIni + "' and ano_vigencia = '" + anoIni + \
                    "') and (mes_vigencia <= '" + mesFim + "' and ano_vigencia = '" + \
                anoFim + "')) group by ano_vigencia, mes_vigencia"
            print('===========> com and')
        else:
            query = "select mes_vigencia, ano_vigencia, sum(vl_unidade) from " + MySql.DB_NAME + ".tb_unidades where id_empreendimento = " + str(idEmpreend) + " and status = 'Estoque' and ac_historico is null and ((mes_vigencia >= '" + \
                mesIni + "' and ano_vigencia = '" + anoIni + \
                    "') or  (mes_vigencia <= '" + mesFim + "' and ano_vigencia = '" + \
                anoFim + "')) group by ano_vigencia, mes_vigencia"
            print('===========> com or')

        print(query)

        cursor.execute(query)

        lista = cursor.fetchall()
        listaEstoque = []

        for x in lista:
            u = unidade()
            u.setMesVigencia(x[0])
            u.setAnoVigencia(x[1])
            u.setTtUnidade(x[2])
            listaEstoque.append(u)

        cursor.close()

        MySql.close(self.__connection)

        return listaEstoque

    def salvarUnidade(self, unidade):
        self.__connection = MySql.connect()
        cursor = self.__connection.cursor()

        query = f"""UPDATE {MySql.DB_NAME}.tb_unidades SET
      id_torre = %s,
      id_empreendimento = %s,
      unidade = %s,
      mes_vigencia = %s,
      ano_vigencia = %s,
      vl_unidade = %s,
      status = %s,
      cpf_cnpj_comprador = %s,
      vl_receber = %s,
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
            unidade.getVlReceber(),
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
        query = f"""SELECT COUNT(id_unidade) total FROM {MySql.DB_NAME}.tb_unidades WHERE id_torre = %s AND ac_historico IS NULL;"""
        ret = MySql.getAll(query, (idTorre,))
        return ret[0]['total'] > 0

    def mudarHistoricoEditado(self, idUnidade):
        query = f"UPDATE {MySql.DB_NAME}.tb_unidades SET ac_historico = 'EDITADO' where id_unidade = %s"
        MySql.exec(query, (idUnidade,))

    def recursiveCalculoData(self, dataInicio: datetime, dataFinal: datetime, item: tuple, lista: list[unidade], changeInitDate: bool):
        vigNext = dataInicio
        if changeInitDate:
            vigNext += relativedelta.relativedelta(months=1)
        vig = vigNext.strftime('%Y-%m').split('-')
        copy = deepcopy(item)
        copy['mes_vigencia'] = vig[1].zfill(2)
        copy['ano_vigencia'] = vig[0]
        lista.append(self.mapeamentoUnidade(copy))
        if not changeInitDate:
            vigNext = dataInicio + relativedelta.relativedelta(months=1)
        if vigNext < dataFinal:
            self.recursiveCalculoData(
                vigNext, dataFinal, item, lista, changeInitDate)

    def gerarInsumoRelatorio(self, idEmpreend: int, dataInicio: datetime, dataFim: datetime) -> list[unidade]:
        query = f""" SELECT * FROM {MySql.DB_NAME}.tb_unidades uni
          WHERE uni.id_empreendimento = %s
          AND DATE(CONCAT(uni.ano_vigencia, '-', uni.mes_vigencia, '-01')) <= %s
          AND uni.status IN ('Estoque', 'Vendido')
          AND uni.id_unidade = (
              SELECT MAX(id_unidade) FROM {MySql.DB_NAME}.tb_unidades
              WHERE unidade = uni.unidade
              AND ano_vigencia = uni.ano_vigencia
              AND mes_vigencia = uni.mes_vigencia
              AND id_empreendimento = uni.id_empreendimento
              AND id_torre = uni.id_torre
          )
          ORDER BY uni.id_torre, uni.unidade, DATE(CONCAT(uni.ano_vigencia, '-', uni.mes_vigencia, '-01')), uni.id_unidade;
        """

        result = []
        totais = {}
        totaisList = []

        print("Buscando unidades para calcular com parametros: ", {
            "IdEmpreendimento": idEmpreend,
            "Data Início": dataInicio,
            "Data Final": dataFim
        }, end="\n\n")

        unidades = MySql.getAll(
            query, (
                idEmpreend,
                format(dataFim, '%Y-%m-%d')
            )
        )

        if not unidades:
            return []

        print("Quantidade de unidades encontradas: ", len(unidades), end="\n\n")

        for idx, current in enumerate(unidades):
            idxPrevius = idx - 1
            idxNext = idx + 1
            previus = unidades[idxPrevius] if idx > 0 else None
            next = unidades[idxNext] if idxNext < len(
                unidades) else None

            vigCurrent = datetime(
                int(current['ano_vigencia']),
                int(current['mes_vigencia']),
                1
            )
            nextVig = datetime(
                int(next['ano_vigencia']),
                int(next['mes_vigencia']),
                1
            ) if next else 0

            if vigCurrent > dataInicio and (not previus or previus['unidade'] != current['unidade']):
                self.recursiveCalculoData(
                    dataInicio,
                    vigCurrent,
                    current,
                    result,
                    False
                )

            result.append(self.mapeamentoUnidade(current))

            if next and current['unidade'] == next['unidade'] and diff_mes(nextVig, vigCurrent) > 1:
                self.recursiveCalculoData(
                    vigCurrent,
                    nextVig - relativedelta.relativedelta(months=1),
                    current,
                    result,
                    True
                )

            elif (not next and vigCurrent < dataFim) or (next and current['unidade'] != next['unidade'] and vigCurrent < dataFim):
                self.recursiveCalculoData(
                    vigCurrent,
                    dataFim,
                    current,
                    result,
                    True
                )

        print("Quantidade de unidades geradas", len(result), end="\n\n")

        for uni in result:
            if datetime(int(uni.getAnoVigencia()), int(uni.getMesVigencia()), 1) < dataInicio or datetime(int(uni.getAnoVigencia()), int(uni.getMesVigencia()), 1) > dataFim:
                continue

            key = f"{uni.getMesVigencia()}_{uni.getAnoVigencia()}"
            if not totais.get(key, None):
                if uni.getStatus() == 'Estoque':
                    totais[key] = {
                        "valorUnidade": uni.getVlUnidade(),
                        "valorPago": 0,
                        "valorReceber": 0
                    }
                else:
                    totais[key] = {
                        "valorUnidade": uni.getVlUnidade(),
                        "valorPago": uni.getVlUnidade(),
                        "valorReceber": uni.getVlReceber()
                    }
            else:
                tt = totais[key]
                valorUnidade = tt["valorUnidade"] + uni.getVlUnidade()

                valorPago = tt["valorPago"]
                valorReceber = tt["valorReceber"]
                if uni.getStatus() == 'Vendido':
                    valorPago = tt["valorPago"] + uni.getVlUnidade()
                    valorReceber = tt["valorReceber"] + uni.getVlReceber()

                totais[key] = {
                    "valorUnidade": valorUnidade,
                    "valorPago": valorPago,
                    "valorReceber": valorReceber
                }

        for key, value in totais.items():
            vigencia = key.split('_')
            uni = unidade()
            uni.setMesVigencia(vigencia[0])
            uni.setAnoVigencia(vigencia[1])
            uni.setTtUnidade(value["valorUnidade"] - value["valorPago"])
            uni.setTtPago(value["valorReceber"])
            print("Unidade mapeada: ", {
                  "Vigencia": vigencia,
                  "ValorUnidade": value["valorUnidade"],
                  "ValorPago": value["valorPago"]},
                  end="\n\n"
                  )
            totaisList.append(uni)

        return totaisList

    def mapeamentoUnidade(self, linha) -> unidade:
        linhaU = unidade()
        linhaU.setIdUnidade(linha['id_unidade'])
        linhaU.setIdTorre(linha['id_torre'])
        linhaU.setIdEmpreend(linha['id_empreendimento'])
        linhaU.setUnidade(linha['unidade'])
        linhaU.setMesVigencia(linha['mes_vigencia'])
        linhaU.setAnoVigencia(linha['ano_vigencia'])
        linhaU.setVlUnidade(linha['vl_unidade'] if linha['vl_unidade'] else 0)
        linhaU.setStatus(linha['status'])
        linhaU.setCpfComprador(linha['cpf_cnpj_comprador'])
        linhaU.setVlReceber(linha['vl_receber'] if linha['vl_receber'] else 0)
        linhaU.setDtOcorrencia(linha['dt_ocorrencia'])
        linhaU.setFinanciado(linha['financiado'])
        linhaU.setVlChaves(linha['vl_chaves'])
        linhaU.setVlPreChaves(linha['vl_pre_chaves'])
        linhaU.setVlPosChaves(linha['vl_pos_chaves'])
        linhaU.setNmTorre(linha['nm_torre'] if 'nm_torre' in linha else '')

        return linhaU

    @staticmethod
    def idTorrePeloNomeeUnidade(unidade: int, nmTorre: str, idEmpreend: int) -> int:
        query = f"""SELECT uni.id_torre FROM {MySql.DB_NAME}.tb_unidades uni
                  INNER JOIN {MySql.DB_NAME}.tb_torres tor
                  ON uni.id_torre = tor.id_torre
                  AND uni.id_empreendimento = tor.id_empreendimento
                  AND tor.nm_torre = %s
                  WHERE uni.unidade = %s
                  AND uni.id_empreendimento = %s
                  AND uni.ac_historico IS NULL;"""
        result = MySql.getOne(query, (nmTorre, unidade, idEmpreend))
        return result['id_torre'] if result else None

    @staticmethod
    def atualizarValoresUnidade(listData: tuple):
        queryUpdate = f"""UPDATE {MySql.DB_NAME}.tb_unidades
                          SET ac_historico = 'EDITADO'
                          WHERE id_torre = %s
                          AND unidade = %s
                          AND id_empreendimento = %s
                          AND ac_historico IS NULL;"""
        query = f"""INSERT INTO {MySql.DB_NAME}.tb_unidades (
                    id_empreendimento,
                    id_torre,
                    unidade,
                    status,
                    mes_vigencia,
                    ano_vigencia,
                    cpf_cnpj_comprador,
                    vl_unidade,
                    vl_pre_chaves,
                    vl_chaves,
                    vl_pos_chaves,
                    vl_receber
                  ) VALUES (
                    %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s
                  );"""
        MySql.exec(queryUpdate, (listData[1], listData[2], listData[0]))
        MySql.exec(query, listData)

    def unidadesVendidasSemCliente(self, idEmpreend: int, mesVig: str, anoVig: str):
        query = f"""SELECT *, tor.nm_torre FROM {MySql.DB_NAME}.tb_unidades uni
          INNER JOIN {MySql.DB_NAME}.tb_torres tor
          ON tor.id_torre = uni.id_torre
          WHERE uni.id_empreendimento = %s
          AND uni.mes_vigencia = %s
          AND uni.ano_vigencia = %s
          AND uni.status IN ('Vendido', 'Quitado')
          AND uni.ac_historico IS NULL
          AND (
              uni.cpf_cnpj_comprador IS NULL
              OR uni.cpf_cnpj_comprador IN ('None', '')
          ); """

        unidades = MySql.getAll(query, (idEmpreend, mesVig, anoVig))
        result = []
        for uni in unidades:
            result.append(self.mapeamentoUnidade(uni))
        return result
