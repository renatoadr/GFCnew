#controller or business logic
# Trata base de NOTAS

from datetime import datetime
import pandas as pd
from utils.converter import converterDateTimeToDateEnFormat
from dto.nota import nota
from utils.dbContext import MySql

class notaController:
    __connection = None

    def __init__(self):
        pass

    def consultarNotas(self, idEmpreend):
        self.__connection = MySql.connect()
        cursor = self.__connection.cursor()   

        print('---consultarn notas---')
        print(idEmpreend)  

        query =  "select mes_vigencia, ano_vigencia, dt_carga  from " + MySql.DB_NAME + ".tb_notas where id_empreendimento = " +  str (idEmpreend) + " group by mes_vigencia, ano_vigencia, dt_carga"

        print('-----------------')
        print(query)
        print('-----------------')
        
        cursor.execute(query)

        lista = cursor.fetchall()
        
        listaNotas = []

        for x in lista:
            n = nota()
            n.setMesVigencia(x[0])
            n.setAnoVigencia(x[1])
            n.setDtCarga(x[2])
            listaNotas.append(n)

        cursor.close()
        MySql.close(self.__connection)
        return listaNotas

    def consultarNotaPelaData(self, idEmpreend, dtCarga):
        self.__connection = MySql.connect()
        cursor = self.__connection.cursor(dictionary=True)   

#        query =  "select id_empreendimento, mes_vigencia, ano_vigencia, dt_carga, item, vl_nota_fiscal, vl_estoque from " + MySql.DB_NAME + ".tb_notas where id_empreendimento = '" + idEmpreend + "' and dt_carga = '" + dtCarga + "'"
        query =  "select id_empreendimento, mes_vigencia, ano_vigencia, dt_carga, item, vl_nota_fiscal, vl_estoque from " + MySql.DB_NAME + ".tb_notas where id_empreendimento = '" + str(idEmpreend) + "'"
    
        print(query)

        cursor.execute(query)

#        linha = cursor.fetchone()
        print('++++++++++++ consultarNotaPelaData +++++++++++++++')
#        print (linha)
#        print('+++++++++++++++++++++++++++')

        lista = cursor.fetchall()
        
        listaItens = []

        for x in lista:
            n = nota()
            n.setMesVigencia(x['mes_vigencia'])
            n.setAnoVigencia(x['ano_vigencia'])
            n.setDtCarga(x['dt_carga'])
            n.setItem(x['item'])
            n.setVlNotaFiscal(x['vl_nota_fiscal'])
            n.setVlEstoque(x['vl_estoque'])
            listaItens.append(n)

#        dados = [list(linha) for linha in listaItens()]

        print('------------------------')       
        print('------------------------')
        cursor.close()
        MySql.close(self.__connection)
#        print ('-----------------> ', dados)
        print ('-----------------> ', listaItens)

        return listaItens

    def carregar_notas(self, caminhoArq, idEmpreend):

        self.__connection = MySql.connect()
        cursor = self.__connection.cursor()

        tabela = pd.read_excel(caminhoArq)

        l, c = tabela.shape
        linha = 0
        m = nota()
        dtTime = datetime.now()
        dateTime = dtTime.strftime("%Y-%m-%d %H:%M:%S")

        print ('------------ carregar_notas -----------------')
        print (idEmpreend)
        print (linha, l)

        while linha < l:

            mesVigencia   = str(tabela.at[linha, 'Mês']).zfill(2)
            anoVigencia   = str(tabela.at[linha, 'Ano'])
            produto       = tabela.at[linha, 'Produtos']
            vlNotaFiscal  = float(tabela.at[linha, 'Valor NF'])
            vlEstoque     = float(tabela.at[linha, 'Estoque'])

            query =  "INSERT INTO " + MySql.DB_NAME + ".tb_notas (id_empreendimento, mes_vigencia, ano_vigencia, dt_carga, produto, vl_nota_fiscal, vl_estoque) VALUES ('" + str(idEmpreend) + "', '" + mesVigencia + "', '" + anoVigencia + "', '" + dateTime + "', '" + produto + "', " + str(vlNotaFiscal) + ", " + str(vlEstoque) + ")"

            print (query)
            cursor.execute(query)
            linha += 1

        self.__connection.commit()
        print(cursor.rowcount,"Nota cadastrada com sucesso")
        cursor.close()
        MySql.close(self.__connection)
