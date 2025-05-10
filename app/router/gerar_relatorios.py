from flask import Blueprint, request, render_template, redirect, current_app, flash, send_file

from controller.financeiroController import financeiroController
from controller.orcamentoController import orcamentoController
from router.graficos import gerar_graf_orcamento_liberacao, gerar_graf_indices_garantia_I, gerar_graf_indices_garantia_II, gerar_graf_chaves, gerar_graf_vendas, gerar_graf_progresso_obra
from controller.contaController import contaController
from controller.notaController import notaController
from router.tabelas import gerar_tab_conta_corrente, gerar_tab_notas, gerar_tab_orcamento_liberacao, gerar_tab_acomp_financeiro, gerar_tab_certidoes, gerar_tab_garantias_geral, gerar_tab_garantias_obra, gerar_tab_medicoes
from decorators.login_riquired import login_required
from utils.CtrlSessao import IdEmpreend, NmEmpreend
from utils.flash_message import flash_message
from utils.logger import logger
import datetime
import os

gerar_relatorio_bp = Blueprint('gerar_relatorios', __name__)

opcoes = [
    ['graf_orcamento_liberacao_valor',
     'Gráfico do Orçamento para Liberação de Valor', 'Não'],
    ['graf_chaves_perc', 'Gráfico de Liberação das Chaves (%)', 'Não'],
    ['graf_chaves_valor', 'Gráfico de Liberação das Chaves (R$)', 'Não'],
    ['graf_vendas_perc', 'Gráfico de Vendas (%)', 'Não'],
    ['graf_vendas_valor', 'Gráfico de Vendas (R$)', 'Não'],
    ['tab_acomp_financeiro', 'Tabela de Acompanhamento Financeiro', 'Não'],
    ['tab_conta_corrente', 'Tabela das Contas Correntes', 'Não'],
    ['tab_notas', 'Tabela das Notas', 'Não'],
    ['tab_orcamento_liberacao', 'Tabela do Orçamento para Liberação', 'Não'],
    ['tab_certidoes', 'Tabela das Certidões', 'Não'],
    ['tab_garantias_geral', 'Tabela de Garantias Geral', 'Não'],
    ['tab_garantias_obra', 'Tabela com as Garantias da Obra', 'Não'],
]

