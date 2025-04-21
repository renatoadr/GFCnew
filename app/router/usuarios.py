from flask import Blueprint, request, render_template, redirect, flash
from controller.usuarioController import usuarioController
from utils.helper import protectedPage
import utils.converter as converter
from dto.usuario import usuario

usuarios_bp = Blueprint('usuarios', __name__)


@usuarios_bp.route('/tratar_usuarios')
def tratarusuarios():
    protectedPage()

    usrCtrl = usuarioController()
    usrs = usrCtrl.lista_usuarios()

    return render_template("lista_usuarios.html", usuarios=usrs)


@usuarios_bp.route('/abrir_cad_usuario')
def abrir_cad_usuario():
    return render_template("usuario.html")


@usuarios_bp.route('/cadastrar_usuarios', methods=['POST'])
def cadastrar_usuarios():
    cli = usuarios()
    cli.setCpfCnpj(converter.removeAlpha(request.form.get('cpfCnpj')))
    cli.setTpCpfCnpj(request.form.get('tpCpfCnpj'))
    cli.setNmusuarios(request.form.get('nmusuarios'))
    cli.setDdd(request.form.get('ddd'))
    cli.setTel(converter.removeAlpha(request.form.get('tel')))
    cli.setEmail(request.form.get('email'))
    cliC = usuariosController()

    if (cliC.existeusuarios(cli.getCpfCnpj())):
        cli.setCpfCnpj(converter.maskCpfOrCnpj(cli.getCpfCnpj()))
        flash('Este documento já está em uso. Informe outro número de documento.',
              category='error')
        return render_template(
            "usuarios.html",
            usuarios=cli,
            criacao=True,
        )

    cliC.inserirusuarios(cli)
    return redirect("/tratar_usuarios")


@usuarios_bp.route('/editar_usuarios')
def editar_usuarios():
    idCli = request.args.get("cpfCnpj")
    cliC = usuariosController()
    usuarios = cliC.consultarusuariosPeloId(idCli)
    if usuarios is None:
        return redirect('/tratar_usuarios')

    usuarios.setCpfCnpj(converter.maskCpfOrCnpj(usuarios.getCpfCnpj()))
    return render_template("usuarios.html", usuarios=usuarios, criacao=False)


@usuarios_bp.route('/salvar_alteracao_usuarios', methods=['POST'])
def salvar_alteracao_usuarios():
    cli = usuarios()
    cli.setCpfCnpj(converter.removeAlpha(request.form.get('cpfCnpj')))
    cli.setTpCpfCnpj(request.form.get('tpCpfCnpj'))
    cli.setNmusuarios(request.form.get('nmusuarios'))
    cli.setDdd(request.form.get('ddd'))
    cli.setTel(converter.removeAlpha(request.form.get('tel')))
    cli.setEmail(request.form.get('email'))

    cliC = usuariosController()
    cliC.salvarusuarios(cli)

    return redirect("/tratar_usuarios")


@usuarios_bp.route('/excluir_usuarios')
def excluir_usuarios():

    idCli = request.args.get('cpfCnpj')
#    idEmpreend = request.args.get('idEmpreend')

    print('--------------excluir_usuarios -------------')
    print(idCli)

    cliC = usuariosController()
    cliC.excluirusuarios(idCli)
    cliS = cliC.consultarusuarios()

    return render_template("lista_usuarios.html", usuarios=cliS)
