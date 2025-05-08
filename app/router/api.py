from flask import Blueprint, request, jsonify
from controller.clienteController import clienteController
from utils.security import login_required_api

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
