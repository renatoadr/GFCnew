from utils.dbContext import MySql
from dto.agenda import agenda


class agendaController:

    def inserirAgendas(self, agds: list[agenda]):
        query = "INSERT INTO " + MySql.DB_NAME + \
            """.tb_agendas ( id_empreendimento, mes_vigencia, ano_vigencia, id_atividade, status, dt_atividade, nm_resp_atividade, dt_baixa, nm_resp_baixa ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s )"""

        itens = []

        for ag in agds:
            itens.append((
                ag.getIdEmpreend(),
                ag.getMesVigencia(),
                ag.getAnoVigencia(),
                ag.getIdAtividade(),
                ag.getStatus(),
                ag.getDtAtividade(),
                ag.getNmRespAtividade(),
                ag.getDtBaixa(),
                ag.getNmRespBaixa()
            ))

        MySql.exec(query, (itens))

    def consultarAgendas(self, idEmpreend, cur_date):
        query = f"""SELECT A.id, A.id_empreendimento, A.mes_vigencia, A.ano_vigencia, A.id_atividade, AT.descr_atividade, A.status, A.dt_atividade, A.nm_resp_atividade, A.dt_baixa, A.nm_resp_baixa
        FROM {MySql.DB_NAME}.tb_agendas A
        INNER JOIN  {MySql.DB_NAME}.tb_agendas_atividades AT
        ON A.id_atividade = AT.id_atividade
        WHERE A.id_empreendimento = %s
        AND DATE(CONCAT(A.ano_vigencia, '-', A.mes_vigencia, '-01')) = DATE(CONCAT(%s, '-01'))
        ORDER BY A.dt_atividade"""

        lista = MySql.getAll(query, (idEmpreend, cur_date))

        listaAgendas = []

        for x in lista:
            a = agenda()
            a.setId(x['id'])
            a.setIdEmpreend(x['id_empreendimento'])
            a.setMesVigencia(x['mes_vigencia'])
            a.setAnoVigencia(x['ano_vigencia'])
            a.setIdAtividade(x['id_atividade'])
            a.setDescrAtividade(x['descr_atividade'])
            a.setStatus(x['status'])
            a.setDtAtividade(x['dt_atividade'])
            a.setNmRespAtividade(x['nm_resp_atividade'])
            a.setDtBaixa(x['dt_baixa'])
            a.setNmRespBaixa(x['nm_resp_baixa'])
            listaAgendas.append(a)

        return listaAgendas

    def consultarAgendaPeloId(self, idAgenda):
        query = f"""SELECT A.id, A.id_empreendimento, A.mes_vigencia, A.ano_vigencia, A.id_atividade, AT.descr_atividade, A.status, A.dt_atividade, A.nm_resp_atividade, A.dt_baixa, A.nm_resp_baixa
        FROM {MySql.DB_NAME}.tb_agendas A
        INNER JOIN  {MySql.DB_NAME}.tb_agendas_atividades AT
        ON A.id_atividade = AT.id_atividade
        WHERE A.id = %s"""

        record = MySql.getOne(query, (idAgenda,))

        if not record:
            return None
        else:
            agd = agenda()
            agd.setId(record['id'])
            agd.setIdEmpreend(record['id_empreendimento'])
            agd.setMesVigencia(record['mes_vigencia'])
            agd.setAnoVigencia(record['ano_vigencia'])
            agd.setIdAtividade(record['id_atividade'])
            agd.setDescrAtividade(record['descr_atividade'])
            agd.setStatus(record['status'])
            agd.setDtAtividade(record['dt_atividade'])
            agd.setNmRespAtividade(record['nm_resp_atividade'])
            agd.setDtBaixa(record['dt_baixa'])
            agd.setNmRespBaixa(record['nm_resp_baixa'])
            return agd

    def salvarAgenda(self, agd: agenda, id):
        query = f"""UPDATE {MySql.DB_NAME}.tb_agendas SET
            id_empreendimento = %s,
            mes_vigencia = %s,
            ano_vigencia = %s,
            id_atividade = %s,
            status = %s,
            dt_atividade = %s,
            nm_resp_atividade = %s,
            dt_baixa = %s,
            nm_resp_baixa = %s
            WHERE id = %s
        """
        MySql.exec(query, (
            agd.getIdEmpreend(),
            agd.getMesVigencia(),
            agd.getAnoVigencia(),
            agd.getIdAtividade(),
            agd.getStatus(),
            agd.getDtAtividade(),
            agd.getNmRespAtividade(),
            agd.getDtBaixa(),
            agd.getNmRespBaixa(),
            id
        ))

    def excluirAgenda(self, idAgenda):
        query = f"DELETE FROM {MySql.DB_NAME}.tb_Agendas WHERE id = %s "
        MySql.exec(query, (idAgenda,))
