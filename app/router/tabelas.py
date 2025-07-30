
from flask import Blueprint, request, render_template

from controller.empreendimentoController import empreendimentoController
from controller.orcamentoController import orcamentoController
from controller.certidaoController import certidaoController
from controller.garantiaController import garantiaController
from controller.aspectosController import aspectosController
from controller.medicaoController import medicaoController
from controller.graficoController import graficoController
from controller.medicaoController import medicaoController
from controller.contaController import contaController
from controller.torreController import torreController
from controller.geralController import geralController
from controller.notaController import notaController
from utils.security import login_required
from utils.CtrlSessao import IdEmpreend
from matplotlib import pyplot as plt
import matplotlib.pyplot as plt
from datetime import datetime
import random
import os

tabelas_bp = Blueprint('tabelas', __name__)

tam_tit = 40
tam_dado = 12

medCtrl = medicaoController()


@tabelas_bp.route('/tab_notas')
@login_required
def tab_notas():
    idEmpreend = IdEmpreend().get()
    dtCarga = request.args.get("dtCarga")
    mesVigencia = str(request.args.get('mesV')).zfill(2)
    anoVigencia = str(request.args.get('anoV'))
    codBanco = int(request.args.get('codBanco')
                   ) if request.args.get('codBanco') else None

    notC = notaController()
    notS = notC.consultarNotaPelaData(idEmpreend, dtCarga)

    grafNome = gerar_tab_notas(
        idEmpreend,
        mesVigencia,
        anoVigencia,
        notS,
        codBanco
    )

    return render_template("nota_liberacao.html", grafNome=grafNome, version=random.randint(1, 100000))


def gerar_tab_notas(idEmpreend, mesVigencia, anoVigencia, notS, codBanco):
    geral = geralController()

    plt.switch_backend('agg')

    fig, ax = plt.subplots(1, 1)

    data = []
    somaVlNotaFiscal = 0
    somaVlEstoque = 0

    for n in notS:
        dd = []
        dd.append(n.getProduto())
        somaVlNotaFiscal += n.getVlNotaFiscal()
        dd.append(geral.formataNumero(n.getVlNotaFiscal()))
        somaVlEstoque += n.getVlEstoque()
        dd.append(geral.formataNumero(n.getVlEstoque()))
        data.append(dd)

    # incluindo a linha de totais
    dd = []
    mesEstoque = str(int(mesVigencia) - 1).zfill(2)
    dd.append('Estoque em ' + mesEstoque + '/' + anoVigencia)
    dd.append(' ')
    dd.append(geral.formataNumero(somaVlEstoque))
    data.append(dd)

    column_labels = ["Produtos", "Valor da NF", "Estoque"]

    # Definir tamanho das células
    cell_width = 2.5  # Largura de cada célula
    cell_height = 0.2  # Altura de cada célula
    # Calcular o tamanho total da figura com base no número de células
    num_rows = len(data) + 1  # +1 para incluir os cabeçalhos
    num_cols = len(column_labels)
    fig_width = num_cols * cell_width
    fig_height = num_rows * cell_height
    # Criar a figura com o tamanho calculado
    fig, ax = plt.subplots(figsize=(fig_width, fig_height))

    # Remove os eixos do gráfico, deixando apenas a tabela visível.
    ax.axis("off")
    tabela = ax.table(cellText=data, colLabels=column_labels, loc="center")
    # Desativa o ajuste automático do tamanho da fonte. Isso permite que você defina manualmente o tamanho da fonte.
    tabela.auto_set_font_size(False)
    tabela.set_fontsize(8)
#    tabela.scale(2,1)

#   Ajustando o tamanho das colunas
    for x in range(0, num_cols):
        tabela.auto_set_column_width(x)

    if codBanco == 77:  # Banco Inter
        corCabecalho = (0.945, 0.662, 0.513)  # Cor laranja
    else:
        corCabecalho = "lightblue"

#   colocando cor de fundo no cabeçalho
    for (row, col), cell in tabela.get_celld().items():
        if row == 0 or row == num_rows-1:
            if codBanco == 77:  # Banco Inter
                cell.set_facecolor(corCabecalho)
            else:
                cell.set_facecolor("lightblue")

            if row == 0:
                # Alinhar 1ª linha no centro
                cell.set_text_props(ha='center', va='center')
            else:
                if col == 0:
                    # Alinhar coluna 1 da ultima linha à esquerda
                    cell.set_text_props(ha='left', va='center')
        else:  # Demais itens da tabela
            if col == 0:
                # Alinhar à esquerda
                cell.set_text_props(ha='left', va='center')

    grafC = graficoController()

    diretorio = grafC.montaDir(idEmpreend, mesVigencia, anoVigencia)
    grafC.criaDir(diretorio)
    grafNome = os.path.join(diretorio, 'tab_notas.png')

    if os.path.exists(grafNome):
        os.remove(grafNome)

    plt.savefig(grafNome)

    return grafNome


@tabelas_bp.route('/tab_conta')
@login_required
def tab_conta_corrente():
    idEmpreend = IdEmpreend().get()
    dtCarga = request.args.get("dtCarga")
    mesVigencia = str(request.args.get('mesV')).zfill(2)
    anoVigencia = str(request.args.get('anoV'))
    codBanco = int(request.args.get('codBanco')
                   ) if request.args.get('codBanco') else None

    conC = contaController()
    conS = conC.consultarContaPelaCarga(idEmpreend, dtCarga)

    grafNome = gerar_tab_conta_corrente(
        idEmpreend,
        mesVigencia,
        anoVigencia,
        conS,
        codBanco
    )
    return render_template("conta_liberacao.html", grafNome=grafNome, version=random.randint(1, 100000))


def gerar_tab_conta_corrente(idEmpreend, mesVigencia, anoVigencia, conS, codBanco):
    geral = geralController()

    plt.switch_backend('agg')

    fig, ax = plt.subplots(1, 1)
    data = []

    for c in conS:
        dd = []
        periodo = geral.formatammmaa(c.getMesVigencia(), c.getAnoVigencia())
        dd.append(periodo)
        dd.append(geral.formataNumero(c.getVlLiberacao()))
#        dd.append(geral.formataNumero(c.getVlMaterialEstoque()))
        dd.append(geral.formataNumero(c.getVlAporteConstrutora()))
        dd.append(geral.formataNumero(c.getVlReceitaRecebiveis()))
        dd.append(geral.formataNumero(c.getVlPagtoObra()))
        dd.append(geral.formataNumero(c.getVlPagtoRh()))
        dd.append(geral.formataNumero(c.getVlDiferenca()))
        dd.append(geral.formataNumero(c.getVlSaldo()))
        data.append(dd)

