from utils.security import login_required
from flask import Blueprint, request, render_template, send_file
from controller.empreendimentoController import empreendimentoController
from controller.orcamentoController import orcamentoController
from controller.unidadeController import unidadeController
from controller.graficoController import graficoController
from controller.medicaoController import medicaoController
from controller.geralController import geralController
from utils.CtrlSessao import IdEmpreend
import matplotlib.pyplot as plt
from datetime import datetime
import pandas as pd
import numpy as np
import random
import os

graficos_bp = Blueprint('graficos', __name__)


@graficos_bp.route('/obter_grafico', methods=['GET'])
@login_required
def obter_grafico():

    grafNome = request.args.get("grafNome")

    print('------------ obter_grafico -------------')
    print(grafNome)
    return send_file(grafNome, mimetype='image/png')


@graficos_bp.route('/graf_orcamento_liberacao', methods=['GET'])
@login_required
def graf_orcamento_liberacao():

    tipo = request.args.get("tipo")
    idEmpreend = IdEmpreend().get()
    dtCarga = request.args.get("dtCarga")
    mes = request.args.get("mesV")
    ano = request.args.get("anoV")

    medC = orcamentoController()
    medS = medC.consultarOrcamentoPelaData(idEmpreend, dtCarga)

    grafNome = gerar_graf_orcamento_liberacao(
        idEmpreend, mes, ano, tipo, medS)

    return render_template("orcamento_liberacao.html", grafNome=grafNome, version=random.randint(1, 100000))


def gerar_graf_orcamento_liberacao(idEmpreend, mes, ano, tipo, medS):

    fisico = []
    financeiro = []
    orcado = []
    index = []

    plt.switch_backend('agg')

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

        if tipo == "valor":
            df = pd.DataFrame(
                {'Físico': fisico, 'Financeiro': financeiro, 'Orçado': orcado}, index=index)
        else:
            df = pd.DataFrame(
                {'Físico': fisico, 'Financeiro': financeiro}, index=index)

    ax = df.plot.barh()
    ax.set_xlabel('Valor em milhões')
    plt.legend(loc='lower left', bbox_to_anchor=(0, -0.2),
               fontsize=8, ncols=3)

    grafC = graficoController()

    diretorio = grafC.montaDir(idEmpreend, mes, ano)
    grafC.criaDir(diretorio)

    if tipo == "valor":
        grafNome = os.path.join(
            diretorio, 'graf_orcamento_liberacao_valor.png')
    else:
        grafNome = os.path.join(
            diretorio, 'graf_orcamento_liberacao_percentual.png')

    if os.path.exists(grafNome):
        os.remove(grafNome)

    plt.savefig(grafNome, bbox_inches='tight')

    plt.close('all')

    return grafNome


@graficos_bp.route('/graf_progresso_obra', methods=['GET'])
@login_required
def graf_progresso_obra():

    # Gráfico de linhas
    # PROGRESSO FÍSICO DA OBRA (Previsto x Realizado)

    idEmpreend = IdEmpreend().get()
    mesVigencia = request.args.get("mesVigencia")
    anoVigencia = request.args.get("anoVigencia")
    mesInicio = request.args.get("mesInicio")
    anoInicio = request.args.get("anoInicio")
    mesFinal = request.args.get("mesFinal")
    anoFinal = request.args.get("anoFinal")

    grafNome = gerar_graf_progresso_obra(
        idEmpreend,
        mesVigencia,
        anoVigencia,
        mesInicio,
        anoInicio,
        mesFinal,
        anoFinal
    )

    return render_template("medicoes_liberacao.html", grafNome=grafNome, version=random.randint(1, 100000))


def gerar_graf_progresso_obra(idEmpreend, mesVigencia, anoVigencia, mesInicio, anoInicio, mesFinal, anoFinal):
    geral = geralController()
    preC = medicaoController()
    preS = preC.consultarMedicoesPorPeriodo(
        idEmpreend, mesInicio, anoInicio, mesFinal, anoFinal)

    if not preS:
        return ''

    plt.switch_backend('agg')

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

