from flask import Blueprint, request, render_template, redirect
from controller.agendaAtividadeController import agendaAtividadeController
from utils.security import login_required, permission_access
from utils.flash_message import flash_message
from dto.agenda_atividade import agenda_atividade
from enums.tipo_acessos import TipoAcessos

agenda_atividades_bp = Blueprint('agenda_atividades', __name__)

ctrl = agendaAtividadeController()


@agenda_atividades_bp.route('/agenda_atividades')
@login_required
@permission_access([TipoAcessos.RT, TipoAcessos.ADM])
def agenda_atividades():
    atividades = ctrl.lista_atividades()
    return render_template("lista_atividades_agenda.html", atividades=atividades, hideVig=True)


@agenda_atividades_bp.route('/editar_atividade')
@login_required
@permission_access([TipoAcessos.RT, TipoAcessos.ADM])
def editar_atividade():
    id = request.args.get('id')
    atividade = ctrl.buscar_pelo_id(id)
    return render_template("cad_agenda_atividade.html", atividade=atividade, novo=False, hideVig=True)


@agenda_atividades_bp.route('/cadastrar_atividade', methods=['POST'])
@login_required
@permission_access([TipoAcessos.RT, TipoAcessos.ADM])
def cadastrar_atividade():
    id = request.form.get('idAtividade')
    desc = request.form.get('nmAtividade')
    if ctrl.existe(id):
        atividade = agenda_atividade(id, desc)
        flash_message.error('Essa identificação já existe.')
        return render_template("cad_agenda_atividade.html", atividade=atividade, novo=True)
    else:
        ctrl.cadastrar_atividade(id, desc)
        return redirect("/agenda_atividades")


@agenda_atividades_bp.route('/salvar_atividade', methods=['POST'])
@login_required
@permission_access([TipoAcessos.RT, TipoAcessos.ADM])
def salvar_atividade():
    id = request.form.get('idAtividade')
    desc = request.form.get('nmAtividade')
    idAntiga = request.form.get('idAnterior')
    if ctrl.existe(id):
        atividade = agenda_atividade(id, desc)
        flash_message.error('Essa identificação já existe.')
        return render_template("cad_agenda_atividade.html", atividade=atividade, novo=False)
    else:
        ctrl.salvar_atividade(id, desc, idAntiga)
        return redirect("/agenda_atividades")


@agenda_atividades_bp.route('/abrir_cad_atividade')
@login_required
@permission_access([TipoAcessos.RT, TipoAcessos.ADM])
def abrir_cad_atividade():
    return render_template("cad_agenda_atividade.html", atividade=None, novo=True, hideVig=True)


@agenda_atividades_bp.route('/excluir_atividade')
@login_required
@permission_access([TipoAcessos.RT, TipoAcessos.ADM])
def excluir_atividade():
    id = request.args.get('id')
    if id and ctrl.existe(id):
        ctrl.apagar(id)
    return redirect("/agenda_atividades")
