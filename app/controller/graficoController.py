# controller or business logic
# Tratamento de gáficos

from flask import Flask, request, render_template, redirect, url_for, flash, send_file, session, current_app
from controller.consideracaoController import consideracaoController
from dto.orcamento import orcamento
from utils.dbContext import MySql
from werkzeug.utils import secure_filename

import pandas as pd
import os
import numpy as np
import easygui


class graficoController:
    __connection = None
    app = None

    def __init__(self):
        self.app = current_app
        pass

    def pdfPag1(self, c, diretorio, pagina):
        #   Primeira Página
        construtora = 'Construtora: ' + 'Nacional'
        empreendimento = 'Empreendimento: ' + 'Flat Norte' + ' - ' + 'End da Obra: ' + \
            'Rua Paulo Lobo s/n' + ' - ' + 'Centro' + ' - ' + 'Limeira' + ' - ' + 'SP'
        agenteFinanc = 'Agente financeiro: ' + 'Banco Público'
        vistoria = '2ª' + ' Vistoria - Período de Medição: ' + '20/11/2024 à 20/12/2024'

        logo = "C:\\Desafios JavaScript\\gfc\\app\\static\\imgs\\franca.jpg"
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

        foto = diretorio + "perspectiva.png"
        c.drawImage(foto,  40, 420, width=220, height=150, mask='auto')
        foto = diretorio + "evolucao_3D_1.png"
        c.drawImage(foto, 300, 380, width=300, height=200, mask='auto')
        foto = diretorio + "foto_atual.jpeg"
        c.drawImage(foto,  40, 180, width=220, height=150, mask='auto')
        foto = diretorio + "evolucao_3D_2.png"
        c.drawImage(foto, 350, 150, width=200, height=200, mask='auto')
        logo = "C:\\Desafios JavaScript\\gfc\\app\\static\\imgs\\legenda 2.png"
        c.drawImage(logo, 420, 100, width=150, height=25,
                    mask='auto')  # preserveAspectRatio=True,

        c.setFont('Helvetica', 10)
        c.drawString(40,  95, 'Riscos relacionados ao orçamento e prazo;')
        c.drawString(40,  80, 'Carteira de recebíveis;')
        c.drawString(40,  65, 'Garantias contratuais;')
        c.drawString(40,  50, 'Status da documentação da obra;')
        c.drawString(40,  35, 'Resumo comentado da evolução.')
        c.drawString(570, 10, str(pagina))

    def pdfPag2(self, c, diretorio, pagina):
        #   Segunda Página

        logo = "C:\\Desafios JavaScript\\gfc\\app\\static\\imgs\\franca.jpg"
        c.drawImage(logo, 450, 800, width=100, height=40,
                    mask='auto')  # preserveAspectRatio=True,

        c.setFont('Helvetica-Bold', 14)
        c.setFillColor("black")
        c.drawString(30, 780, "Comparativo: Previsto x Realizado Físico (%)")
        imgFotoObra = diretorio + "tab_medicoes.png"
        c.drawImage(imgFotoObra, 30, 450, width=520, height=300,
                    mask='auto')   # preserveAspectRatio=True
        imgFotoObra = diretorio + "graf_progresso_obra.png"
        c.drawImage(imgFotoObra, 30, 100, width=520, height=300,
                    mask='auto')   # preserveAspectRatio=True

        c.setFont('Helvetica', 10)
        c.drawString(570, 10, str(pagina))

    def pdfPag3(self, c, diretorio, pagina):
        #   Terceira Página

        logo = "C:\\Desafios JavaScript\\gfc\\app\\static\\imgs\\franca.jpg"
        c.drawImage(logo, 450, 800, width=90, height=30,
                    mask='auto')  # preserveAspectRatio=True,

        c.setFont('Helvetica-Bold', 14)
        c.setFillColor("black")
        c.drawString(30, 780, "Acompanhamento financeiro")
        c.drawString(30, 640, "Medição e liberação financeira por item orçado")
        c.drawString(30, 300, "Demonstrativo de uso do orçamento")

        imgFotoObra = diretorio + "tab_acomp_financeiro.png"
        c.drawImage(imgFotoObra, 30, 685, width=280, height=80,
                    mask='auto')   # preserveAspectRatio=True
        imgFotoObra = diretorio + "graf_orcamento_liberacao_valor.png"
        c.drawImage(imgFotoObra, 30, 340, width=530, height=260,
                    mask='auto')   # preserveAspectRatio=True
        imgFotoObra = diretorio + "tab_orcamento_liberacao.png"
        c.drawImage(imgFotoObra, 30, 30, width=530, height=260,
                    mask='auto')   # preserveAspectRatio=True

        c.setFont('Helvetica', 10)
        c.drawString(570, 10, str(pagina))

    def pdfPag4(self, c, diretorio, pagina):
        #   Quarta Página

        logo = "C:\\Desafios JavaScript\\gfc\\app\\static\\imgs\\franca.jpg"
        c.drawImage(logo, 450, 800, width=90, height=30,
                    mask='auto')  # preserveAspectRatio=True,

        c.setFont('Helvetica-Bold', 14)
        c.setFillColor("black")
        c.drawString(30, 780, "Controle de pagamento a fornecedores")
