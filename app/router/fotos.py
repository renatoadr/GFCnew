from flask import Blueprint, request, render_template, current_app
from controller.graficoController import graficoController

foto_bp = Blueprint('fotos', __name__)

@foto_bp.route('/upload_fotos')
def upload_fotos():
    return render_template("upload_fotos.html")

@foto_bp.route('/upload_arquivo_fotos', methods=['POST'])
def upload_arquivo_fotos():

    grafC = graficoController(current_app)

# verifique se a solicitação de postagem tem a parte do arquivo
    if 'file' not in request.files:
        mensagem = "Erro no upload do arquivo. No file part."
        return render_template("erro.html", mensagem=mensagem)

    id_empreend = str(42)
    anoMes = "2024_12"

    diretorio = current_app['DIRSYS'] + id_empreend + \
        current_app['BARRADIR'] + anoMes + current_app['BARRADIR']
    grafC.criaDir(diretorio)

    files = request.files.getlist("file")

    for file in files:
        file.save(diretorio + file.filename)
#        file.save(current_app['UPLOAD_FOLDER'] + '\\' + file.filename)

#    print('é aqui Rodrigo !!!!!!!!')

    return render_template("erro.html", mensagem=mensagem)
