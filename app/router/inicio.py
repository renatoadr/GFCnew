from flask import Blueprint, request, render_template, redirect, session, url_for, send_from_directory, current_app
from models.User import User
from controller.usuarioController import usuarioController
from controller.geralController import geralController
from controller.empreendimentoController import empreendimentoController
from utils.security import login_user, logout_user, has_user_logged, has_user_mobile_logged, logout_user_mobile, get_user_logged_mobile, login_user_mobile
import re
import os

init_bp = Blueprint('inicio', __name__)


@init_bp.route('/m')
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


@init_bp.route('/login_m', methods=['POST'])
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


@init_bp.route('/mobile/home')
def home_m():
    sUs = get_user_logged_mobile()
    if not has_user_mobile_logged():
        redirect('/m')

    usuC = empreendimentoController()
    uApelidos = usuC.consultarApelidos(sUs.codBank)
    return render_template("mobile/home.html", apelidos=uApelidos)


@init_bp.route('/logout_m')
def logout_m():
    logout_user_mobile()
    return redirect("/m")


@init_bp.route('/')
def login():
    if re.search('Android|webOS|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini', request.user_agent.string, re.IGNORECASE):
        return redirect('/m')

    if has_user_logged():
        return redirect('/home')
    return render_template("login.html")


@init_bp.route('/login', methods=['POST'])
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


@init_bp.route('/sem_permissao')
def sem_permissao():
    return render_template("sem_permissao.html")


@init_bp.route('/lista_relatorios', methods=['GET'])
def lista_relatorios():
    idEmpreend = request.args.get('idEmpreend')
    apelido = request.args.get('apelido')
#    apelido = 'Quinta vez'
    mobile = request.form.get('mobile', 'false').lower() == 'true'

#    print('==========lista_relatorios==========', apelido)
    gerC = geralController()
    diretorio = os.path.join(current_app.config['DIRSYS'], 'Relatorios')
    arqS = gerC.listar_arquivos_com_prefixo(
        os.path.normpath(diretorio), apelido)
#    print ('=========== lista de arquivos   ', arqS)
    print('=========== lista de arquivos   ', arqS)
    if mobile:
        return render_template("mobile/download.html", arquivos=arqS)
    else:
        meses = ['  ', '01', '02', '03', '04', '05',
                 '06', '07', '08', '09', '10', '11', '12']
        anos = ['    ', '2025', '2026', '2027', '2028', '2029', '2030']
        return render_template("relatorio.html", arquivos=arqS, listaMes=meses, listaAno=anos, apelido=apelido, idEmpreend=idEmpreend)


@init_bp.route('/logout')
def logout():
    logout_user()
    return redirect("/")


@init_bp.route('/download_arquivo', methods=['GET'])
def download_arquivo():
    arquivo = request.args.get('arquivo')
    diretorio = os.path.join(current_app.config['DIRSYS'], 'Relatorios')
    print('+++++++++++++', arquivo)
    return send_from_directory(os.path.normpath(diretorio), arquivo, as_attachment=True)