#    column_labels = ["Mês", "Liberação P.E.", "Mat. em estoque", "Aporte construtora", "Receita revebiveis", "Pagto obra", "Pagto RH", "Dif. encontradas", "Saldo"]
    column_labels = ["Mês", "Liberação P.E.", "Aporte construtora",
                     "Receita revebiveis", "Pagto obra", "Pagto RH", "Dif. encontradas", "Saldo"]

    # Definir tamanho das células
    cell_width = 1.0   # Largura de cada célula
    cell_height = 0.2  # Altura de cada célula
    # Calcular o tamanho total da figura com base no número de células
    num_rows = len(data) + 1  # +1 para incluir os cabeçalhos
    num_cols = len(column_labels)
    fig_width = num_cols * cell_width
    fig_height = num_rows * cell_height
    # Criar a figura com o tamanho calculado
    fig, ax = plt.subplots(figsize=(fig_width, fig_height))

    # Remove os eixos do gráfico, deixando apenas a tabela visível.
    ax.axis("off")
    tabela = ax.table(cellText=data, colLabels=column_labels, loc="center")
    # Desativa o ajuste automático do tamanho da fonte. Isso permite que você defina manualmente o tamanho da fonte.
    tabela.auto_set_font_size(False)
    tabela.set_fontsize(8)
#    tabela.scale(2,1)

#   Ajustando o tamanho das colunas
    for x in range(0, num_cols):
        tabela.auto_set_column_width(x)

    if codBanco == 77:  # Banco Inter
        corCabecalho = (0.945, 0.662, 0.513)  # Cor laranja
    else:
        corCabecalho = "lightblue"

#   colocando cor de fundo no cabeçalho
    for (row, col), cell in tabela.get_celld().items():
        if row == 0:
            cell.set_facecolor(corCabecalho)  # Cor laranja
            cell.set_text_props(ha='center', va='center')  # Alinhar no centro
        else:  # Demais itens da tabela
            cell.set_text_props(ha='right', va='center')  # Alinhar à esquerda

    grafC = graficoController()

    diretorio = grafC.montaDir(idEmpreend, mesVigencia, anoVigencia)
    grafC.criaDir(diretorio)
    grafNome = os.path.join(diretorio, 'tab_conta_corrente.png')

    if os.path.exists(grafNome):
        os.remove(grafNome)

    plt.savefig(grafNome)
    plt.close('all')
    return grafNome


@tabelas_bp.route('/tab_garantias_geral')
@login_required
def tab_garantias_geral():

    idEmpreend = IdEmpreend().get()
    mesVigencia = request.args.get("mesVigencia")
    anoVigencia = request.args.get("anoVigencia")
    codBanco = int(request.args.get("codBanco")
                   ) if request.args.get("codBanco") else None

    grafNome = gerar_tab_garantias_geral(idEmpreend, mesVigencia, anoVigencia)

    return render_template("garantia_liberacao.html", grafNome=grafNome, version=random.randint(1, 100000))


def gerar_tab_garantias_geral(idEmpreend, mesVigencia, anoVigencia, codBanco):
    ponC = garantiaController()
    ponS = ponC.consultargarantiaatual(idEmpreend, 'Geral')

    if not ponS:
        return ''

    plt.switch_backend('agg')

    fig, ax = plt.subplots(1, 1)

    data = []

    for p in ponS:
        dd = []
        dd.append(p.documento)
        dd.append(p.status)
        dd.append(p.observacao)
        data.append(dd)

    column_labels = ["Histórico", "Status", "Obs"]

    # Definir tamanho das células
    cell_width = 2.2  # Largura de cada célula
    cell_height = 0.2  # Altura de cada célula
    # Calcular o tamanho total da figura com base no número de células
    num_rows = len(data) + 1  # +1 para incluir os cabeçalhos
    num_cols = len(column_labels)
    fig_width = num_cols * cell_width
    fig_height = num_rows * cell_height
    # Criar a figura com o tamanho calculado
    fig, ax = plt.subplots(figsize=(fig_width, fig_height))

    # Remove os eixos do gráfico, deixando apenas a tabela visível.
    ax.axis("off")
    tabela = ax.table(cellText=data, colLabels=column_labels, loc="center")
    # Desativa o ajuste automático do tamanho da fonte. Isso permite que você defina manualmente o tamanho da fonte.
    tabela.auto_set_font_size(False)
    tabela.set_fontsize(8)
#    tabela.scale(2,1)

#   Ajustando o tamanho das colunas
    for x in range(0, num_cols):
        tabela.auto_set_column_width(x)

    if codBanco == 77:  # Banco Inter
        corCabecalho = (0.945, 0.662, 0.513)  # Cor laranja
    else:
        corCabecalho = "lightblue"

#   colocando cor de fundo no cabeçalho
    for (row, col), cell in tabela.get_celld().items():
        # Define a cor da borda como "none" (sem borda)
        cell.set_edgecolor("none")
        if row == 0:
            cell.set_facecolor(corCabecalho)
            cell.set_text_props(ha='center', va='center')  # Alinhar no centro
        else:  # Demais itens da tabela
            if col == 1:
                cell_text = cell.get_text().get_text()  # Obtém o texto da célula
                if "Atenção" in cell_text:  # Verifica se contém a palavra "Atenção"
                    # Alinhar à esquerda
                    cell.set_text_props(ha='left', va='center', color='red')
                elif "Verificar" in cell_text:  # Verifica se contém a palavra "Atenção"
                    # Alinhar à esquerda
                    cell.set_text_props(ha='left', va='center', color='orange')
                else:
                    # Alinhar à esquerda
                    cell.set_text_props(ha='left', va='center', color='green')
            else:
                # Alinhar no centro
                cell.set_text_props(ha='left', va='center')

    grafC = graficoController()

    diretorio = grafC.montaDir(idEmpreend, mesVigencia, anoVigencia)
    grafC.criaDir(diretorio)
    grafNome = os.path.join(diretorio, 'tab_garantias_geral.png')

    if os.path.exists(grafNome):
        os.remove(grafNome)

    plt.savefig(grafNome)
    plt.close('all')
    return grafNome


@tabelas_bp.route('/tab_garantias_obra')
@login_required
def tab_garantias_obra():
    idEmpreend = IdEmpreend().get()
    mesVigencia = request.args.get("mesVigencia")
    anoVigencia = request.args.get("anoVigencia")
    codBanco = int(request.args.get('codBanco')
                   ) if request.args.get('codBanco') else None

    grafNome = gerar_tab_garantias_obra(idEmpreend, mesVigencia, anoVigencia)

    return render_template("garantia_liberacao.html", grafNome=grafNome, version=random.randint(1, 100000))


