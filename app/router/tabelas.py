
from flask import Blueprint, request, render_template, redirect, flash
from controller.inadimplenciaController import inadimplenciaController
from controller.financeiroController import financeiroController
from controller.orcamentoController import orcamentoController
from controller.certidaoController import certidaoController
from controller.garantiaController import garantiaController
from controller.graficoController import graficoController
from controller.medicaoController import medicaoController
from controller.contaController import contaController
from controller.geralController import geralController
from controller.notaController import notaController
from utils.CtrlSessao import IdEmpreend
from matplotlib import pyplot as plt
import matplotlib.pyplot as plt
import random

from dto.certidao import certidao

tabela_bp = Blueprint('tabelas', __name__)

@tabela_bp.route('/tab_inadimplencia')
def tab_inadimplencia():

    #    tipo = request.args.get("tipo")
    #    idEmpreend = request.args.get("idEmpreend")
    #    dtCarga = request.args.get("dtCarga")

    idEmpreend = 55
    mesIni = '10'
    anoIni = '2024'
    mesFim = '01'
    anoFim = '2025'

    geral = geralController()
    inaC = inadimplenciaController()
    inaS = inaC.consultarInadimplenciaPelaData(
        idEmpreend, mesIni, anoIni, mesFim, anoFim)

    column_labels = []
    mesTeste = ''
    anoTeste = ''
    atrasoTeste = True

    column_labels.append('Atraso')

    for m in inaS:
        if m.getOrdem() == 1:
            column_labels.append(geral.formatammmaa(
                m.getMesVigencia(), m.getAnoVigencia()))
        else:
            break

#    print('++++++++ column_labels', column_labels )

    data = []

    periodoTeste = True
    ordemTeste = 1
    dd = []
    tamanho = len(inaS)
#    print ('===============> ', tamanho)
    posicao = 0

    while posicao < tamanho:
        print('a ', posicao, tamanho)
        m = inaS[posicao]
        print('b ', ordemTeste, m.getOrdem())
        if ordemTeste == m.getOrdem():
            if len(dd) == 0:
                dd.append(m.getPeriodo())
            dd.append(m.getQtUnidades())
        else:
            data.append(dd)
            dd = []
            dd.append(m.getPeriodo())
            dd.append(m.getQtUnidades())
            ordemTeste += 1
        posicao += 1
    data.append(dd)

#    print('++++++++ Data', data )

    title_text = 'Inadimplência'
    fig, ax = plt.subplots(1, 1)

    # Definir tamanho das células
    cell_width = 0.6  # Largura de cada célula
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
        if row == 0:
            cell.set_facecolor("lightblue")

    grafC = graficoController()

    idEmpreend = 55  # preciso montar esse informação
    mes = "12"
    ano = "2024"

    diretorio = grafC.montaDir(idEmpreend, mes, ano)
    grafC.criaDir(diretorio)
    grafNome = diretorio + 'tab_inadimplencia.png'

#    plt.savefig(grafNome, edgecolor=fig.get_edgecolor(), facecolor=fig.get_facecolor(), dpi=150 )
    plt.savefig(grafNome)  # , bbox_inches='tight')

    return


@tabela_bp.route('/tab_notas')
def tab_notas():

#    idEmpreend = request.args.get("idEmpreend")
    idEmpreend = IdEmpreend().get()
    dtCarga = request.args.get("dtCarga")
    mesVigencia = str(request.args.get('mesV')).zfill(2)
    anoVigencia = str(request.args.get('anoV'))


#    idEmpreend = 55
#    dtCarga = '2024-12-30 16:57:31'
#    mes = "12"  # preciso montar esse informação
#    ano = "2024"

    geral = geralController()
    notC = notaController()
    notS = notC.consultarNotaPelaData(idEmpreend, dtCarga)

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
    dd.append('Estoque em ' + mesVigencia + '/' + anoVigencia)
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

#   colocando cor de fundo no cabeçalho
    for (row, col), cell in tabela.get_celld().items():
        if row == 0 or row == num_rows-1:
            cell.set_facecolor("lightblue")  # campos em azul encima e embaixo
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
    grafNome = diretorio + 'tab_notas.png'

    plt.savefig(grafNome)

    return render_template("nota_liberacao.html", grafNome=grafNome, version=random.randint(1, 100000))


@tabela_bp.route('/tab_conta')
def tab_conta_corrente():

    fig, ax = plt.subplots(1, 1)

    idEmpreend = IdEmpreend().get()
    dtCarga = request.args.get("dtCarga")
    mesVigencia = str(request.args.get('mesV')).zfill(2)
    anoVigencia = str(request.args.get('anoV'))

    geral = geralController()
    conC = contaController()
    conS = conC.consultarContaPelaCarga(idEmpreend, dtCarga)

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