#***************
#    linhas = [-0.10, 0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
#
#    tamLinha = len(x1) - 1
#    plt.hlines(linhas, 0, tamLinha, '#9feafc')
#    plt.plot(x1, y1, label='Estipulado em contrato')
#    plt.plot(
##**********

    annotationsy1 = y1
    annotationsy2 = y2

    # Determina caracteristicas dos pontos x/y no gráfico
    plt.scatter(x1, y1, s=30)
    plt.scatter(x2, y2, s=30)
    plt.ylim(-5, 100)            # Força os valores do eixo Y
    plt.tick_params(labelsize=14)  # tamanho da letra nos eixos X e Y

    plt.title("PROGRESSO FÍSICO DA OBRA (Previsto x Realizado)", fontdict={
              'family': 'serif', 'color': 'black', 'weight': 'bold', 'size': 28}, loc='center')

    contx1 = 0
    tamX1 = len(x1)
    tamX2 = len(x2)
    for x in range(tamX1):
        if x < tamX2:
            if annotationsy1[x] > annotationsy2[x]:
                desvioX1 = 20 # define a posição do texto no ponto x/y
                desvioX2 = -20 # define a posição do texto no ponto x/y
            else:
                desvioX1 = -20
                desvioX2 = 20
        else:
            desvioX1 = 20
            desvioX2 = -20
        plt.annotate(annotationsy1[x], xy=(x1[x], y1[x]), xycoords='data', xytext=(3, desvioX1), textcoords='offset points', fontsize=14, color='blue')
        if contx1 < tamX2:   
            plt.annotate(annotationsy2[x], xy=(x2[x], y2[x]), xycoords='data', xytext=(3, desvioX2), textcoords='offset points', fontsize=14, color='darkorange')
            contx1 += 1  

    plt.legend(fontsize=20, loc="upper left")
#    plt.xlabel(fontsize=14)
#    plt.ylabel(fontsize=14)

    grafC = graficoController()

    diretorio = grafC.montaDir(idEmpreend, mesVigencia, anoVigencia)
    grafC.criaDir(diretorio)
    grafNome = os.path.join(diretorio, 'graf_progresso_obra.png')

    if os.path.exists(grafNome):
        os.remove(grafNome)

    plt.savefig(grafNome)  # , bbox_inches='tight')
    plt.close('all')
    return grafNome


@graficos_bp.route('/graf_indices_garantia_I', methods=['GET'])
@login_required
def graf_indices_garantia_I():
    # ÍNDICES DE GARANTIA
    idEmpreend = IdEmpreend().get()
    mesVigencia = request.args.get("mesVigencia")
    anoVigencia = request.args.get("anoVigencia")
    mesInicio = request.args.get("mesInicio")
    anoInicio = request.args.get("anoInicio")
    mesFinal = request.args.get("mesFinal")
    anoFinal = request.args.get("anoFinal")

    grafNome = gerar_graf_indices_garantia_I(
        idEmpreend, mesVigencia, anoVigencia, mesInicio, anoInicio, mesFinal, anoFinal)

    return render_template("indices_liberacao.html", grafNome=grafNome, version=random.randint(1, 100000))


def gerar_graf_indices_garantia_I(idEmpreend, mesVigencia, anoVigencia, mesInicio, anoInicio, mesFinal, anoFinal):
    geral = geralController()
    empC = empreendimentoController()
    empS = empC.consultarEmpreendimentoPeloId(idEmpreend)

    VlPlanoEmp = empS.getVlPlanoEmp()
    IndiceGarantia = empS.getIndiceGarantia()

    uniC = unidadeController()
    recS = uniC.gerarInsumoRelatorio(
        idEmpreend,
        datetime(int(anoInicio), int(mesInicio), 1),
        datetime(int(anoFinal), int(mesFinal), 20)
    )

    if not recS:
        return ''

    plt.switch_backend('agg')

    x1 = []
    y1 = []
    y2 = []

    vlrAnterior = 0
    varicao = 0

    for u in recS:
        x1.append(geral.formatammmaa(u.getMesVigencia(), u.getAnoVigencia()))
        y1.append(IndiceGarantia if IndiceGarantia else 0.0)
#        y2.append(round((u.getTtPago() + u.getTtUnidade()) / VlPlanoEmp, 2))
#        vlrAtual = round((u.getTtPago() + u.getTtUnidade()) / VlPlanoEmp, 2)
        y2.append(round(VlPlanoEmp / (u.getTtPago() + u.getTtUnidade()), 2))
        vlrAtual = round(VlPlanoEmp / (u.getTtPago() + u.getTtUnidade()), 2)
