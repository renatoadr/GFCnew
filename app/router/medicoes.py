from flask import Blueprint, request, render_template, redirect, session, current_app
from utils.CtrlSessao import IdEmpreend, NmEmpreend, DtCarga, IdMedicao
from controller.medicaoController import medicaoController
from utils.helper import allowed_file, protectedPage
from werkzeug.utils import secure_filename
from dto.medicao import medicao
import utils.converter as converter
import os

medicoes_bp = Blueprint('medicoes', __name__)

@medicoes_bp.route('/tratar_medicoes')
def tratar_medicoes():
    protectedPage()

 #   idMedicao = request.args.get("idMedicao")
 #   IdMedicao().set(idMedicao)

    idEmpreend = request.args.get("idEmpreend")
    nmEmpreend = request.args.get('nmEmpreend')

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

    print('-----tratar_medicoes----')
    print(idEmpreend, nmEmpreend)

    medC = medicaoController()
    medS = medC.consultarMedicoes(idEmpreend)

    if len(medS) == 0:
        return render_template("lista_medicoes.html", mensagem="Medição não Cadastrada, importar o arquivo Excel!!!", medicoes=medS)
    else:
        return render_template("lista_medicoes.html", medicoes=medS)

@medicoes_bp.route('/consultar_medicao_pelo_id')
def consultar__medicao_pelo_id():

    idMedicao = request.args.get("idMedicao")
    IdMedicao().set(idMedicao)

    print('------ consultar_medicao_pelo_ID ------')
    print(idMedicao)

    medC = medicaoController()
    medS = medC.consultarMedicaoPeloId(idMedicao)

    print('------ consultar_medicao_pelo_id fim --------')
    
    print(medS.getNrMedicao())

    return render_template("medicao_item.html", medicao=medS)

@medicoes_bp.route('/upload_arquivo_medicoes', methods=['GET', 'POST'])
def upload_arquivo_medicoes():
    # check if the post request has the file part
    if 'file' not in request.files:
        mensagem = "Erro no upload do arquivo. No file part."
        return render_template("erro.html", mensagem=mensagem)
    file = request.files['file']
    if file:
        if file.filename == '':
            mensagem = "Erro no upload do arquivo. Nome do arquivo='" + file.filename + "'."
        elif not allowed_file(file.filename):
            mensagem = "Erro no upload do arquivo. Arquivo='" + \
                file.filename + "' não possui uma das extensões permitidas."
        else:
            filename = secure_filename(file.filename)
            caminhoArq = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)
            file.save(caminhoArq)

<<<<<<< Updated upstream
#            idEmpreend = request.args.get("idEmpreend")
=======
>>>>>>> Stashed changes
            idEmpreend = IdEmpreend().get()

            print('-------------- upload_arquivo_medicoes ----------------')

            orcC = medicaoController()
            print(caminhoArq, '   ', idEmpreend)
            orcC.carregar_medicoes(caminhoArq, idEmpreend)

            return redirect("/tratar_medicoes")
    else:
        mensagem = "Erro no upload do arquivo. Você precisa selecionar um arquivo."
    return render_template("erro.html", mensagem=mensagem)

@medicoes_bp.route('/excluir_medicao')
def excluir_medicao():
  idMedicao = request.args.get('idMedicao')
  ctrlMed = medicaoController()
  ctrlMed.excluir_medicao(idMedicao)
  return redirect('/tratar_medicoes')

@medicoes_bp.route('/salvar_item_medicao', methods=['POST'])
def salvar_item_medicao():
    med = medicao ()
    med.setIdMedicao(request.form.get('idMedicao'))
    med.setIdEmpreend(request.form.get('idEmpreend'))
    med.setMesVigencia(request.form.get('mesVigencia'))
    med.setAnoVigencia(request.form.get('anoVigencia'))
    med.setDtCarga(request.form.get('dtCarga'))
    med.setNrMedicao(request.form.get('nrMedicao'))
    med.setPercPrevistoAcumulado(converter.converterStrToFloat(request.form.get('percPrevistoAcumulado')))
    med.setPercRealizadoAcumulado(converter.converterStrToFloat(request.form.get('percRealizadoAcumulado')))
    med.setPercDiferenca(converter.converterStrToFloat(request.form.get('percDiferenca')))
    med.setPercPrevistoPeriodo(converter.converterStrToFloat(request.form.get('percPrevistoPeriodo')))
    med.setPercRealizadoPeriodo(converter.converterStrToFloat(request.form.get('percRealizadoPeriodo')))

    medC = medicaoController()
    medC.salvarItemMedicao(med)

    return redirect('/tratar_medicoes')