def gerar_tab_garantias_obra(idEmpreend, mesVigencia, anoVigencia, codBanco):
    ponC = garantiaController()
    ponS = ponC.consultargarantiaatual(idEmpreend, 'Obra')

    if not ponS:
        return ''

    fig, ax = plt.subplots(1, 1)
    data = []

    for p in ponS:
        dd = []
        dd.append(p.documento)
        dd.append(p.status)
        dd.append(p.observacao)
        data.append(dd)

    column_labels = ["Histórico", "Status", "Obs"]

    # Definir tamanho das células
    cell_width = 2.35  # Largura de cada célula
    cell_height = 0.2  # Altura de cada célula
    # Calcular o tamanho total da figura com base no número de células
    num_rows = len(data) + 1  # +1 para incluir os cabeçalhos
    num_cols = len(column_labels)
    fig_width = num_cols * cell_width
    fig_height = num_rows * cell_height
    # Criar a figura com o tamanho calculado
    fig, ax = plt.subplots(figsize=(fig_width, fig_height))

    # Remove os eixos do gráfico, deixando apenas a tabela visível.
    ax.axis("off")
    tabela = ax.table(cellText=data, colLabels=column_labels, loc="center")
    # Desativa o ajuste automático do tamanho da fonte. Isso permite que você defina manualmente o tamanho da fonte.
    tabela.auto_set_font_size(False)
    tabela.set_fontsize(8)
#    tabela.scale(2,1)

#   Ajustando o tamanho das colunas
    for x in range(0, num_cols):
        tabela.auto_set_column_width(x)

    if codBanco == 77:  # Banco Inter
        corCabecalho = (0.945, 0.662, 0.513)  # Cor laranja
    else:
        corCabecalho = "lightblue"

#   colocando cor de fundo no cabeçalho
    for (row, col), cell in tabela.get_celld().items():
        # Define a cor da borda como "none" (sem borda)
        cell.set_edgecolor("none")
        if row == 0:
            cell.set_facecolor(corCabecalho)
            cell.set_text_props(ha='center', va='center')  # Alinhar no centro
        else:  # Demais itens da tabela
            if col == 1:
                cell_text = cell.get_text().get_text()  # Obtém o texto da célula
                if "Atenção" in cell_text:  # Verifica se contém a palavra "Atenção"
                    # Alinhar à esquerda
                    cell.set_text_props(ha='left', va='center', color='red')
                elif "Verificar" in cell_text:  # Verifica se contém a palavra "Atenção"
                    # Alinhar à esquerda
                    cell.set_text_props(ha='left', va='center', color='orange')
                else:
                    # Alinhar à esquerda
                    cell.set_text_props(ha='left', va='center', color='green')
            else:
                # Alinhar no centro
                cell.set_text_props(ha='left', va='center')

    grafC = graficoController()

    diretorio = grafC.montaDir(idEmpreend, mesVigencia, anoVigencia)
    grafC.criaDir(diretorio)
    grafNome = os.path.join(diretorio, 'tab_garantias_obra.png')

    if os.path.exists(grafNome):
        os.remove(grafNome)

    plt.savefig(grafNome)
    plt.close('all')
    return grafNome


@tabelas_bp.route('/tab_certidoes')
@login_required
def tab_certidoes():

    idEmpreend = IdEmpreend().get()
    mesVigencia = request.args.get("mesVigencia")
    anoVigencia = request.args.get("anoVigencia")
    codBanco = int(request.args.get('codBanco')
                   ) if request.args.get('codBanco') else None

    grafNome = gerar_tab_certidoes(idEmpreend, mesVigencia, anoVigencia)

    return render_template("certidoes_liberacao.html", grafNome=grafNome, version=random.randint(1, 100000))


def gerar_tab_certidoes(idEmpreend, mes, ano, codBanco):
    certC = certidaoController()
    certS = certC.consultarCertidoesGraf(idEmpreend)

    if not certS:
        return ''

    plt.switch_backend('agg')

    fig, ax = plt.subplots(1, 1)
    print(certS)
    print(certS.getEstadualStatus())

    data = []
    a = ['Estadual', certS.getEstadualStatus(), certS.getEstadualValidade()]
    data.append(a)
    b = ['FGTS', certS.getFgtsStatus(), certS.getEstadualValidade()]
    data.append(b)
    c = ['Municipal', certS.getMunicipalStatus(), certS.getMunicipalValidade()]
    data.append(c)
    d = ['SRF/INSS', certS.getSrfInssStatus(), certS.getSrfInssValidade()]
    data.append(d)
    e = ['Trabalhista', certS.getTrabalhistaStatus(), certS.getTrabalhistaValidade()]
    data.append(e)

    column_labels = ["Doc. Fiscal", "Status", "Validade"]

    # Definir tamanho das células
    cell_width = 0.8  # Largura de cada célula
    cell_height = 0.2  # Altura de cada célula
    # Calcular o tamanho total da figura com base no número de células
    num_rows = len(data) + 1  # +1 para incluir os cabeçalhos
    num_cols = len(column_labels)
    fig_width = num_cols * cell_width
    fig_height = num_rows * cell_height
    # Criar a figura com o tamanho calculado
    fig, ax = plt.subplots(figsize=(fig_width, fig_height))

    # Remove os eixos do gráfico, deixando apenas a tabela visível.
    ax.axis("off")
    tabela = ax.table(cellText=data, colLabels=column_labels, loc="center")
    # Desativa o ajuste automático do tamanho da fonte. Isso permite que você defina manualmente o tamanho da fonte.
    tabela.auto_set_font_size(False)
    tabela.set_fontsize(8)
#    tabela.scale(2,1)

#   Ajustando o tamanho das colunas
    for x in range(0, num_cols):
        tabela.auto_set_column_width(x)

    if codBanco == 77:  # Banco Inter
        corCabecalho = (0.945, 0.662, 0.513)  # Cor laranja
    else:
        corCabecalho = "lightblue"

#   colocando cor de fundo no cabeçalho
    for (row, col), cell in tabela.get_celld().items():
        # Define a cor da borda como "none" (sem borda)
        cell.set_edgecolor("none")
        if row == 0:
            cell.set_facecolor(corCabecalho)  # Cor laranja
            cell.set_text_props(ha='center', va='center')  # Alinhar no centro
        else:  # Demais itens da tabela
            if col == 1:
                cell_text = cell.get_text().get_text()  # Obtém o texto da célula
                if "Positiva" in cell_text:  # Verifica se contém a palavra "Atenção"
                    # Alinhar à esquerda
                    cell.set_text_props(ha='left', va='center', color='red')
                elif "Pendente" in cell_text:  # Verifica se contém a palavra "Atenção"
                    # Alinhar à esquerda
                    cell.set_text_props(ha='left', va='center', color='orange')
                else:
                    # Alinhar à esquerda
                    cell.set_text_props(ha='left', va='center', color='green')
            else:
                # Alinhar no centro
                cell.set_text_props(ha='left', va='center')

    grafC = graficoController()

    diretorio = grafC.montaDir(idEmpreend, mes, ano)
    grafC.criaDir(diretorio)
    grafNome = os.path.join(diretorio, 'tab_certidoes.png')

    if os.path.exists(grafNome):
        os.remove(grafNome)

    plt.savefig(grafNome)
    plt.close('all')
    return grafNome


