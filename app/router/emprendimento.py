from flask import Blueprint, request, render_template, redirect
import datetime

from controller.empreendimentoController import empreendimentoController
from controller.bancoController import bancoController
from dto.empreendimento import empreendimento
from utils.security import get_user_logged
from utils.security import login_required, login_required_api
from utils.CtrlSessao import Vigencia
from utils.logger import logger
import utils.converter as converter
import json
import threading
from core.sync_elonet.run_sync_elonet import RunSyncElonet
from main import app

emprendimento_bp = Blueprint('empreendimentos', __name__)

ctrlBanco = bancoController()
empc = empreendimentoController()

msg_sync_elonet: dict = {
    "main_task_message": None,
    "sub_task_message": None,
    "error": None,
    "in_progress": False
}


@emprendimento_bp.route('/alterar_vigencia', methods=['POST'])
def alterar_vigencia():
    vigenciaField = request.form.get('vigencia')

    if not vigenciaField:
        vigenciaField = datetime.now().strftime('%Y-%m')

    Vigencia().save(vigenciaField)

    return redirect(request.referrer)


@emprendimento_bp.route('/home')
@login_required
def abrir_home():
    filtro_banco = request.args.get('filtro_banco')
    sUser = get_user_logged()
    lista_bancos = ctrlBanco.lista_bancos()

    usa_filtro = True
    if sUser.codBank and sUser.codBank != '0':
        usa_filtro = False

    if usa_filtro and filtro_banco:
        emps = empc.consultarEmpreendimentos(filtro_banco)
    else:
        emps = empc.consultarEmpreendimentos(sUser.codBank)

    return render_template(
        "home.html",
        empreends=emps,
        hideVig=True,
        usa_filtro=usa_filtro,
        lista_bancos=lista_bancos,
        fitlro_banco_selecionado=int(filtro_banco) if filtro_banco else None
    )


@emprendimento_bp.route('/abrir_cad_empreend')
@login_required
def abrir_cad_empreend():

    bancos = ctrlBanco.lista_bancos()
    return render_template("cad_empreend.html", bancos=bancos, hideVig=True)


@emprendimento_bp.route('/efetuar_cad_empreend', methods=['POST'])
def efetuar_cad_empreend():
    empreend = empreendimento()
    empreend.setApelido(request.form.get('apelido'))
    empreend.setNmEmpreend(request.form.get('nmEmpreendimento'))
    empreend.setCodBanco(request.form.get('codBanco'))
    empreend.setNmIncorp(request.form.get('nmIncorp'))
    empreend.setNmConstrutor(request.form.get('nmConstrutor'))
    empreend.setLogradouro(request.form.get('logradouro'))
    empreend.setBairro(request.form.get('bairro'))
    empreend.setCidade(request.form.get('cidade'))
    empreend.setEstado(request.form.get('estado'))
    empreend.setCep(converter.removeAlpha(request.form.get('cep')))
    empreend.setCpfCnpjEngenheiro(request.form.get('cpfCnpjEngenheiro'))
    empreend.setVlPlanoEmp(converter.converterStrToFloat(
        request.form.get('vlPlanoEmp')))
    empreend.setIndiceGarantia(converter.converterStrToFloat(
        request.form.get('indiceGarantia')))
    empreend.setPrevisaoEntrega(request.form.get('previsaoEntrega'))

    empc.inserirEmpreendimento(empreend)
    return redirect("/home")


@emprendimento_bp.route('/excluir_empreend')
@login_required
def excluir_empreend():
    idEmpreend = request.args.get('idEmpreend')
    print(idEmpreend)
    empc.excluirEmpreendimento(idEmpreend)
    return redirect("/home")


@emprendimento_bp.route('/abrir_edicao_empreend')
@login_required
def abrir_edicao_empreend():
    idEmpreend = request.args.get('idEmpreend')
    bancos = ctrlBanco.lista_bancos()
    empreend = empc.consultarEmpreendimentoPeloId(idEmpreend)
    return render_template("cad_empreend.html", empreend=empreend, bancos=bancos, hideVig=True)


@emprendimento_bp.route('/salvar_empreend', methods=['POST'])
def salvar_empreend():
    empreend = empreendimento()
    empreend.setApelido(request.form.get('apelido'))
    empreend.setIdEmpreend(int(request.form.get('idEmpreendimento')))
    empreend.setNmEmpreend(request.form.get('nmEmpreendimento'))
    empreend.setCodBanco(request.form.get('codBanco'))
    empreend.setNmIncorp(request.form.get('nmIncorp'))
    empreend.setNmConstrutor(request.form.get('nmConstrutor'))
    empreend.setLogradouro(request.form.get('logradouro'))
    empreend.setBairro(request.form.get('bairro'))
    empreend.setCidade(request.form.get('cidade'))
    empreend.setEstado(request.form.get('estado'))
    empreend.setCep(converter.removeAlpha(request.form.get('cep')))
    empreend.setCpfCnpjEngenheiro(request.form.get('cpfCnpjEngenheiro'))
    empreend.setVlPlanoEmp(converter.converterStrToFloat(
        request.form.get('vlPlanoEmp')))
    empreend.setIndiceGarantia(converter.converterStrToFloat(
        request.form.get('indiceGarantia')))
    empreend.setPrevisaoEntrega(request.form.get('previsaoEntrega'))

    empc.salvarEmpreendimento(empreend)
    return redirect("/home")


@emprendimento_bp.route('/sincronizar_elonet')
@login_required_api
def sincronizar_elonet():
    global msg_sync_elonet
    msg_sync_elonet = {
        "main_task_message": None,
        "sub_task_message": None,
        "error": None,
        "in_progress": True
    }
    t = threading.Thread(target=worker_sync_elonet)
    t.start()
    return json.dumps({"message": "Sincronização com Elonet iniciada..."})


@emprendimento_bp.route('/status_sync_elonet')
def status_sync_elonet():
    return json.dumps(msg_sync_elonet)


def worker_sync_elonet():
    global msg_sync_elonet
    try:
        with app.app_context():
            runner = RunSyncElonet()
            for message in runner.start():
                msg_sync_elonet = message
                logger.info(f'Status Sync Elonet: {msg_sync_elonet}')
            msg_sync_elonet = {
                "main_task_message": None,
                "sub_task_message": None,
                "error": None,
                "in_progress": False
            }
    except Exception as e:
        logger.exception(f'Erro durante a sincronização Elonet: {e}')
        msg_sync_elonet = {
            "main_task_message": None,
            "sub_task_message": None,
            "error": "Ocorreu um erro durante a sincronização. Por favor, tente novamente mais tarde.",
            "in_progress": False
        }
