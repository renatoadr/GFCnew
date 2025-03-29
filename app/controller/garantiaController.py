from utils.dbContext import MySql
from dto.garantia import garantia

class garantiaController:

  def list(self, idEmpreend):
    query = "SELECT id_garantia, tipo, historico, status, observacao FROM " + MySql.DB_NAME + """.tb_garantias WHERE id_empreendimento = %s AND criado_em = (SELECT MAX(criado_em) FROM db_gfc.tb_garantias WHERE id_empreendimento = %s) ORDER BY tipo, historico, status, id_garantia;"""
    items = MySql.getAll(query, (idEmpreend, idEmpreend))
    ret = []

    for item in items:
      gt = garantia()
      gt.observacao = item.get('observacao')
      gt.documento = item.get('historico')
      gt.Id = item.get('id_garantia')
      gt.status = item.get('status')
      gt.tipo = item.get('tipo')
      ret.append(gt)

    return ret

  def insert_garantias(self, listValores):
    query = "INSERT INTO " + MySql.DB_NAME + """.tb_garantias (id_empreendimento, tipo, historico, status, observacao, criado_em) VALUES (%s, %s, %s, %s, %s, %s)"""
    MySql.execMany(query, listValores)

  def consultargarantiaatual(self, idEmpreend, tipo):
      self.__connection = MySql.connect()
      cursor = self.__connection.cursor(dictionary=True)   

      query =  "select id_garantia, id_empreendimento, criado_em, tipo, historico, status, observacao from " + MySql.DB_NAME + ".tb_garantias where id_empreendimento = '" + str(idEmpreend) + "' and tipo = '" + tipo + "' and criado_em = (SELECT MAX(criado_em) FROM " + MySql.DB_NAME + ".tb_garantias WHERE id_empreendimento = '" + str(idEmpreend) + "' and tipo = '" + tipo + "')"
      print(query)

      items = MySql.getAll(query) 
#      cursor.execute(query)

#      print('++++++++++++ consultargarantiaatual +++++++++++++++')
#        print (linha)
#        print('+++++++++++++++++++++++++++')

      lista = []
      
      for item in items:
        gt = garantia()
        gt.observacao = item.get('observacao')
        gt.documento = item.get('historico')
        gt.status = item.get('status')
        lista.append(gt)

      print('------------------------')       
      print('------------------------')
#      cursor.close()
#      MySql.close(self.__connection)
#        print ('-----------------> ', dados)
      print ('-----------------> ', lista)

      return lista