@tabelas_bp.route('/tab_acomp_financeiro')
@login_required
def tab_acomp_financeiro():
    idEmpreend = IdEmpreend().get()
    mesVigencia = request.args.get("mesVigencia")
    anoVigencia = request.args.get("anoVigencia")

    medC = orcamentoController()
    medS = medC.consultarOrcamentoPelaVigencia(
        idEmpreend, mesVigencia, anoVigencia)
    notC = notaController()
    notS = notC.consultarNotaPelaVigencia(idEmpreend, mesVigencia, anoVigencia)

    grafNome = gerar_tab_notas(idEmpreend, mesVigencia, anoVigencia, notS)
    grafNome = gerar_tab_acomp_financeiro(
        idEmpreend, mesVigencia, anoVigencia, medS, notS)

    return render_template("financeiro_liberacao.html", grafNome=grafNome, version=random.randint(1, 100000))


def gerar_tab_acomp_financeiro(idEmpreend, mesVigencia, anoVigencia, medS, notS):
    geral = geralController()

    plt.switch_backend('agg')

    fig, ax = plt.subplots(1, 1)

    data = []
    somaOrcadoValor = 0
    somaFisicoValor = 0
#    somaFisicoSaldo = 0
    somaFinanceiroValor = 0
#    somaFinanceiroSaldo = 0

    for m in medS:
        somaOrcadoValor += 0 if m.getOrcadoValor() is None else m.getOrcadoValor()
        somaFisicoValor += 0 if m.getFisicoValor() is None else m.getFisicoValor()
#        somaFisicoSaldo += 0 if m.getFisicoSaldo() is None else m.getFisicoSaldo()
        somaFinanceiroValor += 0 if m.getFinanceiroValor() is None else m.getFinanceiroValor()
#        somaFinanceiroSaldo += 0 if m.getFinanceiroSaldo() is None else m.getFinanceiroSaldo()

    # incluindo a linha de totais
    somaFisicoPercentual = somaFisicoValor/somaOrcadoValor*100
    somaFinanceiroPercentual = somaFinanceiroValor/somaOrcadoValor*100

# 'Aditamento'

#    somaVlNotaFiscal = 0
    somaVlEstoque = 0

    for n in notS:
        #        somaVlNotaFiscal += n.getVlNotaFiscal()
        somaVlEstoque += n.getVlEstoque()

    dd = ['Físico executado', geral.formataPerc(
        somaFisicoPercentual, 0), geral.formataNumero(somaFisicoValor, 'R$')]
    data.append(dd)
    dd = ['Financeiro liberado', geral.formataPerc(
        somaFinanceiroPercentual, 0), geral.formataNumero(somaFinanceiroValor, 'R$')]
    data.append(dd)
    if somaVlEstoque != 0:
        dd = ['Estoque (material)', ' ',
              geral.formataNumero(somaVlEstoque, 'R$')]
        data.append(dd)

#    for m in finS:
#        dd = []
#        dd.append(m.getHistorico())
#        dd.append(geral.formataPerc(m.getPercFinanceiro(), 0))
#        dd.append(geral.formataNumero(m.getVlFinanceiro(), 'R$'))
#        data.append(dd)

    column_labels = ["                            ",
                     "         ", "                "]

    # Definir tamanho das células
    cell_width = 1.2   # Largura de cada célula
    cell_height = 0.2  # Altura de cada célula
    # Calcular o tamanho total da figura com base no número de células
    num_rows = len(data) + 1  # +1 para incluir os cabeçalhos
    num_cols = len(column_labels)
    fig_width = num_cols * cell_width
    fig_height = num_rows * cell_height
    # Criar a figura com o tamanho calculado
    fig, ax = plt.subplots(figsize=(fig_width, fig_height))

    # Remove os eixos do gráfico, deixando apenas a tabela visível.
    ax.axis("off")
    tabela = ax.table(cellText=data, colLabels=column_labels, loc="center")
    # Desativa o ajuste automático do tamanho da fonte. Isso permite que você defina manualmente o tamanho da fonte.
    tabela.auto_set_font_size(False)
    tabela.set_fontsize(8)
#    tabela.scale(2,1)

#   Ajustando o tamanho das colunas
    for x in range(0, num_cols):
        tabela.auto_set_column_width(x)
#   colocando cor de fundo no cabeçalho
    for (row, col), cell in tabela.get_celld().items():
        # Define a cor da borda como "none" (sem borda)
        cell.set_edgecolor("none")
#        if row == 0:
#            cell.set_facecolor("lightblue")
#            cell.set_text_props(ha='center', va='center')  # Alinhar no centro
#        else:  # Demais itens da tabela
        cell.set_text_props(ha='left', va='center')  # Alinhar à esquerda

    grafC = graficoController()

    diretorio = grafC.montaDir(idEmpreend, mesVigencia, anoVigencia)
    grafC.criaDir(diretorio)
    grafNome = os.path.join(diretorio, 'tab_acomp_financeiro.png')

    if os.path.exists(grafNome):
        os.remove(grafNome)

    plt.savefig(grafNome)

    plt.close('all')
    return grafNome


@tabelas_bp.route('/tab_medicoes')
@login_required
def tab_medicoes():

    idEmpreend = IdEmpreend().get()
    mesVigencia = request.args.get("mesVigencia")
    anoVigencia = request.args.get("anoVigencia")
    mesInicio = request.args.get("mesInicio")
    anoInicio = request.args.get("anoInicio")
    mesFinal = request.args.get("mesFinal")
    anoFinal = request.args.get("anoFinal")
    codBanco = int(request.args.get('codBanco')
                   ) if request.args.get('codBanco') else None

    grafNome = gerar_tab_medicoes(
        idEmpreend,
        mesVigencia,
        anoVigencia,
        mesInicio,
        anoInicio,
        mesFinal,
        anoFinal,
        codBanco
    )

    return render_template("medicoes_liberacao.html", grafNome=grafNome, version=random.randint(1, 100000))


def gerar_tab_medicoes(idEmpreend, mesVigencia, anoVigencia, mesInicio, anoInicio, mesFinal, anoFinal, codBanco):
    geral = geralController()
    preC = medicaoController()

#    preS = preC.consultarMedicoes(idEmpreend)

    preS = preC.consultarMedicoesPorPeriodo(
        idEmpreend, mesInicio, anoInicio, mesFinal, anoFinal)

    if not preS:
        return ''

    plt.switch_backend('agg')

    fig, ax = plt.subplots(1, 1)

    data = []

    for p in preS:
        dd = []
        dd.append(str(p.getNrMedicao()))
        periodo = geral.formatammmaa(p.getMesVigencia(), p.getAnoVigencia())
        dd.append(periodo)
        dd.append(geral.formataNumero(p.getPercPrevistoAcumulado()))
        dd.append(geral.formataNumero(p.getPercRealizadoAcumulado()))
        if p.getPercRealizadoAcumulado() != 0:
            dd.append(geral.formataNumero(p.getPercDiferenca()))
#            dd.append(geral.formataNumero(
#                p.getPercRealizadoAcumulado()-p.getPercPrevistoAcumulado()))
        else:
            dd.append('')
        dd.append(geral.formataNumero(p.getPercPrevistoPeriodo()))
        data.append(dd)

