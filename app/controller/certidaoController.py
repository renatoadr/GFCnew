#controller or business logic
# Trata base de CRETIDÕES


from dto.certidao import certidao
from utils.dbContext import MySql
from datetime import datetime
import pandas as pd
from utils.converter import converterDateTimeToDateEnFormat

class certidaoController:
    __connection = None

    def __init__(self):
        pass

    def consultarCertidoes(self, idEmpreend):
        self.__connection = MySql.connect()
        cursor = self.__connection.cursor(dictionary=True)  

        print('---consultar certidoes---')
        print('consultar certidoes ',idEmpreend)  

        query =  "select id_empreendimento, estadual_status, estadual_validade, fgts_status, fgts_validade, municipal_status, municipal_validade, srf_inss_status, srf_inss_validade, trabalhista_status, trabalhista_validade  from " + MySql.DB_NAME + ".tb_certidoes where id_empreendimento = " + str(idEmpreend)
            
        print('-----------------')
        print(query)
        print('-----------------')
        
        cursor.execute(query)

        lista = cursor.fetchall()
        
        listaItens = []

        for x in lista:
            n = certidao()
            n.setIdEmpreend(x['id_empreendimento'])
            n.setEstadualStatus(x['estadual_status'])
            n.setEstadualValidade(x['estadual_validade'])
            n.setFgtsStatus(x['fgts_status'])
            n.setFgtsValidade(x['fgts_validade'])
            n.setMunicipalStatus(x['municipal_status'])
            n.setMunicipalValidade(x['municipal_validade'])
            n.setSrfInssStatus(x['srf_inss_status'])
            n.setSrfInssValidade(x['srf_inss_validade'])
            n.setTrabalhistaStatus(x['trabalhista_status'])
            n.setTrabalhistaValidade(x['trabalhista_validade'])
            listaItens.append(n)

        cursor.close()
        MySql.close(self.__connection)
        return listaItens

    def inserirCertidoes(self, cert):
        self.__connection = MySql.connect()
        cursor = self.__connection.cursor()

        query =  "INSERT INTO " + MySql.DB_NAME + """.tb_certidoes (id_empreendimento, estadual_status, estadual_validade, fgts_status, fgts_validade, municipal_status, municipal_validade, srf_inss_status, srf_inss_validade, trabalhista_status, trabalhista_validade) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""

        print (query)
        print ('inserirCertidoes ', cert.getIdEmpreend())

        cursor.execute(query, (
          cert.getIdEmpreend(),
          cert.getEstadualStatus(),
          cert.getEstadualValidade(),
          cert.getFgtsStatus(),
          cert.getFgtsValidade(),
          cert.getMunicipalStatus(),
          cert.getMunicipalValidade(),
          cert.getSrfInssStatus(),
          cert.getSrfInssValidade(),
          cert.getTrabalhistaStatus(),
          cert.getTrabalhistaValidade()
        ))

        self.__connection.commit()
        print(cursor.rowcount,"Certidões cadastradas com sucesso")
        cursor.close()
        MySql.close(self.__connection)

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
