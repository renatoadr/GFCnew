# controller or business logic
# Tratamento de gáficos

from flask import current_app
from controller.empreendimentoController import empreendimentoController
from controller.consideracaoController import consideracaoController
from controller.unidadeController import unidadeController
from controller.medicaoController import medicaoController
from controller.bancoController import bancoController
from reportlab.lib.colors import white, red, blue, green, black, orange
from reportlab.pdfgen.canvas import Canvas

import os


class graficoInterController:
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
        medCtrl = medicaoController()
        empS = empC.consultarEmpreendimentoPeloId(idEmpreend)
        med = medCtrl.consultarMedicaoAtual(idEmpreend)

        construtora = 'Construtora: ' + empS.getNmConstrutor()
        empreendimento = 'Empreendimento: ' + empS.getNmEmpreend()
        empreendimento += ' - ' + 'End da Obra: ' + empS.getEnderecoCompleto()
        agenteFinanc = bancoController.getNmBanco(empS.getCodBanco())
        vistoria = (med.getNrMedicao() if med else '1ª') + ' Medição'

        # ATENÇÃO AJUSTAR DADOS DA VISTORIA

        self.logo_cabecalho(c)  # Adiciona o logo no cabeçalho

        c.setFont('Helvetica-Bold', 12)
        c.drawString(190, 740, "RELATÓRIO MENSAL DE ATIVIDADES")
        c.setFillColor(blue)
        c.setFont('Helvetica', 10)
        c.setFillColor((0.831, 0.243, 0.007))
        c.drawString(260, 700, vistoria)

        c.drawImage(os.path.join(diretorio, "foto_atual.png"),
                    40, 470, width=220, height=150, mask='auto')
        c.drawImage(os.path.join(diretorio, "evolucao_3D.png"),
                    300, 470, width=220, height=150, mask='auto')
        c.drawImage(os.path.join(diretorio, "eletrica_3D.png"),
                    40, 230, width=220, height=150, mask='auto')
        c.drawImage(os.path.join(diretorio, "hidraulica_3D.png"),
                    350, 230, width=220, height=150, mask='auto')
        c.drawImage(os.path.join(diretorio, "tab_empreend_capa.png"),
                    30, 30, width=500, height=100, mask='auto')
        c.drawImage(self.getPathImgs("legenda_2.png"),
                    350, 140, width=200, height=30, mask='auto')

        c.setFillColor(black)
        c.drawString(40, 630, 'Foto Atual')
        c.drawString(310, 630, 'Evolução da Obra por Equivalência Física de Pavimentos')
        c.drawString(40, 400, 'Elétrica')
        c.drawString(310, 400, 'Hidráulica')
        c.setFont('Helvetica', 10)
        c.drawString(570, 10, str(pagina))

    def pdfPag2(self, c: Canvas, diretorio, pagina):
        #   Segunda Página
        self.logo_cabecalho(c)  # Adiciona o logo no cabeçalho

        self.barraTitulo(30, 760, c, "1.          Prazo")
        c.drawImage(os.path.join(diretorio, "tab_prazo_inter.png"),
                    30, 690, width=520, height=60, mask='auto')  # 30 690   520  60

        c.drawImage(os.path.join(diretorio, "tab_medicoes.png"),
                    30, 370, width=520, mask='auto')
        self.barraTitulo(
            30, 660, c, "2.          Comparativo: Previsto x Realizado Físico (%)")

        c.setFillColor(black)
        c.setFont('Helvetica', 10)
        c.drawString(570, 10, str(pagina))

        c.drawImage(os.path.join(diretorio, "graf_progresso_obra.png"),
                    30, 20, width=520, height=300, mask='auto')

    def pdfPag2a(self, c, diretorio, pagina):
        #   Segunda Página
        self.logo_cabecalho(c)  # Adiciona o logo no cabeçalho

        c.drawImage(os.path.join(diretorio, "tab_situacao_inter.png"),
                    20, 730, width=420, height=40, mask='auto')  # 15 730
        self.barraTitulo(30, 760, c, "3.          Situação da obra")

        c.drawImage(os.path.join(diretorio, "tab_projeto_inter.png"),
                    15, 580, width=420, height=120, mask='auto')  # 20 590
        self.barraTitulo(
            30, 680, c, "4.          Padrão construtivo de projeto")  # 690

        c.drawImage(os.path.join(diretorio, "tab_qualidade_inter.png"),
                    30, 210, width=420, height=300, mask='auto')  # 30 230
        self.barraTitulo(
            30, 490, c, "5.          Considerações de qualidade - aspecto visial")  # 30 510

        c.drawImage(os.path.join(diretorio, "tab_seguranca_inter.png"),
                    25, 100, width=420, height=60, mask='auto')  # 20 130  w420 h70
        self.barraTitulo(
            30, 150, c, "6.          Considerações de segurança - aspecto visual")  # 30 180

        c.setFillColor(black)
        c.setFont('Helvetica', 10)
        c.drawString(570, 10, str(pagina))

    def pdfPag3(self, c, diretorio, pagina):
        #   Terceira Página
        self.logo_cabecalho(c)  # Adiciona o logo no cabeçalho

