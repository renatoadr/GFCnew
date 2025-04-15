from flask import Blueprint, request, render_template, send_file, current_app
from controller.empreendimentoController import empreendimentoController
from controller.orcamentoController import orcamentoController
from controller.unidadeController import unidadeController
from controller.graficoController import graficoController
from controller.medicaoController import medicaoController
from controller.geralController import geralController
from utils.CtrlSessao import IdEmpreend
from matplotlib import pyplot as plt
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import random

grafico_bp = Blueprint('graficos', __name__)


@grafico_bp.route('/obter_grafico', methods=['GET'])
def obter_grafico():

    grafNome = request.args.get("grafNome")

    print('------------ obter_grafico -------------')
    print(grafNome)
    return send_file(grafNome, mimetype='image/png')


@grafico_bp.route('/graf_orcamento_liberacao', methods=['GET'])
def graf_orcamento_liberacao():

    tipo = request.args.get("tipo")
    idEmpreend = IdEmpreend().get()
    dtCarga = request.args.get("dtCarga")
    mes = request.args.get("mesV")
    ano = request.args.get("anoV")
    print('==============>', mes, ano)

    medC = orcamentoController()
    medS = medC.consultarOrcamentoPelaData(idEmpreend, dtCarga)

    fisico = []
    financeiro = []
    orcado = []
    index = []

    for m in medS:
        index.append(m.getItem())

        if tipo == "valor":
            fisico.append(float(0 if m.getFisicoValor()
                          is None else m.getFisicoValor()))
            financeiro.append(float(0 if m.getFinanceiroValor()
                              is None else m.getFinanceiroValor()))
            orcado.append(float(0 if m.getOrcadoValor()
                          is None else m.getOrcadoValor()))
        else:
            fisico.append(float(m.getFisicoPercentual()))
            financeiro.append(float(m.getFinanceiroPercentual()))

#    plt.title("\Medição Física da Obra x Liberação Financeira (em %)", fontdict={'family': 'serif', 'color': 'black', 'weight': 'bold', 'size': 12}, loc='center')
        if tipo == "valor":
            df = pd.DataFrame(
                {'Físico': fisico, 'Financeiro': financeiro, 'Orçado': orcado}, index=index)
        else:
            df = pd.DataFrame(
                {'Físico': fisico, 'Financeiro': financeiro}, index=index)

    ax = df.plot.barh()
    ax.set_xlabel('Valor em milhões')
    plt.legend(loc='lower left', bbox_to_anchor=(0, -0.2),
               fontsize=8, ncols=3)  # Adicionar a legenda fora do gráfico

    grafC = graficoController()

    diretorio = grafC.montaDir(idEmpreend, mes, ano)
    grafC.criaDir(diretorio)

    if tipo == "valor":
        grafNome = diretorio + 'graf_orcamento_liberacao_valor.png'
    else:
        grafNome = diretorio + 'graf_orcamento_liberacao_percentual.png'

    plt.savefig(grafNome, bbox_inches='tight')

    return render_template("orcamento_liberacao.html", grafNome=grafNome, version=random.randint(1, 100000))


@grafico_bp.route('/graf_progresso_obra', methods=['GET'])
def graf_progresso_obra():

    # Gráfico de linhas
    # PROGRESSO FÍSICO DA OBRA (Previsto x Realizado)

    idEmpreend  = IdEmpreend().get()
    mesVigencia = request.args.get("mesVigencia")
    anoVigencia = request.args.get("anoVigencia")
    mesInicio  = request.args.get("mesInicio")
    anoInicio  = request.args.get("anoInicio")
    mesFinal   = request.args.get("mesFinal")
    anoFinal   = request.args.get("anoFinal")

    geral = geralController()
    preC = medicaoController()
    preS = preC.consultarMedicoesPorPeriodo(idEmpreend, mesInicio, anoInicio, mesFinal, anoFinal)

    fig, ax = plt.subplots(1, 1)

    x1 = []
    x2 = []
    y1 = []
    y2 = []
    for p in preS:
        #        dd = []
        periodo = geral.formatammmaa(p.getMesVigencia(), p.getAnoVigencia())
        x1.append(periodo)
        y1.append(p.getPercPrevistoAcumulado())
        if p.getPercRealizadoAcumulado() > 0:
            y2.append(p.getPercRealizadoAcumulado())
            x2.append(periodo)

    plt.figure(figsize=(25, 10))     # Determina o tamanho da figura
    plt.plot(x1, y1, label='Previsto', linewidth=4,
             marker='o')  # espessura da linha =4
    plt.plot(x2, y2, label='Realizado', linewidth=4,
             marker='o')  # marker indica o ponto xy

    annotationsy1 = y1
    annotationsy2 = y2

    # Determina caracteristicas dos pontos x/y no gráfico
    plt.scatter(x1, y1, s=20)
    plt.scatter(x2, y2, s=20)
    plt.ylim(-5, 120)            # Força os valores do eixo Y
    plt.tick_params(labelsize=14)  # tamanho da letra nos eixos X e Y

    plt.title("PROGRESSO FÍSICO DA OBRA (Previsto x Realizado)", fontdict={
              'family': 'serif', 'color': 'black', 'weight': 'bold', 'size': 28}, loc='center')

    for xi, yi, text in zip(x1, y1, annotationsy1):
        plt.annotate(text, xy=(xi, yi), xycoords='data', xytext=(
            3, 10), textcoords='offset points', fontsize=14)
    for xi, yi, text in zip(x2, y2, annotationsy2):
        plt.annotate(text, xy=(xi, yi), xycoords='data', xytext=(
            3, -20), textcoords='offset points', fontsize=14)

    plt.legend(fontsize=20, loc="upper left")
