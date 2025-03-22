from flask import Blueprint, request, render_template, redirect, jsonify
from controller.clienteController import clienteController
from utils.helper import protectedPage, is_logged
import utils.converter as converter
from dto.cliente import cliente

cliente_bp = Blueprint('clientes', __name__)

@cliente_bp.route('/tratar_clientes')
def tratarclientes():
    protectedPage()

    cliC = clienteController ()
    cliS = cliC.consultarClientes ()

    if len(cliS) == 0:
        return render_template("lista_clientes.html", clienteS=cliS)
    else:
        return render_template("lista_clientes.html", clienteS=cliS)

@cliente_bp.route('/abrir_cad_cliente')
def abrir_cad_cliente():
    return render_template("cliente.html")

@cliente_bp.route('/cadastrar_cliente', methods=['POST'])
def cadastrar_cliente():
  cli = cliente ()
  cli.setCpfCnpj (converter.removeAlpha(request.form.get('cpfCnpj')))
  cli.setTpCpfCnpj (request.form.get('tpCpfCnpj'))
  cli.setNmCliente (request.form.get('nmCliente'))
  cli.setDdd (request.form.get('ddd'))
  cli.setTel (converter.removeAlpha(request.form.get('tel')))
  cli.setEmail (request.form.get('email'))

  cliC = clienteController()
  cliC.inserirCliente(cli)

  return redirect("/tratar_clientes")

@cliente_bp.route('/editar_cliente')
def editar_cliente():
  idCli = request.args.get("cpfCnpj")
  cliC = clienteController ()
  cliente = cliC.consultarClientePeloId (idCli)
  return render_template("cliente.html", cliente=cliente)

@cliente_bp.route('/salvar_alteracao_cliente', methods=['POST'])
def salvar_alteracao_cliente():
  cli = cliente ()
  cli.setCpfCnpj (converter.removeAlpha(request.form.get('cpfCnpj')))
  cli.setTpCpfCnpj (request.form.get('tpCpfCnpj'))
  cli.setNmCliente (request.form.get('nmCliente'))
  cli.setDdd (request.form.get('ddd'))
  cli.setTel (converter.removeAlpha(request.form.get('tel')))
  cli.setEmail (request.form.get('email'))

  cliC = clienteController()
  cliC.salvarCliente(cli)

  return redirect("/tratar_clientes")

@cliente_bp.route('/excluir_cliente')
def excluir_cliente():

    idCli = request.args.get('cpfCnpj')
#    idEmpreend = request.args.get('idEmpreend')

    print('--------------excluir_cliente -------------')
    print (idCli)

    cliC = clienteController()
    cliC.excluirCliente(idCli)
    cliS = cliC.consultarClientes ()

    return render_template("lista_clientes.html", clienteS=cliS)


########## API #########
@cliente_bp.route('/api/clientes', methods=['GET'])
def get_clientes_api():
  if not is_logged():
    return jsonify([])
  search = request.args.get('search')
  cliC = clienteController()
  cliS = cliC.consultarClientes(search.lower())
  newList = list(map(lambda it: it.to_json(), cliS))
  return jsonify(newList)

@cliente_bp.route('/api/cliente/<doc>', methods=['GET'])
def get_cliente_api(doc):
  if not is_logged():
    return jsonify([])
  cliC = clienteController()
  cli = cliC.consultarClientePeloId(doc)
  return jsonify(cli.to_json())
