from flask import Blueprint, request, render_template, redirect

from utils.CtrlSessao import IdEmpreend, NmEmpreend, Vigencia
from controller.aspectosController import aspectosController
from utils.security import login_required

aspectos_bp = Blueprint('aspectos', __name__)
ctrl = aspectosController()


@aspectos_bp.route('/aspectos_obra')
@login_required
def tratar_aspectos_obra():

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

    aspectos = ctrl.todasPerguntasComRespostas(
        IdEmpreend().get(),
        Vigencia().getMonth(),
        Vigencia().getYear()
    )
    return render_template(
        "aspectos.html",
        aspectos=aspectos,
    )


@aspectos_bp.route('/atualizar_aspectos', methods=['POST'])
def atualizar_aspectos():
    campos = request.form.to_dict()
    ctrl.salvar_aspectos(
        campos,
        IdEmpreend().get(),
        Vigencia().getMonth(),
        Vigencia().getYear()
    )
    return redirect('/home')