#    plt.xlabel(fontsize=14)
#    plt.ylabel(fontsize=14)

    grafC = graficoController()

    diretorio = grafC.montaDir(idEmpreend, mesVigencia, anoVigencia)
    grafC.criaDir(diretorio)
    grafNome = diretorio + 'graf_progresso_obra.png'

    plt.savefig(grafNome)  # , bbox_inches='tight')

    return render_template("medicoes_liberacao.html", grafNome=grafNome, version=random.randint(1, 100000))


@grafico_bp.route('/graf_indices_garantia_I', methods=['GET'])
def graf_indices_garantia_I():
    # ÍNDICES DE GARANTIA

    idEmpreend = 55
    mes = "12"
    ano = "2024"
    mesVigenciaIni = '01'
    anoVigenciaIni = '2024'
    mesVigenciaFim = '04'
    anoVigenciaFim = '2024'

    geral = geralController()
    empC = empreendimentoController()
    empS = empC.consultarEmpreendimentoPeloId(idEmpreend)
    uniC = unidadeController()
    uniS = uniC.consultarUnidadeRecebibeis(idEmpreend)

    x1 = ['jan', 'fev', 'mar', 'abr']
    y1 = [1.20, 1.20, 1.20, 1.20]
    y2 = [1.00, 1.23, 1.29, 1.42]

    linhas = [1.00, 1.10, 1.20, 1.30, 1.40, 1.50, 1.60]
    plt.hlines(linhas, 0, 3, '#9feafc')

    plt.plot(x1, y1, label='IC Estipulado em contrato')
    plt.plot(x1, y2, label='IC Recebiveis + estoque')

    annotationsy1 = y1
    annotationsy2 = y2

    plt.scatter(x1, y1, s=20)
    plt.scatter(x1, y2, s=20)

    plt.ylim(0.9, 1.6)

    plt.title("Índices de garantia previsto x existente", fontdict={
              'family': 'serif', 'color': 'black', 'weight': 'bold', 'size': 12}, loc='center')

    for xi, yi, text in zip(x1, y1, annotationsy1):
        plt.annotate(text, xy=(xi, yi), xycoords='data',
                     xytext=(3, 10), textcoords='offset points')
    for xi, yi, text in zip(x1, y2, annotationsy2):
        plt.annotate(text, xy=(xi, yi), xycoords='data',
                     xytext=(3, -10), textcoords='offset points')

    plt.legend(loc='lower left', bbox_to_anchor=(0, -0.2),
               fontsize=8, ncols=2)  # Adicionar a legenda fora do gráfico
    plt.tight_layout()    # Ajustar o layout para evitar cortes
    plt.margins(0.1, 0.1)  # Ajustar margens da caixa x gráfico

    grafC = graficoController()

    idEmpreend = str(55)  # preciso montar esse informação
    mes = "12"
    ano = "2024"

    diretorio = grafC.montaDir(idEmpreend, mes, ano)
    grafC.criaDir(diretorio)
    grafNome = diretorio + 'graf_indices_garantia_I.png'

    plt.savefig(grafNome)  # , bbox_inches='tight')

    return