#       c.setFont('Helvetica-Bold', 14)
#       c.setFillColor("black")

        c.drawImage(os.path.join(diretorio, "tab_acomp_financeiro.png"),
                    30, 680, width=280, height=80, mask='auto')
        self.barraTitulo(30, 760, c, "7.          Acompanhamento financeiro")

        self.barraTitulo(
            30, 640, c, "8.          Medição e liberação financeiro por item orçado")
        c.drawImage(os.path.join(diretorio, "graf_orcamento_liberacao_valor.png"),
                    30, 340, width=530, height=260, mask='auto')

        self.barraTitulo(
            30, 300, c, "9.          Demonstrativo de uso do orçamento")
        c.drawImage(os.path.join(diretorio, "tab_orcamento_liberacao.png"),
                    30, 30, width=530, height=260, mask='auto')

        c.setFillColor(black)
        c.setFont('Helvetica', 10)
        c.drawString(570, 10, str(pagina))

    def pdfPag4(self, c, diretorio, pagina):
        #   Quarta Página
        self.logo_cabecalho(c)  # Adiciona o logo no cabeçalho

#       c.setFont('Helvetica-Bold', 14)
#       c.setFillColor("black")
#        self.barraTitulo(30, 760, c, "10.         Controle de pagamento a fornecedores")

#       c.drawString(30, 780, "Controle de pagamento a fornecedores")
#       c.drawString(30, 250,"Obrigações formais")

        c.drawImage(os.path.join(diretorio, "tab_notas.png"),
                    20, 360, width=530, height=400, mask='auto')
        self.barraTitulo(
            30, 760, c, "10.         Controle de pagamento a fornecedores")

        c.drawImage(os.path.join(diretorio, "graf_indices_garantia_I.png"),
                    30, 30, width=510, height=300, mask='auto')

        c.setFillColor(black)
        c.setFont('Helvetica', 10)
        c.drawString(570, 10, str(pagina))

    def pdfPag5(self, c, diretorio, pagina):
        #   Quinta Página
        self.logo_cabecalho(c)  # Adiciona o logo no cabeçalho

        c.drawImage(os.path.join(diretorio, "graf_indices_garantia_II.png"),
                    30, 455, width=510, height=300, mask='auto')

#       c.setFont('Helvetica-Bold', 14)
#       c.setFillColor("black")
#       c.drawString(30, 450, "Recebíveis por unidades produzidas")
        self.barraTitulo(
            30, 450, c, "11.         Recebíveis por unidades produzidas")

        c.drawImage(os.path.join(diretorio, "graf_chaves_perc.png"),
                    30, 270, width=200, height=150, mask='auto')
        c.drawImage(os.path.join(diretorio, "graf_vendas_perc.png"),
                    220, 270, width=330, height=150, mask='auto')

