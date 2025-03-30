# controller or business logic
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

        query = "select mes_vigencia, ano_vigencia, dt_carga  from " + MySql.DB_NAME + \
            ".tb_notas where id_empreendimento = " + \
                str(idEmpreend) + " group by mes_vigencia, ano_vigencia, dt_carga"

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
        query = "select id_empreendimento, mes_vigencia, ano_vigencia, dt_carga, item, vl_nota_fiscal, vl_estoque from " + \
            MySql.DB_NAME + ".tb_notas where id_empreendimento = '" + \
                str(idEmpreend) + "'"

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
        print('-----------------> ', listaItens)

        return listaItens

    def carregar_notas(self, file, idEmpreend):

        self.__connection = MySql.connect()
        cursor = self.__connection.cursor()

        tabela = pd.read_excel(file)

        l, c = tabela.shape
        linha = 0
        m = nota()
        dtTime = datetime.now()
        dateTime = dtTime.strftime("%Y-%m-%d %H:%M:%S")

        print('------------ carregar_notas -----------------')
        print(idEmpreend)
        print(linha, l)

        while linha < l:

            mesVigencia = str(tabela.at[linha, 'Mês']).zfill(2)
            anoVigencia = str(tabela.at[linha, 'Ano'])
            produto = tabela.at[linha, 'Produtos']
            vlNotaFiscal = float(tabela.at[linha, 'Valor NF'])
            vlEstoque = float(tabela.at[linha, 'Estoque'])

            query = "INSERT INTO " + MySql.DB_NAME + ".tb_notas (id_empreendimento, mes_vigencia, ano_vigencia, dt_carga, produto, vl_nota_fiscal, vl_estoque) VALUES ('" + str(
                idEmpreend) + "', '" + mesVigencia + "', '" + anoVigencia + "', '" + dateTime + "', '" + produto + "', " + str(vlNotaFiscal) + ", " + str(vlEstoque) + ")"

            print(query)
            cursor.execute(query)
            linha += 1

        self.__connection.commit()
        print(cursor.rowcount, "Nota cadastrada com sucesso")
        cursor.close()
        MySql.close(self.__connection)

    def excluir_por_data(self, idEmpreend, dt_carga, mes_vig, ano_vig):
        query = "DELETE FROM " + MySql.DB_NAME + \
            """.tb_notas WHERE id_empreendimento = %s AND mes_vigencia = %s AND ano_vigencia = %s AND dt_carga = %s """
        MySql.exec(query, (idEmpreend, mes_vig, ano_vig, dt_carga))

    def listaNotas(self, idEmpreend, dtCarga, mesVig, anoVig):
        query = "SELECT id_nota, mes_vigencia, ano_vigencia, produto, vl_nota_fiscal, vl_estoque FROM " + \
            MySql.DB_NAME + ".tb_notas WHERE id_empreendimento = %s AND dt_carga = %s AND mes_vigencia = %s AND ano_vigencia = %s "

        lista = MySql.getAll(query, (idEmpreend, dtCarga, mesVig, anoVig))

        listaNotas = []

        for it in lista:
            n = nota()
            n.setIdNota(it['id_nota'])
            n.setMesVigencia(it['mes_vigencia'])
            n.setAnoVigencia(it['ano_vigencia'])
            n.setProduto(it['produto'])
            n.setVlNotaFiscal(it['vl_nota_fiscal'])
            n.setVlEstoque(it['vl_estoque'])
            listaNotas.append(n)
        return listaNotas

    def excluir_nota(self, id):
        query = "DELETE FROM " + MySql.DB_NAME + \
            """.tb_notas WHERE id_nota = %s """
        MySql.exec(query, (id,))

    def nota_por_id(self, id):
        query = "SELECT id_nota, id_empreendimento, mes_vigencia, ano_vigencia, dt_carga, produto, vl_nota_fiscal, vl_estoque FROM " + \
            MySql.DB_NAME + ".tb_notas WHERE id_nota = %s "
        nt = MySql.getOne(query, (id,))

        recNota = nota()
        recNota.setIdNota(nt['id_nota'])
        recNota.setIdEmpreend(nt['id_empreendimento'])
        recNota.setMesVigencia(nt['mes_vigencia'])
        recNota.setAnoVigencia(nt['ano_vigencia'])
        recNota.setDtCarga(nt['dt_carga'])
        recNota.setProduto(nt['produto'])
        recNota.setVlNotaFiscal(nt['vl_nota_fiscal'])
        recNota.setVlEstoque(nt['vl_estoque'])
        return recNota

    def salvar_nota(self, nota: nota):
        query = "UPDATE " + MySql.DB_NAME + \
            ".tb_notas SET produto = %s, vl_nota_fiscal = %s, vl_estoque = %s WHERE id_nota = %s "
        MySql.exec(query, (
            nota.getProduto(),
            nota.getVlNotaFiscal(),
            nota.getVlEstoque(),
            nota.getIdNota()
        ))

    def inserir_nota(self, nota: nota):
        query = "INSERT INTO " + MySql.DB_NAME + \
            ".tb_notas (id_empreendimento, mes_vigencia, ano_vigencia, dt_carga, produto, vl_nota_fiscal, vl_estoque) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        MySql.exec(query, (
            nota.getIdEmpreend(),
            nota.getMesVigencia(),
            nota.getAnoVigencia(),
            nota.getDtCarga(),
            nota.getProduto(),
            nota.getVlNotaFiscal(),
            nota.getVlEstoque()
        ))
