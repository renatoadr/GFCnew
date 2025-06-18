from flask import Blueprint, request, render_template, redirect
from controller.agendaAtividadeController import agendaAtividadeController
from controller.empreendimentoController import empreendimentoController
from controller.agendaController import agendaController
from utils.CtrlSessao import IdEmpreend, NmEmpreend
from utils.flash_message import flash_message
from enums.status_agenda import StatusAgenda
from utils.security import login_required
from dto.option import option
from dto.agenda import agenda
from dateutil import relativedelta
from datetime import datetime


agenda_bp = Blueprint('agendas', __name__)

agdAtivCtrl = agendaAtividadeController()
empCtrl = empreendimentoController()
agdCtrl = agendaController()


@agenda_bp.route('/tratar_agendas')
@login_required
def tratar_agendas():
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

    return render_template("lista_agendas.html")


@agenda_bp.route('/abrir_cad_agenda')
@login_required
def abrir_cad_agenda():
    listStatus = []

    for sts in StatusAgenda.to_list():
        listStatus.append(option(sts[0], sts[1]))

    atividades = agdAtivCtrl.lista_atividades()
    emp = empCtrl.consultarEmpreendimentoPeloId(IdEmpreend().get())

    idT = request.args.get("id")
    agenda = None
    if idT:
        agenda = agdCtrl.consultarAgendaPeloId(idT)
        if not agenda:
            flash_message.error(
                'Não foi possível encontrar a agenda com o id informado')
            return redirect('/tratar_agendas')

    return render_template(
        "cad_agenda.html",
        previsao=emp.getPrevisaoEntrega(),
        atividades=atividades,
        listStatus=listStatus,
        agenda=agenda,
    )


@agenda_bp.route('/salvar_agenda', methods=['POST'])
def cadastrar_agenda():
    id = request.form.get('idAgenda')
    ag = mapeamento(
        request.form.get('vigencia'),
        request.form.get('dtAtividade'),
        request.form.get('status')
    )
    if id:
        agdCtrl.salvarAgenda(ag, id)
    else:
        rec = request.form.get('recorrencia')
        if rec is not None:
            agendas = prepararRecorrencia(ag)
            # agdCtrl.inserirAgendas(agendas)
        else:
            agdCtrl.inserirAgendas([ag])

    return redirect("/tratar_agendas")


def prepararRecorrencia(inicio):
    tipoRec = request.form.get('recTipo')
    nSalto = request.form.get('saltarSeq')
    dtAte = request.form.get('dtRecAte')

    agendas = [inicio]

    if not nSalto or not dtAte:
        return agendas

    rodadas = 1
    nSalto = int(nSalto)
    dtCorrente = datetime.strptime(request.form.get('dtAtividade'), '%Y-%m-%d')
    dtAteLimite = datetime.strptime(dtAte, '%Y-%m-%d')

    if tipoRec == 'year':
        dtLimite = dtCorrente + relativedelta.relativedelta(years=nSalto)
    elif tipoRec == 'month':
        dtLimite = dtCorrente + relativedelta.relativedelta(months=nSalto)
    elif tipoRec == 'semana':
        dtLimite = dtCorrente + relativedelta.relativedelta(weeks=nSalto)
    elif tipoRec == 'day':
        dtLimite = dtCorrente + relativedelta.relativedelta(days=nSalto)

    while rodadas <= nSalto and dtCorrente <= dtLimite and dtCorrente < dtAteLimite:
        if tipoRec == 'year':
            dtCorrente = dtCorrente + relativedelta.relativedelta(years=1)
        elif tipoRec == 'month':
            dtCorrente = dtCorrente + relativedelta.relativedelta(months=1)
        elif tipoRec == 'semana':
            dtCorrente = dtCorrente + relativedelta.relativedelta(weeks=1)
        elif tipoRec == 'day':
            dtCorrente = dtCorrente + relativedelta.relativedelta(days=1)

        agendas.append(mapeamento(
            format(dtCorrente, '%Y-%m'),
            format(dtCorrente, '%Y-%m-%d'),
            StatusAgenda.NAO_INICIADO
        ))
        rodadas += 1

    return agendas


def mapeamento(vigencia: str, dtAtividade: str, status: str):
    vig = vigencia.split('-')

    ag = agenda()
    ag.setStatus(status)
    ag.setAnoVigencia(vig[0])
    ag.setMesVigencia(vig[1])
    ag.setDtAtividade(dtAtividade)
    ag.setIdEmpreend(IdEmpreend().get())
    ag.setDtBaixa(request.form.get('dtBaixa'))
    ag.setIdAtividade(request.form.get('atividade'))
    ag.setNmRespAtividade(request.form.get('responsavel'))
    ag.setNmRespBaixa(request.form.get('responsavelBaixa'))

    return ag
