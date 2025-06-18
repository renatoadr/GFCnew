from flask import Blueprint, request, render_template, redirect, url_for

from utils.security import login_user, logout_user, has_user_logged, has_user_mobile_logged, logout_user_mobile, get_user_logged_mobile, login_user_mobile
from controller.empreendimentoController import empreendimentoController
from controller.usuarioController import usuarioController
from models.User import User
import re
import os

inicio_bp = Blueprint('inicio', __name__)


@inicio_bp.route('/m')
def mlogin():
    if not re.search(
        'Android|webOS|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini',
        request.user_agent.string,
        re.IGNORECASE
    ):
        return redirect('/')
    if has_user_mobile_logged():
        return redirect('/mobile/home')
    if request.args.get('mensagem') is not None:
        return render_template("mobile/login.html", mensagem=request.args.get('mensagem'))
    return render_template("mobile/login.html")


@inicio_bp.route('/login_m', methods=['POST'])
def valida_login_m():
    email = request.form.get('email')
    senha = request.form.get('senha')
    usuC = usuarioController()
    usu = usuC.consultarAcesso(email, senha)

    if usu:
        login_user_mobile(User(
            usu.getIdUsuario(),
            usu.getNmUsuario(),
            usu.getEmail(),
            usu.getTpAcesso(),
            usu.getCodBanco()
        ))
        logout_user()

        return redirect('/mobile/home')
    else:
        return redirect(url_for(".mlogin", mensagem='Falha no login, verifique o usuário e a senha'))


@inicio_bp.route('/mobile/home')
def home_m():
    sUs = get_user_logged_mobile()
    if not has_user_mobile_logged():
        redirect('/m')

    usuC = empreendimentoController()
    uApelidos = usuC.consultarApelidos(sUs.codBank)
    return render_template("mobile/home.html", apelidos=uApelidos)


@inicio_bp.route('/logout_m')
def logout_m():
    logout_user_mobile()
    return redirect("/m")


@inicio_bp.route('/')
def login():
    if re.search('Android|webOS|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini', request.user_agent.string, re.IGNORECASE):
        return redirect('/m')

    if has_user_logged():
        return redirect('/home')
    return render_template("login.html")


@inicio_bp.route('/login', methods=['POST'])
def valida_login():
    email = request.form.get('email')
    senha = request.form.get('senha')
    usuC = usuarioController()
    usu = usuC.consultarAcesso(email, senha)

    if usu:
        login_user(User(
            usu.getIdUsuario(),
            usu.getNmUsuario(),
            usu.getEmail(),
            usu.getTpAcesso(),
            usu.getCodBanco()
        ))
        logout_user_mobile()
        return redirect('/home')
    else:
        logout_user()
        return render_template("login.html", mensagem='Falha no login, verifique o usuário e a senha')


@inicio_bp.route('/sem_permissao')
def sem_permissao():
    return render_template("sem_permissao.html")


@inicio_bp.route('/logout')
def logout():
    logout_user()
    return redirect("/")
