from flask import Blueprint, request, render_template, redirect, current_app
from controller.notaController import notaController
from utils.helper import protectedPage, allowed_file
from utils.CtrlSessao import IdEmpreend, NmEmpreend

nota_bp = Blueprint('notas', __name__)


@nota_bp.route('/upload_arquivo_notas', methods=['POST'])
def upload_arquivo_notas():
    # check if the post request has the file part
    if 'file' not in request.files:
        mensagem = "Erro no upload do arquivo. No file part."
        return render_template("erro.html", mensagem=mensagem)
    file = request.files['file']
    if file:
        if file.filename == '':
            mensagem = "Erro no upload do arquivo. Nome do arquivo='" + file.filename + "'."
        elif not allowed_file(file.filename):
            mensagem = "Erro no upload do arquivo. Arquivo '"
            mensagem += file.filename + "' não possui uma das extensões permitidas."
        else:
            idEmpreend = IdEmpreend().get()
            notC = notaController()
            notC.carregar_notas(file, idEmpreend)
            return redirect("/tratar_notas")
    else:
        mensagem = "Erro no upload do arquivo. Você precisa selecionar um arquivo."
    return render_template("erro.html", mensagem=mensagem)


@nota_bp.route('/tratar_notas')
def tratar_notas():
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

    print('-----tratar_notas----')
    print(idEmpreend, nmEmpreend)

    notC = notaController()
    notS = notC.consultarNotas(idEmpreend)

    if len(notS) == 0:
        return render_template("lista_notas.html", mensagem="Nota não Cadastrada, importar o arquivo Excel!!!", notas=notS)
    else:
        return render_template("lista_notas.html", notas=notS)


@nota_bp.route('/excluir_nota_carga')
def excluir_nota():
    mes = request.args.get('mesV')
    ano = request.args.get('anoV')
    data = request.args.get('dtCarga')
    contC = notaController()
    contC.excluir_por_data(IdEmpreend().get(), data, mes, ano)
    return redirect('/tratar_notas')