@grafico_bp.route('/graf_indices_garantia_II', methods=['GET'])
def graf_indices_garantia_II():
    # ÍNDICES DE GARANTIA

    idEmpreend = 55
    mes = "12"
    ano = "2024"
    mesVigenciaIni = '01'
    anoVigenciaIni = '2024'
    mesVigenciaFim = '04'
    anoVigenciaFim = '2024'

    geral = geralController()
    preC = medicaoController()
    preS = preC.consultarMedicoesPorPeriodo(idEmpreend, mesVigenciaIni, anoVigenciaIni, mesVigenciaFim, anoVigenciaFim)

    x1 = ['jan', 'fev', 'mar', 'abr']
    y3 = [0.10, 0.15, 0.20, 0.29]
    y4 = [0.90, 1.08, 1.09, 1.13]

    linhas = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5,
              0.6, 0.7, 0.8, 0.9, 1.00, 1.10, 1.20]

    plt.hlines(linhas, 0, 3, '#9feafc')
    plt.plot(x1, y3, label='IC Recebiveis')
    plt.plot(x1, y4, label='IC Estoque')

    annotationsy3 = y3
    annotationsy4 = y4

    plt.scatter(x1, y3, s=20)
    plt.scatter(x1, y4, s=20)

    plt.ylim(0.0, 1.2)

    plt.title("Índices de garantia previsto x existente", fontdict={
              'family': 'serif', 'color': 'black', 'weight': 'bold', 'size': 12}, loc='center')

    for xi, yi, text in zip(x1, y3, annotationsy3):
        plt.annotate(text, xy=(xi, yi), xycoords='data',
                     xytext=(3, 10), textcoords='offset points')
    for xi, yi, text in zip(x1, y4, annotationsy4):
        plt.annotate(text, xy=(xi, yi), xycoords='data',
                     xytext=(3, -10), textcoords='offset points')

    plt.legend(loc='lower left', bbox_to_anchor=(0, -0.2),
               fontsize=8, ncols=2)  # Adicionar a legenda fora do gráfico
    plt.tight_layout()    # Ajustar o layout para evitar cortes
    plt.margins(0.1, 0.1)  # Ajustar margens da caixa x gráfico

    grafC = graficoController()

    idEmpreend = str(55)  # preciso montar esse informação
    mes = "12"
    ano = "2024"

    diretorio = grafC.montaDir(idEmpreend, mes, ano)
    grafC.criaDir(diretorio)
    grafNome = diretorio + 'graf_indices_garantia_II.png'

    plt.savefig(grafNome)  # , bbox_inches='tight')

    return


@grafico_bp.route('/graf_vendas', methods=['GET'])
def graf_vendas():
    # Gráfico de rosca
    # ÍNDICES DE VENDAS

    idEmpreend = str(55)  # preciso montar esse informação
    mes = "12"
    ano = "2024"
    unidc = unidadeController()
    unid = unidc.consultarUnidadeVendas(idEmpreend)

    fig, ax = plt.subplots(figsize=(6, 3), subplot_kw=dict(aspect="equal"))

    tpStatus = []
    data = []
    soma = 0

    for n in unid:
        soma += n.getTtStatus()
        data.append(n.getTtStatus())

    recipe = []

    for n in unid:
        perc = round((n.getTtStatus()/soma)*100)
        texto = str(n.getTtStatus()) + " " + \
            n.getStatus() + " (" + str(perc) + "%)"
        recipe.append(texto)

    wedges, texts = ax.pie(data, wedgeprops=dict(width=0.5), startangle=-40)

    bbox_props = dict(boxstyle="square,pad=0.3", fc="w", ec="k", lw=0.72)
    kw = dict(arrowprops=dict(arrowstyle="-"),
              bbox=bbox_props, zorder=0, va="center")

    for i, p in enumerate(wedges):
        ang = (p.theta2 - p.theta1)/2. + p.theta1
        y = np.sin(np.deg2rad(ang))
        x = np.cos(np.deg2rad(ang))
        horizontalalignment = {-1: "right", 1: "left"}[int(np.sign(x))]
        connectionstyle = f"angle,angleA=0,angleB={ang}"
        kw["arrowprops"].update({"connectionstyle": connectionstyle})
        ax.annotate(recipe[i], xy=(x, y), xytext=(1.35*np.sign(x), 1.4*y),
                    horizontalalignment=horizontalalignment, **kw)

    ax.set_title("Vendas", fontdict={
                 'family': 'serif', 'color': 'black', 'weight': 'bold', 'size': 12}, loc='center')

    grafC = graficoController()

    diretorio = grafC.montaDir(idEmpreend, mes, ano)
    grafC.criaDir(diretorio)
    grafNome = diretorio + 'graf_vendas.png'

    plt.savefig(grafNome)  # , bbox_inches='tight')

    return


@grafico_bp.route('/graf_chaves', methods=['GET'])
def graf_chaves():
    # ÍNDICES DE CHAVES

    idEmpreend = str(55)  # preciso montar esse informação
    mes = "12"
    ano = "2024"
    unidc = unidadeController()
    unid = unidc.consultarUnidadeChaves(idEmpreend)

    labels = ['Chaves', 'Pré-chaves', 'Pós-chaves']

    total = unid.getTtChaves() + unid.getTtPreChaves() + unid.getTtPosChaves()

    perChave = unid.getTtChaves() / total
    perPreChave = unid.getTtPreChaves() / total
    perPosChave = unid.getTtPosChaves() / total

    sizes = [perChave, perPreChave, perPosChave]
#    print('sizes = ', sizes)

    fig1, ax1 = plt.subplots()

    ax1.pie(sizes, labels=labels, autopct='%1.1f%%', shadow=False,
            startangle=90, textprops={'fontsize': 16})

    ax1.axis('equal')

    grafC = graficoController()

    idEmpreend = str(55)  # preciso montar esse informação
    mes = "12"
    ano = "2024"

    diretorio = grafC.montaDir(idEmpreend, mes, ano)
    grafC.criaDir(diretorio)
    grafNome = diretorio + 'graf_chaves.png'

    plt.savefig(grafNome)  # , bbox_inches='tight')
    return
