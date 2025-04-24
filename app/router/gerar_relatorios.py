from flask import Blueprint, request, render_template, redirect, current_app, flash

from controller.financeiroController import financeiroController
from controller.orcamentoController import orcamentoController
from router.graficos import gerar_graf_orcamento_liberacao, gerar_graf_indices_garantia_I
from controller.contaController import contaController
from controller.notaController import notaController
from router.tabelas import gerar_tab_conta_corrente, gerar_tab_notas, gerar_tab_orcamento_liberacao, gerar_tab_acomp_financeiro
from decorators.login_riquired import login_required
from utils.CtrlSessao import IdEmpreend, NmEmpreend
import datetime
import os

gerar_relatorio_bp = Blueprint('gerar_relatorios', __name__)

opcoes = [
    ['graf_indices_garantia_I', 'Gráfico de Índices de Garantias I', 'Não'],
    ['graf_indices_garantia_II', 'Gráfico de Índices de Garantias II', 'Não'],
    ['graf_orcamento_liberacao_valor',
     'Gráfico do Orçamento para Liberação de Valor', 'Não'],
    ['graf_progresso_obra', 'Gráfico do Progresso da Obra', 'Não'],
    ['graf_chaves', 'Gráfico de Liberação das Chaves', 'Não'],
    ['graf_vendas', 'Gráfico de Vendas', 'Não'],
    ['tab_acomp_financeiro', 'Tabela de Acompanhamento Financeiro', 'Não'],
    ['tab_conta_corrente', 'Tabela das Contas Correntes', 'Não'],
    ['tab_medicoes', 'Tabela das Medições', 'Não'],
    ['tab_notas', 'Tabela das Notas', 'Não'],
    ['tab_orcamento_liberacao', 'Tabela do Orçamento para Liberação', 'Não'],
    ['tab_pontos_atencao_documentos',
     'Tabela dos Pontos de Atenção dos Documentos', 'Não'],
    ['tab_pontos_atencao_geral', 'Tabela dos Pontos de Atenção Geral', 'Não'],
    ['tab_pontos_atencao_obra', 'Tabela dos Pontos de Atenção da Obra', 'Não'],
]


@gerar_relatorio_bp.route('/gerar_insumos_relatorios')
@login_required
def gerar_relatorio():
    idEmpreend = request.args.get("idEmpreend")
    nmEmpreend = request.args.get("nmEmpreend")

    if (idEmpreend is None and not IdEmpreend().has()) or (nmEmpreend is None and not NmEmpreend().has()):
        return redirect('/home')

    if idEmpreend is None:
        idEmpreend = IdEmpreend().get()
    else:
        IdEmpreend().set(idEmpreend)

    if nmEmpreend is None:
        nmEmpreend = NmEmpreend().get()
    else:
        NmEmpreend().set(nmEmpreend)

    mes = request.args.get('mes')
    ano = request.args.get('ano')

    if mes is None:
        mes = str(datetime.date.today().month).zfill(2)
    if ano is None:
        ano = datetime.date.today().year

    for opt in opcoes:
        opt[2] = 'Sim' if existe_insumo(opt[0], mes, ano) else 'Não'

    return render_template('gerar_relatorio.html', opcoes=opcoes, mes=mes, ano=ano)


@gerar_relatorio_bp.route('/gerar_insumos', methods=['POST'])
def gerar_insumos():
    insumos = request.form.getlist('opcoes_relatorio')
    mes = request.form.get('mes_vigencia')
    ano = request.form.get('ano_vigencia')

    for ins in insumos:
        if ins in insumos:
            fn = globals()[ins]
            fn(mes, ano)

    return redirect('/gerar_insumos_relatorios')


def graf_orcamento_liberacao_valor(mes, ano):
    medC = orcamentoController()
    medS = medC.consultarOrcamentoPelaVigencia(IdEmpreend().get(), mes, ano)
    if medS:
        gerar_graf_orcamento_liberacao(
            IdEmpreend().get(), mes, ano, 'valor', medS)
    else:
        flash(
            'Não há dados para gerar o gráfico de orçamento de liberação de valor',
            category='warning'
        )


def tab_conta_corrente(mes, ano):
    conC = contaController()
    conS = conC.consultarContaPelaVigencia(IdEmpreend().get(), mes, ano)
    if conS:
        gerar_tab_conta_corrente(IdEmpreend().get(), mes, ano, conS)
    else:
        flash(
            'Não há dados para gerar a tabela de contas corrente',
            category='warning'
        )


def tab_notas(mes, ano):
    notC = notaController()
    notS = notC.consultarNotaPelaVigencia(IdEmpreend().get(), mes, ano)
    if notS:
        gerar_tab_notas(IdEmpreend().get(), mes, ano, notS)
    else:
        flash(
            'Não há dados para gerar a tabela de notas',
            category='warning'
        )


def tab_orcamento_liberacao(mes, ano):
    medC = orcamentoController()
    medS = medC.consultarOrcamentoPelaVigencia(IdEmpreend().get(), mes, ano)
    if medS:
        gerar_tab_orcamento_liberacao(IdEmpreend().get(), mes, ano, medS)
    else:
        flash(
            'Não há dados para gerar a tabela de orçamento liberação',
            category='warning'
        )


def tab_acomp_financeiro(mes, ano):
    finC = financeiroController()
    finS = finC.consultarFinanceiroPelaVigencia(IdEmpreend().get(), mes, ano)
    if finS:
        gerar_tab_acomp_financeiro(IdEmpreend().get(), mes, ano, finS)
    else:
        flash(
            'Não há dados para gerar a tabela de acompanhamento financeiro',
            category='warning'
        )


def graf_indices_garantia_I(mes, ano):
    medC = orcamentoController()
    medS = medC.consultarOrcamentoPelaVigencia(IdEmpreend().get(), mes, ano)
    if medS:
        gerar_graf_indices_garantia_I(IdEmpreend().get(), mes, ano, medS)
    else:
        flash(
            'Não há dados para gerar o gráfico de orçamento de liberação de valor',
            category='warning'
        )


def existe_insumo(nome, mes, ano):
    file = getDir(os.path.join(f"{ano}_{mes}", nome))
    return os.path.exists(f"{file}.jpg") or os.path.exists(f"{file}.png")


def getDir(path=None):
    nPath = os.path.join(current_app.config['DIRSYS'], IdEmpreend().get())
    if path is not None:
        nPath = os.path.join(nPath, path)
    return os.path.normpath(nPath)
