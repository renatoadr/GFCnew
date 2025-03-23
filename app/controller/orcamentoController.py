#controller or business logic
# Trata base de ORCAMENTOS

from dto.orcamento import orcamento
from utils.dbContext import MySql
from datetime import datetime
import pandas as pd
from utils.converter import converterDateTimeToDateEnFormat

class orcamentoController:
    __connection = None

    def __init__(self):
        pass

    def consultarOrcamentos(self, idEmpreend):
        self.__connection = MySql.connect()
        cursor = self.__connection.cursor()

        print('---consultarorcamentos---')
        print(idEmpreend)

        query =  "select mes_vigencia, ano_vigencia, dt_carga from " + MySql.DB_NAME + ".tb_orcamentos where id_empreendimento = " +  str (idEmpreend) + " group by mes_vigencia, ano_vigencia, dt_carga"

        print('-----------------')
        print(query)
        print('-----------------')

        cursor.execute(query)

        lista = cursor.fetchall()

        listaOrcamentos = []

        for x in lista:
            m = orcamento()
#            m.setIdOrcamento(x[0])
#            m.setIdEmpreend(x[1])
            m.setMesVigencia(x[0])
            m.setAnoVigencia(x[1])
            m.setDtCarga(x[2])
            listaOrcamentos.append(m)

        cursor.close()
        MySql.close(self.__connection)
        return listaOrcamentos

    def consultarOrcamentoPelaData(self, idEmpreend, dtCarga):
        self.__connection = MySql.connect()
        cursor = self.__connection.cursor(dictionary=True)

        query =  "select id_orcamento, id_empreendimento, mes_vigencia, ano_vigencia, dt_carga, item, orcado_valor, fisico_valor, fisico_percentual, fisico_saldo, financeiro_valor, financeiro_percentual, financeiro_saldo from " + MySql.DB_NAME + ".tb_orcamentos where id_empreendimento = '" + str(idEmpreend) + "' and dt_carga = '" + dtCarga + "' order by id_orcamento"

        print(query)

        cursor.execute(query)

#        linha = cursor.fetchone()
        print('++++++++++++ consultarOrcamentoPelaData +++++++++++++++')
#        print (linha)
#        print('+++++++++++++++++++++++++++')

        lista = cursor.fetchall()

        listaItens = []

        for x in lista:
            m = orcamento()
            m.setIdOrcamento(x['id_orcamento'])
            m.setIdEmpreend(x['id_empreendimento'])
            m.setMesVigencia(x['mes_vigencia'])
            m.setAnoVigencia(x['ano_vigencia'])
            m.setDtCarga(x['dt_carga'])
            m.setItem(x['item'])
            m.setOrcadoValor(x['orcado_valor'])
            m.setFisicoValor(x['fisico_valor'])
            m.setFisicoPercentual(x['fisico_percentual'])
            m.setFisicoSaldo(x['fisico_saldo'])
            m.setFinanceiroValor(x['financeiro_valor'])
            m.setFinanceiroPercentual(x['financeiro_percentual'])
            m.setFinanceiroSaldo(x['financeiro_saldo'])
            listaItens.append(m)

        print('------------------------')
        print('------------------------')
        cursor.close()
        MySql.close(self.__connection)
        print ('-----------------> ', listaItens)

        return listaItens

    def consultarOrcamentoPeloId(self, idOrcamento):
        self.__connection = MySql.connect()
        cursor = self.__connection.cursor(dictionary=True)

        query =  "select id_orcamento, id_empreendimento, mes_vigencia, ano_vigencia, dt_carga, item, orcado_valor, fisico_valor, fisico_percentual, fisico_saldo, financeiro_valor, financeiro_percentual, financeiro_saldo from " + MySql.DB_NAME + ".tb_orcamentos where id_orcamento = '" + str(idOrcamento) + "'"

        print(query)

        cursor.execute(query)

#        linha = cursor.fetchone()
        print('++++++++++++ consultarOrcamentoPeloId +++++++++++++++')
#        print (linha)
#        print('+++++++++++++++++++++++++++')

        item = cursor.fetchone()

        m = orcamento()
        m.setIdOrcamento(item['id_orcamento'])
        m.setIdEmpreend(item['id_empreendimento'])
        m.setMesVigencia(item['mes_vigencia'])
        m.setAnoVigencia(item['ano_vigencia'])
        m.setDtCarga(item['dt_carga'])
        m.setItem(item['item'])
        m.setOrcadoValor(item['orcado_valor'])
        m.setFisicoValor(item['fisico_valor'])
        m.setFisicoPercentual(item['fisico_percentual'])
        m.setFisicoSaldo(item['fisico_saldo'])
        m.setFinanceiroValor(item['financeiro_valor'])
        m.setFinanceiroPercentual(item['financeiro_percentual'])
        m.setFinanceiroSaldo(item['financeiro_saldo'])

#        dados = [list(linha) for linha in listaItens()]

        print('------------------------')
        print('------------------------')
        cursor.close()
        MySql.close(self.__connection)