#        c.setFont('Helvetica-Bold', 14)
#        c.setFillColor("black")
#        c.drawString(30, 215, "Financeiro a receber")
        self.barraTitulo(30, 215, c, "12.         Financeiro a receber")

        c.drawImage(os.path.join(diretorio, "graf_chaves_valor.png"),
                    30, 35, width=200, height=150, mask='auto')
        c.drawImage(os.path.join(diretorio, "graf_vendas_valor.png"),
                    220, 35, width=330, height=150, mask='auto')

        c.setFillColor(black)
        c.setFont('Helvetica', 10)
        c.drawString(570, 10, str(pagina))

    def pdfPag6(self, c, diretorio, pagina):
        #   Sexta Página
        self.logo_cabecalho(c)  # Adiciona o logo no cabeçalho

#        c.setFont('Helvetica-Bold', 14)
#        c.setFillColor("black")
#        c.drawString(30, 780, "Evolução de saldo em conta corrente")
        self.barraTitulo(
            30, 740, c, "13.         Evolução de saldo em conta corrente")

        c.drawImage(os.path.join(diretorio, "tab_conta_corrente.png"),
                    40, 650, width=400, height=60, mask='auto')

#        c.setFont('Helvetica-Bold', 14)
#        c.setFillColor("black")
#        c.drawString(200, 360, "Pontos de atenção")
        self.barraTitulo(30, 360, c, "14.         Pontos de atenção")

        c.setFillColor(black)
        c.drawString(30, 340, "Garantias")
        c.drawString(30, 120, "Certidões")

        c.drawImage(os.path.join(diretorio, "tab_garantias_geral.png"),
                    20, 235, width=400, height=100, mask='auto')  # w350 h100
        c.drawImage(os.path.join(diretorio, "tab_garantias_obra.png"),
                    20, 135, width=400, height=100, mask='auto')
        c.drawImage(os.path.join(diretorio, "tab_certidoes.png"),
                    40, 5, width=240, height=110, mask='auto')

        c.setFillColor(black)
        c.setFont('Helvetica', 10)
        c.drawString(570, 10, str(pagina))

    def pdfPag7(self, c, diretorio, pagina):
        #   Setima Página
        self.logo_cabecalho(c)  # Adiciona o logo no cabeçalho

#        c.setFont('Helvetica-Bold', 14)
#        c.setFillColor("black")
#        c.drawString(30, 780, "Imagens 3D projetadas retratando a realidade da obra")
        self.barraTitulo(
            30, 760, c, "15.         Imagens 3D projetadas retratando a realidade da obra")

        c.drawImage(os.path.join(diretorio, "foto_3D_1.png"),
                    30, 550, width=250, height=141, mask='auto')
        c.drawImage(os.path.join(diretorio, "foto_3D_2.png"),
                    310, 550, width=250, height=141,  mask='auto')
        c.drawImage(os.path.join(diretorio, "foto_3D_3.png"),
                    30, 280, width=250, height=141, mask='auto')
        c.drawImage(os.path.join(diretorio, "foto_3D_4.png"),
                    310, 280, width=250, height=141, mask='auto')
        c.drawImage(self.getPathImgs("legenda_2.png"), 420,
                    100, width=150, height=50, mask='auto')

        c.setFillColor(black)
        c.setFont('Helvetica', 10)
        c.drawString(570, 10, str(pagina))

    def pdfPag8(self, c, diretorio, pagina):
        #   Oitava Página
        self.logo_cabecalho(c)  # Adiciona o logo no cabeçalho

