from flask import Blueprint, request, render_template, redirect, current_app, flash, send_file

from controller.orcamentoController import orcamentoController
from router.graficos import gerar_graf_orcamento_liberacao, gerar_graf_indices_garantia_I, gerar_graf_indices_garantia_II, gerar_graf_chaves, gerar_graf_vendas, gerar_graf_progresso_obra
from controller.contaController import contaController
from controller.notaController import notaController
from router.tabelas import gerar_tab_conta_corrente, gerar_tab_notas, gerar_tab_orcamento_liberacao, gerar_tab_acomp_financeiro, gerar_tab_certidoes, gerar_tab_garantias_geral, gerar_tab_garantias_obra, gerar_tab_medicoes, gerar_tab_prazo_inter, gerar_tab_projeto_inter, gerar_tab_qualidade_inter, gerar_tab_seguranca_inter, gerar_tab_situacao_inter, gerar_tab_empreend_capa
from utils.security import login_required
from utils.CtrlSessao import IdEmpreend, NmEmpreend, CodBanco, Vigencia
from utils.flash_message import flash_message
from utils.logger import logger
from datetime import datetime
import os

gerar_relatorios_bp = Blueprint('gerar_relatorios', __name__)

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


class OpcoesView:
    opcoes = []
    opcoesComRange = []


vopt = OpcoesView()


def existeEmOpcoes(nome):
    for opt in opcoes:
        if opt[0] == nome:
            return True
    return False


@gerar_relatorios_bp.route('/gerar_insumos_relatorios', methods=['GET'])
@login_required
def gerar_relatorio():
    idEmpreend = request.args.get("idEmpreend")
    nmEmpreend = request.args.get("nmEmpreend")
    codBanco = int(request.args.get("codBanco")
                   ) if request.args.get("codBanco") else None

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

    if codBanco is None:
        codBanco = CodBanco().get()
    else:
        CodBanco().set(codBanco)

    vopt.opcoes = opcoes.copy()
    vopt.opcoesComRange = opcoesComRange.copy()

    if codBanco == 77:
        prazo = ['tab_prazo_inter', 'Tabela de Prazo', 'Não']
        projeto = ['tab_projeto_inter', 'Tabela de Projeto', 'Não']
        qualidade = ['tab_qualidade_inter', 'Tabela de Qualidade', 'Não']
        seguranca = ['tab_seguranca_inter', 'Tabela de Segurança', 'Não']
        situacao = ['tab_situacao_inter', 'Tabela de Situação', 'Não']

        if not existeEmOpcoes('tab_prazo_inter'):
            vopt.opcoes.append(prazo)
        if not existeEmOpcoes('tab_projeto_inter'):
            vopt.opcoes.append(projeto)
        if not existeEmOpcoes('tab_qualidade_inter'):
            vopt.opcoes.append(qualidade)
        if not existeEmOpcoes('tab_seguranca_inter'):
            vopt.opcoes.append(seguranca)
        if not existeEmOpcoes('tab_situacao_inter'):
            vopt.opcoes.append(situacao)

    vig = Vigencia().get()

    for opt in vopt.opcoes:
        opt[2] = 'Sim' if existe_insumo(opt[0], vig[1], vig[0]) else 'Não'

    for opt in vopt.opcoesComRange:
        opt[2] = 'Sim' if existe_insumo(opt[0], vig[1], vig[0]) else 'Não'

    return render_template(
        'gerar_relatorio.html',
        opcoesComRange=vopt.opcoesComRange,
        opcoes=vopt.opcoes,
    )


