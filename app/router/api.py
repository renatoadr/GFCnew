from flask import Blueprint, request, jsonify
from core.request_bot import RequestBot
from controller.clienteController import clienteController
from controller.agendaController import agendaController
from utils.security import login_required_api
from utils.CtrlSessao import IdEmpreend

api_bp = Blueprint('api', __name__)


@api_bp.route('/api/clientes', methods=['GET'])
@login_required_api
def get_clientes_api():
    search = request.args.get('search')
    cliC = clienteController()
    cliS = cliC.consultarClientes(search.lower())
    newList = list(map(lambda it: it.to_json(), cliS))
    return jsonify(newList)


@api_bp.route('/api/cliente/<doc>', methods=['GET'])
@login_required_api
def get_cliente_api(doc):
    cliC = clienteController()
    cli = cliC.consultarClientePeloId(doc)
    return jsonify(cli.to_json())


@api_bp.route('/api/agenda/<cur_date>', methods=['GET'])
@login_required_api
def get_agenda_api(cur_date):
    ctrl = agendaController()
    agendas = ctrl.consultarAgendas(IdEmpreend().get(), cur_date)
    newList = list(map(lambda it: it.to_json(), agendas))
    return jsonify(newList)


@api_bp.route('/api/agenda/deletar/<id>', methods=['GET'])
@login_required_api
def deletar_agenda_api(id):
    try:
        ctrl = agendaController()
        ctrl.excluirAgenda(id)
        return jsonify({'deletado': True})
    except:
        return jsonify({'deletado': False})