#        c.drawString(30, 250,"Obrigações formais")
        imgFotoObra = diretorio + "tab_notas.png"
        c.drawImage(imgFotoObra, 20, 360, width=530, height=400,
                    mask='auto')   # preserveAspectRatio=True
        imgFotoObra = diretorio + "graf_indices_garantia_I.png"
        c.drawImage(imgFotoObra, 30, 30, width=510, height=300,
                    mask='auto')   # preserveAspectRatio=True

        c.setFont('Helvetica', 10)
        c.drawString(570, 10, str(pagina))

    def pdfPag5(self, c, diretorio, pagina):
        #   Quinta Página

        logo = "C:\\Desafios JavaScript\\gfc\\app\\static\\imgs\\franca.jpg"
        c.drawImage(logo, 450, 800, width=90, height=30,
                    mask='auto')  # preserveAspectRatio=True,

        imgFotoObra = diretorio + "graf_indices_garantia_II.png"
        c.drawImage(imgFotoObra, 30, 500, width=510, height=300,
                    mask='auto')   # preserveAspectRatio=True
        c.setFont('Helvetica-Bold', 14)
        c.setFillColor("black")
        c.drawString(30, 450, "Recebíveis por unidades produzidas")

        imgFotoObra = diretorio + "graf_chaves_perc.png"
        c.drawImage(imgFotoObra, 30, 270, width=200, height=150,
                    mask='auto')   # preserveAspectRatio=True
        imgFotoObra = diretorio + "graf_vendas_perc.png"
        c.drawImage(imgFotoObra, 220, 270, width=330, height=150,
                    mask='auto')   # preserveAspectRatio=True
        
        c.setFont('Helvetica-Bold', 14)
        c.setFillColor("black")
        c.drawString(30, 215, "Financeiro a receber")
        
        imgFotoObra = diretorio + "graf_chaves_valor.png"
        c.drawImage(imgFotoObra, 30, 35, width=200, height=150,
                    mask='auto')   # preserveAspectRatio=True
        imgFotoObra = diretorio + "graf_vendas_valor.png"
        c.drawImage(imgFotoObra, 220, 35, width=330, height=150,
                    mask='auto')   # preserveAspectRatio=True

        c.setFont('Helvetica', 10)
        c.drawString(570, 10, str(pagina))

    def pdfPag6(self, c, diretorio, pagina):
        #   Sexta Página

        logo = "C:\\Desafios JavaScript\\gfc\\app\\static\\imgs\\franca.jpg"
        c.drawImage(logo, 450, 800, width=90, height=30,
                    mask='auto')  # preserveAspectRatio=True,

        c.setFont('Helvetica-Bold', 14)
        c.setFillColor("black")
        c.drawString(30, 780, "Evolução de saldo em conta corrente")
        imgFotoObra = diretorio + "tab_conta_corrente.png"
        c.drawImage(imgFotoObra, 40, 650, width=400, height=60,
                    mask='auto')   # preserveAspectRatio=True
        c.setFont('Helvetica-Bold', 14)
        c.setFillColor("black")
        c.drawString(200, 360, "Pontos de atenção")
        c.drawString(30, 340, "Garantias")
        c.drawString(30, 180, "Certidões")

        imgFotoObra = diretorio + "tab_garantias_geral.png"
        c.drawImage(imgFotoObra, 20, 220, width=300, height=100,
                    mask='auto')   # preserveAspectRatio=True
        imgFotoObra = diretorio + "tab_garantias_obra.png"
        c.drawImage(imgFotoObra, 290, 220, width=300, height=100,
                    mask='auto')   # preserveAspectRatio=True
        imgFotoObra = diretorio + "tab_certidoes.png"
        c.drawImage(imgFotoObra, 20, 60, width=250, height=100,
                    mask='auto')   # preserveAspectRatio=True

        c.setFont('Helvetica', 10)
        c.drawString(570, 10, str(pagina))

    def pdfPag7(self, c, diretorio, pagina):
        #   Setima Página

        logo = "C:\\Desafios JavaScript\\gfc\\app\\static\\imgs\\franca.jpg"
        c.drawImage(logo, 450, 800, width=90, height=30,
                    mask='auto')  # preserveAspectRatio=True,

        c.setFont('Helvetica-Bold', 14)
        c.setFillColor("black")
        c.drawString(
            30, 780, "Imagens 3D projetadas retratando a realidade da obra")
        imgFotoObra = diretorio + "foto_3D_1.png"
        c.drawImage(imgFotoObra, 30, 550, width=250, height=200,
                    mask='auto')   # preserveAspectRatio=True
        imgFotoObra = diretorio + "foto_3D_2.png"
        c.drawImage(imgFotoObra, 310, 550, width=250, height=200,
                    mask='auto')   # preserveAspectRatio=True
        imgFotoObra = diretorio + "foto_3D_3.png"
        c.drawImage(imgFotoObra, 30, 280, width=250, height=200,
                    mask='auto')   # preserveAspectRatio=True
        logo = "C:\\Desafios JavaScript\\gfc\\app\\static\\imgs\\legenda 2.png"
        c.drawImage(logo, 420, 100, width=150, height=25,
                    mask='auto')  # preserveAspectRatio=True,

        c.setFont('Helvetica', 10)
        c.drawString(570, 10, str(pagina))

    def pdfPag8(self, c, diretorio, pagina):
        #   Oitava Página

        logo = "C:\\Desafios JavaScript\\gfc\\app\\static\\imgs\\franca.jpg"
        c.drawImage(logo, 450, 800, width=90, height=30,
                    mask='auto')  # preserveAspectRatio=True,

        c.setFont('Helvetica-Bold', 14)
        c.setFillColor("black")
        c.drawString(30, 800, "Relatório fotográfico")
        if os.path.isfile(diretorio+"foto_1.png"):
           imgFotoObra = diretorio + "foto_1.png"
           c.drawImage(imgFotoObra, 30, 550, width=250, height=200, mask='auto')   # preserveAspectRatio=True
        if os.path.isfile(diretorio+"foto_2.png"):
            imgFotoObra = diretorio + "foto_2.png"
            c.drawImage(imgFotoObra, 310, 550, width=250, height=200, mask='auto')   # preserveAspectRatio=True
        if os.path.isfile(diretorio+"foto_3.png"):
            imgFotoObra = diretorio + "foto_3.png"
            c.drawImage(imgFotoObra, 30, 295, width=250, height=200,
                        mask='auto')   # preserveAspectRatio=True
        if os.path.isfile(diretorio+"foto_4.png"):
            imgFotoObra = diretorio + "foto_4.png"
            c.drawImage(imgFotoObra, 310, 295, width=250, height=200,
                        mask='auto')   # preserveAspectRatio=True
        if os.path.isfile(diretorio+"foto_5.png"):
            imgFotoObra = diretorio + "foto_5.png"
            c.drawImage(imgFotoObra, 30,  45, width=250, height=200,
                        mask='auto')   # preserveAspectRatio=True
        if os.path.isfile(diretorio+"foto_6.png"):
            imgFotoObra = diretorio + "foto_6.png"
            c.drawImage(imgFotoObra, 310,  45, width=250, height=200,
                        mask='auto')   # preserveAspectRatio=True

        c.setFont('Helvetica', 10)
        c.drawString(570, 10, str(pagina))

    def pdfPag9(self, c, diretorio, pagina):
        #   Nona Página

        logo = "C:\\Desafios JavaScript\\gfc\\app\\static\\imgs\\franca.jpg"
        c.drawImage(logo, 450, 800, width=90, height=30,
                    mask='auto')  # preserveAspectRatio=True,

        c.setFont('Helvetica-Bold', 14)
        c.setFillColor("black")
        c.drawString(30, 800, "Relatório fotográfico")
        imgFotoObra = diretorio + "foto_7.png"
        c.drawImage(imgFotoObra, 30, 550, width=250, height=200,
                    mask='auto')   # preserveAspectRatio=True
        if os.path.isfile(diretorio+"foto_8.png"):
            imgFotoObra = diretorio + "foto_8.png"
            c.drawImage(imgFotoObra, 310, 550, width=250, height=200,
                        mask='auto')   # preserveAspectRatio=True
        if os.path.isfile(diretorio+"foto_9.png"):
            imgFotoObra = diretorio + "foto_9.png"
            c.drawImage(imgFotoObra, 30, 295, width=250, height=200,
                        mask='auto')   # preserveAspectRatio=True
        if os.path.isfile(diretorio+"foto_10.png"):
            imgFotoObra = diretorio + "foto_10.png"
            c.drawImage(imgFotoObra, 310, 295, width=250, height=200,
                        mask='auto')   # preserveAspectRatio=True
        if os.path.isfile(diretorio+"foto_11.png"):
            imgFotoObra = diretorio + "foto_11.png"
            c.drawImage(imgFotoObra, 30,  45, width=250, height=200,
                        mask='auto')   # preserveAspectRatio=True
        if os.path.isfile(diretorio+"foto_12.png"):
            imgFotoObra = diretorio + "foto_12.png"
            c.drawImage(imgFotoObra, 310,  45, width=250, height=200,
                        mask='auto')   # preserveAspectRatio=True

        c.setFont('Helvetica', 10)
        c.drawString(570, 10, str(pagina))

    def pdfPag10(self, c, diretorio, pagina):
        #   Décima Página

        logo = "C:\\Desafios JavaScript\\gfc\\app\\static\\imgs\\franca.jpg"
        c.drawImage(logo, 450, 800, width=90, height=30,
                    mask='auto')  # preserveAspectRatio=True,

        c.setFont('Helvetica-Bold', 14)
        c.setFillColor("black")
        c.drawString(30, 800, "Relatório fotográfico")
        imgFotoObra = diretorio + "foto_13.png"
        c.drawImage(imgFotoObra, 30, 550, width=250, height=200,
                    mask='auto')   # preserveAspectRatio=True
        if os.path.isfile(diretorio+"foto_14.png"):
            imgFotoObra = diretorio + "foto_14.png"
            c.drawImage(imgFotoObra, 310, 550, width=250, height=200,
                        mask='auto')   # preserveAspectRatio=True
        if os.path.isfile(diretorio+"foto_15.png"):
            imgFotoObra = diretorio + "foto_15.png"
            c.drawImage(imgFotoObra, 30, 295, width=250, height=200,
                        mask='auto')   # preserveAspectRatio=True
        if os.path.isfile(diretorio+"foto_16.png"):
            imgFotoObra = diretorio + "foto_16.png"
            c.drawImage(imgFotoObra, 310, 295, width=250, height=200,
                        mask='auto')   # preserveAspectRatio=True
        if os.path.isfile(diretorio+"foto_17.png"):
            imgFotoObra = diretorio + "foto_17.png"
            c.drawImage(imgFotoObra, 30,  45, width=250, height=200,
                        mask='auto')   # preserveAspectRatio=True
        if os.path.isfile(diretorio+"foto_18.png"):
            imgFotoObra = diretorio + "foto_18.png"
            c.drawImage(imgFotoObra, 310,  45, width=250, height=200,
                        mask='auto')   # preserveAspectRatio=True

        c.setFont('Helvetica', 10)
        c.drawString(570, 10, str(pagina))

    def pdfPag11(self, c, diretorio, pagina):
        #   Décima Primeira Página

        logo = "C:\\Desafios JavaScript\\gfc\\app\\static\\imgs\\franca.jpg"
        c.drawImage(logo, 450, 800, width=90, height=30,
                    mask='auto')  # preserveAspectRatio=True,

        c.setFont('Helvetica-Bold', 14)
        c.setFillColor("black")
        c.drawString(30, 800, "Relatório fotográfico")
        imgFotoObra = diretorio + "foto_19.png"
        c.drawImage(imgFotoObra, 30, 550, width=250, height=200,
                    mask='auto')   # preserveAspectRatio=True
        if os.path.isfile(diretorio+"foto_20.png"):
            imgFotoObra = diretorio + "foto_20.png"
            c.drawImage(imgFotoObra, 310, 550, width=250, height=200,
                        mask='auto')   # preserveAspectRatio=True
        if os.path.isfile(diretorio+"foto_21.png"):
            imgFotoObra = diretorio + "foto_21.png"
            c.drawImage(imgFotoObra, 30, 295, width=250, height=200,
                        mask='auto')   # preserveAspectRatio=True
        if os.path.isfile(diretorio+"foto_22.png"):
            imgFotoObra = diretorio + "foto_22.png"
            c.drawImage(imgFotoObra, 310, 295, width=250, height=200,
                        mask='auto')   # preserveAspectRatio=True
        if os.path.isfile(diretorio+"foto_23.png"):
            imgFotoObra = diretorio + "foto_23.png"
            c.drawImage(imgFotoObra, 30,  45, width=250, height=200,
                        mask='auto')   # preserveAspectRatio=True
        if os.path.isfile(diretorio+"foto_24.png"):
            imgFotoObra = diretorio + "foto_24.png"
            c.drawImage(imgFotoObra, 310,  45, width=250, height=200,
                        mask='auto')   # preserveAspectRatio=True

        c.setFont('Helvetica', 10)
        c.drawString(570, 10, str(pagina))

    def pdfPag12(self, c, diretorio, pagina, idEmpreend, mes, ano):
        #   Décima Segunda Página
 
        logo = os.path.normpath("C:\\Desafios JavaScript\\gfc\\app\\static\\imgs\\franca.jpg")
          
        c.drawImage(logo, 450, 800, width=90, height=30, mask='auto')  # preserveAspectRatio=True,

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
            diretorio = self.app.config['DIRSYS'] + "Relatorios" + self.app.config['BARRADIR']
        else:
            diretorio = self.app.config['DIRSYS'] + str(idEmpreend) + self.app.config['BARRADIR'] + ano + "_" + mes + self.app.config['BARRADIR']

        return (diretorio)

    def criaDir(self, diretorio):
        # Criar diretórios

        if not os.path.exists(diretorio):
            os.makedirs(diretorio)
            print(f"Diretorio '{diretorio}' criado com sucesso.")

        else:
            print(f"Diretorio '{diretorio}' já existe.")

        return

    def verificaDir(self, diretorio):
        # Criar diretórios

        if not os.path.exists(diretorio):
            print(f"Diretorio '{diretorio}' não existe.")
            return False
        else:
            print(f"Diretorio '{diretorio}' já existe.")
            return True

    def verificaArqRelatorio(self, diretorio):

        listaErro = []