opcoesComRange = [
    ['graf_indices_garantia_I', 'Gráfico de Índices de Garantias I', 'Não'],
    ['graf_indices_garantia_II', 'Gráfico de Índices de Garantias II', 'Não'],
    ['graf_progresso_obra', 'Gráfico do Progresso da Obra', 'Não'],
    ['tab_medicoes', 'Tabela das Medições', 'Não'],
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

    for opt in opcoesComRange:
        opt[2] = 'Sim' if existe_insumo(opt[0], mes, ano) else 'Não'

    return render_template(
        'gerar_relatorio.html',
        opcoesComRange=opcoesComRange,
        opcoes=opcoes,
        mes=mes,
        ano=ano
    )


@gerar_relatorio_bp.route('/gerar_insumos', methods=['POST', 'GET'])
def gerar_insumos():
    insumos = request.form.getlist('opcoes_relatorio')
    insumosIntervalo = request.form.getlist('opcoes_relatorio_range')
    mes = request.form.get('mes_vigencia')
    ano = request.form.get('ano_vigencia')

    if (not mes or not ano) or (not insumos and not insumosIntervalo):
        return redirect('/gerar_insumos_relatorios')
    inicioIntervalo = request.form.get('intervaloInicio')
    finalIntervalo = request.form.get('finalIntervalo')
    initAno, initMes = inicioIntervalo.split(
        '-') if inicioIntervalo else [None, None]
    endAno, endMes = finalIntervalo.split(
        '-') if finalIntervalo else [None, None]

    if insumos:
        for ins in insumos:
            if ins in insumos:
                fn = globals()[ins]
                fn(mes, ano)

    if initAno and initMes and endAno and endMes and insumosIntervalo:
        if int(f"{initMes}{initAno}") > int(f"{endMes}{endAno}"):
            initMes = endMes
            initAno = endAno

        for ins in insumosIntervalo:
            if ins in insumosIntervalo:
                fn = globals()[ins]
                fn(mes, ano, initMes, initAno, endMes, endAno)

    todasOpcoes = opcoes.copy()
    todasOpcoes.extend(opcoesComRange)
    todosInsumos = insumos.copy()

    if initAno and initMes and endAno and endMes:
        todosInsumos.extend(insumosIntervalo)

    opcoesView = []
    for ins in todosInsumos:
        item = next(it for it in todasOpcoes if it[0] == ins)
        if existe_insumo(ins, mes, ano):
            opcoesView.append(item)

    return render_template('gerar_relatorio_resultado.html', opcoes=opcoesView, mes=mes, ano=ano)


@gerar_relatorio_bp.route('/ver_insumo/<mes>/<ano>/<arquivo>')
def ver_insumo(mes, ano, arquivo):
    pathFile = os.path.join(
        current_app.config['DIRSYS'],
        IdEmpreend().get(),
        f"{ano}_{mes}",
        arquivo
    )
    if os.path.exists(f"{pathFile}.png"):
        return send_file(f"{pathFile}.png")
    elif os.path.exists(f"{pathFile}.jpg"):
        return send_file(f"{pathFile}.jpg")


def graf_orcamento_liberacao_valor(mes, ano):
    try:
        medC = orcamentoController()
        medS = medC.consultarOrcamentoPelaVigencia(
            IdEmpreend().get(), mes, ano)
        if medS:
            gerar_graf_orcamento_liberacao(
                IdEmpreend().get(), mes, ano, 'valor', medS)
        else:
            flash_message.warning(
                'Não há dados para gerar o gráfico de orçamento de liberação de valor')
    except Exception as error:
        logger.error(
            'Erro ao gerar o gráfico de orçamento de liberação de valor', error)
        flash_message.error(
            'Erro ao gerar o gráfico de orçamento de liberação de valor')


def tab_conta_corrente(mes, ano):
    try:
        conC = contaController()
        conS = conC.consultarContaPelaVigencia(IdEmpreend().get(), mes, ano)
        if conS:
            gerar_tab_conta_corrente(IdEmpreend().get(), mes, ano, conS)
        else:
            flash_message.warning(
                'Não há dados para gerar a tabela de contas corrente')
    except Exception as error:
        logger.error(
            'Erro ao gerar a tabela de contas correntes', error)
        flash_message.error('Erro ao gerar a tabela de contas correntes')


def tab_notas(mes, ano):
    try:
        notC = notaController()
        notS = notC.consultarNotaPelaVigencia(IdEmpreend().get(), mes, ano)
        if notS:
            gerar_tab_notas(IdEmpreend().get(), mes, ano, notS)
        else:
            flash_message.warning('Não há dados para gerar a tabela de notas')
    except Exception as error:
        logger.error(
            'Erro ao gerar a tabela de notas', error)
        flash_message.error('Erro ao gerar a tabela de notas')


def tab_orcamento_liberacao(mes, ano):
    try:
        medC = orcamentoController()
        medS = medC.consultarOrcamentoPelaVigencia(IdEmpreend().get(), mes, ano)
        if medS:
            gerar_tab_orcamento_liberacao(IdEmpreend().get(), mes, ano, medS)
        else:
            flash_message.warning(
                'Não há dados para gerar a tabela de orçamento liberação')
    except Exception as error:
        logger.error(
            'Erro ao gerar a tabela de orçamento liberação', error)
        flash_message.error('Erro ao gerar a tabela de orçamento liberação')


def tab_acomp_financeiro(mes, ano):
    try:
        finC = orcamentoController()
        finS = finC.consultarOrcamentoPelaVigencia(IdEmpreend().get(), mes, ano)

        notC = notaController()
        notS = notC.consultarNotaPelaVigencia(IdEmpreend().get(), mes, ano)

        if finS:
            gerar_tab_acomp_financeiro(IdEmpreend().get(), mes, ano, finS, notS)
        else:
            flash('Não há dados para gerar a tabela de acompanhamento financeiro')
    except Exception as error:
        logger.error(
            'Erro ao gerar tabela de acompanhamento financeiro', error)
        flash_message.error(
            'Erro ao gerar tabela de acompanhamento financeiro')


def graf_indices_garantia_I(mes, ano, mesInit, anoInit, mesFinal, anoFinal):
    try:
        gerar_graf_indices_garantia_I(
            IdEmpreend().get(), mes, ano, mesInit, anoInit, mesFinal, anoFinal)
    except Exception as error:
        logger.error('Erro ao gerar gráfico de índices de garantia I', error)
        flash_message.error('Erro ao gerar gráfico de índices de garantia I')


def graf_indices_garantia_II(mes, ano, mesInit, anoInit, mesFinal, anoFinal):
    try:
        gerar_graf_indices_garantia_II(
            IdEmpreend().get(), mes, ano, mesInit, anoInit, mesFinal, anoFinal)
    except Exception as error:
        logger.error('Erro ao gerar gráfico de índices de garantia II', error)
        flash_message.error('Erro ao gerar gráfico de índices de garantia II')


def graf_progresso_obra(mes, ano, mesInit, anoInit, mesFinal, anoFinal):
    try:
        gerar_graf_progresso_obra(
            IdEmpreend().get(), mes, ano, mesInit, anoInit, mesFinal, anoFinal)
    except Exception as error:
        logger.error('Erro ao gerar gráfico do progresso da obra', error)
        flash_message.error('Erro ao gerar gráfico do progresso da obra')


def tab_medicoes(mes, ano, mesInit, anoInit, mesFinal, anoFinal):
    try:
        gerar_tab_medicoes(IdEmpreend().get(), mes, ano,
                           mesInit, anoInit, mesFinal, anoFinal)
    except Exception as error:
        logger.error('Erro a tabela de medições', error)
        flash_message.error('Erro a tabela de medições')


def graf_chaves_perc(mes, ano):
    try:
        if not gerar_graf_chaves(IdEmpreend().get(), mes, ano, 'perc'):
            flash_message.warning(
                'Não foram encontrados dados para gerar o gráfico de chaves ')
    except Exception as error:
        logger.error('Erro ao gerar o gráfico de chaves (%)', error)
        flash_message.error('Erro ao gerar o gráfico de chaves (%)')

def graf_chaves_valor(mes, ano):
    try:
        if not gerar_graf_chaves(IdEmpreend().get(), mes, ano, 'valor'):
            flash_message.warning(
                'Não foram encontrados dados para gerar o gráfico de chaves (R$)')
    except Exception as error:
        logger.error('Erro ao gerar o gráfico de chaves (R$)', error)
        flash_message.error('Erro ao gerar o gráfico de chaves (R$)')


def graf_vendas_perc(mes, ano):
    try:
        gerar_graf_vendas(IdEmpreend().get(), mes, ano, 'perc')
    except Exception as error:
        logger.error('Erro ao gerar o gráfico de vendas (%)', error)
        flash_message.error('Erro ao gerar o gráfico de vendas (%)')


def graf_vendas_valor(mes, ano):
    try:
        gerar_graf_vendas(IdEmpreend().get(), mes, ano, 'valor')
    except Exception as error:
        logger.error('Erro ao gerar o gráfico de vendas (R$)', error)
        flash_message.error('Erro ao gerar o gráfico de vendas (R$)')


def tab_certidoes(mes, ano):
    try:
        gerar_tab_certidoes(IdEmpreend().get(), mes, ano)
    except Exception as error:
        logger.error(
            'Erro ao gerar a tabela de certidões', error)
        flash_message.error('Erro ao gerar a tabela de certidões')


def tab_garantias_geral(mes, ano):
    try:
        gerar_tab_garantias_geral(IdEmpreend().get(), mes, ano)
    except Exception as error:
        logger.error(
            'Erro ao gerar a tabela de garantias gerais', error)
        flash_message.error('Erro ao gerar a tabela de garantias gerais')


def tab_garantias_obra(mes, ano):
    try:
        gerar_tab_garantias_obra(IdEmpreend().get(), mes, ano)
    except Exception as error:
        logger.error(
            'Erro ao gerar a tabela de garantias da obra', error)
        flash_message.error('Erro ao gerar a tabela de garantias da obra')


def existe_insumo(nome, mes, ano):
    file = getDir(os.path.join(f"{ano}_{mes}", nome))
    return os.path.exists(f"{file}.jpg") or os.path.exists(f"{file}.png")


def getDir(path=None):
    nPath = os.path.join(current_app.config['DIRSYS'], IdEmpreend().get())
    if path is not None:
        nPath = os.path.join(nPath, path)
    return os.path.normpath(nPath)
