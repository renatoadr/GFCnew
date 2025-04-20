from flask import Blueprint, request, render_template, redirect, url_for, flash

from utils.CtrlSessao import IdEmpreend, NmEmpreend
from utils.helper import protectedPage
from controller.consideracaoController import consideracaoController
import datetime

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

    mes = request.args.get('mes')
    ano = request.args.get('ano')

    if mes is None:
        mes = str(datetime.date.today().month).zfill(2)
    if ano is None:
        ano = datetime.date.today().year

    ctrl = consideracaoController()
    consid = ctrl.listar_campos(IdEmpreend().get(), mes, ano)
    return render_template("consideracoes.html", consid=consid, ano=ano, mes=mes)


@consideracoes_bp.route('/atualizar_consideracoes', methods=['POST'])
def atualizar_consideracoes():
    campos = request.form.to_dict()
    mes = request.args.get('mes')
    ano = request.args.get('ano')
    ctrl = consideracaoController()
    ctrl.insert_registros(campos, IdEmpreend().get(), mes, ano)
    return redirect('/home')
