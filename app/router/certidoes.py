from flask import Blueprint, request, render_template, redirect
from controller.certidaoController import certidaoController
from utils.security import login_required
from utils.CtrlSessao import IdEmpreend, NmEmpreend
from dto.certidao import certidao
from datetime import datetime

certidoes_bp = Blueprint('certidoes', __name__)


@certidoes_bp.route('/tratar_certidoes')
@login_required
def tratar_certidoes():

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

    certC = certidaoController()
    certS = certC.consultarCertidoes(idEmpreend)

    if len(certS) == 0:
        return render_template(
            "certidoes.html",
            mensagem="Certidões não Cadastradas!!!",
            certidoes=certS,
            minDate='2000-01',
            maxDate=datetime.now().strftime('%Y-%m')
        )
    else:
        return render_template(
            "certidoes.html",
            certidoes=certS[0],
            minDate='2000-01',
            maxDate=datetime.now().strftime('%Y-%m')
        )


@certidoes_bp.route('/efetuar_cad_certidoes', methods=['POST'])
def efetuar_cad_certidoes():
    cert = get_form_data()
    certC = certidaoController()
    certC.inserirCertidoes(cert)
    return redirect("/home")


@certidoes_bp.route('/salvar_certidoes', methods=['POST'])
def salvar_certidoes():
    item = get_form_data()
    certC = certidaoController()
    certC.salvarCertidoes(item)
    return redirect("/home")


@certidoes_bp.route('/gerar_relatorio_certidoes', methods=['POST'])
def gerar_relatorio_certidoes():
    idEmpreend = IdEmpreend().get()
    vigencia = request.form.get('vigencia')

    if not vigencia:
        vigencia = datetime.now().strftime('%Y-%m')

    vigencia = vigencia.split('-')
    mesVigencia = vigencia[1]
    anoVigencia = vigencia[0]

    return redirect(f'/tab_certidoes?idEmpreend={idEmpreend}&mesVigencia={mesVigencia}&anoVigencia={anoVigencia}')


def get_form_data():
    estadualValidate = request.form.get('estadualValidade')
    fgtsValidate = request.form.get('fgtsValidade')
    municipalValidate = request.form.get('municipalValidade')
    inssValidate = request.form.get('srfInssValidade')
    trabalhistaValidate = request.form.get('trabalhistaValidade')

    item = certidao()
    item.setIdEmpreend(IdEmpreend().get())
    item.setEstadualStatus(request.form.get('estadualStatus'))
    item.setEstadualValidade(None if estadualValidate ==
                             '' else estadualValidate)
    item.setFgtsStatus(request.form.get('fgtsStatus'))
    item.setFgtsValidade(None if fgtsValidate ==
                         '' else fgtsValidate)
    item.setMunicipalStatus(request.form.get('municipalStatus'))
    item.setMunicipalValidade(None if municipalValidate ==
                              '' else municipalValidate)
    item.setSrfInssStatus(request.form.get('srfInssStatus'))
    item.setSrfInssValidade(None if inssValidate ==
                            '' else inssValidate)
    item.setTrabalhistaStatus(request.form.get('trabalhistaStatus'))
    item.setTrabalhistaValidade(None if trabalhistaValidate ==
                                '' else trabalhistaValidate)
    return item