#    print (data)
    column_labels = ["Medição", "Período", "Previsto acum.",
                     "Realizado acum.", "Diferença", "Previsto período"]

    # Definir tamanho das células
    cell_width = 1.2  # Largura de cada célula
    cell_height = 0.2  # Altura de cada célula
    # Calcular o tamanho total da figura com base no número de células
    num_rows = len(data) + 1  # +1 para incluir os cabeçalhos
    num_cols = len(column_labels)
    fig_width = num_cols * cell_width
    fig_height = num_rows * cell_height
#    print ('===============>>>>', num_rows, num_cols)
    # Criar a figura com o tamanho calculado
    fig, ax = plt.subplots(figsize=(fig_width, fig_height))

    # Remove os eixos do gráfico, deixando apenas a tabela visível.
    ax.axis("off")
    tabela = ax.table(cellText=data, colLabels=column_labels, loc="center")
    # Desativa o ajuste automático do tamanho da fonte. Isso permite que você defina manualmente o tamanho da fonte.
    tabela.auto_set_font_size(False)
    tabela.set_fontsize(8)
#    tabela.scale(2,1)

#   Ajustando o tamanho das colunas
    for x in range(0, num_cols):
        tabela.auto_set_column_width(x)

    if codBanco == 77:  # Banco Inter
        corCabecalho = (0.945, 0.662, 0.513)  # Cor laranja
    else:
        corCabecalho = "lightblue"

#   colocando cor de fundo no cabeçalho
    for (row, col), cell in tabela.get_celld().items():
        if row == 0:
            cell.set_facecolor(corCabecalho)

    grafC = graficoController()

    diretorio = grafC.montaDir(idEmpreend, mesVigencia, anoVigencia)
    grafC.criaDir(diretorio)
    grafNome = os.path.join(diretorio, 'tab_medicoes.png')

    if os.path.exists(grafNome):
        os.remove(grafNome)

    plt.savefig(grafNome)

    return grafNome


@tabelas_bp.route('/tab_orcamento_liberacao')
@login_required
def tab_orcamento_liberacao():
    idEmpreend = IdEmpreend().get()
    dtCarga = request.args.get("dtCarga")
    mes = request.args.get("mesV")
    ano = request.args.get("anoV")
    codBanco = int(request.args.get('codBanco')
                   ) if request.args.get('codBanco') else None

    medC = orcamentoController()
    medS = medC.consultarOrcamentoPelaData(idEmpreend, dtCarga)
    grafNome = gerar_tab_orcamento_liberacao(
        idEmpreend, mes, ano, medS, codBanco)
    return render_template("orcamento_liberacao.html", grafNome=grafNome, version=random.randint(1, 100000))


def gerar_tab_orcamento_liberacao(idEmpreend, mes, ano, medS, codBanco):
    geral = geralController()

    plt.switch_backend('agg')

    fig, ax = plt.subplots(1, 1)

    data = []
    somaOrcadoValor = 0
    somaFisicoValor = 0
    somaFisicoSaldo = 0
    somaFinanceiroValor = 0
    somaFinanceiroSaldo = 0

    for m in medS:
        dd = []
        dd.append(m.getItem())
        somaOrcadoValor += 0 if m.getOrcadoValor() is None else m.getOrcadoValor()
        dd.append(geral.formataNumero(m.getOrcadoValor()))
        dd.append(' ')
        somaFisicoValor += 0 if m.getFisicoValor() is None else m.getFisicoValor()
        dd.append(geral.formataNumero(m.getFisicoValor()))
        dd.append(geral.formataNumero(m.getFisicoPercentual()))
        somaFisicoSaldo += 0 if m.getFisicoSaldo() is None else m.getFisicoSaldo()
        dd.append(geral.formataNumero(m.getFisicoSaldo()))
        dd.append(' ')
        somaFinanceiroValor += 0 if m.getFinanceiroValor() is None else m.getFinanceiroValor()
        dd.append(geral.formataNumero(m.getFinanceiroValor()))
        dd.append(geral.formataNumero(m.getFinanceiroPercentual()))
        somaFinanceiroSaldo += 0 if m.getFinanceiroSaldo() is None else m.getFinanceiroSaldo()
        dd.append(geral.formataNumero(m.getFinanceiroSaldo()))
        data.append(dd)

    # incluindo a linha de totais
    dd = []
    dd.append('Total do Orçamento')
    dd.append(geral.formataNumero(somaOrcadoValor))
    dd.append(' ')
    dd.append(geral.formataNumero(somaFisicoValor))
    somaFisicoPercentual = somaFisicoValor/somaOrcadoValor*100
    dd.append(geral.formataNumero(somaFisicoPercentual))
    dd.append(geral.formataNumero(somaFisicoSaldo))
    dd.append(' ')
    dd.append(geral.formataNumero(somaFinanceiroValor))
    somaFinanceiroPercentual = somaFinanceiroValor/somaOrcadoValor*100
    dd.append(geral.formataNumero(somaFinanceiroPercentual))
    dd.append(geral.formataNumero(somaFinanceiroSaldo))
    data.append(dd)

    column_labels = ['Descrição', 'Orçamento (R$)', ' ', 'Medição física acumulado (R$)',
                     '(%)', 'Saldo (R$)', ' ', 'Liberação financ acumulado (R$)', '(%)', 'Saldo (R$)']

    # Definir tamanho das células
    cell_width = 1.2  # Largura de cada célula
    cell_height = 0.2  # Altura de cada célula
    # Calcular o tamanho total da figura com base no número de células
    num_rows = len(data) + 1  # +1 para incluir os cabeçalhos
    num_cols = len(column_labels)

    fig_width = num_cols * cell_width
    fig_height = num_rows * cell_height
    # Criar a figura com o tamanho calculado
    fig, ax = plt.subplots(figsize=(fig_width, fig_height))

    # Remove os eixos do gráfico, deixando apenas a tabela visível.
    ax.axis("off")
    tabela = ax.table(cellText=data, colLabels=column_labels, loc="center")
    # Desativa o ajuste automático do tamanho da fonte. Isso permite que você defina manualmente o tamanho da fonte.
    tabela.auto_set_font_size(False)
    tabela.set_fontsize(8)
#    tabela.scale(2,1)

#   Ajustando o tamanho das colunas
    for x in range(0, num_cols):
        tabela.auto_set_column_width(x)

    if codBanco == 77:  # Banco Inter
        corCabecalho = (0.945, 0.662, 0.513)  # Cor laranja
    else:
        corCabecalho = "lightblue"

    for (row, col), cell in tabela.get_celld().items():
        if row == 0 or row == num_rows-1:     # pinta a 1ª 1 ultima linhas
            cell.set_facecolor(corCabecalho)
        if col == 2 or col == 6:                     # pinta as colunas de divisão
            cell.set_facecolor(corCabecalho)
        if row > 0 and col == 0:
            cell.set_text_props(ha='left', va='center')  # Alinhar à esquerda

    grafC = graficoController()

    diretorio = grafC.montaDir(idEmpreend, mes, ano)
    grafC.criaDir(diretorio)
    grafNome = os.path.join(diretorio, 'tab_orcamento_liberacao.png')

    if os.path.exists(grafNome):
        os.remove(grafNome)

    plt.savefig(grafNome)
    plt.close('all')
    return grafNome