#   colocando cor de fundo no cabeçalho
    for (row, col), cell in tabela.get_celld().items():
        if row == 0:
            cell.set_facecolor("lightblue")
            cell.set_text_props(ha='center', va='center')  # Alinhar no centro
        else:  # Demais itens da tabela
            cell.set_text_props(ha='right', va='center')  # Alinhar à esquerda

    grafC = graficoController()

    diretorio = grafC.montaDir(idEmpreend, mesVigencia, anoVigencia)
    grafC.criaDir(diretorio)
    grafNome = diretorio + 'tab_conta_corrente.png'

    plt.savefig(grafNome)

    return render_template("conta_liberacao.html", grafNome=grafNome, version=random.randint(1, 100000))


@tabela_bp.route('/tab_garantias_geral', methods=['GET'])
def tab_garantias_geral():

    idEmpreend = IdEmpreend().get()
    tipo = request.args.get("tipo")
    mesVigencia = request.args.get("mesVigencia")
    anoVigencia = request.args.get("anoVigencia")

    geral = geralController()
    ponC = garantiaController()
    ponS = ponC.consultargarantiaatual(idEmpreend, tipo)

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
#   colocando cor de fundo no cabeçalho
    for (row, col), cell in tabela.get_celld().items():
        # Define a cor da borda como "none" (sem borda)
        cell.set_edgecolor("none")
        if row == 0:
            cell.set_facecolor("lightblue")
            cell.set_text_props(ha='center', va='center')  # Alinhar no centro
        else:  # Demais itens da tabela
            if col == 1: 
                cell_text = cell.get_text().get_text()  # Obtém o texto da célula
                if "Atenção" in cell_text:  # Verifica se contém a palavra "Atenção"
                    cell.set_text_props(ha='left', va='center',color='red')  # Alinhar à esquerda
                elif "Verificar" in cell_text:  # Verifica se contém a palavra "Atenção"
                    cell.set_text_props(ha='left', va='center',color='orange')  # Alinhar à esquerda
                else:
                    cell.set_text_props(ha='left', va='center',color='green')  # Alinhar à esquerda
            else:
                cell.set_text_props(ha='left', va='center')  # Alinhar no centro

    grafC = graficoController()

    diretorio = grafC.montaDir(idEmpreend, mesVigencia, anoVigencia)
    grafC.criaDir(diretorio)
    grafNome = diretorio + 'tab_garantias_geral.png'

    plt.savefig(grafNome)

    return render_template("garantia_liberacao.html", grafNome=grafNome, version=random.randint(1, 100000))

@tabela_bp.route('/tab_garantias_obra')
def tab_garantias_obra():

    idEmpreend = IdEmpreend().get()
    tipo = request.args.get("tipo")
    mesVigencia = request.args.get("mesVigencia")
    anoVigencia = request.args.get("anoVigencia")

    geral = geralController()
    ponC = garantiaController()
    ponS = ponC.consultargarantiaatual(idEmpreend, tipo)

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
#   colocando cor de fundo no cabeçalho
    for (row, col), cell in tabela.get_celld().items():
        # Define a cor da borda como "none" (sem borda)
        cell.set_edgecolor("none")
        if row == 0:
            cell.set_facecolor("lightblue")
            cell.set_text_props(ha='center', va='center')  # Alinhar no centro
        else:  # Demais itens da tabela
            if col == 1: 
                cell_text = cell.get_text().get_text()  # Obtém o texto da célula
                if "Atenção" in cell_text:  # Verifica se contém a palavra "Atenção"
                    cell.set_text_props(ha='left', va='center',color='red')  # Alinhar à esquerda
                elif "Verificar" in cell_text:  # Verifica se contém a palavra "Atenção"
                    cell.set_text_props(ha='left', va='center',color='orange')  # Alinhar à esquerda
                else:
                    cell.set_text_props(ha='left', va='center',color='green')  # Alinhar à esquerda
            else:
                cell.set_text_props(ha='left', va='center')  # Alinhar no centro

    grafC = graficoController()

    diretorio = grafC.montaDir(idEmpreend, mesVigencia, anoVigencia)
    grafC.criaDir(diretorio)
    grafNome = diretorio + 'tab_garantias_obra.png'

    plt.savefig(grafNome)

    return render_template("garantia_liberacao.html", grafNome=grafNome, version=random.randint(1, 100000))


