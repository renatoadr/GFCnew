from utils.dbContext import MySql
from dto.garantia import garantia

class garantiaController:

  def list(self, idEmpreend):
    query = "SELECT id_garantia, mes_vigencia, ano_vigencia, tipo, historico, status, observacao FROM " + MySql.DB_NAME + """.tb_garantias WHERE id_empreendimento = %s AND criado_em = (SELECT MAX(criado_em) FROM db_gfc.tb_garantias WHERE id_empreendimento = %s) ORDER BY tipo, historico, status, id_garantia;"""
    items = MySql.getAll(query, (idEmpreend, idEmpreend))
    ret = []

    for item in items:
      gt = garantia()
      gt.anoVigencia = item.get('ano_vigencia')
      gt.mesVigencia = item.get('mes_vigencia')
      gt.observacao = item.get('observacao')
      gt.documento = item.get('historico')
      gt.Id = item.get('id_garantia')
      gt.status = item.get('status')
      gt.tipo = item.get('tipo')
      ret.append(gt)

    return ret

  def insert_garantias(self, listValores):
    query = "INSERT INTO " + MySql.DB_NAME + """.tb_garantias (id_empreendimento, mes_vigencia, ano_vigencia, tipo, historico, status, observacao, criado_em) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"""
    MySql.execMany(query, listValores)