#        print (u.getMesVigencia()+'/'+u.getAnoVigencia()+'>', 'plano emp ', VlPlanoEmp, u.getTtPago(), u.getTtUnidade(), 'Soma ', u.getTtPago() + u.getTtUnidade())            #  tirar 
        variacao = vlrAtual - vlrAnterior
        vlrAnterior = vlrAtual
#s       print(vlrAnterior, vlrAtual, variacao)

    linhas = [-0.1, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.00,
              1.10, 1.20, 1.30, 1.40, 1.50, 1.60, 1.70, 1.80]

    tamLinha = len(x1) - 1
    plt.hlines(linhas, 0, tamLinha, '#9feafc')
    plt.plot(x1, y1, label='Estipulado em contrato')
    plt.plot(
        x1, y2, label='Recebiveis + estoque - Variação no período: ' + str(variacao))

    annotationsy1 = y1
    annotationsy2 = y2

    plt.scatter(x1, y1, s=20)
    plt.scatter(x1, y2, s=20)

#    plt.ylim(1.0, 1.8)

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

    diretorio = grafC.montaDir(idEmpreend, mesVigencia, anoVigencia)
    grafC.criaDir(diretorio)
    grafNome = os.path.join(diretorio, 'graf_indices_garantia_I.png')

    if os.path.exists(grafNome):
        os.remove(grafNome)

    plt.savefig(grafNome)  # , bbox_inches='tight')

    plt.close('all')

    return grafNome


@graficos_bp.route('/graf_indices_garantia_II', methods=['GET'])
@login_required
def graf_indices_garantia_II():
    # ÍNDICES DE GARANTIA

    idEmpreend = IdEmpreend().get()
    mesVigencia = request.args.get("mesVigencia")
    anoVigencia = request.args.get("anoVigencia")
    mesInicio = request.args.get("mesInicio")
    anoInicio = request.args.get("anoInicio")
    mesFinal = request.args.get("mesFinal")
    anoFinal = request.args.get("anoFinal")

    grafNome = gerar_graf_indices_garantia_II(
        idEmpreend, mesVigencia, anoVigencia, mesInicio, anoInicio, mesFinal, anoFinal)

    return render_template(".html", grafNome=grafNome, version=random.randint(1, 100000))


def gerar_graf_indices_garantia_II(idEmpreend, mesVigencia, anoVigencia, mesInicio, anoInicio, mesFinal, anoFinal):
    geral = geralController()
    empC = empreendimentoController()
    empS = empC.consultarEmpreendimentoPeloId(idEmpreend)
    VlPlanoEmp = empS.getVlPlanoEmp()

    uniC = unidadeController()
    recS = uniC.gerarInsumoRelatorio(
        idEmpreend,
        datetime(int(anoInicio), int(mesInicio), 1),
        datetime(int(anoFinal), int(mesFinal), 28)
    )

    if not recS:
        return ''

    plt.switch_backend('agg')

    x2 = []
    y3 = []
    y4 = []

    for u in recS:
        x2.append(geral.formatammmaa(u.getMesVigencia(), u.getAnoVigencia()))
        if u.getTtPago() > 0:
           y3.append(round(u.getTtPago() / VlPlanoEmp, 2))
#           y3.append(round(VlPlanoEmp / u.getTtPago(), 2))
        else:
            y3.append(0.0)
        y4.append(round(u.getTtUnidade() / VlPlanoEmp, 2))
#        y4.append(round(VlPlanoEmp / u.getTtUnidade(), 2))
#        print(u.getMesVigencia()+'/'+u.getAnoVigencia()+'>', 'plano emp ', VlPlanoEmp, u.getTtPago(), u.getTtUnidade())            #  tirar

    linhas = [-0.1, 0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.00,
              1.10, 1.20, 1.30, 1.40, 1.50, 1.60, 1.70, 1.80]

    tamLinha = len(x2) - 1
    plt.hlines(linhas, 0, tamLinha, '#9feafc')
    plt.plot(x2, y3, label='Recebiveis')
    plt.plot(x2, y4, label='Estoque')

    annotationsy3 = y3
    annotationsy4 = y4

    plt.scatter(x2, y3, s=20)
    plt.scatter(x2, y4, s=20)

