# controller or business logic
# Tratamento de gáficos

from flask import current_app
from controller.empreendimentoController import empreendimentoController
from controller.consideracaoController import consideracaoController
from controller.unidadeController import unidadeController
from controller.bancoController import bancoController
import os


class graficoController:
    app = None

    def __init__(self):
        self.app = current_app

    def getPathImgs(self, img):
        path = os.path.split(__file__)
        base = os.path.basename(path[0])
        path = path[0].replace(base, '')
        return os.path.join(path, 'static', 'imgs', img)

    def pdfPag1(self, c, diretorio, pagina, idEmpreend):
        #   Primeira Página
        empC = empreendimentoController()
        empS = empC.consultarEmpreendimentoPeloId(idEmpreend)

        construtora = 'Construtora: ' + empS.getNmConstrutor()
        empreendimento = 'Empreendimento: ' + empS.getNmEmpreend() + ' - ' + 'End da Obra: ' + \
            empS.getLogradouro() + ' - ' + empS.getBairro() + ' - ' + \
            empS.getCidade() + ' - ' + empS.getEstado()
        # + bancoController.getNmBanco(empS.getCodBanco())
        agenteFinanc = 'Agente financeiro: Banco do Brasil S.A.'
        vistoria = '4ª' + ' Vistoria - Período de Medição: ' + '20/03/2025 à 20/04/2025'
        # ATENÇÃO AJUSTAR DADOS DA VISTORIA

        logo = self.getPathImgs("franca.jpg")
        c.drawImage(logo, 450, 800, width=90, height=30,
                    mask='auto')  # preserveAspectRatio=True,
        c.setFont('Helvetica-Bold', 24)
        c.drawString(90, 760, "RELATÓRIO DE GESTÃO MENSAL")
        c.setFont('Helvetica', 10)
        c.drawString(40, 700, construtora)
        c.drawString(40, 690, empreendimento)
        c.drawString(40, 670, agenteFinanc)
        c.drawString(40, 660, vistoria)
        c.drawString(40, 600, 'Perspectiva')
        c.drawString(300, 600, 'Evolução em 3D')
        c.drawString(40, 350, 'Foto Atual')

        c.drawImage(os.path.join(diretorio, "perspectiva.png"),
                    40, 420, width=220, height=150, mask='auto')
        c.drawImage(os.path.join(diretorio, "evolucao_3D_1.png"),
                    300, 380, width=300, height=200, mask='auto')
        c.drawImage(os.path.join(diretorio, "foto_atual.png"),
                    40, 180, width=220, height=150, mask='auto')
        c.drawImage(os.path.join(diretorio, "evolucao_3D_2.png"),
                    350, 150, width=200, height=200, mask='auto')
        c.drawImage(self.getPathImgs("legenda_2.png"), 420,
                    100, width=150, height=25, mask='auto')

        c.setFont('Helvetica', 10)
        c.drawString(40,  95, 'Riscos relacionados ao orçamento e prazo;')
        c.drawString(40,  80, 'Carteira de recebíveis;')
        c.drawString(40,  65, 'Garantias contratuais;')
        c.drawString(40,  50, 'Status da documentação da obra;')
        c.drawString(40,  35, 'Resumo comentado da evolução.')
        c.drawString(570, 10, str(pagina))

    def pdfPag2(self, c, diretorio, pagina):
        #   Segunda Página
        c.drawImage(self.getPathImgs("franca.jpg"), 450,
                    800, width=100, height=40, mask='auto')

        c.setFont('Helvetica-Bold', 14)
        c.setFillColor("black")
        c.drawString(30, 780, "Comparativo: Previsto x Realizado Físico (%)")

        c.drawImage(os.path.join(diretorio, "tab_medicoes.png"),
                    30, 450, width=520, height=300, mask='auto')
        c.drawImage(os.path.join(diretorio, "graf_progresso_obra.png"),
                    30, 100, width=520, height=300, mask='auto')

        c.setFont('Helvetica', 10)
        c.drawString(570, 10, str(pagina))

    def pdfPag3(self, c, diretorio, pagina):
        #   Terceira Página
        c.drawImage(self.getPathImgs("franca.jpg"), 450,
                    800, width=90, height=30, mask='auto')

        c.setFont('Helvetica-Bold', 14)
        c.setFillColor("black")
        c.drawString(30, 780, "Acompanhamento financeiro")
        c.drawString(30, 640, "Medição e liberação financeira por item orçado")
        c.drawString(30, 300, "Demonstrativo de uso do orçamento")

        c.drawImage(os.path.join(diretorio, "tab_acomp_financeiro.png"),
                    30, 685, width=280, height=80, mask='auto')
        c.drawImage(os.path.join(diretorio, "graf_orcamento_liberacao_valor.png"),
                    30, 340, width=530, height=260, mask='auto')
        c.drawImage(os.path.join(diretorio, "tab_orcamento_liberacao.png"),
                    30, 30, width=530, height=260, mask='auto')

        c.setFont('Helvetica', 10)
        c.drawString(570, 10, str(pagina))

    def pdfPag4(self, c, diretorio, pagina):
        #   Quarta Página
        c.drawImage(self.getPathImgs("franca.jpg"), 450,
                    800, width=90, height=30, mask='auto')

        c.setFont('Helvetica-Bold', 14)
        c.setFillColor("black")
        c.drawString(30, 780, "Controle de pagamento a fornecedores")
