from utils.dbContext import MySql
from decimal import Decimal, ROUND_HALF_UP


class sinapiController:

    def inserir_custos(self, custos: list[tuple]):
        query = f"INSERT INTO {MySql.DB_NAME}.tb_sinapi_custo (dt_criacao, dt_vigencia, dt_emissao, cod_item, nm_tipo, vl_ac, vl_al, vl_am, vl_ap, vl_ba, vl_ce, vl_df, vl_es, vl_go, vl_ma, vl_mg, vl_ms, vl_mt, vl_pa, vl_pb, vl_pe, vl_pi, vl_pr, vl_rj, vl_rn, vl_ro, vl_rr, vl_rs, vl_sc, vl_se, vl_sp, vl_to) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s )"

        MySql.execMany(query, tuple(custos))

    def inserir_itens(self, itens: list[tuple]):
        query = f"INSERT INTO {MySql.DB_NAME}.tb_sinapi_item (dt_criacao, dt_vigencia, dt_emissao, cod_item, cod_composicao, nm_grupo, tp_item, desc_item, tp_unidade, vl_coeficiente) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

        MySql.execMany(query, tuple(itens))

    def deletar_itens(data):
        query = f"DELETE FROM {MySql.DB_NAME}.tb_sinapi_item WHERE dt_criacao <= %s"
        MySql.exec(query, (data,))

    def deletar_custos(data):
        query = f"DELETE FROM {MySql.DB_NAME}.tb_sinapi_custo WHERE dt_criacao <= %s"
        MySql.exec(query, (data,))

    def existe_itens():
        query = f"SELECT COUNT(id) AS total FROM {MySql.DB_NAME}.tb_sinapi_item"
        dados = MySql.getOne(query)
        return dados['total'] > 0

    def valor_total_itens(idEmpreend, codigo, quant):
        query = f"""
          SELECT
            it.vl_coeficiente,
            it.cod_item,
            it.desc_item,
            CASE te.estado
              WHEN 'AC' THEN ct.vl_ac
              WHEN 'AL' THEN ct.vl_al
              WHEN 'AM' THEN ct.vl_am
              WHEN 'AP' THEN ct.vl_ap
              WHEN 'BA' THEN ct.vl_ba
              WHEN 'CE' THEN ct.vl_ce
              WHEN 'ES' THEN ct.vl_es
              WHEN 'GO' THEN ct.vl_go
              WHEN 'MA' THEN ct.vl_ma
              WHEN 'MG' THEN ct.vl_mg
              WHEN 'MS' THEN ct.vl_ms
              WHEN 'MT' THEN ct.vl_mt
              WHEN 'PA' THEN ct.vl_pa
              WHEN 'PB' THEN ct.vl_pb
              WHEN 'PE' THEN ct.vl_pe
              WHEN 'PI' THEN ct.vl_pi
              WHEN 'PR' THEN ct.vl_pr
              WHEN 'RJ' THEN ct.vl_rj
              WHEN 'RN' THEN ct.vl_rn
              WHEN 'RO' THEN ct.vl_ro
              WHEN 'RR' THEN ct.vl_rr
              WHEN 'RS' THEN ct.vl_rs
              WHEN 'SC' THEN ct.vl_sc
              WHEN 'SE' THEN ct.vl_se
              WHEN 'SP' THEN ct.vl_sp
              WHEN 'TO' THEN ct.vl_to
              WHEN 'DF' THEN ct.vl_df
              ELSE 0
            END vl_base
            FROM {MySql.DB_NAME}.tb_sinapi_item it
            JOIN {MySql.DB_NAME}.tb_sinapi_custo ct
            ON it.cod_item = ct.cod_item
            LEFT JOIN {MySql.DB_NAME}.tb_empreendimentos te
            ON te.id_empreendimento = %s
            WHERE it.cod_composicao = %s
            AND it.dt_vigencia = (
              SELECT MAX(dt_vigencia) FROM {MySql.DB_NAME}.tb_sinapi_item
              WHERE cod_composicao = it.cod_composicao
            );
        """

        itens = MySql.getAll(query, (idEmpreend, codigo))
        total = 0
        vl_unitario = 0

        for item in itens:
            temp_calc = item['vl_base'] * item['vl_coeficiente']
            vl_unitario += temp_calc
            total += temp_calc * quant
        return {
            "vl_unitario": vl_unitario.quantize(Decimal('0.' + '0' * 2), rounding=ROUND_HALF_UP),
            "total": total.quantize(Decimal('0.' + '0' * 2), rounding=ROUND_HALF_UP)
        }