#        c.setFont('Helvetica-Bold', 14)
#        c.setFillColor("black")
#        c.drawString(30, 800, "Relatório fotográfico")
        self.barraTitulo(30, 760, c, "17.         Relatório fotográfico")

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

        c.setFillColor(black)
        c.setFont('Helvetica', 10)
        c.drawString(570, 10, str(pagina))

    def pdfPag9(self, c, diretorio, pagina):
        #   Nona Página
        self.logo_cabecalho(c)  # Adiciona o logo no cabeçalho

#        c.setFont('Helvetica-Bold', 14)
#        c.setFillColor("black")
#        c.drawString(30, 800, "Relatório fotográfico")
        self.barraTitulo(30, 760, c, "17.         Relatório fotográfico")

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

        c.setFillColor(black)
        c.setFont('Helvetica', 10)
        c.drawString(570, 10, str(pagina))

    def pdfPag10(self, c, diretorio, pagina):
        #   Décima Página
        self.logo_cabecalho(c)  # Adiciona o logo no cabeçalho

#        c.setFont('Helvetica-Bold', 14)
#        c.setFillColor("black")
#        c.drawString(30, 800, "Relatório fotográfico")
        self.barraTitulo(30, 760, c, "17.         Relatório fotográfico")

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

        c.setFillColor(black)
        c.setFont('Helvetica', 10)
        c.drawString(570, 10, str(pagina))

    def pdfPag11(self, c, diretorio, pagina):
        #   Décima Primeira Página
        self.logo_cabecalho(c)  # Adiciona o logo no cabeçalho

#        c.setFont('Helvetica-Bold', 14)
#        c.setFillColor("black")
#        c.drawString(30, 800, "Relatório fotográfico")
        self.barraTitulo(30, 760, c, "17.         Relatório fotográfico")

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

        c.setFillColor(black)
        c.setFont('Helvetica', 10)
        c.drawString(570, 10, str(pagina))

    def pdfPag12(self, c, diretorio, pagina, idEmpreend, mes, ano):
        #   Décima Segunda Página
        self.logo_cabecalho(c)  # Adiciona o logo no cabeçalho

        consC = consideracaoController()
        consS = consC.listar_campos(idEmpreend, mes, ano)

#        c.setFont('Helvetica', 14)
#        c.setFillColor("black")
        lin = 760
#        c.drawString(30, lin, "Considerações Finais")
        self.barraTitulo(30, lin, c, "18.         Considerações finais")

        c.setFont('Helvetica', 14)
        c.setFillColor("black")

#        c.setFont('Helvetica-Bold', 12)
        lin -= 30
        c.drawString(30, lin, "Qualidade - segurança e aspecto visual:")
#        self.barraTitulo(30, lin, c, "19.         qualidade - segurança e aspécto visual:")

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

        c.setFont('Helvetica', 14)
        c.setFillColor("black")

#        c.setFont('Helvetica-Bold', 12)
        lin -= 20
        c.drawString(30, lin, "Serviços realizados e andamento:")
#        self.barraTitulo(30, lin, c, "20.         Serviços realizados e em andamento")

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

        c.setFont('Helvetica', 14)
        c.setFillColor("black")

#        c.setFont('Helvetica-Bold', 12)
        lin -= 20
        c.drawString(30, lin, "Efetivo e estoque:")
#        self.barraTitulo(30, lin, c, "21.         Efetivo e estoque")

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

        c.setFont('Helvetica', 14)
        c.setFillColor("black")

#        c.setFont('Helvetica-Bold', 12)
        lin -= 20
        c.drawString(30, lin, "Empreiteiros diversos:")
#        self.barraTitulo(30, lin, c, "22.         Empreiteiros diversos:")

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

        c.setFont('Helvetica', 14)
        c.setFillColor("black")

#        c.setFont('Helvetica-Bold', 12)
        lin -= 20
        c.drawString(30, lin, "Estoque:")
#        self.barraTitulo(30, lin, c, "23.         Estoque:")

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

        c.setFont('Helvetica', 14)
        c.setFillColor("black")