@gerar_relatorios_bp.route('/gerar_insumos', methods=['POST', 'GET'])
def gerar_insumos():
    insumos = request.form.getlist('opcoes_relatorio')
    insumosIntervalo = request.form.getlist('opcoes_relatorio_range')

    vig = Vigencia().get()

    if not insumos and not insumosIntervalo:
        return redirect('/gerar_insumos_relatorios')

    inicioIntervalo = request.form.get('intervaloInicio')
    finalIntervalo = request.form.get('finalIntervalo')
    initAno, initMes = inicioIntervalo.split(
        '-') if inicioIntervalo else [None, None]
    endAno, endMes = finalIntervalo.split(
        '-') if finalIntervalo else [None, None]

    todasOpcoes = vopt.opcoes.copy()
    todasOpcoes.extend(vopt.opcoesComRange.copy())

    if len(todasOpcoes) == 0:
        return redirect('/gerar_insumos_relatorios')

    if CodBanco().get() == 77:
        gerar_tab_empreend_capa(IdEmpreend().get(), vig[1], vig[0])

    if insumos:
        for ins in insumos:
            if ins in insumos:
                fn = globals()[ins]
                fn(vig[1], vig[0])

    if initAno and initMes and endAno and endMes and insumosIntervalo:
        if datetime(int(initAno), int(initMes), 1) > datetime(int(endAno), int(endMes), 1):
            initMes = endMes
            initAno = endAno

        for ins in insumosIntervalo:
            if ins in insumosIntervalo:
                fn = globals()[ins]
                fn(vig[1], vig[0], initMes, initAno, endMes, endAno)

    todosInsumos = insumos.copy()

    if initAno and initMes and endAno and endMes:
        todosInsumos.extend(insumosIntervalo)

    opcoesView = []
    for ins in todosInsumos:
        if existe_insumo(ins, vig[1], vig[0]):
            item = next(it for it in todasOpcoes if it[0] == ins)
            opcoesView.append(item)

    return render_template(
        'gerar_relatorio_resultado.html',
        opcoes=opcoesView,
    )


@gerar_relatorios_bp.route('/ver_insumo/<arquivo>')
def ver_insumo(arquivo):
    pathFile = os.path.join(
        current_app.config['DIRSYS'],
        IdEmpreend().get(),
        '_'.join(Vigencia().get()),
        arquivo
    )
    if os.path.exists(f"{pathFile}.png"):
        return send_file(f"{pathFile}.png")
    elif os.path.exists(f"{pathFile}.jpg"):
        return send_file(f"{pathFile}.jpg")


def tab_situacao_inter(mes, ano):
    try:
        gerar_tab_situacao_inter(IdEmpreend().get(), mes, ano)
    except Exception as error:
        logger.exception(
            'Erro ao gerar a tabela de situação do inter', error)
        flash_message.error('Erro ao gerar a tabela de situação do Inter')


def tab_seguranca_inter(mes, ano):
    try:
        gerar_tab_seguranca_inter(IdEmpreend().get(), mes, ano)
    except Exception as error:
        logger.exception(
            'Erro ao gerar a tabela de segurança do inter', error)
        flash_message.error('Erro ao gerar a tabela de segurança do Inter')


def tab_qualidade_inter(mes, ano):
    try:
        gerar_tab_qualidade_inter(IdEmpreend().get(), mes, ano)
    except Exception as error:
        logger.exception(
            'Erro ao gerar a tabela de qualidade do inter', error)
        flash_message.error('Erro ao gerar a tabela de qualidade do Inter')


def tab_projeto_inter(mes, ano):
    try:
        gerar_tab_projeto_inter(IdEmpreend().get(), mes, ano)
    except Exception as error:
        logger.exception(
            'Erro ao gerar a tabela de projeto do inter', error)
        flash_message.error('Erro ao gerar a tabela de projeto do Inter')


def tab_prazo_inter(mes, ano):
    try:
        gerar_tab_prazo_inter(IdEmpreend().get(), mes, ano, 77)
    except Exception as error:
        logger.exception(
            'Erro ao gerar a tabela de prazos do inter', error)
        flash_message.error('Erro ao gerar a tabela de prazos do Inter')


