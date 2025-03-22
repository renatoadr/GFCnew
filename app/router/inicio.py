from flask import Blueprint, request, render_template, redirect, session, url_for, send_from_directory
from controller.usuarioController import usuarioController
from controller.geralController import geralController
import re

init_bp = Blueprint('inicio', __name__)

@init_bp.route('/m')
def mlogin():
    if session.get('m_logged_in') == True:
        return redirect('/mobile/home')
    if request.args.get('mensagem') is not None:
      return render_template("mobile/login.html", mensagem=request.args.get('mensagem'))
    return render_template("mobile/login.html")


@init_bp.route('/login_m', methods=['POST'])
def valida_login_m():

    email = request.form.get('email')
    senha = request.form.get('senha')
    usuC = usuarioController ()
    usu = usuC.consultarAcesso(email, senha)
#    print ('++++++++++++++++++>>>>', usu)

    if  usu:                       # encontrou usuário e senha corretos
#        print ('++++++++++++++++++>>>>', idUsuario)
#        print ('++++++++++++++++++>>>>', uApelidos)

        session['m_logged_in'] = True
        session['m_email'] = email
        session['nome'] = usu.getNmUsuario()
        session['m_user_id'] = usu.getIdUsuario()

        return redirect('/mobile/home')
    else:
        session['m_logged_in'] = False
        return redirect(url_for(".mlogin", mensagem='Falha no login, verifique o usuário e a senha'))

@init_bp.route('/mobile/home')
def home_m():
  idUsuario = session.get('m_user_id')
  if idUsuario is None:
      redirect('/m')

  usuC = usuarioController ()
  uApelidos = usuC.consultarApelidos(idUsuario)
  return render_template("mobile/home.html", apelidos=uApelidos)

@init_bp.route('/logout_m')
def logout_m():
    session.pop('m_email', None)
    session.pop('m_logged_in', None)
    session.pop('nome', None)
    session.pop('m_user_id', None)
    return redirect("/m")

@init_bp.route('/')
def login():
  if re.search('Android|webOS|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini', request.user_agent.string, re.IGNORECASE):
    return redirect('/m')

  if session.get('logged_in') == True:
    return redirect('/home')
  return render_template("login.html")

@init_bp.route('/login', methods=['POST'])
def valida_login():

    email = request.form.get('email')
    senha = request.form.get('senha')
    usuC = usuarioController ()
    usu = usuC.consultarAcesso(email, senha)
    # print ('++++++++++++++++++>>>>', usu)

    if  usu:                       # encontrou usuário e senha corretos
        session['logged_in'] = True
        session['email'] = email
        session['nome'] = usu.getNmUsuario()
        return redirect('/home')
    else:
        session['logged_in'] = False
        return render_template("login.html", mensagem='Falha no login, verifique o usuário e a senha')

@init_bp.route('/lista_relatorios', methods=['GET'])
def lista_relatorios():
  idEmpreend = request.args.get('idEmpreend')
  apelido = request.args.get('apelido')
  mobile  = request.form.get('mobile', 'false').lower() == 'true'

#    print('==========lista_relatorios==========', apelido)
  gerC = geralController ()
  diretorio = "c://GFC//Relatorios"
  arqS = gerC.listar_arquivos_com_prefixo(diretorio, apelido)
#    print ('=========== lista de arquivos   ', arqS)
  print ('=========== lista de arquivos   ', arqS)
  if mobile:
    return render_template("mobile/download.html", arquivos=arqS)
  else:
    meses = ['  ','01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
    anos = ['    ','2025', '2026', '2027', '2028', '2029', '2030']
    return render_template("relatorio.html", arquivos=arqS, listaMes = meses, listaAno = anos, apelido=apelido, idEmpreend=idEmpreend)

@init_bp.route('/logout')
def logout():
  session.pop('email', None)
  session.pop('logged_in', None)
  session.pop('nome', None)
  return redirect("/")

@init_bp.route('/download_arquivo', methods=['GET'])
def download_arquivo():
    arquivo = request.args.get('arquivo')
    diretorio = "c://GFC//Relatorios"
    print('+++++++++++++', arquivo)
    return send_from_directory(diretorio, arquivo, as_attachment=True)
