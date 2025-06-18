from flask import Blueprint, request, render_template, redirect

from utils.CtrlSessao import IdEmpreend, NmEmpreend
from controller.aspectosController import aspectosController
from utils.security import login_required
from datetime import datetime

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

    vigencia = request.args.get('vigencia')
    if not vigencia:
        vigencia = datetime.now().strftime('%Y-%m')
    vig = vigencia.split('-')

    aspectos = ctrl.todasPerguntasComRespostas(
        IdEmpreend().get(),
        vig[1],
        vig[0]
    )
    return render_template(
        "aspectos.html",
        aspectos=aspectos,
        minDate='2000-01',
        maxDate=datetime.now().strftime('%Y-%m'),
        vigencia=vigencia
    )


@aspectos_bp.route('/atualizar_aspectos', methods=['POST'])
def atualizar_aspectos():
    campos = request.form.to_dict()
    vigencia = request.args.get('vigencia')
    if not vigencia:
        vigencia = datetime.now().strftime('%Y-%m')
    vig = vigencia.split('-')
    ctrl.salvar_aspectos(campos, IdEmpreend().get(), vig[1], vig[0])
    return redirect('/home')