#        print ('-----------------> ', dados)
        print ('-----------------> ', item)
        print('++++++++++++ consultarOrcamentoPeloId ++++ FIM +++++++++++')

        return m

    def inserirOrcamento(self, orcamento):

        self.__connection = MySql.connect()
        cursor = self.__connection.cursor()

        query =  "INSERT INTO " + MySql.DB_NAME + """.tb_orcamentos (id_empreendimento, mes_vigencia, ano_vigencia, dt_carga, item, orcado_valor, fisico_valor, fisico_percentual, fisico_saldo, financeiro_valor, financeiro_percentual, financeiro_saldo)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""

        print (query)
        cursor.execute(query, (
          orcamento.getIdEmpreend (),
          orcamento.getMesVigencia (),
          orcamento.getAnoVigencia (),
          orcamento.getDtCarga (),
          orcamento.getItem (),
          orcamento.getOrcadoValor(),
          orcamento.getFisicoPercentual (),
          orcamento.getFisicoValor (),
          orcamento.getFisicoSaldo (),
          orcamento.getFinanceiroPercentual (),
          orcamento.getFinanceiroValor (),
          orcamento.getFinanceiroSaldo ()
        ))

        self.__connection.commit()
        print(cursor.rowcount,"Orçamento cadastrado com sucesso")
        cursor.close()
        MySql.close(self.__connection)

    def carregar_orcamentos(self, caminhoArq, idEmpreend):

        self.__connection = MySql.connect()
        cursor = self.__connection.cursor()

        tabela = pd.read_excel(caminhoArq)

        l, c = tabela.shape
        linha = 0
        m = orcamento()
        dtTime = datetime.now()
        dateTime = dtTime.strftime("%Y-%m-%d %H:%M:%S")

        print ('------------ carregar_orcamentos -----------------')
        print (idEmpreend)
        print (linha, l)

        while linha < l:

            mesVigencia = str(tabela.at[linha, 'Mês']).zfill(2)
            anoVigencia = str(tabela.at[linha, 'Ano'])
            item        = str(tabela.at[linha, 'Descrição'])
            orcado      = float(tabela.at[linha, 'Orçado'])
            fisicoP     = float(tabela.at[linha, 'Físico %'])
            financR     = float(tabela.at[linha, 'Financeiro R$'])
            if financR > 0:
                financP = (financR/orcado) * 100
            else:
                financP = 0
            if fisicoP > 0:
                fisicoR = orcado * (fisicoP/100)
            else:
                fisicoR = 0
            fisicoS     = orcado-fisicoR
            financS     = orcado-financR

            query =  "INSERT INTO " + MySql.DB_NAME + ".tb_orcamentos (id_empreendimento, mes_vigencia, ano_vigencia, dt_carga, item, orcado_valor, fisico_valor, fisico_percentual, fisico_saldo, financeiro_valor, financeiro_percentual, financeiro_saldo) VALUES ('" + idEmpreend + "', '" + mesVigencia + "', '" + anoVigencia + "', '" + dateTime + "', '" + item + "', " + str(orcado) + ", " + str(fisicoR) + ", " + str(fisicoP) + ", " + str(fisicoS) + ", " + str(financR) + ", " + str(financP) + ", " + str(financS) + ")"

            print (query)
            cursor.execute(query)
            linha += 1

        self.__connection.commit()
        print(cursor.rowcount,"Orçamento cadastrado com sucesso")
        cursor.close()
        MySql.close(self.__connection)

    def excluirItemOrcamento(self,idOrcamento):
        self.__connection = MySql.connect()
        cursor = self.__connection.cursor()

#        print (emp)

        query =  "delete from " + MySql.DB_NAME + ".tb_orcamentos" + " where id_orcamento = " + str(idOrcamento)
        print (query)

        cursor.execute(query)
        self.__connection.commit()
        cursor.close()
        MySql.close(self.__connection)

    def excluirOrcamento(self, idEmpreend, mesV, anoV, dtCarga):
        self.__connection = MySql.connect()
        cursor = self.__connection.cursor()

#        print (emp)

        query =  "delete from " + MySql.DB_NAME + """.tb_orcamentos
        where id_empreendimento = %s
        and dt_carga = %s
        and mes_vigencia = %s
        and ano_vigencia = %s """
        print (query)

        cursor.execute(query, (
          idEmpreend,
          dtCarga,
          mesV,
          anoV
        ))

        self.__connection.commit()
        cursor.close()
        MySql.close(self.__connection)

    def salvarItemOrcamento(self, item):
        self.__connection = MySql.connect()
        cursor = self.__connection.cursor()

        query =  "update " + MySql.DB_NAME + ".tb_orcamentos set " + "item = '" + item.getItem () + "', " + "orcado_valor = " + str(item.getOrcadoValor ()) + ", " + "fisico_valor = " + str(item.getFisicoValor ()) + ", " + "fisico_percentual = " + str(item.getFisicoPercentual ()) + ", " + "fisico_saldo = " + str(item.getFisicoSaldo ()) + ", " + "financeiro_valor = " + str(item.getFinanceiroValor ()) + ", " + "financeiro_percentual = " + str(item.getFinanceiroPercentual ()) + ", " + "financeiro_saldo = " + str(item.getFinanceiroSaldo ()) + " where id_orcamento = " + str(item.getIdOrcamento())

        print (query)
        cursor.execute(query)

        self.__connection.commit()
        print(cursor.rowcount,"Orcamento atualizado com sucesso")
        cursor.close()
        MySql.close(self.__connection)


