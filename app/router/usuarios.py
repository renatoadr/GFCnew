from flask import Blueprint, request, render_template, redirect
from controller.usuarioController import usuarioController
from utils.security import login_required, permission_access
from dto.usuario import usuario
from enums.tipo_acessos import TipoAcessos

usuarios_bp = Blueprint('usuarios', __name__)


@usuarios_bp.route('/tratar_usuarios')
@login_required
@permission_access(TipoAcessos.ADM)
def tratarusuarios():
    usrCtrl = usuarioController()
    usrs = usrCtrl.lista_usuarios()

    return render_template("lista_usuarios.html", usuarios=usrs)


@usuarios_bp.route('/abrir_cad_usuario')
@login_required
@permission_access(TipoAcessos.ADM)
def abrir_cad_usuario():
    return render_template("usuario.html", tipos=TipoAcessos.to_list())


@usuarios_bp.route('/cadastrar_usuario', methods=['POST'])
def cadastrar_usuarios():
    user = getForm()
    ctrlUser = usuarioController()
    ctrlUser.cadastrar_usuario(user)
    return redirect('/tratar_usuarios')


@usuarios_bp.route('/editar_usuario')
@login_required
@permission_access(TipoAcessos.ADM)
def editar_usuarios():
    idUser = request.args.get("id")
    ctrlUser = usuarioController()
    usuario = ctrlUser.get_usuario_pelo_id(idUser)
    if usuario is None:
        return redirect('/tratar_usuarios')

    return render_template("usuario.html", user=usuario, tipos=TipoAcessos.to_list())


@usuarios_bp.route('/salvar_alteracao_usuario', methods=['POST'])
def salvar_alteracao_usuarios():
    user = getForm()
    ctrlUser = usuarioController()
    ctrlUser.atulizar_usuario(user)

    if user.getSenha():
        ctrlUser.alterar_senha(user.getSenha(), user.getIdUsuario())

    return redirect("/tratar_usuarios")


@usuarios_bp.route('/excluir_usuario')
def excluir_usuarios():
    idUser = request.args.get('id')
    cliC = usuarioController()
    cliC.excluir_usuario(idUser)
    return redirect("/tratar_usuarios")


def getForm() -> usuario:
    user = usuario()
    user.setIdUsuario(request.form.get('id_user'))
    user.setEmail(request.form.get('email_user'))
    user.setNmUsuario(request.form.get('nm_user').title())
    user.setSenha(request.form.get('pass_user'))
    user.setTpAcesso(request.form.get('tp_access'))
    return user
