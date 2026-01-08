import math
from dto.produto import produto
from utils.dbContext import MySql
from utils.logger import logger


class produtosController:

    def todos_produtos(self, filtros, pagina_atual=1, itens_por_pagina=15):
        query_total = f"""SELECT COUNT(*) AS total
        FROM {MySql.DB_NAME}.tb_itens_produtos p
        JOIN {MySql.DB_NAME}.tb_categorias c
        ON p.id_cat = c.id """
        query = f"""SELECT
          p.id,
          p.id_cat,
          c.descricao AS categoria,
          p.codigo,
          p.unidade,
          p.ativo,
          p.descricao
        FROM {MySql.DB_NAME}.tb_itens_produtos p
        JOIN {MySql.DB_NAME}.tb_categorias c
        ON p.id_cat = c.id """

        where_clauses = []
        params = []

        if filtros[0] is not None and filtros[0] != "":
            where_clauses.append(
                "(lower(c.descricao) REGEXP lower(%s))"
            )
            params.append(filtros[0])

        if filtros[1] is not None and filtros[1] != "":
            where_clauses.append("lower(p.descricao) REGEXP lower(%s)")
            params.append(filtros[1])

        if where_clauses:
            query += " WHERE " + " AND ".join(where_clauses)
            query_total += " WHERE " + " AND ".join(where_clauses)
            total_data = MySql.getOne(query_total, tuple(params))
        else:
            total_data = MySql.getOne(query_total)

        query += " ORDER BY p.id LIMIT %s OFFSET %s;"
        params.extend(
            [itens_por_pagina, (pagina_atual - 1) * itens_por_pagina]
        )

        total_paginas = math.ceil(
            total_data["total"] / itens_por_pagina
        ) if itens_por_pagina > 0 else 1
        data = MySql.getAll(query, tuple(params))

        produtos = []
        for row in data:
            prod = produto()
            prod.setId(row['id'])
            prod.setIdCategoria(row['id_cat'])
            prod.setCategoria(row['categoria'])
            prod.setCodigo(row['codigo'])
            prod.setUnidade(row['unidade'])
            prod.setAtivo(row['ativo'])
            prod.setDescricao(row['descricao'])
            produtos.append(prod)
        return (produtos, total_paginas)

    def obter_produto_por_id(self, id):
        query = f"""SELECT
          p.id,
          p.id_cat,
          c.descricao AS categoria,
          p.codigo,
          p.unidade,
          p.ativo,
          p.descricao
        FROM {MySql.DB_NAME}.tb_itens_produtos p
        JOIN {MySql.DB_NAME}.tb_categorias c
        ON p.id_cat = c.id
        WHERE p.id = %s;"""
        row = MySql.getOne(query, (id,))
        if row:
            prod = produto()
            prod.setId(row['id'])
            prod.setIdCategoria(row['id_cat'])
            prod.setCategoria(row['categoria'])
            prod.setCodigo(row['codigo'])
            prod.setUnidade(row['unidade'])
            prod.setAtivo(row['ativo'])
            prod.setDescricao(row['descricao'])
            return prod
        else:
            return None

    def deletar_produto(self, id):
        query = f"DELETE FROM {MySql.DB_NAME}.tb_itens_produtos WHERE id = %s;"
        MySql.exec(query, (id,))
        logger.info(f"Produto com ID {id} deletado com sucesso.")

    def atualizar_produto(self, id, id_cat, codigo, unidade, ativo, descricao):
        query = f"""UPDATE {MySql.DB_NAME}.tb_itens_produtos
          SET id_cat = %s,
              descricao = %s,
              unidade = %s,
              codigo = %s,
              ativo = %s
          WHERE id = %s;"""
        MySql.exec(query, (id_cat, descricao, unidade, codigo, ativo, id))
        logger.info(f"Produto com ID {id} atualizado com sucesso.")

    def cadastrar_produto(self, id_cat, descricao, unidade, codigo, ativo):
        try:
            query = f"""INSERT INTO {MySql.DB_NAME}.tb_itens_produtos
              (id_cat, descricao, unidade, codigo, ativo)
              VALUES (%s, %s, %s, %s, %s);"""
            MySql.exec(query, (id_cat, descricao, unidade, codigo, ativo))
            logger.info(f"Produto '{descricao}' cadastrado com sucesso.")
        except Exception as e:
            logger.exception(
                f"Erro ao cadastrar produto '{descricao}': {str(e)}")
