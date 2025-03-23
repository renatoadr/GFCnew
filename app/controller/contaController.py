#controller or business logic
# Trata base de CONTAS

from dto.conta import conta
from utils.dbContext import MySql
from datetime import datetime
import pandas as pd
from utils.dbContext import MySql


class contaController:
  __connection = None

  def __init__(self):
      pass

  def consultarContas(self, idEmpreend):
      self.__connection = MySql.connect()
      cursor = self.__connection.cursor()

      print('---consultarn contas---')
      print(idEmpreend)

      query =  "select mes_vigencia, ano_vigencia, dt_carga  from " + MySql.DB_NAME + ".tb_contas where id_empreendimento = " +  str (idEmpreend) + " group by mes_vigencia, ano_vigencia, dt_carga"

      print('-----------------')
      print(query)
      print('-----------------')

      cursor.execute(query)

      lista = cursor.fetchall()

      listaContas = []

      for x in lista:
          n = conta()
          n.setMesVigencia(x[0])
          n.setAnoVigencia(x[1])
          n.setDtCarga(x[2])
          listaContas.append(n)

      cursor.close()
      MySql.close(self.__connection)
      return listaContas

  def consultarConta(self, idEmpreend):
      self.__connection = MySql.connect()
      cursor = self.__connection.cursor(dictionary=True)

      query =  "select id_empreendimento, mes_vigencia, ano_vigencia, vl_liberacao, vl_material_estoque, vl_aporte_construtora, vl_receita_recebiveis, vl_pagto_obra, vl_pagto_rh, vl_diferenca, vl_saldo from " + MySql.DB_NAME + ".tb_contas where id_empreendimento = '" + str(idEmpreend) + "'"

      print(query)

      cursor.execute(query)

#        linha = cursor.fetchone()
#        print('++++++++++++ consultarContaPelaData +++++++++++++++')
#        print (linha)
#        print('+++++++++++++++++++++++++++')

      lista = cursor.fetchall()

      listaItens = []

      for x in lista:
          m = conta()
          m.setMesVigencia(x['mes_vigencia'])
          m.setAnoVigencia(x['ano_vigencia'])
          m.setVlLiberacao(x['vl_liberacao'])
          m.setVlMaterialEstoque(x['vl_material_estoque'])
          m.setVlAporteConstrutora(x['vl_aporte_construtora'])
          m.setVlReceitaRecebiveis(x['vl_receita_recebiveis'])
          m.setVlPagtoObra(x['vl_pagto_obra'])
          m.setVlPagtoRh(x['vl_pagto_rh'])
          m.setVlDiferenca(x['vl_diferenca'])
          m.setVlSaldo(x['vl_saldo'])
          listaItens.append(m)

#        dados = [list(linha) for linha in listaItens()]

#        print('------------------------')
#        print('------------------------')
      cursor.close()
      MySql.close(self.__connection)
#        print ('-----------------> ', dados)
#        print ('-----------------> ', listaItens)

      return listaItens

  def carregar_contas(self, caminhoArq, idEmpreend):

      self.__connection = MySql.connect()
      cursor = self.__connection.cursor()

      tabela = pd.read_excel(caminhoArq)

      l, c = tabela.shape
      linha = 0
      m = conta()
      dtTime = datetime.now()
      dateTime = dtTime.strftime("%Y-%m-%d %H:%M:%S")

      print ('------------ carregar_contas -----------------')
      print (idEmpreend)
      print (linha, l)

      while linha < l:

          mesVigencia          = str(tabela.at[linha, 'Mês']).zfill(2)
          anoVigencia          = str(tabela.at[linha, 'Ano'])
          vlLiberacao          = tabela.at[linha, 'Valor Liberação']
          vlAporteConstrutora  = float(tabela.at[linha, 'Valor Aporte Construtora'])
          vlReceitaRecebiveis  = float(tabela.at[linha, 'Valor Receita Recebíveis'])
          vlPagtoObra          = float(tabela.at[linha, 'Valor Pagamento Obra'])
          vlPagtoRh            = float(tabela.at[linha, 'Valor Pagamento RH'])
          vlDiferenca          = float(tabela.at[linha, 'Valor Diferença'])
          vlSaldo              = float(tabela.at[linha, 'Valor Saldo'])

          query =  "INSERT INTO " + MySql.DB_NAME + ".tb_contas (id_empreendimento, mes_vigencia, ano_vigencia, dt_carga, vl_liberacao, vl_aporte_construtora, vl_receita_recebiveis, vl_pagto_obra, vl_pagto_rh, vl_diferenca, vl_saldo ) VALUES ('" + str(idEmpreend) + "', '" + mesVigencia + "', '" + anoVigencia + "', '" + dateTime + "', " + str(vlLiberacao) + ", " + str(vlAporteConstrutora) + ", " + str(vlReceitaRecebiveis) + ", " + str(vlPagtoObra) + ", " + str(vlPagtoRh) + ", " + str(vlDiferenca) + ", " + str(vlSaldo) + ")"

          print (query)
          cursor.execute(query)
          linha += 1

      self.__connection.commit()
      print(cursor.rowcount,"Conta cadastrada com sucesso")
      cursor.close()
      MySql.close(self.__connection)

  def excluir_por_data(self, dt_carga, mes_vig, ano_vig):
    self.__connection = MySql.connect()
    cursor = self.__connection.cursor()
    query = "DELETE FROM " + MySql.DB_NAME + """.tb_contas WHERE mes_vigencia = %s AND ano_vigencia = %s AND dt_carga = %s """
    cursor.execute(query, (mes_vig, ano_vig, dt_carga))
    self.__connection.commit()
    cursor.close()
    MySql.close(self.__connection)