@tabelas_bp.route('/tab_empreend_capa')
@login_required
def tab_empreend_capa():
    idEmpreend = IdEmpreend().get()
    mes = request.args.get("mesV")
    ano = request.args.get("anoV")
    grafNome = gerar_tab_empreend_capa(idEmpreend, mes, ano)
    return render_template("orcamento_liberacao.html", grafNome=grafNome, version=random.randint(1, 100000))


def gerar_tab_empreend_capa(idEmpreend, mes, ano):
    empCtrl = empreendimentoController()
    emp = empCtrl.consultarEmpreendimentoPeloId(idEmpreend)
    fig, ax = plt.subplots(1, 1)
    medAtual = medCtrl.consultarMedicaoAtual(idEmpreend)
    medAnterior = None
    dataAtual = (medAtual.getDataMedicao()
                 if medAtual and medAtual.getDataMedicao() is not None else datetime.now()).strftime("%d/%m/%Y")

    if medAtual:
        medAnterior = medCtrl.consultarMedicaoAnteriorPeloId(
            medAtual.getIdEmpreend(),
            medAtual.getIdMedicao()
        )

    if medAnterior is None or medAnterior.getDataMedicao() is None:
        periodo = f'De -- até {dataAtual}'
    else:
        periodo = f'De {medAnterior.getDataMedicao().strftime("%d/%m/%Y")} até {dataAtual}'

    data = [
        ['Incorporação         ', emp.getNmEmpreend()],
        ['Construção           ', emp.getNmConstrutor()],
        ['Empreendimento       ', emp.getNmEmpreend()],
        ['Endereço da obra     ', emp.getEnderecoCompleto()],
        ['Data da medição      ', dataAtual],
        ['Período da medição   ', periodo],
        ['Etapa do cronograma  ', medAtual.getNrMedicao() if medAtual else '1ª' + ' Etapa']
    ]

    column_labels = ['                     ', '                           ']

    # Definir tamanho das células
    cell_width = 6.0   # Largura de cada célula
    cell_height = 0.4  # Altura de cada célula
    # Calcular o tamanho total da figura com base no número de células
    num_rows = len(data) + 1  # +1 para incluir os cabeçalhos
    num_cols = len(column_labels)
    fig_width = num_cols * cell_width
    fig_height = num_rows * cell_height
    # Criar a figura com o tamanho calculado
    fig, ax = plt.subplots(figsize=(fig_width, fig_height))

    # Remove os eixos do gráfico, deixando apenas a tabela visível.
    ax.axis("off")
    tabela = ax.table(cellText=data, colLabels=column_labels, loc="center")
    # Desativa o ajuste automático do tamanho da fonte. Isso permite que você defina manualmente o tamanho da fonte.
    tabela.auto_set_font_size(False)
    tabela.set_fontsize(14)
    # Aumenta o espaçamento entre linhas (exemplo: 2.0 dobra o espaçamento)
    tabela.scale(1, 2.0)
  #    tabela.scale(2,1)

  #   Ajustando o tamanho das colunas
    for x in range(0, num_cols):
        tabela.auto_set_column_width(x)
  #   colocando cor de fundo no cabeçalho
    for (row, col), cell in tabela.get_celld().items():
        # Define a cor da borda como "none" (sem borda)
        cell.set_edgecolor("none")
        cell.set_text_props(ha='left', va='center')  # Alinhar à esquerda

    grafC = graficoController()

    diretorio = grafC.montaDir(idEmpreend, mes, ano)
    grafC.criaDir(diretorio)
    grafNome = os.path.join(diretorio, 'tab_empreend_capa.png')

    plt.savefig(grafNome)

    plt.close('all')
    return grafNome


@tabelas_bp.route('/gerar_tab_prazo_inter', methods=['GET'])
@login_required
def tab_prazo_inter():

    idEmpreend = IdEmpreend().get()
    mes = request.args.get("mesV")
    ano = request.args.get("anoV")
    grafNome = gerar_tab_prazo_inter(idEmpreend, mes, ano)
    return render_template("orcamento_liberacao.html", grafNome=grafNome, version=random.randint(1, 100000))


def centraliza_texto(text: str, tamanho: int = 37) -> str:
    lent = len(text)
    dif = tamanho - lent
    tam = round(dif / 2)
    return text.rjust(tam + lent).ljust(tamanho)


def exibicao_porcent(texto: float) -> str:
    return f"{str(texto).replace('.', ',')}%"


def gerar_tab_prazo_inter(idEmpreend, mes, ano, codBanco):
    med = medCtrl.consultarMedicaoAtual(idEmpreend)

    if not med:
        return ''

    fig, ax = plt.subplots(1, 1)

    data = [
        [
            'Evolução do mês'.rjust(21).ljust(37),
            centraliza_texto(exibicao_porcent(med.getPercPrevistoPeriodo())),
            centraliza_texto(exibicao_porcent(med.getPercRealizadoPeriodo()))
        ],
        [
            'Acumulado do mês'.rjust(21).ljust(37),
            centraliza_texto(exibicao_porcent(med.getPercPrevistoAcumulado())),
            centraliza_texto(exibicao_porcent(med.getPercRealizadoAcumulado()))
        ]
    ]
    medicao = f"{med.getNrMedicao() if med.getNrMedicao() else '1ª'} Medição"

    column_labels = [
        centraliza_texto(medicao),
        centraliza_texto('Previsto'),
        centraliza_texto('Executado')
    ]

    # Definir tamanho das células
    cell_width = 2.0  # Largura de cada célula
    cell_height = 0.2  # Altura de cada célula
    # Calcular o tamanho total da figura com base no número de células
    num_rows = len(data) + 1  # +1 para incluir os cabeçalhos
    num_cols = len(column_labels)
    fig_width = num_cols * cell_width
    fig_height = num_rows * cell_height
    # Criar a figura com o tamanho calculado
    fig, ax = plt.subplots(figsize=(fig_width, fig_height))

    # Remove os eixos do gráfico, deixando apenas a tabela visível.
    ax.axis("off")
    tabela = ax.table(cellText=data, colLabels=column_labels, loc="center")
    # Desativa o ajuste automático do tamanho da fonte. Isso permite que você defina manualmente o tamanho da fonte.
    tabela.auto_set_font_size(False)
    tabela.set_fontsize(8)
#    tabela.scale(2,1)

#   Ajustando o tamanho das colunas
    for x in range(0, num_cols):
        tabela.auto_set_column_width(x)

    if codBanco == 77:  # Banco Inter
        corCabecalho = (0.945, 0.662, 0.513)  # Cor laranja
    else:
        corCabecalho = "lightblue"

