from flask import Blueprint, request, render_template, redirect

from utils.CtrlSessao import IdEmpreend, NmEmpreend
from controller.consideracaoController import consideracaoController
from utils.security import login_required
from datetime import datetime

consideracoes_bp = Blueprint('consideracoes', __name__)


@consideracoes_bp.route('/consideracoes')
@login_required
def tratartorres():

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

    vigencia = request.args.get('vigencia')
    if not vigencia:
        vigencia = datetime.now().strftime('%Y-%m')
    vig = vigencia.split('-')

    ctrl = consideracaoController()
    consid = ctrl.listar_campos(IdEmpreend().get(), vig[1], vig[0])
    return render_template(
        "consideracoes.html",
        consid=consid,
        minDate='2000-01',
        maxDate=datetime.now().strftime('%Y-%m'),
        vigencia=vigencia
    )


@consideracoes_bp.route('/atualizar_consideracoes', methods=['POST'])
def atualizar_consideracoes():
    campos = request.form.to_dict()
    vigencia = request.args.get('vigencia')
    if not vigencia:
        vigencia = datetime.now().strftime('%Y-%m')
    vig = vigencia.split('-')
    ctrl = consideracaoController()
    ctrl.insert_registros(campos, IdEmpreend().get(), vig[1], vig[0])
    return redirect('/home')
