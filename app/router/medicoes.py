from flask import Blueprint, request, render_template, redirect
from utils.CtrlSessao import IdEmpreend, NmEmpreend, IdMedicao
from controller.medicaoController import medicaoController
from werkzeug.utils import secure_filename
from utils.security import login_required
from utils.helper import allowed_file
import utils.converter as converter
from dto.medicao import medicao
from datetime import datetime
import os

medicoes_bp = Blueprint('medicoes', __name__)


@medicoes_bp.route('/tratar_medicoes')
@login_required
def tratar_medicoes():

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
        return render_template(
            "lista_medicoes.html",
            mensagem="Medição não Cadastrada, importar o arquivo Excel!!!",
            medicoes=medS,
            minDate='2000-01',
            maxDate=datetime.now().strftime('%Y-%m')
        )
    else:
        medCurrent = None
        medPrevius = None
        for idx in range(0, len(medS)):
            if medS[idx].getPercRealizadoAcumulado() == 0:
                medCurrent = medS[idx]
                if idx > 0:
                    medPrevius = medS[idx-1]
                break
        return render_template(
            "lista_medicoes.html",
            medicoes=medS,
            medCurrent=medCurrent,
            medPrevius=medPrevius,
            minDate='2000-01',
            maxDate=datetime.now().strftime('%Y-%m')
        )


@medicoes_bp.route('/consultar_medicao_pelo_id')
@login_required
def consultar__medicao_pelo_id():
    idMedicao = request.args.get("idMedicao")
    IdMedicao().set(idMedicao)

    medC = medicaoController()
    medS = medC.consultarMedicaoPeloId(idMedicao)
    medOld = medC.consultarMedicaoAnteriorPeloId(IdEmpreend().get(), idMedicao)

    if not medOld:
        medS.setPercRealizadoAcumulado(
            medS.getPercRealizadoAcumulado() if medS.getPercRealizadoAcumulado() is not None else 0
        )
    else:
        medS.setPercRealizadoAcumulado(medOld.getPercRealizadoAcumulado())

    return render_template("medicao_item.html", medicao=medS)


@medicoes_bp.route('/upload_arquivo_medicoes', methods=['GET', 'POST'])
@login_required
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
            pathTemp = os.path.join(os.environ.get('temp'), 'gfc')

            if not os.path.exists(pathTemp):
                os.makedirs(pathTemp)

            caminhoArq = os.path.join(pathTemp, filename)

            if os.path.isfile(caminhoArq):
                os.remove(caminhoArq)

            file.save(caminhoArq)

            idEmpreend = IdEmpreend().get()
            orcC = medicaoController()
            print(caminhoArq, '   ', idEmpreend)
            orcC.carregar_medicoes(caminhoArq, idEmpreend)

        return redirect("/tratar_medicoes")
    else:
        mensagem = "Erro no upload do arquivo. Você precisa selecionar um arquivo."
        return render_template("erro.html", mensagem=mensagem)


@medicoes_bp.route('/excluir_medicao')
@login_required
def excluir_medicao():
    idMedicao = request.args.get('idMedicao')
    ctrlMed = medicaoController()
    ctrlMed.excluir_medicao(idMedicao)
    return redirect('/tratar_medicoes')


@medicoes_bp.route('/salvar_item_medicao', methods=['POST'])
def salvar_item_medicao():
    med = medicao()
    med.setIdMedicao(request.form.get('idMedicao'))
    med.setIdEmpreend(request.form.get('idEmpreend'))
    med.setMesVigencia(request.form.get('mesVigencia'))
    med.setAnoVigencia(request.form.get('anoVigencia'))
    med.setDtCarga(request.form.get('dtCarga'))
    med.setNrMedicao(request.form.get('nrMedicao'))
    med.setPercPrevistoAcumulado(converter.converterStrToFloat(
        request.form.get('percPrevistoAcumulado')))
    med.setPercRealizadoAcumulado(converter.converterStrToFloat(
        request.form.get('percRealizadoAcumulado')))
    med.setPercDiferenca(converter.converterStrToFloat(
        request.form.get('percDiferenca')))
    med.setPercPrevistoPeriodo(converter.converterStrToFloat(
        request.form.get('percPrevistoPeriodo')))
    med.setPercRealizadoPeriodo(converter.converterStrToFloat(
        request.form.get('percRealizadoPeriodo')))

    med.setPercRealizadoAcumulado(
        med.getPercRealizadoPeriodo() + med.getPercRealizadoAcumulado())
    med.setPercDiferenca(med.getPercRealizadoAcumulado() -
                         med.getPercPrevistoAcumulado())
    med.setDataMedicao(request.form.get('dtMedicao'))

    medC = medicaoController()
    medC.salvarItemMedicao(med)

    return redirect('/tratar_medicoes')


@medicoes_bp.route('/gerar_relatorio_medicoes', methods=['POST'])
def gerar_relatorio_medicoes():
    idEmpreend = IdEmpreend().get()
    tipo = request.form.get('tipo')

    vig = request.form.get('vigencia')
    if not vig:
        vig = datetime.now().strftime('%Y-%m')
    vig = vig.split('-')

    vigInit = request.form.get('vigenciaInicial')
    if not vigInit:
        vigInit = datetime.now().strftime('%Y-%m')
    vigInit = vigInit.split('-')

    vigEnd = request.form.get('vigenciaFinal')
    if not vigEnd:
        vigEnd = datetime.now().strftime('%Y-%m')
    vigEnd = vigEnd.split('-')

    if tipo == 'tabela':
        return redirect(f'/tab_medicoes?idEmpreend={idEmpreend}&mesVigencia={vig[1]}&anoVigencia={vig[0]}&mesInicio={vigInit[1]}&anoInicio={vigInit[0]}&mesFinal={vigEnd[1]}&anoFinal={vigEnd[0]}')
    else:
        return redirect(f'/graf_progresso_obra?idEmpreend={idEmpreend}&mesVigencia={vig[1]}&anoVigencia={vig[0]}&mesInicio={vigInit[1]}&anoInicio={vigInit[0]}&mesFinal={vigEnd[1]}&anoFinal={vigEnd[0]}')