#        c.setFont('Helvetica-Bold', 12)
        lin -= 20
        c.drawString(30, lin, "Para conclusão de obra:")
#        self.barraTitulo(30, lin, c, "24.         Para conclusão da obra")

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

        c.setFont('Helvetica', 14)
        c.setFillColor("black")

#        c.setFont('Helvetica-Bold', 12)
        lin -= 20
        c.drawString(30, lin, "Considerações Finais:")
#        self.barraTitulo(30, lin, c, "25.         Considerações finais:")

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

        c.setFont('Helvetica', 14)
        c.setFillColor("black")

        c.setFont('Helvetica-Bold', 12)
        lin -= 30
        c.drawString(30, lin, "Engenheiro responsável pela vistoria:")
        lin -= 20
        c.drawString(40, lin, consS.getResponsavel())
        lin -= 15
        c.drawString(40, lin, consS.getCREA())

        c.setFillColor(black)
        c.setFont('Helvetica', 10)
        c.drawString(570, 10, str(pagina))
        return

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

    def verificaArqRelatorio(self, idEmpreend, vigencia, diretorio):
        listaErro = self.verificaUnidadesVendidas(idEmpreend, vigencia)

        imgs = [
            ('foto_atual', 'FOTO ATUAL', 1),
            ('evolucao_3D', 'EVOLUÇÃO 3D', 1),
            ('eletrica_3D', 'ELÉTRICA 3D', 1),
            ('hidraulica_3D', 'HIDRÁULICA 3D', 1),

            ('tab_prazo_inter', 'TABELA DE PRAZOS', 2),
            ('tab_medicoes', 'TABELA DE MEDIÇÕES', 2),
            ('graf_progresso_obra', 'GRÁFICO DO PROGRESSO DA OBRA', 2),

            ('tab_situacao_inter', 'TABELA DE SITUAÇÕES', '2a'),
            ('tab_projeto_inter', 'TABELA DE PROJETO', '2a'),
            ('tab_qualidade_inter', 'TABELA DE QUALIDADE', '2a'),
            ('tab_seguranca_inter', 'TABELA DE SEGURANÇA', '2a'),

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

        foto = self.getPathImgs("franca.jpg")
        if not os.path.isfile(foto):
            listaErro.append(
                'A imagem franca.jpg na 1ª página não foi encontrada')

        foto = self.getPathImgs("legenda_2.png")
        if not os.path.isfile(foto):
            listaErro.append(
                'A imagem LEGENDA_2 na 1ª página não foi encontrada')

        for img in imgs:
            foto = os.path.join(diretorio, f"{img[0]}.png")
            if not os.path.isfile(foto):
                listaErro.append(
                    f'A imagem {img[1]} da {img[2]}ª página não foi encontrada')

        return listaErro

    def logo_cabecalho(self, c):
        logoBanco = self.getPathImgs("inter.png")
        c.drawImage(logoBanco, 450, 795, width=110, height=30,
                    mask='auto')  # preserveAspectRatio=True,
        logoWs = self.getPathImgs("logo_ws.png")
        c.drawImage(logoWs, 20, 790, width=90, height=40,
                    mask='auto')  # preserveAspectRatio=True,

        return

    def barraTitulo(self, x, y, c, texto):

        fonte = 'Helvetica-Bold'
        tamanho = 12

        # Define a fonte para calcular a largura do texto
        c.setFont(fonte, tamanho)
        largura_texto = 600  # Definindo uma largura fixa para o exemplo
        altura_texto = 14  # Pequena margem extra

        c.setFillColorRGB(0.831, 0.243, 0.007)  # define a cor de fundo laranja
        c.rect(x, y, largura_texto, altura_texto, fill=1, stroke=0)

        c.setFillColor(white)  # Define a cor do texto como branco
        c.drawString(x, y+2.0, texto)

        return
