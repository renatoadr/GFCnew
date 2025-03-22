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

    if (not IdEmpreend().has() or not NmEmpreend().has()) and (idEmpreend is None or nmEmpreend is None):
      return redirect('/home')

    if idEmpreend:
      IdEmpreend().set(idEmpreend)
    else:
      idEmpreend = IdEmpreend().get()

    if nmEmpreend:
      NmEmpreend().set(nmEmpreend)
    else:
      nmEmpreend = NmEmpreend().get()

    print('-----tratar_contas----')
    print(idEmpreend, nmEmpreend)

    contC = contaController ()
    contS = contC.consultarContas(idEmpreend)

    if len(contS) == 0:
        return render_template("lista_contas.html", mensagem="Conta não Cadastrada, importar o arquivo Excel!!!", contas=contS)
    else:
        return render_template("lista_contas.html", contas=contS)