#   Primeira Página

        foto = "C:\\Desafios JavaScript\\gfc\\app\\static\\imgs\\franca.jpg"
        if not os.path.isfile(foto):
            listaErro.append('1ª pag - ' + foto + ' não encontrado')
        foto = diretorio + "perspectiva.png"
        if not os.path.isfile(foto):
            listaErro.append('1ª pag - ' + foto + ' não encontrado')
        foto = diretorio + "foto_3D_1.png"
        if not os.path.isfile(foto):
            listaErro.append('1ª pag - ' + foto + ' não encontrado')
        foto = diretorio + "foto_atual.jpeg"
        if not os.path.isfile(foto):
            listaErro.append('1ª pag - ' + foto + ' não encontrado')
        foto = diretorio + "foto_3D_2.png"
        if not os.path.isfile(foto):
            listaErro.append('1ª pag - ' + foto + ' não encontrado')
        foto = "C:\\Desafios JavaScript\\gfc\\app\\static\\imgs\\legenda 2.png"
        if not os.path.isfile(foto):
            listaErro.append('1ª pag - ' + foto + ' não encontrado')

#   Segunda Página
        foto = diretorio + "tab_medicoes.png"
        if not os.path.isfile(foto):
            listaErro.append('2ª pag - ' + foto + ' não encontrado')
        foto = diretorio + "graf_progresso_obra.png"
        if not os.path.isfile(foto):
            listaErro.append('2ª pag - ' + foto + ' não encontrado')

