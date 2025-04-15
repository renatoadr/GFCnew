#controller or business logic
# Trata base de MEDIÇÕES

from datetime import datetime
import pandas as pd
from utils.converter import converterDateTimeToDateEnFormat
from dto.medicao import medicao
from utils.dbContext import MySql

class medicaoController:
  __connection = None

  def consultarMedicoes(self, idEmpreend):
      self.__connection = MySql.connect()
      cursor = self.__connection.cursor(dictionary=True)

      query =  "select id_medicao, id_empreendimento, mes_vigencia, ano_vigencia, dt_carga, nr_medicao, perc_previsto_acumulado, perc_realizado_acumulado, perc_diferenca, perc_previsto_periodo, perc_realizado_periodo from " + MySql.DB_NAME + ".tb_medicoes where id_empreendimento = '" + str(idEmpreend) + " order by nr_medicao'"

      print(query)

      cursor.execute(query)

      lista = cursor.fetchall()

      listaItens = []

      for x in lista:
          m = medicao()
          m.setIdMedicao(x['id_medicao'])
          m.setMesVigencia(x['mes_vigencia'])
          m.setAnoVigencia(x['ano_vigencia'])
          m.setDtCarga(converterDateTimeToDateEnFormat(x['dt_carga']))
          m.setNrMedicao(x['nr_medicao'])
          m.setPercPrevistoAcumulado(x['perc_previsto_acumulado'])
          m.setPercRealizadoAcumulado(x['perc_realizado_acumulado'])
          m.setPercDiferenca(x['perc_diferenca'])
          m.setPercPrevistoPeriodo(x['perc_previsto_periodo'])
          m.setPercRealizadoPeriodo(x['perc_realizado_periodo'])

          listaItens.append(m)

      cursor.close()
      MySql.close(self.__connection)

      return listaItens

  def consultarMedicoesPorPeriodo(self, idEmpreend, mesVigenciaIni, anoVigenciaIni, mesVigenciaFim, anoVigenciaFim):
      self.__connection = MySql.connect()
      cursor = self.__connection.cursor(dictionary=True)

      if anoVigenciaIni == anoVigenciaFim:
          query =  "select id_empreendimento, nr_medicao, mes_vigencia, ano_vigencia, perc_previsto_acumulado, perc_realizado_acumulado, perc_diferenca, perc_previsto_periodo from " + MySql.DB_NAME + ".tb_medicoes where id_empreendimento = '" + str(idEmpreend) + "' and ((mes_vigencia >= '" + mesVigenciaIni + "' and ano_vigencia = '" + anoVigenciaIni + "') and (mes_vigencia <= '" + mesVigenciaFim + "' and ano_vigencia = '" + anoVigenciaFim + "')) order by id_medicao"
      else:
          query =  "select id_empreendimento, nr_medicao, mes_vigencia, ano_vigencia, perc_previsto_acumulado, perc_realizado_acumulado, perc_diferenca, perc_previsto_periodo from " + MySql.DB_NAME + ".tb_medicoes where id_empreendimento = '" + str(idEmpreend) + "' and ((mes_vigencia >= '" + mesVigenciaIni + "' and ano_vigencia = '" + anoVigenciaIni + "') or (mes_vigencia <= '" + mesVigenciaFim + "' and ano_vigencia <= '" + anoVigenciaFim + "')) order by id_medicao"

      print(query)

      cursor.execute(query)

      lista = cursor.fetchall()

      listaItens = []

      for x in lista:
          m = medicao()
          m.setNrMedicao(x['nr_medicao'])
          m.setMesVigencia(x['mes_vigencia'])
          m.setAnoVigencia(x['ano_vigencia'])
          m.setPercPrevistoAcumulado(x['perc_previsto_acumulado'])
          m.setPercRealizadoAcumulado(x['perc_realizado_acumulado'])
          m.setPercDiferenca(x['perc_diferenca'])
          m.setPercPrevistoPeriodo(x['perc_previsto_periodo'])
          listaItens.append(m)

      cursor.close()
      MySql.close(self.__connection)

      return listaItens

  def consultarMedicaoPeloId(self, idMedicao) -> medicao:
      query =  "select id_medicao, id_empreendimento, nr_medicao, mes_vigencia, ano_vigencia, dt_carga, perc_previsto_acumulado, perc_realizado_acumulado, perc_diferenca, perc_previsto_periodo, perc_realizado_periodo from " + MySql.DB_NAME + ".tb_medicoes where id_medicao = %s"
      linha = MySql.getOne(query, (idMedicao,))
      return self.mapper(linha)

  def consultarMedicaoAnteriorPeloId(self, idEmpreend, idMedicao) -> medicao:
      query =  "select id_medicao, id_empreendimento, nr_medicao, mes_vigencia, ano_vigencia, dt_carga, perc_previsto_acumulado, perc_realizado_acumulado, perc_diferenca, perc_previsto_periodo, perc_realizado_periodo from " + MySql.DB_NAME + ".tb_medicoes where id_empreendimento = %s AND id_medicao < %s ORDER BY 1 DESC LIMIT 1"
      linha = MySql.getOne(query, (idEmpreend, idMedicao))
      if not linha:
        return None
      return self.mapper(linha)

  def carregar_medicoes(self, caminhoArq, idEmpreend):

      self.__connection = MySql.connect()
      cursor = self.__connection.cursor()

      tabela = pd.read_excel(caminhoArq)

      l, c = tabela.shape
      linha = 0
      m = medicao()
      dtTime = datetime.now()
      dateTime = dtTime.strftime("%Y-%m-%d %H:%M:%S")

      print ('------------ carregar_medicoes -----------------')
      print (idEmpreend)
      print (linha, l)

      while linha < l:
          print(linha)
          nrMedicao              = str(tabela.at[linha, 'Medição'])
          mesVigencia            = str(tabela.at[linha, 'Mês']).zfill(2)
          anoVigencia            = str(tabela.at[linha, 'Ano'])
          percPrevistoPeriodo    = float(tabela.at[linha, 'Previsto Período'])
          percRealizadoPeriodo   = float(tabela.at[linha, 'Realizado Período'])

          # Substituir valores NaN por 0
          if pd.isna(percRealizadoPeriodo):
              percRealizadoPeriodo = 0.0

          percRealizadoPeriodo = float(percRealizadoPeriodo)

          if linha == 0:
              percPrevistoAcumulado  = percPrevistoPeriodo
              percRealizadoAcumulado = percRealizadoPeriodo
              percDiferenca           = percRealizadoAcumulado - percPrevistoAcumulado
          else:
              percPrevistoAcumulado  += percPrevistoPeriodo
              if percRealizadoPeriodo != 0:
                  percRealizadoAcumulado += percRealizadoPeriodo
                  percDiferenca           = percRealizadoAcumulado - percPrevistoAcumulado
              else:
                  percRealizadoAcumulado = 0
                  percDiferenca = 0

          query =  "INSERT INTO " + MySql.DB_NAME + ".tb_medicoes (id_empreendimento, mes_vigencia, ano_vigencia, dt_carga, nr_medicao, perc_previsto_acumulado, perc_realizado_acumulado, perc_diferenca, perc_previsto_periodo, perc_realizado_periodo) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

          print (query)
          cursor.execute(query, (idEmpreend, mesVigencia , anoVigencia , dateTime, nrMedicao + 'ª', percPrevistoAcumulado, percRealizadoAcumulado, percDiferenca, percPrevistoPeriodo, percRealizadoPeriodo))
          linha += 1

      self.__connection.commit()
      print(cursor.rowcount,"medição cadastrada com sucesso")
      cursor.close()
      MySql.close(self.__connection)

  def excluir_medicao(self, idMedicao):
      query = "delete from " + MySql.DB_NAME + """.tb_medicoes WHERE id_medicao = %s;"""
      MySql.exec(query, (idMedicao,))

  def salvarItemMedicao(self,medicao):
    query =  "update " + MySql.DB_NAME + """.tb_medicoes set
      perc_previsto_acumulado =  %s,
      perc_realizado_acumulado =  %s,
      perc_diferenca =  %s,
      perc_previsto_periodo = %s,
      perc_realizado_periodo = %s
      where id_medicao = %s """
    MySql.exec(query, (
      medicao.getPercPrevistoAcumulado(),
      medicao.getPercRealizadoAcumulado(),
      medicao.getPercDiferenca(),
      medicao.getPercPrevistoPeriodo(),
      medicao.getPercRealizadoPeriodo(),
      medicao.getIdMedicao()
    ))

  def mapper(self, linha):
    item = medicao()
    item.setIdMedicao(linha['id_medicao'])
    item.setIdEmpreend(linha['id_empreendimento'])
    item.setNrMedicao(linha['nr_medicao'])
    item.setMesVigencia(linha['mes_vigencia'])
    item.setAnoVigencia(linha['ano_vigencia'])
    item.setDtCarga(linha['dt_carga'])
    item.setPercPrevistoAcumulado(linha['perc_previsto_acumulado'])
    item.setPercRealizadoAcumulado(linha['perc_realizado_acumulado'])
    item.setPercDiferenca(linha['perc_diferenca'])
    item.setPercPrevistoPeriodo(linha['perc_previsto_periodo'])
    item.setPercRealizadoPeriodo(linha['perc_realizado_periodo'])
    return item
