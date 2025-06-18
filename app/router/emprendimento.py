from flask import Blueprint, request, render_template, redirect
from controller.empreendimentoController import empreendimentoController
from utils.security import login_required
from dto.empreendimento import empreendimento
import utils.converter as converter
from controller.bancoController import bancoController
from utils.security import get_user_logged

emprendimento_bp = Blueprint('empreendimentos', __name__)

ctrlBanco = bancoController()
empc = empreendimentoController()


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
        usa_filtro=usa_filtro,
        lista_bancos=lista_bancos,
        fitlro_banco_selecionado=int(filtro_banco) if filtro_banco else None
    )


@emprendimento_bp.route('/abrir_cad_empreend')
@login_required
def abrir_cad_empreend():

    bancos = ctrlBanco.lista_bancos()
    return render_template("cad_empreend.html", bancos=bancos)


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
    return render_template("cad_empreend.html", empreend=empreend, bancos=bancos)


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
