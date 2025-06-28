from utils.dbContext import MySql
from dto.perguntas_aspectos import perguntaAspecto


class aspectosController:
    def todasPerguntasComRespostas(self, idEmpreend, mesVigencia, anoVigencia) -> dict[str, list[perguntaAspecto]]:
        query = f"""SELECT perg.id, perg.pergunta, perg.grupo, perg.opcoes, asp.status, asp.descricao
          FROM {MySql.DB_NAME}.tb_perguntas_aspectos perg
          LEFT JOIN {MySql.DB_NAME}.tb_aspectos asp
          ON asp.id_pergunta_aspecto = perg.id
          AND asp.id_empreendimento = %s
          AND asp.mes_vigencia = %s
          AND asp.ano_vigencia = %s;
        """
        result = MySql.getAll(query, (idEmpreend, mesVigencia, anoVigencia))
        items = {}
        for per in result:
            if per['grupo'] in items:
                items[per['grupo']].append(
                    perguntaAspecto(
                        per['id'],
                        per['pergunta'],
                        per['grupo'],
                        per['opcoes'],
                        per['status'],
                        per['descricao'],
                    )
                )
            else:
                items[per['grupo']] = [
                    perguntaAspecto(
                        per['id'],
                        per['pergunta'],
                        per['grupo'],
                        per['opcoes'],
                        per['status'],
                        per['descricao'],
                    )
                ]
        return items

    def salvar_aspectos(self, campos, idEmpreend, mesVigencia, anoVigencia):
        insertes = []
        updates = []
        total = int(len(campos) / 3) + 1

        for idx in range(1, total):
            idPergunta = campos[f'id_pergunta_{idx}']
            status = campos[f'status_{idx}']
            descricao = campos[f'descricao_{idx}']

            if not status:
                continue

            data = (status, descricao, idEmpreend,
                    idPergunta, mesVigencia, anoVigencia)
            if self.existeResposta(idEmpreend, idPergunta, mesVigencia, anoVigencia):
                updates.append(data)
            else:
                insertes.append(data)

        self.atualiza_aspectos(updates)
        self.inserte_aspectos(insertes)

    def inserte_aspectos(self, data: list[tuple]):
        query = f"INSERT INTO {MySql.DB_NAME}.tb_aspectos (status, descricao, id_empreendimento, id_pergunta_aspecto, mes_vigencia, ano_vigencia) VALUES (%s, %s, %s, %s, %s, %s);"
        MySql.execMany(query, data)

    def atualiza_aspectos(self, data: list[tuple]):
        query = f"""UPDATE {MySql.DB_NAME}.tb_aspectos
                    SET status = %s,
                        descricao = %s
                    WHERE id_empreendimento = %s
                    AND   id_pergunta_aspecto = %s
                    AND   mes_vigencia = %s
                    AND   ano_vigencia = %s;"""
        MySql.execMany(query, data)

    def existeResposta(self, id_empreendimento, id_pergunta_aspecto, mes_vigencia, ano_vigencia) -> bool:
        query = f"""SELECT COUNT(id) existe FROM {MySql.DB_NAME}.tb_aspectos
                        WHERE id_empreendimento = %s
                        AND id_pergunta_aspecto = %s
                        AND mes_vigencia = %s
                        AND ano_vigencia = %s; """
        result = MySql.getOne(
            query, (id_empreendimento, id_pergunta_aspecto, mes_vigencia, ano_vigencia))
        return result['existe'] > 0 if 'existe' in result else False
