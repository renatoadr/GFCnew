#controller or business logic
# Trata base de MEDIÇÕES

from datetime import datetime
import pandas as pd
from utils.converter import converterDateTimeToDateEnFormat
from dto.medicao import medicao
from utils.dbContext import MySql

class medicaoController:
    __connection = None

    def __init__(self):
        pass

    def consultarMedicoes(self, idEmpreend):
        self.__connection = MySql.connect()
        cursor = self.__connection.cursor(dictionary=True)   

        query =  "select id_medicao, id_empreendimento, mes_vigencia, ano_vigencia, dt_carga, nr_medicao, perc_previsto_acumulado, perc_realizado_acumulado, perc_diferenca, perc_previsto_periodo from " + MySql.DB_NAME + ".tb_medicoes where id_empreendimento = '" + str(idEmpreend) + " order by nr_medicao'"
    
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
            listaItens.append(m)

        cursor.close()
        MySql.close(self.__connection)

        return listaItens

    def consultarMedicoesPorPeriodo(self, idEmpreend, mesVigenciaIni, anoVigenciaIni, mesVigenciaFim, anoVigenciaFim):
        self.__connection = MySql.connect()
        cursor = self.__connection.cursor(dictionary=True)   

        if anoVigenciaIni == anoVigenciaFim:
            query =  "select id_empreendimento, nr_medicao, mes_vigencia, ano_vigencia, perc_previsto_acumulado, perc_realizado_acumulado, perc_diferenca, perc_previsto_periodo from " + MySql.DB_NAME + ".tb_medicoes where id_empreendimento = '" + str(idEmpreend) + "' and (mes_vigencia >= '" + mesVigenciaIni + "' and ano_vigencia = '" + anoVigenciaIni + "') and (mes_vigencia <= '" + mesVigenciaFim + "' and ano_vigencia = '" + anoVigenciaFim + "')"
        else:
            query =  "select id_empreendimento, nr_medicao, mes_vigencia, ano_vigencia, perc_previsto_acumulado, perc_realizado_acumulado, perc_diferenca, perc_previsto_periodo from " + MySql.DB_NAME + ".tb_medicoes where id_empreendimento = '" + str(idEmpreend) + "' and (mes_vigencia >= '" + mesVigenciaIni + "' and ano_vigencia = '" + anoVigenciaIni + "') or (mes_vigencia <= '" + mesVigenciaFim + "' and ano_vigencia = '" + anoVigenciaFim + "')"
    
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

            nrMedicao              = str(tabela.at[linha, 'Medição'])
            mesVigencia            = str(tabela.at[linha, 'Mês']).zfill(2)
            anoVigencia            = str(tabela.at[linha, 'Ano'])
            percPrevistoAcumulado  = float(tabela.at[linha, 'Previsto Acumulado'])
            percRealizadoAcumulado = float(tabela.at[linha, 'Realizado Acumulado'])
            if percRealizadoAcumulado == 0:
                percDiferenca      = 0
            else:
                percDiferenca      = percRealizadoAcumulado - percPrevistoAcumulado 
            percPrevistoPeriodo    = float(tabela.at[linha, 'Previsto Período'])

            query =  "INSERT INTO " + MySql.DB_NAME + ".tb_medicoes (id_empreendimento, mes_vigencia, ano_vigencia, dt_carga, nr_medicao, perc_previsto_acumulado, perc_realizado_acumulado, perc_diferenca, perc_previsto_periodo) VALUES ('" + str(idEmpreend) + "', '" + mesVigencia + "', '" + anoVigencia + "', '" + dateTime + "', '" + str(nrMedicao) + "ª', " + str(percPrevistoAcumulado) + ", " + str(percRealizadoAcumulado) + ", " + str(percDiferenca) + ", " + str(percPrevistoPeriodo) + ")"

            print (query)
            cursor.execute(query)
            linha += 1

        self.__connection.commit()
        print(cursor.rowcount,"medição cadastrada com sucesso")
        cursor.close()
        MySql.close(self.__connection)