@tabela_bp.route('/tab_certidoes')
def tab_certidoes():

    idEmpreend = IdEmpreend().get()
    mesVigencia = request.args.get("mesVigencia")
    anoVigencia = request.args.get("anoVigencia")

    geral = geralController()
    certC = certidaoController()
    certS = certC.consultarCertidoesGraf(idEmpreend)
 
    fig, ax = plt.subplots(1, 1)
    print (certS)
    print (certS.getEstadualStatus())

    data = []
    a = ['Estadual', certS.getEstadualStatus(), certS.getEstadualValidade()]
    data.append (a)
    b = ['FGTS', certS.getFgtsStatus(), certS.getEstadualValidade()]
    data.append (b)    
    c = ['Municipal', certS.getMunicipalStatus(), certS.getMunicipalValidade()]
    data.append (c)
    d = ['SRF/INSS', certS.getSrfInssStatus(), certS.getSrfInssValidade()]
    data.append (d)
    e = ['Trabalhista', certS.getTrabalhistaStatus(), certS.getTrabalhistaValidade()]
    data.append (e)

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
#   colocando cor de fundo no cabeçalho
    for (row, col), cell in tabela.get_celld().items():
        # Define a cor da borda como "none" (sem borda)
        cell.set_edgecolor("none")
        if row == 0:
            cell.set_facecolor("lightblue")
            cell.set_text_props(ha='center', va='center')  # Alinhar no centro
        else:  # Demais itens da tabela
            if col == 1: 
                cell_text = cell.get_text().get_text()  # Obtém o texto da célula
                if "Positiva" in cell_text:  # Verifica se contém a palavra "Atenção"
                    cell.set_text_props(ha='left', va='center',color='red')  # Alinhar à esquerda
                elif "Pendente" in cell_text:  # Verifica se contém a palavra "Atenção"
                    cell.set_text_props(ha='left', va='center',color='orange')  # Alinhar à esquerda
                else:
                    cell.set_text_props(ha='left', va='center',color='green')  # Alinhar à esquerda
            else:
                cell.set_text_props(ha='left', va='center')  # Alinhar no centro

    grafC = graficoController()

    diretorio = grafC.montaDir(idEmpreend, mesVigencia, anoVigencia)
    grafC.criaDir(diretorio)
    grafNome = diretorio + 'tab_certidoes.png'

    plt.savefig(grafNome)

    return render_template("certidoes_liberacao.html", grafNome=grafNome, version=random.randint(1, 100000))


@tabela_bp.route('/tab_acomp_financeiro')
def tab_acomp_financeiro():

    #    tipo = request.args.get("tipo")
    #    idEmpreend = request.args.get("idEmpreend")
    #    dtCarga = request.args.get("dtCarga")

    idEmpreend = 55
    dtCarga = '2024-12-30 16:57:31'

    geral = geralController()
    finC = financeiroController()
    finS = finC.consultarFinanceiroPelaData(idEmpreend, dtCarga)
    fig, ax = plt.subplots(1, 1)

    data = []

    for m in finS:
        dd = []
        dd.append(m.getHistorico())
        dd.append(geral.formataPerc(m.getPercFinanceiro(), 0))
        dd.append(geral.formataNumero(m.getVlFinanceiro(), 'R$'))
        data.append(dd)

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

    idEmpreend = str(55)  # preciso montar esse informação
    mes = "12"
    ano = "2024"

    diretorio = grafC.montaDir(idEmpreend, mes, ano)
    grafC.criaDir(diretorio)
    grafNome = diretorio + 'tab_acomp_financeiro.png'

    plt.savefig(grafNome)


@tabela_bp.route('/tab_medicoes')
def tab_medicoes():

    idEmpreend  = IdEmpreend().get()
    mesVigencia = request.args.get("mesVigencia")
    anoVigencia = request.args.get("anoVigencia")
    mesInicio  = request.args.get("mesInicio")
    anoInicio  = request.args.get("anoInicio")
    mesFinal   = request.args.get("mesFinal")
    anoFinal   = request.args.get("anoFinal")

    geral = geralController()
    preC  = medicaoController()

#    preS = preC.consultarMedicoes(idEmpreend)

    preS = preC.consultarMedicoesPorPeriodo(idEmpreend, mesInicio, anoInicio, mesFinal, anoFinal)

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
#   colocando cor de fundo no cabeçalho
    for (row, col), cell in tabela.get_celld().items():
        if row == 0:
            cell.set_facecolor("lightblue")

    grafC = graficoController()

    diretorio = grafC.montaDir(idEmpreend, mesVigencia, anoVigencia)
    grafC.criaDir(diretorio)
    grafNome = diretorio + 'tab_medicoes.png'

    plt.savefig(grafNome)

    return render_template("medicoes_liberacao.html", grafNome=grafNome, version=random.randint(1, 100000))


@tabela_bp.route('/tab_orcamento_liberacao')
def tab_orcamento_liberacao():

    idEmpreend = IdEmpreend().get()
    dtCarga = request.args.get("dtCarga")
    mes = request.args.get("mesV")
    ano = request.args.get("anoV")

    geral = geralController()
    medC = orcamentoController()
    medS = medC.consultarOrcamentoPelaData(idEmpreend, dtCarga)
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

    for (row, col), cell in tabela.get_celld().items():
        if row == 0 or row == num_rows-1:     # pinta a 1ª 1 ultima linhas
            cell.set_facecolor("lightblue")
        if col == 2 or col == 6:                     # pinta as colunas de divisão
            cell.set_facecolor("lightblue")
        if row > 0 and col == 0:
            cell.set_text_props(ha='left', va='center')  # Alinhar à esquerda

    grafC = graficoController()

    diretorio = grafC.montaDir(idEmpreend, mes, ano)
    grafC.criaDir(diretorio)
    grafNome = diretorio + 'tab_orcamento_liberacao.png'

    plt.savefig(grafNome)

#    plt.savefig(grafNome, bbox_inches='tight')

    return render_template("orcamento_liberacao.html", grafNome=grafNome, version=random.randint(1, 100000))
