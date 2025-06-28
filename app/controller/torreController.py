# controller or business logic
# Trata base de TORRES

from dto.torre_cosolidado import torre_consolidado
from utils.dbContext import MySql
from datetime import datetime
from dto.torre import torre


class torreController:
    __connection = None

    def inserirTorre(self, torre: torre):
        self.__connection = MySql.connect()
        cursor = self.__connection.cursor()

        queryUnidade = "INSERT INTO " + MySql.DB_NAME + \
            ".tb_unidades (id_empreendimento, id_torre, unidade, mes_vigencia, ano_vigencia, status, vl_unidade) VALUES (%s, %s, %s, %s, %s, %s, %s);"
        queryTorre = "INSERT INTO " + MySql.DB_NAME + \
            ".tb_torres ( id_empreendimento, nm_torre, qt_unidade, qt_andar, qt_coberturas, prefix_cobertura, num_apt_um_andar_um, vl_unidade, vl_cobertura ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);"

        dadosUnidade = []

        cursor.execute(queryTorre, (
            torre.getIdEmpreend(),
            torre.getNmTorre(),
            torre.getQtUnidade(),
            torre.getQtAndar(),
            torre.getQtCobertura(),
            torre.getPrefixCobertura(),
            torre.getNumAptUmAndarUm(),
            torre.getVlrCobertura(),
            torre.getVlrUnidade()
        ))

        date = datetime.now()
        baseAndar = 10 if len(str(torre.getNumAptUmAndarUm())) == 2 else 100
        initAp = int(torre.getNumAptUmAndarUm())
        qtdAndar = int(torre.getQtAndar())
        qtdApt = int(torre.getQtUnidade())
        qtdCobertura = int(torre.getQtCobertura()
                           ) if torre.getQtCobertura() else 0
        prefix = torre.getPrefixCobertura()
        vlrUnidade = torre.getVlrUnidade()
        vlrCobertura = torre.getVlrCobertura()

        currentAndar = 1
        currentApt = initAp
        currentBase = baseAndar
        limitePorAndar = currentApt + qtdApt - 1

        while currentAndar <= qtdAndar:
            dadosUnidade.append((
                torre.getIdEmpreend(),
                cursor.lastrowid,
                currentApt,
                str(date.month).zfill(2),
                date.year,
                'Estoque',
                vlrUnidade
            ))
            currentApt += 1

            if currentApt > limitePorAndar:
                currentAndar += 1
                currentBase += baseAndar
                currentApt = currentBase + 1
                limitePorAndar += baseAndar

        if qtdCobertura > 0:
            for num in range(1, qtdCobertura + 1):
                dadosUnidade.append((
                    torre.getIdEmpreend(),
                    cursor.lastrowid,
                    f"{prefix} {num}",
                    str(date.month).zfill(2),
                    date.year,
                    'Estoque',
                    vlrCobertura
                ))

        cursor.executemany(queryUnidade, dadosUnidade)
        self.__connection.commit()
        cursor.close()
        MySql.close(self.__connection)

    def consultarTorres(self, idEmpreend):
        query = "select * from " + MySql.DB_NAME + \
            ".tb_torres where id_empreendimento = %s order by nm_torre"

        lista = MySql.getAll(query, (idEmpreend,))
        listatorres = []

        for x in lista:
            t = torre()
            t.setIdTorre(x['id_torre'])
            t.setIdEmpreend(x['id_empreendimento'])
            t.setNmTorre(x['nm_torre'])
            t.setQtUnidade(x['qt_unidade'])
            t.setQtAndar(x['qt_andar'])
            t.setQtCobertura(x['qt_coberturas'])
            t.setPrefixCobertura(x['prefix_cobertura'])
            t.setNumAptUmAndarUm(x['num_apt_um_andar_um'])
            listatorres.append(t)

        return listatorres

    def consultarTorrePeloId(self, idTorre):
        query = f"""SELECT id_torre, id_empreendimento, nm_torre, qt_unidade, qt_andar, qt_coberturas, prefix_cobertura, num_apt_um_andar_um from {MySql.DB_NAME}.tb_torres WHERE id_torre = %s"""

        linha = MySql.getOne(query, (idTorre,))

        linhaT = torre()
        linhaT.setIdTorre(linha['id_torre'])
        linhaT.setIdEmpreend(linha['id_empreendimento'])
        linhaT.setNmTorre(linha['nm_torre'])
        linhaT.setQtUnidade(linha['qt_unidade'])
        linhaT.setQtAndar(linha['qt_andar'])
        linhaT.setQtCobertura(linha['qt_coberturas'])
        linhaT.setPrefixCobertura(linha['prefix_cobertura'])
        linhaT.setNumAptUmAndarUm(linha['num_apt_um_andar_um'])

        return linhaT

    def consultarNomeTorre(self, idTorre):
        self.__connection = MySql.connect()
        cursor = self.__connection.cursor(dictionary=True)

        query = "select nm_torre from " + MySql.DB_NAME + \
            ".tb_torres where id_torre = " + str(idTorre)

        print('-----------consultarNomeTorre----------')
        print(query)

        cursor.execute(query)

        linha = cursor.fetchone()
    #    print('+++++++++++++++++++++++++++')
    #    print (linha)

        linhaT = torre()
        linhaT.setNmTorre(linha['nm_torre'])
        nmTorre = linha['nm_torre']
     #   print('------------------------')
     #   print(nmTorre)
     #   print('-----------fim consultarNomeTorre----------')
        cursor.close()
        MySql.close(self.__connection)

        return nmTorre

    def salvarTorre(self, torre):
        self.__connection = MySql.connect()
        cursor = self.__connection.cursor()

        queryTorre = "update " + MySql.DB_NAME + \
            ".tb_torres set nm_torre = %s, qt_unidade = %s, qt_andar = %s, qt_coberturas = %s, prefix_cobertura = %s, num_apt_um_andar_um = %s where id_torre = %s;"

        cursor.execute(queryTorre, (
            torre.getNmTorre(),
            torre.getQtUnidade(),
            torre.getQtAndar(),
            torre.getQtCobertura(),
            torre.getPrefixCobertura(),
            torre.getNumAptUmAndarUm()
        ))

        self.__connection.commit()
        print(cursor.rowcount, "Torre atualizada com sucesso")
        cursor.close()
        MySql.close(self.__connection)

    def excluirTorre(self, idTorre):
        query = f"delete from {MySql.DB_NAME}.tb_torres" + \
            " where id_torre = %s "
        MySql.exec(query, (idTorre,))

    def existeNomeTorre(self, nome):
        query = f"select count(id_torre) existe FROM {MySql.DB_NAME}.tb_torres" + \
            " WHERE nm_torre = %s "
        result = MySql.getOne(query, (nome,))
        return result['existe'] > 0

    def consolidado(self, idEmpreend: int) -> torre_consolidado:
        query = f"""SELECT
                      SUM(qt_unidade * qt_andar + qt_coberturas) num_unidades,
                      COUNT(id_torre) num_blocos,
                      SUM(qt_andar) num_pavimentos
                  FROM tb_torres
                  WHERE id_empreendimento = %s ;"""
        result = MySql.getOne(query, (idEmpreend,))
        return torre_consolidado(
            result['num_blocos'],
            result['num_pavimentos'],
            result['num_unidades']
        )
