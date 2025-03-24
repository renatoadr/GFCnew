from flask import Blueprint, request, render_template, redirect
from controller.empreendimentoController import empreendimentoController
from controller.empreendimentoController import empreendimentoController
from controller.agendaController import agendaController
from utils.helper import protectedPage
from dto.agenda import agenda
from utils.CtrlSessao import IdEmpreend, NmEmpreend

agenda_bp = Blueprint('agendas', __name__)

@agenda_bp.route('/tratar_agendas')
def tratar_agendas():
    protectedPage()
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

    print('-----tratar_agendas----')
    print(idEmpreend, nmEmpreend)

    agendaC = agendaController()
    agendaS = agendaC.consultarAgendas(idEmpreend)

    if len(agendaS) == 0:
        return render_template("lista_agendas.html", idEmpreend=idEmpreend, mensagem="Agenda não cadastrada!!!", nmEmpreend=nmEmpreend, agendaS=agendaS)
    else:
        return render_template("lista_agendas.html", idEmpreend=idEmpreend, nmEmpreend=nmEmpreend, agendaS=agendaS)


@agenda_bp.route('/abrir_cad_agenda', methods=['POST'])
def abrir_cad_agenda():

    idEmpreend = request.form.get("idEmpreend")
    nmEmpreend = request.form.get("nmEmpreend")

    print('-----------abrir_cad_agenda-----------')
    print(idEmpreend)

    return render_template("agenda.html", idEmpreend=idEmpreend, nmEmpreend=nmEmpreend)


@agenda_bp.route('/cadastrar_agenda', methods=['POST'])
def cadastrar_agenda():

    print('passei aqui 1')
    nmEmpreend = request.form.get('nmEmpreend')

    t = agenda()
    t.setIdEmpreend(request.form.get('idEmpreend'))
    t.setNmAgenda(request.form.get('nmAgenda'))
    t.setQtUnidade(request.form.get('qtUnidade'))

    print('passei aqui 2')

    agendaC = agendaController()
    agendaC.inserirAgenda(t)

    idEmpreend = request.form.get('idEmpreend')
    agendaS = agendaC.consultarAgendas(idEmpreend)
    print('passei aqui')
    return render_template("lista_agendas.html", agendaS=agendaS, nmEmpreend=nmEmpreend)


@agenda_bp.route('/editar_agenda')
def editar_agenda():

    idT = request.args.get("idAgenda")
    idEmpreend = request.args.get("idEmpreend")
    nmEmpreend = request.args.get("nmEmpreend")

    print('------ editar_agenda --------')
    print(idT, nmEmpreend)

    agendaC = agendaController()
    agenda = agendaC.consultarAgendaPeloId(idT)

    print(agenda)
    return render_template("agenda.html", agenda=agenda, idEmpreend=idEmpreend, nmEmpreend=nmEmpreend)


@agenda_bp.route('/salvar_alteracao_agenda', methods=['POST'])
def salvar_alteracao_agenda():

    print('------- salvar_alteracao_agenda INICIO --------')
    nmEmpreend = request.form.get("nmEmpreend")

    t = agenda()
    t.setIdAgenda(request.form.get('idAgenda'))
    t.setIdEmpreend(request.form.get('idEmpreend'))
    t.setNmAgenda(request.form.get('nmAgenda'))
    t.setQtUnidade(request.form.get('qtUnidade'))

    print('------- salvar_alteracao_agenda --------')
    idEmpreend = request.form.get('idEmpreend')
    print(idEmpreend)

    agendaC = agendaController()
    agendaC.salvarAgenda(t)

    agendaS = agendaC.consultarAgendas(idEmpreend)
    return render_template("lista_agendas.html", idEmpreend=idEmpreend, nmEmpreend=nmEmpreend, agendaS=agendaS)


@agenda_bp.route('/consultar_agenda')
def consultar_agenda():

    modo = request.args.get("modo")
    idT = request.args.get("idAgenda")
    idEmpreend = request.args.get("idEmpreend")
    nmEmpreend = request.args.get("nmEmpreend")

    print('------ consultar_agenda --------')
    print(modo, idT, idEmpreend, nmEmpreend)

    agendac = agendaController()
    agenda = agendac.consultarAgendaPeloId(idT)
    print(agenda)

    print('------ consultar_agenda --------')
    print(modo)

    return render_template("agenda.html", agenda=agenda, modo=modo, idEmpreend=idEmpreend, nmEmpreend=nmEmpreend)


@agenda_bp.route('/excluir_agenda')
def excluir_agenda():

    idAgenda = request.args.get('idAgenda')
    idEmpreend = request.args.get('idEmpreend')
    nmEmpreend = request.args.get('nmEmpreend')

    print('--------------excluir_agenda -------------')
    print(idAgenda, idEmpreend)

    agendaC = agendaController()
    agendaC.excluirAgenda(idAgenda)
    agendaS = agendaC.consultarAgendas(idEmpreend)

    if len(agendaS) == 0:
        empc = empreendimentoController()
        emps = empc.consultarEmpreendimentos()
        return render_template("home.html", empreends=emps)
    else:
        return render_template("lista_agendas.html", agendaS=agendaS, idEmpreend=idEmpreend, nmEmpreend=nmEmpreend)