#       c.drawString(30, 250,"Obrigações formais")

        c.drawImage(os.path.join(diretorio, "tab_notas.png"),
                    20, 360, width=530, height=400, mask='auto')
        c.drawImage(os.path.join(diretorio, "graf_indices_garantia_I.png"),
                    30, 30, width=510, height=300, mask='auto')

        c.setFont('Helvetica', 10)
        c.drawString(570, 10, str(pagina))

    def pdfPag5(self, c, diretorio, pagina):
        #   Quinta Página
        c.drawImage(self.getPathImgs("franca.jpg"), 450,
                    800, width=90, height=30, mask='auto')
        c.drawImage(os.path.join(diretorio, "graf_indices_garantia_II.png"),
                    30, 500, width=510, height=300, mask='auto')

        c.setFont('Helvetica-Bold', 14)
        c.setFillColor("black")
        c.drawString(30, 450, "Recebíveis por unidades produzidas")

        c.drawImage(os.path.join(diretorio, "graf_chaves_perc.png"),
                    30, 270, width=200, height=150, mask='auto')
        c.drawImage(os.path.join(diretorio, "graf_vendas_perc.png"),
                    220, 270, width=330, height=150, mask='auto')

        c.setFont('Helvetica-Bold', 14)
        c.setFillColor("black")
        c.drawString(30, 215, "Financeiro a receber")

        c.drawImage(os.path.join(diretorio, "graf_chaves_valor.png"),
                    30, 35, width=200, height=150, mask='auto')
        c.drawImage(os.path.join(diretorio, "graf_vendas_valor.png"),
                    220, 35, width=330, height=150, mask='auto')

        c.setFont('Helvetica', 10)
        c.drawString(570, 10, str(pagina))

    def pdfPag6(self, c, diretorio, pagina):
        #   Sexta Página
        c.drawImage(self.getPathImgs("franca.jpg"), 450,
                    800, width=90, height=30, mask='auto')

        c.setFont('Helvetica-Bold', 14)
        c.setFillColor("black")
        c.drawString(30, 780, "Evolução de saldo em conta corrente")

        c.drawImage(os.path.join(diretorio, "tab_conta_corrente.png"),
                    40, 650, width=400, height=60, mask='auto')

        c.setFont('Helvetica-Bold', 14)
        c.setFillColor("black")
        c.drawString(200, 360, "Pontos de atenção")
        c.drawString(30, 340, "Garantias")
        c.drawString(30, 180, "Certidões")

        c.drawImage(os.path.join(diretorio, "tab_garantias_geral.png"),
                    20, 220, width=300, height=100, mask='auto')
        c.drawImage(os.path.join(diretorio, "tab_garantias_obra.png"),
                    290, 220, width=300, height=100, mask='auto')
        c.drawImage(os.path.join(diretorio, "tab_certidoes.png"),
                    20, 60, width=250, height=100, mask='auto')

        c.setFont('Helvetica', 10)
        c.drawString(570, 10, str(pagina))

    def pdfPag7(self, c, diretorio, pagina):
        #   Setima Página
        c.drawImage(self.getPathImgs("franca.jpg"), 450,
                    800, width=90, height=30, mask='auto')

        c.setFont('Helvetica-Bold', 14)
        c.setFillColor("black")
        c.drawString(
            30, 780, "Imagens 3D projetadas retratando a realidade da obra")

        c.drawImage(os.path.join(diretorio, "foto_3D_1.png"),
                    30, 550, width=250, height=200, mask='auto')
        c.drawImage(os.path.join(diretorio, "foto_3D_2.png"),
                    310, 550, width=250, height=200, mask='auto')
        c.drawImage(os.path.join(diretorio, "foto_3D_3.png"),
                    30, 280, width=250, height=200, mask='auto')
        c.drawImage(self.getPathImgs("legenda_2.png"), 420,
                    100, width=150, height=25, mask='auto')

        c.setFont('Helvetica', 10)
        c.drawString(570, 10, str(pagina))

    def pdfPag8(self, c, diretorio, pagina):
        #   Oitava Página
        c.drawImage(self.getPathImgs("franca.jpg"), 450,
                    800, width=90, height=30, mask='auto')

        c.setFont('Helvetica-Bold', 14)
        c.setFillColor("black")
        c.drawString(30, 800, "Relatório fotográfico")

        imgTemp = os.path.join(diretorio, "foto_1")
        if os.path.isfile(f"{imgTemp}.png"):
            c.drawImage(f"{imgTemp}.png", 30, 550,
                        width=250, height=200, mask='auto')

        imgTemp = os.path.join(diretorio, "foto_2")
        if os.path.isfile(f"{imgTemp}.png"):
            c.drawImage(f"{imgTemp}.png", 310, 550,
                        width=250, height=200, mask='auto')

        imgTemp = os.path.join(diretorio, "foto_3")
        if os.path.isfile(f"{imgTemp}.png"):
            c.drawImage(f"{imgTemp}.png", 30, 295,
                        width=250, height=200, mask='auto')

        imgTemp = os.path.join(diretorio, "foto_4")
        if os.path.isfile(f"{imgTemp}.png"):
            c.drawImage(f"{imgTemp}.png", 310, 295,
                        width=250, height=200, mask='auto')

        imgTemp = os.path.join(diretorio, "foto_5")
        if os.path.isfile(f"{imgTemp}.png"):
            c.drawImage(f"{imgTemp}.png", 30,  45,
                        width=250, height=200, mask='auto')

        imgTemp = os.path.join(diretorio, "foto_6")
        if os.path.isfile(f"{imgTemp}.png"):
            c.drawImage(f"{imgTemp}.png", 310,  45,
                        width=250, height=200, mask='auto')

        c.setFont('Helvetica', 10)
        c.drawString(570, 10, str(pagina))

    def pdfPag9(self, c, diretorio, pagina):
        #   Nona Página
        c.drawImage(self.getPathImgs("franca.jpg"), 450,
                    800, width=90, height=30, mask='auto')

        c.setFont('Helvetica-Bold', 14)
        c.setFillColor("black")
        c.drawString(30, 800, "Relatório fotográfico")

        imgTemp = os.path.join(diretorio, "foto_7.png")
        if os.path.isfile(imgTemp):
            c.drawImage(imgTemp, 30, 550, width=250, height=200, mask='auto')

        imgTemp = os.path.join(diretorio, "foto_8.png")
        if os.path.isfile(imgTemp):
            c.drawImage(imgTemp, 310, 550, width=250, height=200, mask='auto')

        imgTemp = os.path.join(diretorio, "foto_9.png")
        if os.path.isfile(imgTemp):
            c.drawImage(imgTemp, 30, 295, width=250, height=200, mask='auto')

        imgTemp = os.path.join(diretorio, "foto_10.png")
        if os.path.isfile(imgTemp):
            c.drawImage(imgTemp, 310, 295, width=250, height=200, mask='auto')

        imgTemp = os.path.join(diretorio, "foto_11.png")
        if os.path.isfile(imgTemp):
            c.drawImage(imgTemp, 30,  45, width=250, height=200, mask='auto')

        imgTemp = os.path.join(diretorio, "foto_12.png")
        if os.path.isfile(imgTemp):
            c.drawImage(imgTemp, 310,  45, width=250, height=200, mask='auto')

        c.setFont('Helvetica', 10)
        c.drawString(570, 10, str(pagina))

    def pdfPag10(self, c, diretorio, pagina):
        #   Décima Página
        c.drawImage(self.getPathImgs("franca.jpg"), 450,
                    800, width=90, height=30, mask='auto')

        c.setFont('Helvetica-Bold', 14)
        c.setFillColor("black")
        c.drawString(30, 800, "Relatório fotográfico")

        imgTemp = os.path.join(diretorio, "foto_13.png")
        if os.path.isfile(imgTemp):
            c.drawImage(imgTemp, 30, 550, width=250, height=200, mask='auto')

        imgTemp = os.path.join(diretorio, "foto_14.png")
        if os.path.isfile(imgTemp):
            c.drawImage(imgTemp, 310, 550, width=250, height=200, mask='auto')

        imgTemp = os.path.join(diretorio, "foto_15.png")
        if os.path.isfile(imgTemp):
            c.drawImage(imgTemp, 30, 295, width=250, height=200, mask='auto')

        imgTemp = os.path.join(diretorio, "foto_16.png")
        if os.path.isfile(imgTemp):
            c.drawImage(imgTemp, 310, 295, width=250, height=200, mask='auto')

        imgTemp = os.path.join(diretorio, "foto_17.png")
        if os.path.isfile(imgTemp):
            c.drawImage(imgTemp, 30,  45, width=250, height=200, mask='auto')

        imgTemp = os.path.join(diretorio, "foto_18.png")
        if os.path.isfile(imgTemp):
            c.drawImage(imgTemp, 310,  45, width=250, height=200, mask='auto')

        c.setFont('Helvetica', 10)
        c.drawString(570, 10, str(pagina))

    def pdfPag11(self, c, diretorio, pagina):
        #   Décima Primeira Página
        c.drawImage(self.getPathImgs("franca.jpg"), 450,
                    800, width=90, height=30, mask='auto')

        c.setFont('Helvetica-Bold', 14)
        c.setFillColor("black")
        c.drawString(30, 800, "Relatório fotográfico")

        imgTemp = os.path.join(diretorio, "foto_19.png")
        if os.path.isfile(imgTemp):
            c.drawImage(imgTemp, 30, 550, width=250, height=200, mask='auto')

        imgTemp = os.path.join(diretorio, "foto_20.png")
        if os.path.isfile(imgTemp):
            c.drawImage(imgTemp, 310, 550, width=250, height=200, mask='auto')

        imgTemp = os.path.join(diretorio, "foto_21.png")
        if os.path.isfile(imgTemp):
            c.drawImage(imgTemp, 30, 295, width=250, height=200, mask='auto')

        imgTemp = os.path.join(diretorio, "foto_22.png")
        if os.path.isfile(imgTemp):
            c.drawImage(imgTemp, 310, 295, width=250, height=200, mask='auto')

        imgTemp = os.path.join(diretorio, "foto_23.png")
        if os.path.isfile(imgTemp):
            c.drawImage(imgTemp, 30,  45, width=250, height=200, mask='auto')

        imgTemp = os.path.join(diretorio, "foto_24.png")
        if os.path.isfile(imgTemp):
            c.drawImage(imgTemp, 310,  45, width=250, height=200, mask='auto')

        c.setFont('Helvetica', 10)
        c.drawString(570, 10, str(pagina))

    def pdfPag12(self, c, diretorio, pagina, idEmpreend, mes, ano):
        #   Décima Segunda Página

        c.drawImage(self.getPathImgs("franca.jpg"), 450,
                    800, width=90, height=30, mask='auto')

        consC = consideracaoController()
        consS = consC.listar_campos(idEmpreend, mes, ano)

        c.setFont('Helvetica-Bold', 14)
        c.setFillColor("black")
        lin = 780
        c.drawString(30, lin, "Considerações Finais")

        c.setFont('Helvetica-Bold', 12)
        lin -= 30
        c.drawString(35, lin, "Qualidade - segurança e aspecto visual:")
        c.setFont('Helvetica', 10)
        if consS.getQualidade1() != "":
            lin -= 15
            c.drawString(40, lin, "\u2022 " + consS.getQualidade1())
        if consS.getQualidade2() != "":
            lin -= 15
            c.drawString(40, lin, "\u2022 " + consS.getQualidade2())
        if consS.getQualidade3() != "":
            lin -= 15
            c.drawString(40, lin, "\u2022 " + consS.getQualidade3())
        if consS.getQualidade4() != "":
            lin -= 15
            c.drawString(40, lin, "\u2022 " + consS.getQualidade4())

        c.setFont('Helvetica-Bold', 12)
        lin -= 20
        c.drawString(35, lin, "Serviços realizados e andamento:")
        c.setFont('Helvetica', 10)
        if consS.getServico1() != "":
            lin -= 15
            c.drawString(40, lin, "\u2022 " + consS.getServico1())
        if consS.getServico2() != "":
            lin -= 15
            c.drawString(40, lin, "\u2022 " + consS.getServico2())
        if consS.getServico3() != "":
            lin -= 15
            c.drawString(40, lin, "\u2022 " + consS.getServico3())
        if consS.getServico4() != "":
            lin -= 15
            c.drawString(40, lin, "\u2022 " + consS.getServico4())

        c.setFont('Helvetica-Bold', 12)
        lin -= 20
        c.drawString(30, lin, "Efetivo e estoque:")
        c.setFont('Helvetica', 10)
        if consS.getEfetivoEstoque1() != "":
            lin -= 15
            c.drawString(40, lin, "\u2022 " + consS.getEfetivoEstoque1())
        if consS.getEfetivoEstoque2() != "":
            lin -= 15
            c.drawString(40, lin, "\u2022 " + consS.getEfetivoEstoque2())
        if consS.getEfetivoEstoque3() != "":
            lin -= 15
            c.drawString(40, lin, "\u2022 " + consS.getEfetivoEstoque3())
        if consS.getEfetivoEstoque4() != "":
            lin -= 15
            c.drawString(40, lin, "\u2022 " + consS.getEfetivoEstoque4())

        c.setFont('Helvetica-Bold', 12)
        lin -= 20
        c.drawString(30, lin, "Empreiteiros diversos:")
        c.setFont('Helvetica', 10)
        if consS.getEmpreiteiro1() != "":
            lin -= 15
            c.drawString(40, lin, "\u2022 " + consS.getEmpreiteiro1())
        if consS.getEmpreiteiro2() != "":
            lin -= 15
            c.drawString(40, lin, "\u2022 " + consS.getEmpreiteiro2())
        if consS.getEmpreiteiro3() != "":
            lin -= 15
            c.drawString(40, lin, "\u2022 " + consS.getEmpreiteiro3())
        if consS.getEmpreiteiro4() != "":
            lin -= 15
            c.drawString(40, lin, "\u2022 " + consS.getEmpreiteiro4())

        c.setFont('Helvetica-Bold', 12)
        lin -= 20
        c.drawString(30, lin, "Estoque:")
        c.setFont('Helvetica', 10)
        if consS.getEstoque1() != "":
            lin -= 15
            c.drawString(40, lin, "\u2022 " + consS.getEstoque1())
        if consS.getEstoque2() != "":
            lin -= 15
            c.drawString(40, lin, "\u2022 " + consS.getEstoque2())
        if consS.getEstoque3() != "":
            lin -= 15
            c.drawString(40, lin, "\u2022 " + consS.getEstoque3())
        if consS.getEstoque4() != "":
            lin -= 15
            c.drawString(40, lin, "\u2022 " + consS.getEstoque4())

        c.setFont('Helvetica-Bold', 12)
        lin -= 20
        c.drawString(30, lin, "Para conclusão de obra:")
        c.setFont('Helvetica', 10)
        if consS.getConclusao1() != "":
            lin -= 15
            c.drawString(40, lin, "\u2022 " + consS.getConclusao1())
        if consS.getConclusao2() != "":
            lin -= 15
            c.drawString(40, lin, "\u2022 " + consS.getConclusao2())
        if consS.getConclusao3() != "":
            lin -= 15
            c.drawString(40, lin, "\u2022 " + consS.getConclusao3())
        if consS.getConclusao4() != "":
            lin -= 15
            c.drawString(40, lin, "\u2022 " + consS.getConclusao4())

        c.setFont('Helvetica-Bold', 12)
        lin -= 20
        c.drawString(30, lin, "Considerações Finais:")
        c.setFont('Helvetica', 10)
        if consS.getConsideracao1() != "":
            lin -= 15
            c.drawString(40, lin, "\u2022 " + consS.getConsideracao1())
        if consS.getConsideracao2() != "":
            lin -= 15
            c.drawString(40, lin, "\u2022 " + consS.getConsideracao2())
        if consS.getConsideracao3() != "":
            lin -= 15
            c.drawString(40, lin, "\u2022 " + consS.getConsideracao3())
        if consS.getConsideracao4() != "":
            lin -= 15
            c.drawString(40, lin, "\u2022 " + consS.getConsideracao4())

        c.setFont('Helvetica-Bold', 12)
        lin -= 30
        c.drawString(30, lin, "Engenheiro responsável pela vistoria:")
        lin -= 20
        c.drawString(40, lin, consS.getResponsavel())
        lin -= 15
        c.drawString(40, lin, consS.getCREA())

        c.setFont('Helvetica', 10)
        c.drawString(570, 10, str(pagina))

    def montaDir(self, idEmpreend, mes, ano, relatorio=False):
        if relatorio:
            diretorio = os.path.join(
                self.app.config['DIRSYS'], "Relatorios")
        else:
            diretorio = os.path.join(
                self.app.config['DIRSYS'], idEmpreend, f"{ano}_{mes}")
        return diretorio

    def criaDir(self, diretorio):
        # Criar diretórios
        if not os.path.exists(diretorio):
            os.makedirs(diretorio)
            print(f"Diretorio '{diretorio}' criado com sucesso.")

        else:
            print(f"Diretorio '{diretorio}' já existe.")

        return

    def verificaDir(self, diretorio):
        if not os.path.exists(diretorio):
            print(f"Diretorio '{diretorio}' não existe.")
            return False
        else:
            print(f"Diretorio '{diretorio}' já existe.")
            return True

    def verificaUnidadesVendidas(self, idEmpreend, vigencia) -> list[str]:
        listError = []
        vig = vigencia.split('-')
        ctrlUnidade = unidadeController()
        unidades = ctrlUnidade.unidadesVendidasSemCliente(
            idEmpreend, vig[1], vig[0])
        for uni in unidades:
            listError.append(
                f"A unidade: {uni.getUnidade()} da torre: {uni.getNmTorre()} está com status: {uni.getStatus()}, porém, não tem cliente associado.")
        return listError

    def verificaArqRelatorio(self, diretorio, idEmpreend, vigencia):
        listaErro = self.verificaUnidadesVendidas(idEmpreend, vigencia)
        #   Primeira Página

        foto = self.getPathImgs("franca.jpg")
        if not os.path.isfile(foto):
            listaErro.append(
                'A imagem franca.jpg na 1ª página não foi encontrada')

        foto = self.getPathImgs("legenda_2.png")
        if not os.path.isfile(foto):
            listaErro.append(
                'A imagem LEGENDA_2 na 1ª página não foi encontrada')

        imgs = [
            ('perspectiva', 'PERSPECTIVA', 1),
            ('foto_atual', 'FOTO ATUAL', 1),
            ('evolucao_3D_1', 'EVOLUÇÃO 3D 1', 1),
            ('evolucao_3D_2', 'EVOLUÇÃO 3D 2', 1),

            ('tab_medicoes', 'TABELA DE MEDIÇÕES', 2),
            ('graf_progresso_obra', 'GRÁFICO DO PROGRESSO DA OBRA', 2),

            ('tab_acomp_financeiro', 'TABELA DE ACOMPANHAMENTO FINANCEIRO', 3),
            ('graf_orcamento_liberacao_valor',
             'GRÁFICO DO ORÇAMENTO DE LIBERAÇÃO', 3),
            ('tab_orcamento_liberacao', 'TABELA DE ORÇAMENTO LIBERAÇÃO', 3),

            ('tab_notas', 'TABELA DE NOTAS', 4),
            ('graf_indices_garantia_I', 'GRÁFICO DE ÍNDICES DE GARANTIAS I', 4),

            ('graf_indices_garantia_II', 'GRÁFICO DE ÍNDICES DE GARANTIAS II', 5),
            ('graf_chaves_perc', 'GRÁFICO DE CHAVES PERCENTUAIS', 5),
            ('graf_chaves_valor', 'GRÁFICO DE CHAVES VALOR', 5),
            ('graf_vendas_perc', 'GRÁFICO DE VENDAS PERCENTUAIS', 5),
            ('graf_vendas_valor', 'GRÁFICO DE VENDAS VALOR', 5),

            ('tab_conta_corrente', 'TABELA DE CONTAS CORRENTES', 6),
            ('tab_garantias_geral', 'TABELA DE GARANTIAS GERAIS', 6),
            ('tab_garantias_obra', 'TABELA DE GARANTIAS DA OBRA', 6),
            ('tab_certidoes', 'TABELA DE CERTIDÕES', 6),

            ('foto_3D_1', 'FOTO 3D 1', 7),
            ('foto_3D_2', 'FOTO 3D 2', 7),
            ('foto_3D_3', 'FOTO 3D 3', 7),

            ('foto_1', 'FOTO DA OBRA 1', 8),
            ('foto_2', 'FOTO DA OBRA 2', 8),

        ]

        for img in imgs:
            foto = os.path.join(diretorio, f"{img[0]}.png")
            if not os.path.isfile(foto):
                listaErro.append(
                    f'A imagem {img[1]} da {img[2]}ª página não foi encontrada')

        return listaErro
