from flask import Blueprint, request, render_template, redirect, url_for, flash

from utils.CtrlSessao import IdEmpreend, NmEmpreend
from utils.helper import protectedPage
from controller.consideracaoController import consideracaoController

consideracoes_bp = Blueprint('consideracoes', __name__)


@consideracoes_bp.route('/consideracoes')
def tratartorres():
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

    ctrl = consideracaoController()
    consid = ctrl.listar_campos(IdEmpreend().get())
    return render_template("consideracoes.html", consid=consid)


@consideracoes_bp.route('/atualizar_consideracoes', methods=['POST'])
def atualizar_consideracoes():
    campos = request.form.to_dict()
    ctrl = consideracaoController()
    ctrl.insert_registros(campos, IdEmpreend().get())
    return redirect('/home')
