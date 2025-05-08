from flask import Blueprint, request, render_template, redirect

from utils.security import login_required, permission_access, get_user_logged, login_user, has_user_logged, get_user_logged_mobile
from controller.usuarioController import usuarioController
from controller.bancoController import bancoController
from enums.tipo_acessos import TipoAcessos
from dto.usuario import usuario
from models.User import User
from utils.flash_message import flash_message

usuarios_bp = Blueprint('usuarios', __name__)


@usuarios_bp.route('/tratar_usuarios')
@login_required
@permission_access([TipoAcessos.RT, TipoAcessos.ADM])
def tratarusuarios():
    usrCtrl = usuarioController()
    usrs = usrCtrl.lista_usuarios()

    for us in usrs:
        us.setTpAcesso(TipoAcessos.to_name(us.getTpAcesso()))

    return render_template("lista_usuarios.html", usuarios=usrs)


@usuarios_bp.route('/abrir_cad_usuario')
@login_required
@permission_access([TipoAcessos.RT, TipoAcessos.ADM])
def abrir_cad_usuario():
    sUser = get_user_logged()
    ctrlBanco = bancoController()
    bancos = ctrlBanco.lista_bancos()
    tipos = []
    if sUser.profile in [TipoAcessos.ADM.name, TipoAcessos.RT.name]:
        tipos = TipoAcessos.to_list()
    return render_template("usuario.html", tipos=tipos, bancos=bancos)


@usuarios_bp.route('/cadastrar_usuario', methods=['POST'])
def cadastrar_usuarios():
    user = getForm()

    if not user.getTpAcesso():
        flash_message.error(
            'Não foi informado o tipo de acesso para este usuário')
    if not user.getEmail():
        flash_message.error(
            'Não foi informado o email para este usuário')
    if not user.getNmUsuario():
        flash_message.error(
            'Não foi informado o nome para este usuário')
    if not user.getSenha():
        flash_message.error(
            'Não foi informado a senha para este usuário')
    if flash_message.has_error():
        return render_template("usuario.html", user=user, tipos=TipoAcessos.to_list())

    ctrlUser = usuarioController()
    ctrlUser.cadastrar_usuario(user)

    return redirect('/tratar_usuarios')


@usuarios_bp.route('/editar_usuario')
@login_required
@permission_access([TipoAcessos.RT, TipoAcessos.ADM])
def editar_usuarios():
    idUser = request.args.get("id")
    ctrlUser = usuarioController()
    usuario = ctrlUser.get_usuario_pelo_id(idUser)
    ctrlBanco = bancoController()
    bancos = ctrlBanco.lista_bancos()
    if usuario is None:
        return redirect('/tratar_usuarios')

    return render_template("usuario.html", user=usuario, tipos=TipoAcessos.to_list(), bancos=bancos)


@usuarios_bp.route('/salvar_alteracao_usuario', methods=['POST'])
def salvar_alteracao_usuarios():
    user = getForm()
    sUs = get_user_logged()
    perfil = request.form.get('pfl')

    if not user.getTpAcesso() and sUs.profile != TipoAcessos.RT.name:
        flash_message.error(
            'Não foi informado o tipo de acesso para este usuário')
    if not user.getEmail():
        flash_message.error(
            'Não foi informado o email para este usuário')
    if not user.getNmUsuario():
        flash_message.error(
            'Não foi informado o nome para este usuário')
    if flash_message.has_error():
        return render_template("usuario.html", user=user, tipos=TipoAcessos.to_list())

    if perfil and perfil == TipoAcessos.RT.name:
        user.setTpAcesso(TipoAcessos.RT.name)

    ctrlUser = usuarioController()
    ctrlUser.atulizar_usuario(user)

    if user.getSenha():
        ctrlUser.alterar_senha(user.getSenha(), user.getIdUsuario())

    if user.getIdUsuario() == sUs.id:
        login_user(User(
            user.getIdUsuario() if user.getIdUsuario() else sUs.id,
            user.getNmUsuario() if user.getNmUsuario() else sUs.name,
            user.getEmail() if user.getEmail() else sUs.email,
            user.getTpAcesso() if user.getTpAcesso() else sUs.profile,
            user.getCodBanco(),
            sUs.logged_in
        ))

    if sUs.profile == TipoAcessos.RT.name:
        return redirect("/tratar_usuarios")

    return redirect("/home")


@usuarios_bp.route('/excluir_usuario')
def excluir_usuarios():
    idUser = request.args.get('id')
    cliC = usuarioController()
    cliC.excluir_usuario(idUser)
    return redirect("/tratar_usuarios")


@usuarios_bp.route('/minha-conta')
def minha_conta():
    sUs = get_user_logged() if has_user_logged() else get_user_logged_mobile()
    ctrlUser = usuarioController()
    usuario = ctrlUser.get_usuario_pelo_id(sUs.id)
    return render_template("usuario.html", user=usuario)


def getForm() -> usuario:
    user = usuario()
    user.setIdUsuario(request.form.get('id_user'))
    user.setEmail(request.form.get('email_user'))
    user.setNmUsuario(request.form.get('nm_user').title())
    user.setSenha(request.form.get('pass_user'))
    user.setTpAcesso(request.form.get('tp_access'))
    user.setCodBanco(request.form.get('cod_banco'))
    return user
