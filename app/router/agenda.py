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

    agendaC = agendaController()
    agendaS = agendaC.consultarAgendas(idEmpreend)

    return render_template("lista_agendas.html", agendaS=agendaS)



@agenda_bp.route('/abrir_cad_agenda')
def abrir_cad_agenda():
  agendaC = agendaController()
  atividades = agendaC.lista_atividades()
  return render_template("cad_agenda.html", atividades=atividades)


@agenda_bp.route('/cadastrar_agenda', methods=['POST'])
def cadastrar_agenda():
    ag = agenda()
    ag.setIdEmpreend(IdEmpreend().get())
    ag.setAnoVigencia(request.form.get('anoVigencia'))
    ag.setMesVigencia(request.form.get('mesVigencia'))
    ag.setIdAtividade(request.form.get('atividade'))
    ag.setStatus(request.form.get('status'))
    ag.setDtAtividade(request.form.get('dtAtividade'))
    ag.setNmRespAtividade(request.form.get('responsavel'))
    ag.setDtBaixa(request.form.get('dtBaixa'))
    ag.setNmRespBaixa(request.form.get('responsavelBaixa'))

    agendaC = agendaController()
    agendaC.inserirAgenda(ag)

    return redirect("/tratar_agendas")


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