#    plt.ylim(0.0, 1.8)

    plt.title("Índices de garantia previsto x existente", fontdict={
              'family': 'serif', 'color': 'black', 'weight': 'bold', 'size': 12}, loc='center')

    for xi, yi, text in zip(x2, y3, annotationsy3):
        plt.annotate(text, xy=(xi, yi), xycoords='data',
                     xytext=(3, 10), textcoords='offset points')
    for xi, yi, text in zip(x2, y4, annotationsy4):
        plt.annotate(text, xy=(xi, yi), xycoords='data',
                     xytext=(3, -10), textcoords='offset points')

    plt.legend(loc='lower left', bbox_to_anchor=(0, -0.2),
               fontsize=8, ncols=2)  # Adicionar a legenda fora do gráfico
    plt.tight_layout()    # Ajustar o layout para evitar cortes
    plt.margins(0.1, 0.1)  # Ajustar margens da caixa x gráfico

    grafC = graficoController()

    diretorio = grafC.montaDir(idEmpreend, mesVigencia, anoVigencia)
    grafC.criaDir(diretorio)
    grafNome = os.path.join(diretorio, 'graf_indices_garantia_II.png')

    if os.path.exists(grafNome):
        os.remove(grafNome)

    plt.savefig(grafNome)  # , bbox_inches='tight')
    plt.close('all')

    return grafNome


@graficos_bp.route('/graf_vendas', methods=['GET'])
@login_required
def graf_vendas():
    # Gráfico de rosca
    # ÍNDICES DE VENDAS

    idEmpreend = IdEmpreend().get()
    mesVigencia = request.args.get("mesVigencia")
    anoVigencia = request.args.get("anoVigencia")

    grafNome = gerar_graf_vendas(idEmpreend, mesVigencia, anoVigencia, 'perc')

    return render_template("vendas_liberacao.html", grafNome=grafNome, version=random.randint(1, 100000))


def gerar_graf_vendas(idEmpreend, mesVigencia, anoVigencia, tipo):
    unidc = unidadeController()
    unid = unidc.consultarUnidadeVendas(idEmpreend, tipo)

    if not unid:
        return ''

    plt.switch_backend('agg')

    fig, ax = plt.subplots(figsize=(6, 3), subplot_kw=dict(aspect="equal"))

    tpStatus = []
    data = []
    soma = 0

    for n in unid:
        soma += n.getTtStatus()
        data.append(n.getTtStatus())

    recipe = []

    if tipo == 'valor':
        for n in unid:
            #            texto = str(n.getTtStatus()/1000)+ " " + n.getStatus() + " (mil)"
            texto = f"{n.getTtStatus()/1000:,.0f}".replace(",", ".") + \
                " " + n.getStatus() + " (mil)"
            recipe.append(texto)
    else:
        for n in unid:
            perc = (n.getTtStatus()/soma)*100
#            texto = str(n.getTtStatus()) + " " + n.getStatus() + " (" + str(perc) + "%)"
            texto = f"{n.getTtStatus()} {n.getStatus()} ({perc:.2f}%)"
            recipe.append(texto)

    wedges, texts = ax.pie(data, wedgeprops=dict(width=0.5), startangle=-40)

    bbox_props = dict(boxstyle="square,pad=0.3", fc="w", ec="k", lw=0.72)
    kw = dict(arrowprops=dict(arrowstyle="-"),
              bbox=bbox_props, zorder=0, va="center")

#    for i, p in enumerate(wedges):
#        ang = (p.theta2 - p.theta1)/2. + p.theta1
#        y = np.sin(np.deg2rad(ang))
#        x = np.cos(np.deg2rad(ang))
#        horizontalalignment = {-1: "right", 1: "left"}[int(np.sign(x))]
#        connectionstyle = f"angle,angleA=0,angleB={ang}"
#        kw["arrowprops"].update({"connectionstyle": connectionstyle})
#        ax.annotate(recipe[i], xy=(x, y), xytext=(1.1*np.sign(x), 1.4*y),
#                    horizontalalignment=horizontalalignment, **kw)        # caixa de anotações

    for i, p in enumerate(wedges):
        ang = (p.theta2 - p.theta1)/2. + p.theta1
        y = np.sin(np.deg2rad(ang))
        x = np.cos(np.deg2rad(ang))
        horizontalalignment = {-1: "right", 1: "left"}[int(np.sign(x))]
        connectionstyle = f"angle,angleA=0,angleB={ang}"
        kw["arrowprops"].update({"connectionstyle": connectionstyle})
        # Ajuste dinâmico para evitar sobreposição
        deslocamento_y = 1.0 + (i % 3) * 0.5  # alterna o deslocamento vertical 3
        deslocamento_x = 1.0 + (i % 2) * 0.2  # alterna o deslocamento horizontal 9
        ax.annotate(recipe[i], xy=(x, y), xytext=(deslocamento_x * np.sign(x), deslocamento_y * y),
        horizontalalignment=horizontalalignment, **kw)

