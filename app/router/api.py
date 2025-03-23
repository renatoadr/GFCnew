from flask import Blueprint, request, jsonify
from controller.clienteController import clienteController
from utils.helper import is_logged

api_bp = Blueprint('api', __name__)

@api_bp.route('/api/clientes', methods=['GET'])
def get_clientes_api():
  if not is_logged():
    return jsonify([])
  search = request.args.get('search')
  cliC = clienteController()
  cliS = cliC.consultarClientes(search.lower())
  newList = list(map(lambda it: it.to_json(), cliS))
  return jsonify(newList)

@api_bp.route('/api/cliente/<doc>', methods=['GET'])
def get_cliente_api(doc):
  if not is_logged():
    return jsonify([])
  cliC = clienteController()
  cli = cliC.consultarClientePeloId(doc)
  return jsonify(cli.to_json())