#   colocando cor de fundo no cabeçalho
    for (row, col), cell in tabela.get_celld().items():
        # Define a cor da borda como "none" (sem borda)
        cell.set_edgecolor("none")
        if row == 0:
            cell.set_facecolor(corCabecalho)
            cell.set_text_props(ha='center', va='center')  # Alinhar no centro
        else:  # Demais itens da tabela
            if col == 2:
                cell_text = cell.get_text().get_text()  # Obtém o texto da célula
                # Alinhar à esquerda
                cell.set_text_props(ha='left', va='center', color='red')
            else:
                # Alinhar no centro
                cell.set_text_props(ha='left', va='center')

    grafC = graficoController()

    diretorio = grafC.montaDir(idEmpreend, mes, ano)
    grafC.criaDir(diretorio)
    grafNome = os.path.join(diretorio, 'tab_prazo_inter.png')

    plt.savefig(grafNome)
    plt.close('all')
    return grafNome


@tabelas_bp.route('/tab_projeto_inter')
def tab_projeto_inter():

    idEmpreend = IdEmpreend().get()
    mes = request.args.get("mesV")
    ano = request.args.get("anoV")
    grafNome = gerar_tab_projeto_inter(idEmpreend, mes, ano)
    return render_template("orcamento_liberacao.html", grafNome=grafNome, version=random.randint(1, 100000))


def gerar_tab_projeto_inter(idEmpreend, mesVigencia, anoVigencia):
    ponC = torreController()
    ponS = ponC.consolidado(idEmpreend)
    aspCtrl = aspectosController()
    pergs = aspCtrl.todasPerguntasComRespostas(
        idEmpreend, mesVigencia, anoVigencia)

    if not ponS:
        return ''

    fig, ax = plt.subplots(1, 1)

    data = [
        ['Número de pavimentos'.ljust(tam_tit),
         str(ponS.getPavimentos()).rjust(tam_dado)],
        ['Número de blocos'.ljust(tam_tit),
            str(ponS.getBlocos()).rjust(tam_dado)],
        ['Número de unidades'.ljust(tam_tit),
            str(ponS.getUnidades()).rjust(tam_dado)]
    ]

    for pg in pergs.get('Projeto'):
        data.append(
            [pg.getPergunta().ljust(tam_tit),
             str(pg.getResposta()).rjust(tam_dado)]
        )

    column_labels = ['            ', '           ']

    # Definir tamanho das células
    cell_width = 2.0  # Largura de cada célula
    cell_height = 0.2  # Altura de cada célula
    # Calcular o tamanho total da figura com base no número de células
    num_rows = len(data) + 1  # +1 para incluir os cabeçalhos
    num_cols = len(column_labels)
    fig_width = num_cols * cell_width
    fig_height = num_rows * cell_height
    # Criar a figura com o tamanho calculado
    fig, ax = plt.subplots(figsize=(fig_width, fig_height))

    # Remove os eixos do gráfico, deixando apenas a tabela visível.
    ax.axis("off")
    tabela = ax.table(cellText=data, colLabels=column_labels, loc="center")
    # Desativa o ajuste automático do tamanho da fonte. Isso permite que você defina manualmente o tamanho da fonte.
    tabela.auto_set_font_size(False)
    tabela.set_fontsize(8)
#    tabela.scale(2,1)

#   Ajustando o tamanho das colunas
    for x in range(0, num_cols):
        tabela.auto_set_column_width(x)
#   colocando cor de fundo no cabeçalho
    for (row, col), cell in tabela.get_celld().items():
        # Define a cor da borda como "none" (sem borda)
        cell.set_edgecolor("none")
        if row == 0:
            #            cell.set_facecolor("lightblue")
            #            cell.set_facecolor((0.945, 0.662, 0.513)) # Cor laranja
            cell.set_text_props(ha='center', va='center')  # Alinhar no centro
        else:  # Demais itens da tabela
            if col == 1:
                cell_text = cell.get_text().get_text()  # Obtém o texto da célula
                # Alinhar à esquerda
                cell.set_text_props(ha='left', va='center', color='green')
            else:
                # Alinhar no centro
                cell.set_text_props(ha='left', va='center')

    grafC = graficoController()

    diretorio = grafC.montaDir(idEmpreend, mesVigencia, anoVigencia)
    grafC.criaDir(diretorio)
    grafNome = os.path.join(diretorio, 'tab_projeto_inter.png')

    plt.savefig(grafNome)
    plt.close('all')
    return grafNome


@tabelas_bp.route('/tab_qualidade_inter')
def tab_qualidade_inter():

    idEmpreend = IdEmpreend().get()
    mes = request.args.get("mesV")
    ano = request.args.get("anoV")
    grafNome = gerar_tab_qualidade_inter(idEmpreend, mes, ano)
    return render_template("orcamento_liberacao.html", grafNome=grafNome, version=random.randint(1, 100000))


def gerar_tab_qualidade_inter(idEmpreend, mesVigencia, anoVigencia):
    aspecCtrl = aspectosController()
    pergs = aspecCtrl.todasPerguntasComRespostas(
        idEmpreend, mesVigencia, anoVigencia)

    if not pergs:
        return ''

    fig, ax = plt.subplots(1, 1)

    data = []

    for pg in pergs.get('Qualidade'):
        data.append(
            [pg.getPergunta().ljust(tam_tit),
             str(pg.getResposta()).rjust(tam_dado)]
        )

    column_labels = ['            ', '           ']

    # Definir tamanho das células
    cell_width = 2.0  # Largura de cada célula
    cell_height = 0.2  # Altura de cada célula
    # Calcular o tamanho total da figura com base no número de células
    num_rows = len(data) + 1  # +1 para incluir os cabeçalhos
    num_cols = len(column_labels)
    fig_width = num_cols * cell_width
    fig_height = num_rows * cell_height
    # Criar a figura com o tamanho calculado
    fig, ax = plt.subplots(figsize=(fig_width, fig_height))

    # Remove os eixos do gráfico, deixando apenas a tabela visível.
    ax.axis("off")
    tabela = ax.table(cellText=data, colLabels=column_labels, loc="center")
    # Desativa o ajuste automático do tamanho da fonte. Isso permite que você defina manualmente o tamanho da fonte.
    tabela.auto_set_font_size(False)
    tabela.set_fontsize(8)
#    tabela.scale(2,1)

#   Ajustando o tamanho das colunas
    for x in range(0, num_cols):
        tabela.auto_set_column_width(x)
#   colocando cor de fundo no cabeçalho
    for (row, col), cell in tabela.get_celld().items():
        # Define a cor da borda como "none" (sem borda)
        cell.set_edgecolor("none")
        if row == 0:
            #            cell.set_facecolor("lightblue")
            #            cell.set_facecolor((0.945, 0.662, 0.513)) # Cor laranja
            cell.set_text_props(ha='center', va='center')  # Alinhar no centro
        else:  # Demais itens da tabela
            if col == 1:
                cell_text = cell.get_text().get_text()  # Obtém o texto da célula
                # Alinhar à esquerda
                if "Bom" in cell_text:
                    cell.set_text_props(ha='left', va='center', color='green')
                elif "Normal" in cell_text:
                    cell.set_text_props(ha='left', va='center', color='orange')
                else:
                    cell.set_text_props(ha='left', va='center', color='red')
            else:
                # Alinhar no centro
                cell.set_text_props(ha='left', va='center')

    grafC = graficoController()

    diretorio = grafC.montaDir(idEmpreend, mesVigencia, anoVigencia)
    grafC.criaDir(diretorio)
    grafNome = os.path.join(diretorio, 'tab_qualidade_inter.png')

    plt.savefig(grafNome)
    plt.close('all')
    return grafNome


