from flask import Blueprint, request, render_template, redirect, current_app
from controller.contaController import contaController
from utils.helper import allowed_file, protectedPage
from utils.CtrlSessao import IdEmpreend, NmEmpreend
from werkzeug.utils import secure_filename
import os

contas_corrente_bp = Blueprint('contas_corrente', __name__)

@contas_corrente_bp.route('/upload_arquivo_contas', methods=['POST'])
def upload_arquivo_contas():
    # check if the post request has the file part
    if 'file' not in request.files:
        mensagem = "Erro no upload do arquivo. No file part."
        return render_template("erro.html", mensagem=mensagem)
    file = request.files['file']
    if file:
        if file.filename == '':
            mensagem = "Erro no upload do arquivo. Nome do arquivo='" + file.filename + "'."
        elif not allowed_file(file.filename):
            mensagem = "Erro no upload do arquivo. Arquivo='" + file.filename + "' não possui uma das extensões permitidas."
        else:
            filename = secure_filename(file.filename)
            caminhoArq = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)
            file.save(caminhoArq)

#            idEmpreend = request.args.get("idEmpreend")
#            idEmpreend = request.form.get("idEmpreend")
            idEmpreend = IdEmpreend().get()

            print ('-------------- upload_arquivo_contas ----------------')

            notC = contaController ()
            print (caminhoArq, '   ', idEmpreend)
            notC.carregar_contas(caminhoArq, idEmpreend)

            return redirect("/tratar_contas")
    else:
        mensagem = "Erro no upload do arquivo. Você precisa selecionar um arquivo."
    return render_template("erro.html", mensagem=mensagem)

@contas_corrente_bp.route('/tratar_contas')
def tratar_contas():
    protectedPage()

    idEmpreend = request.args.get("idEmpreend")
    nmEmpreend = request.args.get("nmEmpreend")

    if (idEmpreend is None and not IdEmpreend().has()) or (nmEmpreend is None and not NmEmpreend().has()):
      redirect('/home')

    if idEmpreend is None:
      idEmpreend = IdEmpreend().get()
    else:
      IdEmpreend().set(idEmpreend)

    if nmEmpreend is None:
      nmEmpreend = NmEmpreend().get()
    else:
      NmEmpreend().set(nmEmpreend)

    print('-----tratar_contas----')
    print(idEmpreend, nmEmpreend)

    contC = contaController ()
    contS = contC.consultarContas(idEmpreend)

    if len(contS) == 0:
        return render_template("lista_contas.html", mensagem="Conta não Cadastrada, importar o arquivo Excel!!!", contas=contS)
    else:
        return render_template("lista_contas.html", contas=contS)

@contas_corrente_bp.route('/consultar_conta_data')
def consultar_conta():
  pass

@contas_corrente_bp.route('/excluir_conta')
def excluir_conta():
  mes = request.args.get('mesV')
  ano = request.args.get('anoV')
  data = request.args.get('dtCarga')
  contC = contaController ()
  contC.excluir_por_data(data, mes, ano)
  return redirect('/tratar_contas')
