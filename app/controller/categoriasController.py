import math
from dto.categoria import categoria
from utils.dbContext import MySql
from utils.logger import logger


class categoriasController:

    def todas_categorias(self, filtros, pagina_atual, itens_por_pagina):
        query_total = f"""SELECT COUNT(*) AS total
        FROM {MySql.DB_NAME}.tb_categorias """
        query = f"""SELECT
          ct1.id,
          ct1.id_cat_pai,
          ct2.descricao desc_pai,
          ct1.descricao,
          ct1.agrupador,
          ct1.ativo
        FROM {MySql.DB_NAME}.tb_categorias ct1
        LEFT JOIN {MySql.DB_NAME}.tb_categorias ct2
        ON ct1.id_cat_pai = ct2.id """

        where_clauses = []
        where_clauses_total = []
        params = []
        params_total = []

        if filtros[0] is not None and filtros[0] != "":
            where_clauses.append(
                "(lower(ct1.descricao) REGEXP lower(%s) OR lower(ct2.descricao) REGEXP lower(%s))"
            )
            where_clauses_total.append(
                "lower(descricao) REGEXP lower(%s)"
            )
            params.append(filtros[0])
            params.append(filtros[0])
            params_total.append(filtros[0])

        if filtros[1] is not None and filtros[1] != "":
            where_clauses.append("lower(ct1.agrupador) REGEXP lower(%s)")
            params.append(filtros[1])
            where_clauses_total.append("lower(agrupador) REGEXP lower(%s)")
            params_total.append(filtros[1])

        if where_clauses:
            query += " WHERE " + " AND ".join(where_clauses)
            query_total += " WHERE " + " AND ".join(where_clauses_total)
            total_data = MySql.getOne(query_total, tuple(params_total))
        else:
            total_data = MySql.getOne(query_total)

        query += " ORDER BY ct1.id LIMIT %s OFFSET %s;"
        params.extend(
            [itens_por_pagina, (pagina_atual - 1) * itens_por_pagina])

        total_paginas = math.ceil(
            total_data["total"] / itens_por_pagina
        ) if itens_por_pagina > 0 else 1
        data = MySql.getAll(query, tuple(params))

        categorias = []
        for row in data:
            cat = categoria()
            cat.setId(row['id'])
            cat.setIdCategoriaPai(row['id_cat_pai'])
            cat.setDescricaoPai(row['desc_pai'])
            cat.setDescricao(row['descricao'])
            cat.setAgrupador(row['agrupador'])
            cat.setAtivo(row['ativo'])
            categorias.append(cat)
        return (categorias, total_paginas)

    def lista_categorias_pai(self):
        query = f"""SELECT
          ct.id,
          ct.descricao,
          ct.agrupador
        FROM {MySql.DB_NAME}.tb_categorias ct
        WHERE ct.id_cat_pai IS NULL
        ORDER BY ct.id;"""
        data = MySql.getAll(query)
        categorias = []
        for row in data:
            cat = categoria()
            cat.setId(row['id'])
            cat.setDescricao(row['descricao'])
            cat.setAgrupador(row['agrupador'])
            categorias.append(cat)
        return categorias

    def cadastrar_categoria(self, categoria_pai, descricao, agrupador, ativo=True):
        try:
            query = f"""INSERT INTO {MySql.DB_NAME}.tb_categorias
                  (id_cat_pai, descricao, agrupador, ativo)
                  VALUES (%s, %s, %s, %s);"""
            MySql.exec(
                query, (categoria_pai, descricao, agrupador, ativo))
            logger.info(
                f"Categoria '{descricao}' cadastrada com sucesso.")
        except Exception as e:
            logger.error(
                f"Erro ao cadastrar categoria '{descricao}': {str(e)}")

    def deletar_categoria(self, id):
        try:
            query = f"""DELETE FROM {MySql.DB_NAME}.tb_categorias
              WHERE id = %s;"""
            MySql.exec(query, (id,))
            logger.info(f"Categoria ID '{id}' deletada com sucesso.")
        except Exception as e:
            logger.error(
                f"Erro ao deletar categoria ID '{id}': {str(e)}")

    def listar_agrupadores(self):
        query = f"""SELECT DISTINCT agrupador
          FROM {MySql.DB_NAME}.tb_categorias;"""
        data = MySql.getAll(query)
        agrupadores = [row['agrupador'] for row in data]
        return agrupadores

    def atualizar_categoria(self, id, categoria_pai, descricao, agrupador, ativo):
        try:
            query = f"""UPDATE {MySql.DB_NAME}.tb_categorias
              SET id_cat_pai = %s,
                  descricao = %s,
                  agrupador = %s,
                  ativo = %s
              WHERE id = %s;"""
            MySql.exec(
                query, (categoria_pai, descricao, agrupador, ativo, id))
            logger.info(
                f"Categoria ID '{id}' atualizada com sucesso.")
        except Exception as e:
            logger.error(
                f"Erro ao atualizar categoria ID '{id}': {str(e)}")

    def obter_categoria_por_id(self, id):
        query = f"""SELECT
          id,
          id_cat_pai,
          descricao,
          agrupador,
          ativo
        FROM {MySql.DB_NAME}.tb_categorias
        WHERE id = %s;"""
        data = MySql.getOne(query, (id,))
        if data:
            cat = categoria()
            cat.setId(data['id'])
            cat.setIdCategoriaPai(data['id_cat_pai'])
            cat.setDescricao(data['descricao'])
            cat.setAgrupador(data['agrupador'])
            cat.setAtivo(data['ativo'])
            return cat
        else:
            return None
