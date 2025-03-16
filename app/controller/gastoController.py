#controller or business logic
# Trata base de GASTO


from dto.gasto import gasto
from utils.dbContext import MySql

class gastoController:
    __connection = None

    def __init__(self):
        pass

    def inserirGasto(self, gasto):
        self.__connection = MySql.connect()
        cursor = self.__connection.cursor()   

        query =  "INSERT INTO " + MySql.DB_NAME + \
                ".tb_gastos (id_gasto, id_empreendimento, dt_evento, vlr_medicao, vlr_compras, vlr_rh_adm) \
                VALUES ('" + gasto.getIdGasto() + "', " + str(gasto.getIdEmpreend()) + ", '" + gasto.getDtEvento() + "', " + str(gasto.getVlMedicao()) + ", " + str(gasto.getVlCompras()) + ", " + str(gasto.getVlRhAdm()) + ")"
        
        print (query)
        cursor.execute(query)

        self.__connection.commit()     
        print(cursor.rowcount,"Gasto cadastrado com sucesso")     
        cursor.close()
        MySql.close(self.__connection)