#    ax.set_title("Vendas", fontdict={'family': 'serif', 'color': 'black', 'weight': 'bold', 'size': 12}, loc='center')

    grafC = graficoController()

    diretorio = grafC.montaDir(idEmpreend, mesVigencia, anoVigencia)
    grafC.criaDir(diretorio)
    if tipo == 'valor':
        grafNome = os.path.join(diretorio, 'graf_vendas_valor.png')
    else:
        grafNome = os.path.join(diretorio, 'graf_vendas_perc.png')
#    grafNome = diretorio + 'graf_vendas.png'

    if os.path.exists(grafNome):
        os.remove(grafNome)

    plt.savefig(grafNome)  # , bbox_inches='tight')
    plt.close('all')

    return grafNome


@graficos_bp.route('/graf_chaves', methods=['GET'])
@login_required
def graf_chaves():
    # ÍNDICES DE CHAVES

    idEmpreend = IdEmpreend().get()
    mesVigencia = request.args.get("mesVigencia")
    anoVigencia = request.args.get("anoVigencia")

    grafNome = gerar_graf_chaves(idEmpreend, mesVigencia, anoVigencia, 'perc')

    return render_template("chaves_liberacao.html", grafNome=grafNome, version=random.randint(1, 100000))


def gerar_graf_chaves(idEmpreend, mesVigencia, anoVigencia, tipo):
    unidc = unidadeController()
    unid = unidc.consultarUnidadeChaves(idEmpreend, tipo)

    labels = ['Chaves', 'Pré-chaves', 'Pós-chaves']

    if tipo == 'valor':
        perChave = unid.getTtChaves() / 1000 if unid.getTtChaves() > 0 else 0
        perPreChave = unid.getTtPreChaves() / 1000 if unid.getTtPreChaves() > 0 else 0
        perPosChave = unid.getTtPosChaves() / 1000 if unid.getTtPosChaves() > 0 else 0
    else:
        perChave = unid.getTtChaves() / unid.getQtUnidade() * \
            100 if unid.getTtChaves() and unid.getQtUnidade() else 0
        perPreChave = unid.getTtPreChaves() / unid.getQtUnidade() * \
            100 if unid.getTtPreChaves() and unid.getQtUnidade() else 0
        perPosChave = unid.getTtPosChaves() / unid.getQtUnidade() * \
            100 if unid.getTtPosChaves() and unid.getQtUnidade() else 0

    if not perChave and not perPreChave and not perPosChave:
        return ''

    plt.switch_backend('agg')

    sizes = [perChave, perPreChave, perPosChave]

    # Configuração do gráfico de barras
    fig, ax = plt.subplots(figsize=(8, 6))  # Define o tamanho da figura
#    bars = ax.bar(labels, sizes, color=['blue', 'orange', 'green'])
    bars = ax.bar(labels, sizes, color=['blue', 'orange', 'green'], width=0.3)
    # Adiciona rótulos nas barras
    for bar in bars:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width() / 2, height, f'{height:.0f}',
                ha='center', va='bottom', fontsize=12)

    # Configurações do gráfico
#    ax.set_title('Distribuição de Chaves', fontsize=16, fontweight='bold')
    if tipo == 'valor':
        ax.set_ylabel(
            'R$/mil ' + '(' + str(unid.getQtUnidade()) + ' Unid)', fontsize=14)
    else:
        ax.set_ylabel(
            '% ' + '(' + str(unid.getQtUnidade()) + ' Unid)', fontsize=14)

#    ax.set_xlabel('Categorias', fontsize=14)
    ax.tick_params(axis='both', labelsize=12)

    # Remover as linhas superior e direita da caixa
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    grafC = graficoController()

    diretorio = grafC.montaDir(idEmpreend, mesVigencia, anoVigencia)
    grafC.criaDir(diretorio)
    if tipo == 'valor':
        grafNome = os.path.join(diretorio, 'graf_chaves_valor.png')
    else:
        grafNome = os.path.join(diretorio, 'graf_chaves_perc.png')
#    grafNome = diretorio + 'graf_chaves.png'

    if os.path.exists(grafNome):
        os.remove(grafNome)

    plt.savefig(grafNome, bbox_inches='tight')
    plt.close('all')
    return grafNome