def graf_orcamento_liberacao_valor(mes, ano):
    try:
        medC = orcamentoController()
        medS = medC.consultarOrcamentoPelaVigencia(
            IdEmpreend().get(), mes, ano)
        if medS:
            medS.reverse()
            gerar_graf_orcamento_liberacao(
                IdEmpreend().get(), mes, ano, 'valor', medS)
        else:
            flash_message.warning(
                'Não há dados para gerar o gráfico de orçamento de liberação de valor')
    except Exception as error:
        logger.exception(
            'Erro ao gerar o gráfico de orçamento de liberação de valor', error)
        flash_message.error(
            'Erro ao gerar o gráfico de orçamento de liberação de valor')


def tab_conta_corrente(mes, ano):
    try:
        conC = contaController()
        conS = conC.consultarContaPelaVigencia(IdEmpreend().get(), mes, ano)
        if conS:
            gerar_tab_conta_corrente(
                IdEmpreend().get(), mes, ano, conS, CodBanco().get())
        else:
            flash_message.warning(
                'Não há dados para gerar a tabela de contas corrente')
    except Exception as error:
        logger.exception(
            'Erro ao gerar a tabela de contas correntes', error)
        flash_message.error('Erro ao gerar a tabela de contas correntes')


def tab_notas(mes, ano):
    try:
        notC = notaController()
        notS = notC.consultarNotaPelaVigencia(IdEmpreend().get(), mes, ano)
        if notS:
            gerar_tab_notas(IdEmpreend().get(), mes,
                            ano, notS, CodBanco().get())
        else:
            flash_message.warning('Não há dados para gerar a tabela de notas')
    except Exception as error:
        logger.exception(
            'Erro ao gerar a tabela de notas', error)
        flash_message.error('Erro ao gerar a tabela de notas')


def tab_orcamento_liberacao(mes, ano):
    try:
        medC = orcamentoController()
        medS = medC.consultarOrcamentoPelaVigencia(
            IdEmpreend().get(), mes, ano)
        if medS:
            gerar_tab_orcamento_liberacao(
                IdEmpreend().get(), mes, ano, medS, CodBanco().get())
        else:
            flash_message.warning(
                'Não há dados para gerar a tabela de orçamento liberação')
    except Exception as error:
        logger.exception(
            'Erro ao gerar a tabela de orçamento liberação', error)
        flash_message.error('Erro ao gerar a tabela de orçamento liberação')


def tab_acomp_financeiro(mes, ano):
    try:
        finC = orcamentoController()
        finS = finC.consultarOrcamentoPelaVigencia(
            IdEmpreend().get(), mes, ano)

        notC = notaController()
        notS = notC.consultarNotaPelaVigencia(IdEmpreend().get(), mes, ano)

        if finS:
            gerar_tab_acomp_financeiro(
                IdEmpreend().get(), mes, ano, finS, notS)
        else:
            flash('Não há dados para gerar a tabela de acompanhamento financeiro')
    except Exception as error:
        logger.exception(
            'Erro ao gerar tabela de acompanhamento financeiro', error)
        flash_message.error(
            'Erro ao gerar tabela de acompanhamento financeiro')


def graf_indices_garantia_I(mes, ano, mesInit, anoInit, mesFinal, anoFinal):
    try:
        if not gerar_graf_indices_garantia_I(
                IdEmpreend().get(), mes, ano, mesInit, anoInit, mesFinal, anoFinal):
            flash_message.warning(
                'Não foram encontrados dados para gerar o gráfico de índices de garantias I')
    except Exception as error:
        logger.exception(
            'Erro ao gerar gráfico de índices de garantia I', error)
        flash_message.error('Erro ao gerar gráfico de índices de garantia I')


def graf_indices_garantia_II(mes, ano, mesInit, anoInit, mesFinal, anoFinal):
    try:
        if not gerar_graf_indices_garantia_II(
                IdEmpreend().get(), mes, ano, mesInit, anoInit, mesFinal, anoFinal):
            flash_message.warning(
                'Não foram encontrados dados para gerar o gráfico de índices de garantias II')
    except Exception as error:
        logger.exception(
            'Erro ao gerar gráfico de índices de garantia II', error)
        flash_message.error('Erro ao gerar gráfico de índices de garantia II')


