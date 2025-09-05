from flask import Blueprint, request, render_template, redirect

from utils.CtrlSessao import IdEmpreend, NmEmpreend, Vigencia
from controller.consideracaoController import consideracaoController
from utils.security import login_required

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

    ctrl = consideracaoController()
    consid = ctrl.listar_campos(
        IdEmpreend().get(),
        Vigencia().getMonth(),
        Vigencia().getYear()
    )
    return render_template(
        "consideracoes.html",
        consid=consid,
    )


@consideracoes_bp.route('/atualizar_consideracoes', methods=['POST'])
@login_required
def atualizar_consideracoes():
    campos = request.form.to_dict()
    ctrl = consideracaoController()
    ctrl.insert_registros(
        campos,
        IdEmpreend().get(),
        Vigencia().getMonth(),
        Vigencia().getYear()
    )
    return redirect('/home')
