# controller or business logic
# Tratamento de gáficos

from flask import Flask, request, render_template, redirect, url_for, flash, send_file, session, current_app
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

        logo = "c:\\Desafios JavaScript\\gfc\\static\\franca.jpg"
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

        foto = diretorio + "maquete.png"
        c.drawImage(foto,  40, 420, width=220, height=150, mask='auto')
        foto = diretorio + "foto_3D_1.png"
        c.drawImage(foto, 300, 380, width=300, height=200, mask='auto')
        foto = diretorio + "foto_3.jpeg"
        c.drawImage(foto,  40, 180, width=220, height=150, mask='auto')
        foto = diretorio + "foto_3D_3.png"
        c.drawImage(foto, 350, 150, width=200, height=200, mask='auto')
        logo = "c:\\Desafios JavaScript\\gfc\\static\\legenda 2.png"
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

        logo = "c:\\Desafios JavaScript\\gfc\\static\\franca.jpg"
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

        logo = "c:\\Desafios JavaScript\\gfc\\static\\franca.jpg"
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

        logo = "c:\\Desafios JavaScript\\gfc\\static\\franca.jpg"
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

        logo = "c:\\Desafios JavaScript\\gfc\\static\\franca.jpg"
        c.drawImage(logo, 450, 800, width=90, height=30,
                    mask='auto')  # preserveAspectRatio=True,

        imgFotoObra = diretorio + "graf_indices_garantia_II.png"
        c.drawImage(imgFotoObra, 30, 500, width=510, height=300,
                    mask='auto')   # preserveAspectRatio=True
        c.setFont('Helvetica-Bold', 14)
        c.setFillColor("black")
        c.drawString(30, 400, "Qualificação dos Recebíveis")

        imgFotoObra = diretorio + "graf_chaves.png"
        c.drawImage(imgFotoObra, 30, 200, width=200, height=150,
                    mask='auto')   # preserveAspectRatio=True
        imgFotoObra = diretorio + "graf_vendas.png"
        c.drawImage(imgFotoObra, 220, 200, width=330, height=150,
                    mask='auto')   # preserveAspectRatio=True

        c.setFont('Helvetica', 10)
        c.drawString(570, 10, str(pagina))

    def pdfPag6(self, c, diretorio, pagina):
        #   Sexta Página

        logo = "c:\\Desafios JavaScript\\gfc\\static\\franca.jpg"
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

        imgFotoObra = diretorio + "tab_pontos_atencao_geral.png"
        c.drawImage(imgFotoObra, 20, 220, width=300, height=100,
                    mask='auto')   # preserveAspectRatio=True
        imgFotoObra = diretorio + "tab_pontos_atencao_obra.png"
        c.drawImage(imgFotoObra, 290, 220, width=300, height=100,
                    mask='auto')   # preserveAspectRatio=True
        imgFotoObra = diretorio + "tab_pontos_atencao_documentos.png"
        c.drawImage(imgFotoObra, 20, 60, width=250, height=100,
                    mask='auto')   # preserveAspectRatio=True

        c.setFont('Helvetica', 10)
        c.drawString(570, 10, str(pagina))

    def pdfPag7(self, c, diretorio, pagina):
        #   Setima Página

        logo = "c:\\Desafios JavaScript\\gfc\\static\\franca.jpg"
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
        logo = "c:\\Desafios JavaScript\\gfc\\static\\legenda 2.png"
        c.drawImage(logo, 420, 100, width=150, height=25,
                    mask='auto')  # preserveAspectRatio=True,

        c.setFont('Helvetica', 10)
        c.drawString(570, 10, str(pagina))

    def pdfPag8(self, c, diretorio, pagina):
        #   Oitava Página

        logo = "c:\\Desafios JavaScript\\gfc\\static\\franca.jpg"
        c.drawImage(logo, 450, 800, width=90, height=30,
                    mask='auto')  # preserveAspectRatio=True,

        c.setFont('Helvetica-Bold', 14)
        c.setFillColor("black")
        c.drawString(30, 800, "Relatório fotográfico")
        imgFotoObra = diretorio + "foto_1.jpeg"
        c.drawImage(imgFotoObra, 30, 550, width=250, height=200,
                    mask='auto')   # preserveAspectRatio=True
        if os.path.isfile(diretorio+"foto_2.jpeg"):
            imgFotoObra = diretorio + "foto_2.jpeg"
            c.drawImage(imgFotoObra, 310, 550, width=250, height=200,
                        mask='auto')   # preserveAspectRatio=True
        if os.path.isfile(diretorio+"foto_3.jpeg"):
            imgFotoObra = diretorio + "foto_3.jpeg"
            c.drawImage(imgFotoObra, 30, 295, width=250, height=200,
                        mask='auto')   # preserveAspectRatio=True
        if os.path.isfile(diretorio+"foto_4.jpeg"):
            imgFotoObra = diretorio + "foto_4.jpeg"
            c.drawImage(imgFotoObra, 310, 295, width=250, height=200,
                        mask='auto')   # preserveAspectRatio=True
        if os.path.isfile(diretorio+"foto_5.jpeg"):
            imgFotoObra = diretorio + "foto_5.jpeg"
            c.drawImage(imgFotoObra, 30,  45, width=250, height=200,
                        mask='auto')   # preserveAspectRatio=True
        if os.path.isfile(diretorio+"foto_6.jpeg"):
            imgFotoObra = diretorio + "foto_6.jpeg"
            c.drawImage(imgFotoObra, 310,  45, width=250, height=200,
                        mask='auto')   # preserveAspectRatio=True

        c.setFont('Helvetica', 10)
        c.drawString(570, 10, str(pagina))

    def pdfPag9(self, c, diretorio, pagina):
        #   Nona Página

        logo = "c:\\Desafios JavaScript\\gfc\\static\\franca.jpg"
        c.drawImage(logo, 450, 800, width=90, height=30,
                    mask='auto')  # preserveAspectRatio=True,

        c.setFont('Helvetica-Bold', 14)
        c.setFillColor("black")
        c.drawString(30, 800, "Relatório fotográfico")
        imgFotoObra = diretorio + "foto_7.jpeg"
        c.drawImage(imgFotoObra, 30, 550, width=250, height=200,
                    mask='auto')   # preserveAspectRatio=True
        if os.path.isfile(diretorio+"foto_8.jpeg"):
            imgFotoObra = diretorio + "foto_8.jpeg"
            c.drawImage(imgFotoObra, 310, 550, width=250, height=200,
                        mask='auto')   # preserveAspectRatio=True
        if os.path.isfile(diretorio+"foto_9.jpeg"):
            imgFotoObra = diretorio + "foto_9.jpeg"
            c.drawImage(imgFotoObra, 30, 295, width=250, height=200,
                        mask='auto')   # preserveAspectRatio=True
        if os.path.isfile(diretorio+"foto_10.jpeg"):
            imgFotoObra = diretorio + "foto_10.jpeg"
            c.drawImage(imgFotoObra, 310, 295, width=250, height=200,
                        mask='auto')   # preserveAspectRatio=True
        if os.path.isfile(diretorio+"foto_11.jpeg"):
            imgFotoObra = diretorio + "foto_11.jpeg"
            c.drawImage(imgFotoObra, 30,  45, width=250, height=200,
                        mask='auto')   # preserveAspectRatio=True
        if os.path.isfile(diretorio+"foto_12.jpeg"):
            imgFotoObra = diretorio + "foto_12.jpeg"
            c.drawImage(imgFotoObra, 310,  45, width=250, height=200,
                        mask='auto')   # preserveAspectRatio=True

        c.setFont('Helvetica', 10)
        c.drawString(570, 10, str(pagina))

    def pdfPag10(self, c, diretorio, pagina):
        #   Décima Página

        logo = "c:\\Desafios JavaScript\\gfc\\static\\franca.jpg"
        c.drawImage(logo, 450, 800, width=90, height=30,
                    mask='auto')  # preserveAspectRatio=True,

        c.setFont('Helvetica-Bold', 14)
        c.setFillColor("black")
        c.drawString(30, 800, "Relatório fotográfico")
        imgFotoObra = diretorio + "foto_13.jpeg"
        c.drawImage(imgFotoObra, 30, 550, width=250, height=200,
                    mask='auto')   # preserveAspectRatio=True
        if os.path.isfile(diretorio+"foto_14.jpeg"):
            imgFotoObra = diretorio + "foto_14.jpeg"
            c.drawImage(imgFotoObra, 310, 550, width=250, height=200,
                        mask='auto')   # preserveAspectRatio=True
        if os.path.isfile(diretorio+"foto_15.jpeg"):
            imgFotoObra = diretorio + "foto_15.jpeg"
            c.drawImage(imgFotoObra, 30, 295, width=250, height=200,
                        mask='auto')   # preserveAspectRatio=True
        if os.path.isfile(diretorio+"foto_16.jpeg"):
            imgFotoObra = diretorio + "foto_16.jpeg"
            c.drawImage(imgFotoObra, 310, 295, width=250, height=200,
                        mask='auto')   # preserveAspectRatio=True
        if os.path.isfile(diretorio+"foto_17.jpeg"):
            imgFotoObra = diretorio + "foto_17.jpeg"
            c.drawImage(imgFotoObra, 30,  45, width=250, height=200,
                        mask='auto')   # preserveAspectRatio=True
        if os.path.isfile(diretorio+"foto_18.jpeg"):
            imgFotoObra = diretorio + "foto_18.jpeg"
            c.drawImage(imgFotoObra, 310,  45, width=250, height=200,
                        mask='auto')   # preserveAspectRatio=True

        c.setFont('Helvetica', 10)
        c.drawString(570, 10, str(pagina))

    def pdfPag11(self, c, diretorio, pagina):
        #   Décima Primeira Página

        logo = "c:\\Desafios JavaScript\\gfc\\static\\franca.jpg"
        c.drawImage(logo, 450, 800, width=90, height=30,
                    mask='auto')  # preserveAspectRatio=True,

        c.setFont('Helvetica-Bold', 14)
        c.setFillColor("black")
        c.drawString(30, 800, "Relatório fotográfico")
        imgFotoObra = diretorio + "foto_19.jpeg"
        c.drawImage(imgFotoObra, 30, 550, width=250, height=200,
                    mask='auto')   # preserveAspectRatio=True
        if os.path.isfile(diretorio+"foto_20.jpeg"):
            imgFotoObra = diretorio + "foto_20.jpeg"
            c.drawImage(imgFotoObra, 310, 550, width=250, height=200,
                        mask='auto')   # preserveAspectRatio=True
        if os.path.isfile(diretorio+"foto_21.jpeg"):
            imgFotoObra = diretorio + "foto_21.jpeg"
            c.drawImage(imgFotoObra, 30, 295, width=250, height=200,
                        mask='auto')   # preserveAspectRatio=True
        if os.path.isfile(diretorio+"foto_22.jpeg"):
            imgFotoObra = diretorio + "foto_22.jpeg"
            c.drawImage(imgFotoObra, 310, 295, width=250, height=200,
                        mask='auto')   # preserveAspectRatio=True
        if os.path.isfile(diretorio+"foto_23.jpeg"):
            imgFotoObra = diretorio + "foto_23.jpeg"
            c.drawImage(imgFotoObra, 30,  45, width=250, height=200,
                        mask='auto')   # preserveAspectRatio=True
        if os.path.isfile(diretorio+"foto_24.jpeg"):
            imgFotoObra = diretorio + "foto_24.jpeg"
            c.drawImage(imgFotoObra, 310,  45, width=250, height=200,
                        mask='auto')   # preserveAspectRatio=True

        c.setFont('Helvetica', 10)
        c.drawString(570, 10, str(pagina))

    def pdfPag12(self, c, diretorio, pagina):
        #   Décima Segunda Página

        logo = "c:\\Desafios JavaScript\\gfc\\static\\franca.jpg"
        c.drawImage(logo, 450, 800, width=90, height=30,
                    mask='auto')  # preserveAspectRatio=True,

        c.setFont('Helvetica-Bold', 14)
        c.setFillColor("black")
        c.drawString(30, 780, "Considerações Finais")
        imgFotoObra = diretorio + "consideracoes_finais.png"
        c.drawImage(imgFotoObra, 20, 400, width=500, height=350,
                    mask='auto')   # preserveAspectRatio=True

        c.setFont('Helvetica', 10)
        c.drawString(570, 10, str(pagina))

    def montaDir(self, idEmpreend, mes, ano, relatorio=False):

        if relatorio:
            diretorio = self.app.config['DIRSYS'] + \
                "Relatorios" + self.app.config['BARRADIR']
        else:
            diretorio = self.app.config['DIRSYS'] + str(
                idEmpreend) + self.app.config['BARRADIR'] + ano + "_" + mes + self.app.config['BARRADIR']

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

        foto = "c:\\Desafios JavaScript\\gfc\\static\\franca.jpg"
        if not os.path.isfile(foto):
            listaErro.append('1ª pag - ' + foto + ' não encontrado')
        foto = diretorio + "maquete.png"
        if not os.path.isfile(foto):
            listaErro.append('1ª pag - ' + foto + ' não encontrado')
        foto = diretorio + "foto_3D_1.png"
        if not os.path.isfile(foto):
            listaErro.append('1ª pag - ' + foto + ' não encontrado')
        foto = diretorio + "foto_3.jpeg"
        if not os.path.isfile(foto):
            listaErro.append('1ª pag - ' + foto + ' não encontrado')
        foto = diretorio + "foto_3D_3.png"
        if not os.path.isfile(foto):
            listaErro.append('1ª pag - ' + foto + ' não encontrado')
        foto = "c:\\Desafios JavaScript\\gfc\\static\\legenda 2.png"
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
        foto = diretorio + "graf_chaves.png"
        if not os.path.isfile(foto):
            listaErro.append('5ª pag - ' + foto + ' não encontrado')
        foto = diretorio + "graf_vendas.png"
        if not os.path.isfile(foto):
            listaErro.append('5ª pag - ' + foto + ' não encontrado')

#   Sexta Página
        foto = diretorio + "tab_conta_corrente.png"
        if not os.path.isfile(foto):
            listaErro.append('6ª pag - ' + foto + ' não encontrado')
        foto = diretorio + "tab_pontos_atencao_geral.png"
        if not os.path.isfile(foto):
            listaErro.append('6ª pag - ' + foto + ' não encontrado')
        foto = diretorio + "tab_pontos_atencao_obra.png"
        if not os.path.isfile(foto):
            listaErro.append('6ª pag - ' + foto + ' não encontrado')
        foto = diretorio + "tab_pontos_atencao_documentos.png"
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
        foto = "c:\\Desafios JavaScript\\gfc\\static\\legenda 2.png"
        if not os.path.isfile(foto):
            listaErro.append('7ª pag - ' + foto + ' não encontrado')

#   Oitava Página
        foto = diretorio + "foto_1.jpeg"
        if not os.path.isfile(foto):
            listaErro.append('8ª pag - ' + foto + ' não encontrado')

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
        foto = diretorio + "consideracoes_finais.png"
        if not os.path.isfile(foto):
            listaErro.append('12ª pag - ' + foto + ' não encontrado')

        return listaErro
