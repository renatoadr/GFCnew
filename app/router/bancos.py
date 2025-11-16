from flask import Blueprint, request, render_template, redirect

from controller.bancoController import bancoController
from utils.security import login_required
from dto.banco import banco

bancos_bp = Blueprint('bancos', __name__)


@bancos_bp.route('/tratar_bancos')
@login_required
def tratarbancos():
    usrCtrl = bancoController()
    banks = usrCtrl.lista_bancos()
    return render_template("lista_bancos.html", bancos=banks, hideVig=True)


@bancos_bp.route('/abrir_cad_banco')
@login_required
def abrir_cad_banco():
    return render_template("banco.html", hideVig=True)


@bancos_bp.route('/cadastrar_banco', methods=['POST'])
def cadastrar_bancos():
    banco = getForm()
    ctrlUser = bancoController()
    ctrlUser.cadastrar_banco(banco)

    return redirect('/tratar_bancos')


@bancos_bp.route('/editar_banco')
@login_required
def editar_bancos():
    codBanco = request.args.get("cod")
    ctrlBanco = bancoController()
    banco = ctrlBanco.get_banco_pelo_id(codBanco)
    if banco is None:
        return redirect('/tratar_bancos')

    return render_template("banco.html", banco=banco, hideVig=True)


@bancos_bp.route('/salvar_alteracao_banco', methods=['POST'])
def salvar_alteracao_bancos():
    banco = getForm()
    ctrlBanco = bancoController()
    ctrlBanco.atulizar_banco(banco)
    return redirect("/tratar_bancos")


@bancos_bp.route('/excluir_banco')
def excluir_bancos():
    codBanco = request.args.get('cod')
    cliC = bancoController()
    cliC.excluir_banco(codBanco)
    return redirect("/tratar_bancos")


def getForm() -> banco:
    bank = banco()
    bank.setIspb(request.form.get('ispb'))
    bank.setCodigo(request.form.get('codigo'))
    bank.setDescricao(request.form.get('descricao').title())
    bank.setDescricaoCompleta(request.form.get('desc_completa').title())
    return bank
