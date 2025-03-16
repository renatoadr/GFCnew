#controller or business logic
# Trata base de CONTAS

from dto.conta import conta
from utils.dbContext import MySql

class contaController:
    __connection = None

    def __init__(self):
        pass

    def consultarConta(self, idEmpreend):
        self.__connection = MySql.connect()
        cursor = self.__connection.cursor(dictionary=True)   

        query =  "select id_empreendimento, mes_vigencia, ano_vigencia, vl_liberacao, vl_material_estoque, vl_aporte_construtora, vl_receita_recebiveis, vl_pagto_obra, vl_pagto_rh, vl_diferenca, vl_saldo from " + MySql.DB_NAME + ".tb_contas where id_empreendimento = '" + str(idEmpreend) + "'"
    
        print(query)

        cursor.execute(query)

#        linha = cursor.fetchone()
#        print('++++++++++++ consultarNotaPelaData +++++++++++++++')
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