#   Terceira Página
        foto = diretorio + "tab_acomp_financeiro.png"
        if not os.path.isfile(foto):
            listaErro.append('3ª pag - ' + foto + ' não encontrado')
        foto = diretorio + "graf_orcamento_liberacao_valor.png"
        if not os.path.isfile(foto):
            listaErro.append('3ª pag - ' + foto + ' não encontrado')
        foto = diretorio + "tab_orcamento_liberacao.png"
        if not os.path.isfile(foto):
            listaErro.append('3ª pag - ' + foto + ' não encontrado')

#   Quarta Página
        foto = diretorio + "tab_notas.png"
        if not os.path.isfile(foto):
            listaErro.append('4ª pag - ' + foto + ' não encontrado')
        foto = diretorio + "graf_indices_garantia_I.png"
        if not os.path.isfile(foto):
            listaErro.append('4ª pag - ' + foto + ' não encontrado')

#   Quinta Página
        foto = diretorio + "graf_indices_garantia_II.png"
        if not os.path.isfile(foto):
            listaErro.append('5ª pag - ' + foto + ' não encontrado')
        foto = diretorio + "graf_chaves_perc.png"
        if not os.path.isfile(foto):
            listaErro.append('5ª pag - ' + foto + ' não encontrado')
        foto = diretorio + "graf_chaves_valor.png"
        if not os.path.isfile(foto):
            listaErro.append('5ª pag - ' + foto + ' não encontrado')
        foto = diretorio + "graf_vendas_perc.png"
        if not os.path.isfile(foto):
            listaErro.append('5ª pag - ' + foto + ' não encontrado')
        foto = diretorio + "graf_vendas_valor.png"
        if not os.path.isfile(foto):
            listaErro.append('5ª pag - ' + foto + ' não encontrado')