@tabelas_bp.route('/tab_seguranca_inter')
def tab_seguranca_inter():

    idEmpreend = IdEmpreend().get()
    mes = request.args.get("mesV")
    ano = request.args.get("anoV")
    grafNome = gerar_tab_seguranca_inter(idEmpreend, mes, ano)
    return render_template("orcamento_liberacao.html", grafNome=grafNome, version=random.randint(1, 100000))


def gerar_tab_seguranca_inter(idEmpreend, mesVigencia, anoVigencia):
    aspecCtrl = aspectosController()
    pergs = aspecCtrl.todasPerguntasComRespostas(
        idEmpreend, mesVigencia, anoVigencia)

    if not pergs:
        return ''

    fig, ax = plt.subplots(1, 1)

    data = []

    for pg in pergs.get('Segurança'):
        data.append(
            [pg.getPergunta().ljust(tam_tit),
             str(pg.getResposta()).rjust(tam_dado)]
        )

    column_labels = ['            ', '           ']

    # Definir tamanho das células
    cell_width = 2.0  # Largura de cada célula
    cell_height = 0.2  # Altura de cada célula
    # Calcular o tamanho total da figura com base no número de células
    num_rows = len(data) + 1  # +1 para incluir os cabeçalhos
    num_cols = len(column_labels)
    fig_width = num_cols * cell_width
    fig_height = num_rows * cell_height
    # Criar a figura com o tamanho calculado
    fig, ax = plt.subplots(figsize=(fig_width, fig_height))

    # Remove os eixos do gráfico, deixando apenas a tabela visível.
    ax.axis("off")
    tabela = ax.table(cellText=data, colLabels=column_labels, loc="center")
    # Desativa o ajuste automático do tamanho da fonte. Isso permite que você defina manualmente o tamanho da fonte.
    tabela.auto_set_font_size(False)
    tabela.set_fontsize(8)
#    tabela.scale(2,1)

#   Ajustando o tamanho das colunas
    for x in range(0, num_cols):
        tabela.auto_set_column_width(x)
#   colocando cor de fundo no cabeçalho
    for (row, col), cell in tabela.get_celld().items():
        # Define a cor da borda como "none" (sem borda)
        cell.set_edgecolor("none")
        if row == 0:
            #            cell.set_facecolor("lightblue")
            #            cell.set_facecolor((0.945, 0.662, 0.513)) # Cor laranja
            cell.set_text_props(ha='center', va='center')  # Alinhar no centro
        else:  # Demais itens da tabela
            if col == 1:
                cell_text = cell.get_text().get_text()  # Obtém o texto da célula
                # Alinhar à esquerda
                if "Sim" in cell_text:
                    cell.set_text_props(ha='left', va='center', color='green')
                else:
                    cell.set_text_props(ha='left', va='center', color='red')
            else:
                # Alinhar no centro
                cell.set_text_props(ha='left', va='center')

    grafC = graficoController()

    diretorio = grafC.montaDir(idEmpreend, mesVigencia, anoVigencia)
    grafC.criaDir(diretorio)
    grafNome = os.path.join(diretorio, 'tab_seguranca_inter.png')

    plt.savefig(grafNome)
    plt.close('all')
    return grafNome


@tabelas_bp.route('/tab_situacao_inter')
def tab_situacao_inter():
    idEmpreend = IdEmpreend().get()
    mes = request.args.get("mesV")
    ano = request.args.get("anoV")
    grafNome = gerar_tab_situacao_inter(idEmpreend, mes, ano)
    return render_template("orcamento_liberacao.html", grafNome=grafNome, version=random.randint(1, 100000))


def gerar_tab_situacao_inter(idEmpreend, mesVigencia, anoVigencia):
    aspecCtrl = aspectosController()
    pergs = aspecCtrl.todasPerguntasComRespostas(
        idEmpreend, mesVigencia, anoVigencia)

    if not pergs:
        return ''

    fig, ax = plt.subplots(1, 1)

    data = []

    for pg in pergs.get('Situação'):
        data.append(
            [pg.getPergunta().ljust(tam_tit),
             str(pg.getResposta()).rjust(tam_dado)]
        )

    column_labels = ['            ', '           ']

    # Definir tamanho das células
    cell_width = 2.0  # Largura de cada célula
    cell_height = 0.2  # Altura de cada célula
    # Calcular o tamanho total da figura com base no número de células
    num_rows = len(data) + 1  # +1 para incluir os cabeçalhos
    num_cols = len(column_labels)
    fig_width = num_cols * cell_width
    fig_height = num_rows * cell_height
    # Criar a figura com o tamanho calculado
    fig, ax = plt.subplots(figsize=(fig_width, fig_height))

    # Remove os eixos do gráfico, deixando apenas a tabela visível.
    ax.axis("off")
    tabela = ax.table(cellText=data, colLabels=column_labels, loc="center")
    # Desativa o ajuste automático do tamanho da fonte. Isso permite que você defina manualmente o tamanho da fonte.
    tabela.auto_set_font_size(False)
    tabela.set_fontsize(8)
#    tabela.scale(2,1)

#   Ajustando o tamanho das colunas
    for x in range(0, num_cols):
        tabela.auto_set_column_width(x)
#   colocando cor de fundo no cabeçalho
    for (row, col), cell in tabela.get_celld().items():
        # Define a cor da borda como "none" (sem borda)
        cell.set_edgecolor("none")
        if row == 0:
            #            cell.set_facecolor("lightblue")
            #            cell.set_facecolor((0.945, 0.662, 0.513)) # Cor laranja
            cell.set_text_props(ha='center', va='center')  # Alinhar no centro
        else:  # Demais itens da tabela
            if col == 1:
                cell_text = cell.get_text().get_text()  # Obtém o texto da célula
                # Alinhar à esquerda
                if "Adiantada" in cell_text:
                    cell.set_text_props(ha='left', va='center', color='green')
                elif "No prazo" in cell_text:
                    cell.set_text_props(ha='left', va='center', color='orange')
                else:
                    cell.set_text_props(ha='left', va='center', color='red')
            else:
                # Alinhar no centro
                cell.set_text_props(ha='left', va='center')

    grafC = graficoController()

    diretorio = grafC.montaDir(idEmpreend, mesVigencia, anoVigencia)
    grafC.criaDir(diretorio)
    grafNome = os.path.join(diretorio, 'tab_situacao_inter.png')

    plt.savefig(grafNome)
    plt.close('all')
    return grafNome