def graf_progresso_obra(mes, ano, mesInit, anoInit, mesFinal, anoFinal):
    try:
        if not gerar_graf_progresso_obra(
                IdEmpreend().get(), mes, ano, mesInit, anoInit, mesFinal, anoFinal):
            flash_message.warning(
                'Não foram encontrados dados para gerar o gráfico de progresso da obra')
    except Exception as error:
        logger.exception('Erro ao gerar gráfico do progresso da obra', error)
        flash_message.error('Erro ao gerar gráfico do progresso da obra')


def tab_medicoes(mes, ano, mesInit, anoInit, mesFinal, anoFinal):
    try:
        if not gerar_tab_medicoes(
            IdEmpreend().get(), mes, ano,
            mesInit, anoInit, mesFinal, anoFinal,
            CodBanco().get()
        ):
            flash_message.warning(
                'Não foram encontrados dados para gerar a tabela de medições')
    except Exception as error:
        logger.exception('Erro a tabela de medições', error)
        flash_message.error('Erro a tabela de medições')


def graf_chaves_perc(mes, ano):
    try:
        if not gerar_graf_chaves(IdEmpreend().get(), mes, ano, 'perc'):
            flash_message.warning(
                'Não foram encontrados dados para gerar o gráfico de chaves ')
    except Exception as error:
        logger.exception('Erro ao gerar o gráfico de chaves (%)', error)
        flash_message.error('Erro ao gerar o gráfico de chaves (%)')


def graf_chaves_valor(mes, ano):
    try:
        if not gerar_graf_chaves(IdEmpreend().get(), mes, ano, 'valor'):
            flash_message.warning(
                'Não foram encontrados dados para gerar o gráfico de chaves (R$)')
    except Exception as error:
        logger.exception('Erro ao gerar o gráfico de chaves (R$)', error)
        flash_message.error('Erro ao gerar o gráfico de chaves (R$)')


def graf_vendas_perc(mes, ano):
    try:
        if not gerar_graf_vendas(IdEmpreend().get(), mes, ano, 'perc'):
            flash_message.warning(
                'Não foram encontrados dados para gerar o gráfico de vendas (%)')
    except Exception as error:
        logger.exception('Erro ao gerar o gráfico de vendas (%)', error)
        flash_message.error('Erro ao gerar o gráfico de vendas (%)')


def graf_vendas_valor(mes, ano):
    try:
        if not gerar_graf_vendas(IdEmpreend().get(), mes, ano, 'valor'):
            flash_message.warning(
                'Não foram encontrados dados para gerar o gráfico de vendas (R$)')
    except Exception as error:
        logger.exception('Erro ao gerar o gráfico de vendas (R$)', error)
        flash_message.error('Erro ao gerar o gráfico de vendas (R$)')


def tab_certidoes(mes, ano):
    try:
        if not gerar_tab_certidoes(IdEmpreend().get(), mes, ano, CodBanco().get()):
            flash_message.warning(
                'Não foram encontrados dados para gerar a tabela de certidões')
    except Exception as error:
        logger.exception(
            'Erro ao gerar a tabela de certidões', error)
        flash_message.error('Erro ao gerar a tabela de certidões')


def tab_garantias_geral(mes, ano):
    try:
        if not gerar_tab_garantias_geral(IdEmpreend().get(), mes, ano, CodBanco().get()):
            flash_message.warning(
                'Não foram encontrados dados para gerar a tabela de garantias gerais')
    except Exception as error:
        logger.exception(
            'Erro ao gerar a tabela de garantias gerais', error)
        flash_message.error('Erro ao gerar a tabela de garantias gerais')


def tab_garantias_obra(mes, ano):
    try:
        if not gerar_tab_garantias_obra(IdEmpreend().get(), mes, ano, CodBanco().get()):
            flash_message.warning(
                'Não foram encontrados dados para gerar a tabela de garantias de obra')
    except Exception as error:
        logger.exception(
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