#   Sexta Página
        foto = diretorio + "tab_conta_corrente.png"
        if not os.path.isfile(foto):
            listaErro.append('6ª pag - ' + foto + ' não encontrado')
        foto = diretorio + "tab_garantias_geral.png"
        if not os.path.isfile(foto):
            listaErro.append('6ª pag - ' + foto + ' não encontrado')
        foto = diretorio + "tab_garantias_obra.png"
        if not os.path.isfile(foto):
            listaErro.append('6ª pag - ' + foto + ' não encontrado')
        foto = diretorio + "tab_certidoes.png"
        if not os.path.isfile(foto):
            listaErro.append('6ª pag - ' + foto + ' não encontrado')
#   Setima Página
        foto = diretorio + "foto_3D_1.png"
        if not os.path.isfile(foto):
            listaErro.append('7ª pag - ' + foto + ' não encontrado')
        foto = diretorio + "foto_3D_2.png"
        if not os.path.isfile(foto):
            listaErro.append('7ª pag - ' + foto + ' não encontrado')
        foto = diretorio + "foto_3D_3.png"
        if not os.path.isfile(foto):
            listaErro.append('7ª pag - ' + foto + ' não encontrado')
        foto = "C:\\Desafios JavaScript\\gfc\\app\\static\\imgs\\legenda 2.png"
        if not os.path.isfile(foto):
            listaErro.append('7ª pag - ' + foto + ' não encontrado')

#   Oitava Página
        fotoJpeg = diretorio + "foto_1.jpeg"
        fotoPng = diretorio + "foto_1.png"
        if not (os.path.isfile(fotoJpeg) or os.path.isfile(fotoPng)):
            listaErro.append('8ª pag - ' + fotoPng + ' não encontrado')

#   Nona Página
#        foto = diretorio + "foto_7.jpeg"
#        if not os.path.isfile(foto):
#            listaErro.append('9ª pag - ' + foto + ' não encontrado')
#
#   Décima Página
#        foto = diretorio + "foto_13.jpeg"
#        if not os.path.isfile(foto):
#            listaErro.append('10ª pag - ' + foto + ' não encontrado')
#
#   Décima Primeira Página
#        foto = diretorio + "foto_19.jpeg"
#        if not os.path.isfile(foto):
#            listaErro.append('11ª pag - ' + foto + ' não encontrado')

#   Décima Segunda Página
#        foto = diretorio + "consideracoes_finais.png"
#        if not os.path.isfile(foto):
#            listaErro.append('12ª pag - ' + foto + ' não encontrado')

        return listaErro
