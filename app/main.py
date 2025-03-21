#!python3

#from array import array
from flask import Flask, request, render_template, redirect, url_for, send_file, session, send_from_directory, jsonify
from controller.empreendimentoController import empreendimentoController
from controller.gastoController import gastoController
from controller.unidadeController import unidadeController
from controller.torreController import torreController
from controller.clienteController import clienteController
from controller.orcamentoController import orcamentoController
from controller.agendaController import agendaController
from controller.certidaoController import certidaoController
from controller.clienteController import clienteController
from controller.contaController import contaController
from controller.empreendimentoController import empreendimentoController
from controller.financeiroController import financeiroController
from controller.graficoController import graficoController
from controller.geralController import geralController
from controller.inadimplenciaController import inadimplenciaController
from controller.medicaoController import medicaoController
from controller.notaController import notaController
from controller.orcamentoController import orcamentoController
from controller.pontoController import pontoController
from controller.torreController import torreController
from controller.unidadeController import unidadeController
from controller.usuarioController import usuarioController

from datetime import datetime
from dto.agenda import agenda
#from dto.documento import documento
from dto.empreendimento import empreendimento
from dto.unidade import unidade
from dto.certidao import certidao
from dto.cliente import cliente
from dto.conta import conta
from dto.geral import geral
#from dto.grafico import grafico
from dto.financeiro import financeiro
from dto.inadimpencia import inadimpencia
from dto.torre import torre
from dto.orcamento import orcamento
from dto.medicao import medicao
from dto.nota import nota
from dto.ponto import ponto
from dto.usuario import usuario
from werkzeug.utils import secure_filename
from matplotlib import pyplot as plt
from matplotlib.legend import Legend
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.utils import ImageReader
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter, inch
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer, Image
from utils.CtrlSessao import IdEmpreend, DtCarga, NmEmpreend, IdOrca

# from reportlab.platypus.tables import Table, TableStyle

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import mysql.connector
import os
import locale
import numpy as np
import easygui
import configparser
import utils.converter as converter
import re
import random

app = Flask(__name__)

app.secret_key = "gfc001"

def init(app):
    config = configparser.ConfigParser()
    try:
        config_location = "gfc.cfg"
        config.read(config_location)

        app.config['UPLOAD_FOLDER'] = config.get("config", "UPLOAD_FOLDER")
        app.config['ALLOWED_EXTENSIONS'] = config.get("config", "ALLOWED_EXTENSIONS")
        app.config['BARRADIR'] = config.get("config", "BARRADIR")
        app.config['DIRSYS'] = config.get("config", "DIRSYS")

        print ("Succesfully read configs from: ", config_location)
    except:
        print ("Couldn't read configs from: ", config_location)

def is_logged():
  return session['logged_in'] == True

@app.route('/m')
def mlogin():
    if session.get('m_logged_in') == True:
        return redirect('/mobile/home')
    return render_template("mobile/login.html")

@app.route('/login_m', methods=['POST'])
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
        return redirect(url_for("/m", mensagem='Falha no login, verifique o usuário e a senha'))

@app.route('/mobile/home')
def home_m():
  idUsuario = session.get('m_user_id')
  if idUsuario is None:
      redirect('/m')

  usuC = usuarioController ()
  uApelidos = usuC.consultarApelidos(idUsuario)
  return render_template("mobile/home.html", apelidos=uApelidos)

@app.route('/logout_m')
def logout_m():
    session.pop('m_email', None)
    session.pop('m_logged_in', None)
    session.pop('nome', None)
    session.pop('m_user_id', None)
    return redirect("/m")

@app.route('/')
def login():
  if re.search('Android|webOS|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini', request.user_agent.string, re.IGNORECASE):
    return redirect('/m')

  if session.get('logged_in') == True:
    return redirect('/home')
  return render_template("login.html")

@app.route('/login', methods=['POST'])
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

@app.route('/lista_relatorios', methods=['GET'])
def lista_relatorios():
  idEmpreend = request.args.get('idEmpreend')
  apelido = request.args.get('apelido')
  mobile  = request.form.get('mobile', 'false').lower() == 'true'

#    print('==========lista_relatorios==========', apelido)
  gerC = geralController (app)
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

@app.route('/logout')
def logout():
  session.pop('email', None)
  session.pop('logged_in', None)
  session.pop('nome', None)
  return redirect("/")


def protectedPage():
    if 'logged_in' not in session:
#        print('opcao1')
        return render_template("login.html", code=302)
    if session['logged_in'] == False:
#        print('opcao2')
        return render_template("login.html", code=302)

################ EMPREENDIMENTOS ###############################

@app.route('/home', methods=['POST','GET'])
def abrir_home():

# ---- teste de sessão
    temp = protectedPage()

    if temp != None:
        print ('protectedPage()')
        return temp
#---- fim teste de sessão

    empc = empreendimentoController ()
    emps = empc.consultarEmpreendimentos ()
    return render_template("home.html", empreends=emps)

@app.route('/abrir_cad_empreend')
def abrir_cad_empreend():
    return render_template("cad_empreend.html")

@app.route('/efetuar_cad_empreend', methods=['POST'])
def efetuar_cad_empreend():
    empreend = empreendimento ()
    empreend.setApelido(request.form.get('apelido'))
    empreend.setNmEmpreend (request.form.get('nmEmpreendimento'))
    empreend.setNmBanco (request.form.get('nmBanco'))
    empreend.setNmIncorp (request.form.get('nmIncorp'))
    empreend.setNmConstrutor (request.form.get('nmConstrutor'))
    empreend.setLogradouro (request.form.get('logradouro'))
    empreend.setBairro (request.form.get('bairro'))
    empreend.setCidade (request.form.get('cidade'))
    empreend.setEstado (request.form.get('estado'))
    empreend.setCep (converter.removeAlpha(request.form.get('cep')))
    empreend.setCpfCnpjEngenheiro (request.form.get('cpfCnpjEngenheiro'))
    empreend.setVlPlanoEmp (converter.converterStrToFloat(request.form.get('vlPlanoEmp')))
    empreend.setIndiceGarantia (converter.converterStrToFloat(request.form.get('indiceGarantia')))
    empreend.setPrevisaoEntrega (request.form.get('previsaoEntrega'))

    empc = empreendimentoController()
    empc.inserirEmpreendimento(empreend)
    return redirect("/home")

@app.route('/excluir_empreend')
def excluir_empreend():
    idEmpreend = request.args.get('idEmpreend')
    print (idEmpreend)
    empc = empreendimentoController()
    empc.excluirEmpreendimento(idEmpreend)

    emps = empc.consultarEmpreendimentos ()
    return render_template("home.html", empreends=emps)

@app.route('/abrir_edicao_empreend')
def abrir_edicao_empreend():

    idEmpreend = request.args.get('idEmpreend')
    print (idEmpreend)
    empc = empreendimentoController ()
    empreend = empc.consultarEmpreendimentoPeloId (idEmpreend)

    print(empreend)
    return render_template("cad_empreend.html", empreend=empreend)

@app.route('/salvar_empreend', methods=['POST'])
def salvar_empreend():
    empreend = empreendimento ()
    empreend.setApelido(request.form.get('apelido'))
    empreend.setIdEmpreend (int(request.form.get('idEmpreendimento')))
    empreend.setNmEmpreend (request.form.get('nmEmpreendimento'))
    empreend.setNmBanco (request.form.get('nmBanco'))
    empreend.setNmIncorp (request.form.get('nmIncorp'))
    empreend.setNmConstrutor (request.form.get('nmConstrutor'))
    empreend.setLogradouro (request.form.get('logradouro'))
    empreend.setBairro (request.form.get('bairro'))
    empreend.setCidade (request.form.get('cidade'))
    empreend.setEstado (request.form.get('estado'))
    empreend.setCep (converter.removeAlpha(request.form.get('cep')))
    empreend.setCpfCnpjEngenheiro (request.form.get('cpfCnpjEngenheiro'))
    empreend.setVlPlanoEmp (converter.converterStrToFloat(request.form.get('vlPlanoEmp')))
    empreend.setIndiceGarantia (converter.converterStrToFloat(request.form.get('indiceGarantia')))
    empreend.setPrevisaoEntrega (request.form.get('previsaoEntrega'))

    empc = empreendimentoController()
    empc.salvarEmpreendimento(empreend)
    return redirect("/home")

################ GARANTIAS ###############################

################ CERTIDOES ###############################

@app.route('/tratar_certidoes')
def tratar_certidoes():

# ---- teste de sessão
    temp = protectedPage()

    if temp != None:
        print ('protectedPage()')
        return temp
#---- fim teste de sessão

    idEmpreend = request.args.get("idEmpreend")
    nmEmpreend = request.args.get("nmEmpreend")

    print('-----tratar_certidoes---')
    print('tratar_certidoes ',idEmpreend)

    certC = certidaoController ()
    certS = certC.consultarCertidoes (idEmpreend)

    print('-----tratar_certidoes 2 ---')
    print('tratar_certidoes ',idEmpreend)

    if len(certS) == 0:
        return render_template("certidoes.html", idEmpreend=idEmpreend, mensagem="Certidões não Cadastradas!!!",  nmEmpreend=nmEmpreend, certidoes=certS)
    else:
        return render_template("certidoes.html", idEmpreend=idEmpreend, nmEmpreend=nmEmpreend, certidoes=certS)

@app.route('/efetuar_cad_certidoes', methods=['POST'])
def efetuar_cad_certidoes():
    cert = certidao ()
    print ('/efetuar_cad_certidoes ', request.form.get('idEmpreend'))
    cert.setIdEmpreend (request.form.get('idEmpreend'))
    cert.setEstadualStatus (request.form.get('estadualStatus'))
    cert.setEstadualValidade (request.form.get('estadualValidade'))
    cert.setFgtsStatus (request.form.get('fgtsStatus'))
    cert.setFgtsValidade (request.form.get('fgtsValidade'))
    cert.setMunicipalStatus (request.form.get('municipalStatus'))
    cert.setMunicipalValidade (request.form.get('municipalValidade'))
    cert.setSrfInssStatus (request.form.get('inssStatus'))
    cert.setSrfInssValidade (request.form.get('srfInssValidade'))
    cert.setTrabalhistaStatus (request.form.get('trabalhistaStatus'))
    cert.setTrabalhistaValidade (request.form.get('trabalhistaValidade'))

    certC = certidaoController()
    certC.inserirCertidoes(cert)
    return redirect("/tratar_certidoes")


############ UNIDADES ######################

@app.route('/tratar_unidades')
def tratarunidades():

# ---- teste de sessão
  temp = protectedPage()

  if temp != None:
    print ('protectedPage()')
    return temp
#---- fim teste de sessão

  idEmpreend = request.args.get('idEmpreend')
  nmEmpreend = request.args.get('nmEmpreend')

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

  unidC = unidadeController ()
  unidS = unidC.consultarUnidades (idEmpreend)


  if len(unidS) == 0:
    return render_template("lista_unidades.html",  mensagem="Unidade não Cadastrada.", unidades=unidS)
  else:
    return render_template("lista_unidades.html", unidades=unidS)

@app.route('/abrir_cad_unidade')
def abrir_cad_unidade():
    ctrlTorre = torreController()
    listaTorres = ctrlTorre.consultarTorres(IdEmpreend().get())
    return render_template("unidade.html", listaTorres=listaTorres)

@app.route('/cadastrar_unidade', methods=['POST'])
def cadastrar_unidade():
    un = unidade ()
    un.setIdTorre (request.form.get('idTorre'))
    un.setIdEmpreend (IdEmpreend().get())
    un.setUnidade (request.form.get('unidade'))
    un.setMesVigencia (request.form.get('mesVigencia'))
    un.setAnoVigencia (request.form.get('anoVigencia'))
    un.setVlUnidade (converter.converterStrToFloat(request.form.get('vlUnidade')))
    un.setStatus (request.form.get('status'))
    un.setCpfComprador (request.form.get('cpfCnpjCliente'))
    un.setVlPago (converter.converterStrToFloat(request.form.get('vlPago')))
    un.setDtOcorrencia (request.form.get('dtOcorrencia'))
    un.setFinanciado (request.form.get('financiado'))
    un.setVlChaves (converter.converterStrToFloat(request.form.get('vlChaves')))
    un.setVlPreChaves (converter.converterStrToFloat(request.form.get('vlPreChaves')))
    un.setVlPosChaves (converter.converterStrToFloat(request.form.get('vlPosChaves')))

    unid = unidadeController()
    unid.inserirUnidade(un)
    return redirect("/tratar_unidades")

@app.route('/editar_unidade')
def editar_unidade():
    ctrlTorre = torreController()
    listaTorres = ctrlTorre.consultarTorres(IdEmpreend().get())
    idUni = request.args.get("idUnidade")
    print('------ editar_unidade --------')
    print (idUni)
    unidc = unidadeController ()
    unidade = unidc.consultarUnidadePeloId (idUni)
    return render_template("unidade.html", unidade=unidade, listaTorres=listaTorres)

@app.route('/salvar_alteracao_unidade', methods=['POST'])
def salvar_alteracao_unidade():

    print('------- salvar_alteracao_unidade INICIO --------')

    un = unidade ()
    un.setIdUnidade(request.form.get('idUnidade'))
    un.setIdTorre (request.form.get('idTorre'))
    un.setIdEmpreend (IdEmpreend().get())
    un.setUnidade (request.form.get('unidade'))
    un.setMesVigencia (request.form.get('mesVigencia'))
    un.setAnoVigencia (request.form.get('anoVigencia'))
    un.setVlUnidade (converter.converterStrToFloat(request.form.get('vlUnidade')))
    un.setStatus (request.form.get('status'))
    un.setCpfComprador (request.form.get('cpfCnpjCliente'))
    un.setDtOcorrencia (request.form.get('dtOcorrencia'))
    un.setFinanciado (request.form.get('financiado'))
    un.setVlChaves (converter.converterStrToFloat(request.form.get('vlChaves')))
    un.setVlPreChaves (converter.converterStrToFloat(request.form.get('vlPreChaves')))
    un.setVlPosChaves (converter.converterStrToFloat(request.form.get('vlPosChaves')))

    print('------- salvar_alteracao_unidade --------')
    idEmpreend = request.form.get('idEmpreend')
    print(idEmpreend)

    unidc = unidadeController()
    unidc.salvarUnidade(un)

    print(idEmpreend)

    return redirect("/tratar_unidades")

@app.route('/consultar_unidade')
def consultar_unidade():

    ctrlTorre = torreController()
    listaTorres = ctrlTorre.consultarTorres(IdEmpreend().get())
    modo = request.args.get("modo")
    idUni = request.args.get("idUnidade")

    print('------ consultar_unidade --------')
    print(modo)
    print (idUni)

    unidc = unidadeController ()
    unidade = unidc.consultarUnidadePeloId (idUni)
    print(unidade)

    print('------ consultar_unidade --------')
    print(modo)

    return render_template("unidade.html", unidade=unidade,  listaTorres=listaTorres, modo=modo)

@app.route('/excluir_unidade')
def excluir_unidade():
    idUnidade = request.args.get('idUnidade')
    unidc = unidadeController()
    unidc.excluirUnidade(idUnidade)
    return redirect("/tratar_unidades")


############ TORRES ######################

@app.route('/tratar_torres')
def tratartorres():

# ---- teste de sessão
    temp = protectedPage()

    if temp != None:
        print ('protectedPage()')
        return temp
#---- fim teste de sessão

    idEmpreend = request.args.get("idEmpreend")
    nmEmpreend = request.args.get("nmEmpreend")

    if (idEmpreend is None and not IdEmpreend().has()) or (nmEmpreend is None and not NmEmpreend().has()):
        redirect('/home')

    if idEmpreend is None and IdEmpreend().has():
      idEmpreend = IdEmpreend().get()
    else:
      IdEmpreend().set(idEmpreend)

    if nmEmpreend is None and NmEmpreend().has():
      nmEmpreend = NmEmpreend().get()
    else:
      NmEmpreend().set(nmEmpreend)

    print('-----tratar_torres----')
    print(idEmpreend,nmEmpreend)

    torreC = torreController ()
    torreS = torreC.consultarTorres (idEmpreend)

    if len(torreS) == 0:
        return render_template("lista_torres.html", mensagem="Torre não cadastrada!!!", torreS=torreS)
    else:
        return render_template("lista_torres.html", torreS=torreS)

@app.route('/abrir_cad_torre')
def abrir_cad_torre():

    idEmpreend = request.form.get("idEmpreend")
    nmEmpreend = request.form.get("nmEmpreend")

    print('-----------abrir_cad_torre-----------')
    print(idEmpreend)

    return render_template("torre.html", idEmpreend=idEmpreend, nmEmpreend=nmEmpreend)

@app.route('/cadastrar_torre', methods=['POST'])
def cadastrar_torre():
    t = torre ()
    t.setIdEmpreend (IdEmpreend().get())
    t.setNmTorre (request.form.get('nmTorre'))
    t.setQtUnidade (request.form.get('qtUnidade'))

    torreC = torreController()
    torreC.inserirTorre(t)

    return redirect("/tratar_torres")

@app.route('/editar_torre')
def editar_torre():

    idT = request.args.get("idTorre")
    idEmpreend = request.args.get("idEmpreend")
    nmEmpreend = request.args.get("nmEmpreend")

    print('------ editar_torre --------')
    print (idT,nmEmpreend)

    torreC = torreController ()
    torre = torreC.consultarTorrePeloId (idT)

    print(torre)
    return render_template("torre.html", torre=torre, idEmpreend=idEmpreend, nmEmpreend=nmEmpreend)

@app.route('/salvar_alteracao_torre', methods=['POST'])
def salvar_alteracao_torre():
    print('------- salvar_alteracao_torre INICIO --------')

    t = torre ()
    t.setIdTorre (request.form.get('idTorre'))
    t.setIdEmpreend (IdEmpreend().get())
    t.setNmTorre (request.form.get('nmTorre'))
    t.setQtUnidade (request.form.get('qtUnidade'))

    print('------- salvar_alteracao_torre --------')

    torreC = torreController()
    torreC.salvarTorre(t)

    return redirect("/tratar_torres")


@app.route('/excluir_torre')
def excluir_torre():

    idTorre = request.args.get('idTorre')

    print('--------------excluir_torre -------------')
    print (idTorre)

    torreC = torreController()
    torreC.excluirTorre(idTorre)
    torreS = torreC.consultarTorres (IdEmpreend().get())

    if len(torreS) == 0:
        return redirect("/home")
    else:
        return redirect("/tratar_torres")

############ CLIENTES ######################

@app.route('/tratar_clientes')
def tratarclientes():

# ---- teste de sessão
    temp = protectedPage()

    if temp != None:
        print ('protectedPage()')
        return temp
#---- fim teste de sessão

    cliC = clienteController ()
    cliS = cliC.consultarClientes ()

    if len(cliS) == 0:
        return render_template("lista_clientes.html", clienteS=cliS)
    else:
        return render_template("lista_clientes.html", clienteS=cliS)

@app.route('/abrir_cad_cliente')
def abrir_cad_cliente():
    return render_template("cliente.html")

@app.route('/cadastrar_cliente', methods=['POST'])
def cadastrar_cliente():
  cli = cliente ()
  cli.setCpfCnpj (converter.removeAlpha(request.form.get('cpfCnpj')))
  cli.setTpCpfCnpj (request.form.get('tpCpfCnpj'))
  cli.setNmCliente (request.form.get('nmCliente'))
  cli.setDdd (request.form.get('ddd'))
  cli.setTel (converter.removeAlpha(request.form.get('tel')))
  cli.setEmail (request.form.get('email'))

  cliC = clienteController()
  cliC.inserirCliente(cli)

  return redirect("/tratar_clientes")

@app.route('/editar_cliente')
def editar_cliente():
  idCli = request.args.get("cpfCnpj")
  cliC = clienteController ()
  cliente = cliC.consultarClientePeloId (idCli)
  return render_template("cliente.html", cliente=cliente)

@app.route('/salvar_alteracao_cliente', methods=['POST'])
def salvar_alteracao_cliente():
  cli = cliente ()
  cli.setCpfCnpj (converter.removeAlpha(request.form.get('cpfCnpj')))
  cli.setTpCpfCnpj (request.form.get('tpCpfCnpj'))
  cli.setNmCliente (request.form.get('nmCliente'))
  cli.setDdd (request.form.get('ddd'))
  cli.setTel (converter.removeAlpha(request.form.get('tel')))
  cli.setEmail (request.form.get('email'))

  cliC = clienteController()
  cliC.salvarCliente(cli)

  return redirect("/tratar_clientes")

@app.route('/excluir_cliente')
def excluir_cliente():

    idCli = request.args.get('cpfCnpj')
#    idEmpreend = request.args.get('idEmpreend')

    print('--------------excluir_cliente -------------')
    print (idCli)

    cliC = clienteController()
    cliC.excluirCliente(idCli)
    cliS = cliC.consultarClientes ()

    return render_template("lista_clientes.html", clienteS=cliS)

########## API #########
@app.route('/api/clientes', methods=['GET'])
def get_clientes_api():
  if not is_logged():
    return jsonify([])
  search = request.args.get('search')
  cliC = clienteController()
  cliS = cliC.consultarClientes(search.lower())
  newList = list(map(lambda it: it.to_json(), cliS))
  return jsonify(newList)

@app.route('/api/cliente/<doc>', methods=['GET'])
def get_cliente_api(doc):
  if not is_logged():
    return jsonify([])
  cliC = clienteController()
  cli = cliC.consultarClientePeloId(doc)
  return jsonify(cli.to_json())

############ ORÇAMENTOS ######################

@app.route('/abrir_cad_orcamento')
def criar_orcamento():
    medC = orcamentoController ()
    med = medC.consultarOrcamentoPeloId(IdOrca().get())
    dtCarga = med.getDtCarga()
    ano = med.getAnoVigencia()
    mes = med.getMesVigencia()
    return render_template(
        "Orcamento_item.html",
        item=None,
        dtCarga=dtCarga,
        anoVig=ano,
        mesVig=mes,
        idEmpreend=IdEmpreend().get()
      )

@app.route('/tratar_orcamentos')
def tratar_orcamentos():
# ---- teste de sessão
    temp = protectedPage()

    if temp != None:
        print ('protectedPage()')
        return temp
#---- fim teste de sessão

    idEmpreend = request.args.get("idEmpreend")
    nmEmpreend = request.args.get("nmEmpreend")

    if (not IdEmpreend().has() or not NmEmpreend().has()) and (idEmpreend is None or nmEmpreend is None):
      return redirect('/home')

    if idEmpreend:
      IdEmpreend().set(idEmpreend)
    else:
      idEmpreend = IdEmpreend().get()

    if nmEmpreend:
      NmEmpreend().set(nmEmpreend)
    else:
      nmEmpreend = NmEmpreend().get()

    print('-----tratar_orcamentos----')
    print(idEmpreend, nmEmpreend)

    medC = orcamentoController ()
    medS = medC.consultarOrcamentos(idEmpreend)

    if len(medS) == 0:
        return render_template("lista_orcamentos.html", mensagem="Medição não Cadastrada, importar o arquivo Excel!!!", orcamentos=medS)
    else:
        return render_template("lista_orcamentos.html", orcamentos=medS)

@app.route('/consultar_orcamento_data')
def consultar_orcamento_data():

#    modo = request.args.get("modo")
    idEmpreend = IdEmpreend().get()
    dtCarga = request.args.get("dtCarga")

    if dtCarga is None and not DtCarga().has():
      return redirect('/tratar_orcamentos')
    elif dtCarga is None:
      dtCarga = DtCarga().get()
    else:
      DtCarga().set(dtCarga)

    IdOrca().set(request.args.get('idOrca'))
    print('------ consultar_orcamento_data ------')
#    print(modo)
    print (idEmpreend, dtCarga)

    medC = orcamentoController ()
    medS = medC.consultarOrcamentoPelaData (idEmpreend, dtCarga)

    print('------ consultar_orcamento_data fim --------')
#    print(modo)

    return render_template("orcamentos_itens.html", orcamentos=medS)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

@app.route('/upload_arquivo_orcamentos', methods=['POST'])
def upload_arquivo_orcamentos():
    # check if the post request has the file part
    if 'file' not in request.files:
        mensagem = "Erro no upload do arquivo. No file part."
        return render_template("erro.html", mensagem=mensagem)
    file = request.files['file']
    if file:
        if file.filename == '':
            mensagem = "Erro no upload do arquivo. Nome do arquivo='" + file.filename + "'."
        elif not allowed_file(file.filename):
            mensagem = "Erro no upload do arquivo. Arquivo='" + file.filename + "' não possui uma das extensões permitidas."
        else:
            filename = secure_filename(file.filename)
            caminhoArq = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(caminhoArq)

#            idEmpreend = request.form.get("idEmpreend")
            print ('-------------- upload_arquivo_orcamentos ----------------')
            idEmpreend = 56
            orcC = medicaoController ()
            print (caminhoArq, '   ', idEmpreend)
            orcC.carregar_medicoes(caminhoArq, idEmpreend)

            return redirect("/tratar_orcamentos")
    else:
        mensagem = "Erro no upload do arquivo. Você precisa selecionar um arquivo."
    return render_template("erro.html", mensagem=mensagem)

@app.route('/editar_item_orcamento', methods=['GET'])
def editar_item_orcamento():

    idOrc = request.args.get("idOrcamento")

    print('------ editar_item_orcamanto --------')
    print (idOrc)
    orcC = orcamentoController ()
    item = orcC.consultarOrcamentoPeloId (idOrc)
    print('item    ', item)
    return render_template("Orcamento_item.html", item=item)

@app.route('/excluir_item_orcamento')
def excluir_item_orcamento():
  idOrc = request.args.get("idOrcamento")
  idEmpreend = IdEmpreend().get()
  dtCarga = DtCarga().get()
  print ('idEmpreend, dtCarga  ==>',   idEmpreend, dtCarga)

  print('------ excluir_item_orcamanto --------')
  print (idOrc)
  orcC = orcamentoController ()
  orcC.excluirItemOrcamento(idOrc)
  print('------ excluir_item_orcamanto --- consultar_orcamento_data ------')
  print (idEmpreend, dtCarga)

  print('------ excluir_item_orcamanto --- consultar_orcamento_data fim --------')

  return redirect('/consultar_orcamento_data')

@app.route('/excluir_orcamento')
def excluir_orcamento():

    idEmpreend = session.get("idEmpreend")
    dtCarga = session.get("dtCarga")
    print ('idEmpreend, dtCarga  ==>',   idEmpreend, dtCarga)

    print('------ excluir_orcamanto --------')
    orcC = orcamentoController ()
    orcC.excluirOrcamento(idEmpreend,dtCarga)

    orcS = orcC.consultarOrcamentos(idEmpreend)

    if len(orcS) == 0:
        return render_template("lista_orcamentos.html", mensagem="Medição não Cadastrada, importar o arquivo Excel!!!", orcamentos=orcS)
    else:
        return render_template("lista_orcamentos.html", orcamentos=orcS)

@app.route('/salvar_item_orcamento', methods=['POST'])
def salvar_item_orcamento():
    valorOrcado = converter.converterStrToFloat(request.form.get('orcadoValor'))
    fisicoPercent = converter.converterStrToFloat(request.form.get('fisicoPercentual'), 1)
    valorFinanceiro = converter.converterStrToFloat(request.form.get('financeiroValor'))
    financeiroPercentual = valorFinanceiro / valorOrcado * 100
    fisicoValor = valorOrcado * fisicoPercent / 100

    item = orcamento ()
    item.setIdOrcamento (request.form.get('idOrcamento'))
    item.setIdEmpreend (request.form.get('idEmpreend'))
    item.setMesVigencia (request.form.get('mesVigencia'))
    item.setAnoVigencia (request.form.get('anoVigencia'))
    item.setDtCarga (request.form.get('dtCarga'))
    item.setItem (request.form.get('item'))
    item.setOrcadoValor (valorOrcado)
    item.setFisicoPercentual (fisicoPercent)
    item.setFinanceiroValor (valorFinanceiro)

    item.setFinanceiroPercentual (financeiroPercentual)
    item.setFinanceiroSaldo (valorOrcado - valorFinanceiro)
    item.setFisicoValor (fisicoValor)
    item.setFisicoSaldo (valorOrcado - fisicoValor)

    orcC = orcamentoController()
    orcC.salvarItemOrcamento(item)

    return redirect("/consultar_orcamento_data")

@app.route('/incluir_item_orcamento', methods=['POST'])
def incluir_item_orcamento():
    valorOrcado = converter.converterStrToFloat(request.form.get('orcadoValor'))
    fisicoPercent = converter.converterStrToFloat(request.form.get('fisicoPercentual'), 1)
    valorFinanceiro = converter.converterStrToFloat(request.form.get('financeiroValor'))
    financeiroPercentual = valorFinanceiro / valorOrcado * 100
    fisicoValor = valorOrcado * fisicoPercent / 100

    item = orcamento ()
    item.setIdOrcamento (request.form.get('idOrcamento'))
    item.setIdEmpreend (request.form.get('idEmpreend'))
    item.setMesVigencia (request.form.get('mesVigencia'))
    item.setAnoVigencia (request.form.get('anoVigencia'))
    item.setDtCarga (request.form.get('dtCarga'))
    item.setItem (request.form.get('item'))
    item.setOrcadoValor (valorOrcado)
    item.setFisicoPercentual (fisicoPercent)
    item.setFinanceiroValor (valorFinanceiro)

    item.setFinanceiroPercentual (financeiroPercentual)
    item.setFinanceiroSaldo (valorOrcado - valorFinanceiro)
    item.setFisicoValor (fisicoValor)
    item.setFisicoSaldo (valorOrcado - fisicoValor)

    orcC = orcamentoController()
    orcC.inserirOrcamento(item)

    print('passei aqui')
    return redirect("/consultar_orcamento_data")

############ NOTAS ######################

@app.route('/upload_arquivo_notas', methods=['POST'])
def upload_arquivo_notas():
    # check if the post request has the file part
    if 'file' not in request.files:
        mensagem = "Erro no upload do arquivo. No file part."
        return render_template("erro.html", mensagem=mensagem)
    file = request.files['file']
    if file:
        if file.filename == '':
            mensagem = "Erro no upload do arquivo. Nome do arquivo='" + file.filename + "'."
        elif not allowed_file(file.filename):
            mensagem = "Erro no upload do arquivo. Arquivo='" + file.filename + "' não possui uma das extensões permitidas."
        else:
            filename = secure_filename(file.filename)
            caminhoArq = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(caminhoArq)

#            idEmpreend = request.args.get("idEmpreend")
            idEmpreend = request.form.get("idEmpreend")

            print ('-------------- upload_arquivo_notas ----------------')

            notC = notaController ()
            print (caminhoArq, '   ', idEmpreend)
            notC.carregar_notas(caminhoArq, idEmpreend)

            return redirect("/tratar_notas")
    else:
        mensagem = "Erro no upload do arquivo. Você precisa selecionar um arquivo."
    return render_template("erro.html", mensagem=mensagem)

@app.route('/tratar_notas')
def tratar_notas():
# ---- teste de sessão
    temp = protectedPage()

    if temp != None:
        print ('protectedPage()')
        return temp
#---- fim teste de sessão

    idEmpreend = request.args.get("idEmpreend")
    nmEmpreend = request.args.get("nmEmpreend")

    if (not IdEmpreend().has() or not NmEmpreend().has()) and (idEmpreend is None or nmEmpreend is None):
      return redirect('/home')

    if idEmpreend:
      IdEmpreend().set(idEmpreend)
    else:
      idEmpreend = IdEmpreend().get()

    if nmEmpreend:
      NmEmpreend().set(nmEmpreend)
    else:
      nmEmpreend = NmEmpreend().get()

    print('-----tratar_notas----')
    print(idEmpreend, nmEmpreend)

    notC = notaController ()
    notS = notC.consultarNotas(idEmpreend)

    if len(notS) == 0:
        return render_template("lista_notas.html", mensagem="Nota não Cadastrada, importar o arquivo Excel!!!", notas=notS)
    else:
        return render_template("lista_notas.html", notas=notS)

############ CONTA CORRENTE ######################

@app.route('/upload_arquivo_contas', methods=['POST'])
def upload_arquivo_contas():
    # check if the post request has the file part
    if 'file' not in request.files:
        mensagem = "Erro no upload do arquivo. No file part."
        return render_template("erro.html", mensagem=mensagem)
    file = request.files['file']
    if file:
        if file.filename == '':
            mensagem = "Erro no upload do arquivo. Nome do arquivo='" + file.filename + "'."
        elif not allowed_file(file.filename):
            mensagem = "Erro no upload do arquivo. Arquivo='" + file.filename + "' não possui uma das extensões permitidas."
        else:
            filename = secure_filename(file.filename)
            caminhoArq = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(caminhoArq)

#            idEmpreend = request.args.get("idEmpreend")
            idEmpreend = request.form.get("idEmpreend")

            print ('-------------- upload_arquivo_contas ----------------')

            notC = contaController ()
            print (caminhoArq, '   ', idEmpreend)
            notC.carregar_contas(caminhoArq, idEmpreend)

            return redirect("/tratar_contas")
    else:
        mensagem = "Erro no upload do arquivo. Você precisa selecionar um arquivo."
    return render_template("erro.html", mensagem=mensagem)

@app.route('/tratar_contas')
def tratar_contas():
# ---- teste de sessão
    temp = protectedPage()

    if temp != None:
        print ('protectedPage()')
        return temp
#---- fim teste de sessão

    idEmpreend = request.args.get("idEmpreend")
    nmEmpreend = request.args.get("nmEmpreend")

    if (not IdEmpreend().has() or not NmEmpreend().has()) and (idEmpreend is None or nmEmpreend is None):
      return redirect('/home')

    if idEmpreend:
      IdEmpreend().set(idEmpreend)
    else:
      idEmpreend = IdEmpreend().get()

    if nmEmpreend:
      NmEmpreend().set(nmEmpreend)
    else:
      nmEmpreend = NmEmpreend().get()

    print('-----tratar_contas----')
    print(idEmpreend, nmEmpreend)

    contC = contaController ()
    contS = contC.consultarContas(idEmpreend)

    if len(contS) == 0:
        return render_template("lista_contas.html", mensagem="Conta não Cadastrada, importar o arquivo Excel!!!", contas=contS)
    else:
        return render_template("lista_contas.html", contas=contS)


############ MEDIÇÕES ######################

@app.route('/tratar_medicoes')
def tratar_medicoes():
# ---- teste de sessão
    temp = protectedPage()

    if temp != None:
        print ('protectedPage()')
        return temp
#---- fim teste de sessão

    idEmpreend = request.args.get("idEmpreend")
    nmEmpreend = request.args.get("nmEmpreend")

    if (not IdEmpreend().has() or not NmEmpreend().has()) and (idEmpreend is None or nmEmpreend is None):
      return redirect('/home')

    if idEmpreend:
      IdEmpreend().set(idEmpreend)
    else:
      idEmpreend = IdEmpreend().get()

    if nmEmpreend:
      NmEmpreend().set(nmEmpreend)
    else:
      nmEmpreend = NmEmpreend().get()

    print('-----tratar_medicoes----')
    print(idEmpreend, nmEmpreend)

    medC = medicaoController ()
    medS = medC.consultarMedicoes(idEmpreend)

    if len(medS) == 0:
        return render_template("lista_medicoes.html", mensagem="Medição não Cadastrada, importar o arquivo Excel!!!", medicoes=medS)
    else:
        return render_template("lista_medicoes.html", medicoes=medS)

@app.route('/consultar_medicao_data')
def consultar_medicao_data():

#    modo = request.args.get("modo")
    idEmpreend = IdEmpreend().get()
    dtCarga = request.args.get("dtCarga")

    if dtCarga is None and not DtCarga().has():
      return redirect('/tratar_medicoes')
    elif dtCarga is None:
      dtCarga = DtCarga().get()
    else:
      DtCarga().set(dtCarga)


    print('------ consultar_medicao_data ------')
#    print(modo)
    print (idEmpreend, dtCarga)

    medC = medicaoController ()
    medS = medC.consultarMedicaoPelaData (idEmpreend, dtCarga)

    print('------ consultar_medicao_data fim --------')
#    print(modo)

    return render_template("medicao_itens.html", medicoes=medS)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

@app.route('/upload_arquivo_medicoes', methods=['GET', 'POST'])
def upload_arquivo_medicoes():
    # check if the post request has the file part
    if 'file' not in request.files:
        mensagem = "Erro no upload do arquivo. No file part."
        return render_template("erro.html", mensagem=mensagem)
    file = request.files['file']
    if file:
        if file.filename == '':
            mensagem = "Erro no upload do arquivo. Nome do arquivo='" + file.filename + "'."
        elif not allowed_file(file.filename):
            mensagem = "Erro no upload do arquivo. Arquivo='" + file.filename + "' não possui uma das extensões permitidas."
        else:
            filename = secure_filename(file.filename)
            caminhoArq = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(caminhoArq)

#            idEmpreend = request.args.get("idEmpreend")
            idEmpreend = request.form.get("idEmpreend")

            print ('-------------- upload_arquivo_medicoes ----------------')

            orcC = medicaoController ()
            print (caminhoArq, '   ', idEmpreend)
            orcC.carregar_medicoes(caminhoArq, idEmpreend)

            return redirect("/tratar_medicoes")
    else:
        mensagem = "Erro no upload do arquivo. Você precisa selecionar um arquivo."
    return render_template("erro.html", mensagem=mensagem)


############ NOTAS ######################

@app.route('/upload_arquivo_notas', methods=['POST'])
def upload_arquivo_notas():
    # check if the post request has the file part
    if 'file' not in request.files:
        mensagem = "Erro no upload do arquivo. No file part."
        return render_template("erro.html", mensagem=mensagem)
    file = request.files['file']
    if file:
        if file.filename == '':
            mensagem = "Erro no upload do arquivo. Nome do arquivo='" + file.filename + "'."
        elif not allowed_file(file.filename):
            mensagem = "Erro no upload do arquivo. Arquivo='" + file.filename + "' não possui uma das extensões permitidas."
        else:
            filename = secure_filename(file.filename)
            caminhoArq = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(caminhoArq)

#            idEmpreend = request.args.get("idEmpreend")
            idEmpreend = request.form.get("idEmpreend")

            print ('-------------- upload_arquivo_notas ----------------')

            notC = notaController ()
            print (caminhoArq, '   ', idEmpreend)
            notC.carregar_notas(caminhoArq, idEmpreend)

            return redirect("/tratar_notas")
    else:
        mensagem = "Erro no upload do arquivo. Você precisa selecionar um arquivo."
    return render_template("erro.html", mensagem=mensagem)

@app.route('/tratar_notas')
def tratar_notas():
# ---- teste de sessão
    temp = protectedPage()

    if temp != None:
        print ('protectedPage()')
        return temp
#---- fim teste de sessão

    idEmpreend = request.args.get("idEmpreend")
    nmEmpreend = request.args.get("nmEmpreend")

    if (not IdEmpreend().has() or not NmEmpreend().has()) and (idEmpreend is None or nmEmpreend is None):
      return redirect('/home')

    if idEmpreend:
      IdEmpreend().set(idEmpreend)
    else:
      idEmpreend = IdEmpreend().get()

    if nmEmpreend:
      NmEmpreend().set(nmEmpreend)
    else:
      nmEmpreend = NmEmpreend().get()

    print('-----tratar_notas----')
    print(idEmpreend, nmEmpreend)

    notC = notaController ()
    notS = notC.consultarNotas(idEmpreend)

    if len(notS) == 0:
        return render_template("lista_notas.html", mensagem="Nota não Cadastrada, importar o arquivo Excel!!!", notas=notS)
    else:
        return render_template("lista_notas.html", notas=notS)

############ CONTA CORRENTE ######################

@app.route('/upload_arquivo_contas', methods=['POST'])
def upload_arquivo_contas():
    # check if the post request has the file part
    if 'file' not in request.files:
        mensagem = "Erro no upload do arquivo. No file part."
        return render_template("erro.html", mensagem=mensagem)
    file = request.files['file']
    if file:
        if file.filename == '':
            mensagem = "Erro no upload do arquivo. Nome do arquivo='" + file.filename + "'."
        elif not allowed_file(file.filename):
            mensagem = "Erro no upload do arquivo. Arquivo='" + file.filename + "' não possui uma das extensões permitidas."
        else:
            filename = secure_filename(file.filename)
            caminhoArq = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(caminhoArq)

#            idEmpreend = request.args.get("idEmpreend")
            idEmpreend = request.form.get("idEmpreend")

            print ('-------------- upload_arquivo_contas ----------------')

            notC = contaController ()
            print (caminhoArq, '   ', idEmpreend)
            notC.carregar_contas(caminhoArq, idEmpreend)

            return redirect("/tratar_contas")
    else:
        mensagem = "Erro no upload do arquivo. Você precisa selecionar um arquivo."
    return render_template("erro.html", mensagem=mensagem)

@app.route('/tratar_contas')
def tratar_contas():
# ---- teste de sessão
    temp = protectedPage()

    if temp != None:
        print ('protectedPage()')
        return temp
#---- fim teste de sessão

    idEmpreend = request.args.get("idEmpreend")
    nmEmpreend = request.args.get("nmEmpreend")

    if (not IdEmpreend().has() or not NmEmpreend().has()) and (idEmpreend is None or nmEmpreend is None):
      return redirect('/home')

    if idEmpreend:
      IdEmpreend().set(idEmpreend)
    else:
      idEmpreend = IdEmpreend().get()

    if nmEmpreend:
      NmEmpreend().set(nmEmpreend)
    else:
      nmEmpreend = NmEmpreend().get()

    print('-----tratar_contas----')
    print(idEmpreend, nmEmpreend)

    contC = contaController ()
    contS = contC.consultarContas(idEmpreend)

    if len(contS) == 0:
        return render_template("lista_contas.html", mensagem="Conta não Cadastrada, importar o arquivo Excel!!!", contas=contS)
    else:
        return render_template("lista_contas.html", contas=contS)


############ MEDIÇÕES ######################

@app.route('/tratar_medicoes')
def tratar_medicoes():
# ---- teste de sessão
    temp = protectedPage()

    if temp != None:
        print ('protectedPage()')
        return temp
#---- fim teste de sessão

    idEmpreend = request.args.get("idEmpreend")
    nmEmpreend = request.args.get("nmEmpreend")

    if (not IdEmpreend().has() or not NmEmpreend().has()) and (idEmpreend is None or nmEmpreend is None):
      return redirect('/home')

    if idEmpreend:
      IdEmpreend().set(idEmpreend)
    else:
      idEmpreend = IdEmpreend().get()

    if nmEmpreend:
      NmEmpreend().set(nmEmpreend)
    else:
      nmEmpreend = NmEmpreend().get()

    print('-----tratar_medicoes----')
    print(idEmpreend, nmEmpreend)

    medC = medicaoController ()
    medS = medC.consultarMedicoes(idEmpreend)

    if len(medS) == 0:
        return render_template("lista_medicoes.html", mensagem="Medição não Cadastrada, importar o arquivo Excel!!!", medicoes=medS)
    else:
        return render_template("lista_medicoes.html", medicoes=medS)

@app.route('/consultar_medicao_data')
def consultar_medicao_data():

#    modo = request.args.get("modo")
    idEmpreend = IdEmpreend().get()
    dtCarga = request.args.get("dtCarga")

    if dtCarga is None and not DtCarga().has():
      return redirect('/tratar_medicoes')
    elif dtCarga is None:
      dtCarga = DtCarga().get()
    else:
      DtCarga().set(dtCarga)


    print('------ consultar_medicao_data ------')
#    print(modo)
    print (idEmpreend, dtCarga)

    medC = medicaoController ()
    medS = medC.consultarMedicaoPelaData (idEmpreend, dtCarga)

    print('------ consultar_medicao_data fim --------')
#    print(modo)

    return render_template("medicao_itens.html", medicoes=medS)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

@app.route('/upload_arquivo_medicoes', methods=['GET', 'POST'])
def upload_arquivo_medicoes():
    # check if the post request has the file part
    if 'file' not in request.files:
        mensagem = "Erro no upload do arquivo. No file part."
        return render_template("erro.html", mensagem=mensagem)
    file = request.files['file']
    if file:
        if file.filename == '':
            mensagem = "Erro no upload do arquivo. Nome do arquivo='" + file.filename + "'."
        elif not allowed_file(file.filename):
            mensagem = "Erro no upload do arquivo. Arquivo='" + file.filename + "' não possui uma das extensões permitidas."
        else:
            filename = secure_filename(file.filename)
            caminhoArq = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(caminhoArq)

#            idEmpreend = request.args.get("idEmpreend")
            idEmpreend = request.form.get("idEmpreend")

            print ('-------------- upload_arquivo_medicoes ----------------')

            orcC = medicaoController ()
            print (caminhoArq, '   ', idEmpreend)
            orcC.carregar_medicoes(caminhoArq, idEmpreend)

            return redirect("/tratar_medicoes")
    else:
        mensagem = "Erro no upload do arquivo. Você precisa selecionar um arquivo."
    return render_template("erro.html", mensagem=mensagem)


############ AGENDA ######################

@app.route('/tratar_agendas')
def tratar_agendas():

# ---- teste de sessão
    temp = protectedPage()

    if temp != None:
        print ('protectedPage()')
        return temp
#---- fim teste de sessão

    idEmpreend = request.args.get("idEmpreend")
    nmEmpreend = request.args.get("nmEmpreend")

    print('-----tratar_agendas----')
    print(idEmpreend,nmEmpreend)

    agendaC = agendaController ()
    agendaS = agendaC.consultarAgendas (idEmpreend)

    if len(agendaS) == 0:
        return render_template("lista_agendas.html", idEmpreend=idEmpreend, mensagem="Agenda não cadastrada!!!", nmEmpreend=nmEmpreend, agendaS=agendaS)
    else:
        return render_template("lista_agendas.html", idEmpreend=idEmpreend, nmEmpreend=nmEmpreend, agendaS=agendaS)

@app.route('/abrir_cad_agenda', methods=['POST'])
def abrir_cad_agenda():

    idEmpreend = request.form.get("idEmpreend")
    nmEmpreend = request.form.get("nmEmpreend")

    print('-----------abrir_cad_agenda-----------')
    print(idEmpreend)

    return render_template("agenda.html", idEmpreend=idEmpreend, nmEmpreend=nmEmpreend)

#@app.route('/abrir_edicao_agenda', methods=['POST'])
#def abrir_edicao_agenda():
#
#    idUnidade = request.form.get("idUnidade")
#    print('----------- abrir_edicao_agenda')
#    print (idUnidade)
#    unidc = agendaController ()
#    unid = unidc.consultarUnidadePeloId (idUnidade)
#
#    print(unid)
#    return render_template("agenda.html", agenda=agenda)

@app.route('/cadastrar_agenda', methods=['POST'])
def cadastrar_agenda():

    print('passei aqui 1')
    nmEmpreend = request.form.get('nmEmpreend')

    t = agenda ()
    t.setIdEmpreend (request.form.get('idEmpreend'))
    t.setNmAgenda (request.form.get('nmAgenda'))
    t.setQtUnidade (request.form.get('qtUnidade'))

    print('passei aqui 2')

    agendaC = agendaController()
    agendaC.inserirAgenda(t)

    idEmpreend = request.form.get('idEmpreend')
    agendaS = agendaC.consultarAgendas (idEmpreend)
    print('passei aqui')
    return render_template("lista_agendas.html", agendaS=agendaS, nmEmpreend=nmEmpreend)

@app.route('/editar_agenda')
def editar_agenda():

    idT = request.args.get("idAgenda")
    idEmpreend = request.args.get("idEmpreend")
    nmEmpreend = request.args.get("nmEmpreend")

    print('------ editar_agenda --------')
    print (idT,nmEmpreend)

    agendaC = agendaController ()
    agenda = agendaC.consultarAgendaPeloId (idT)

    print(agenda)
    return render_template("agenda.html", agenda=agenda, idEmpreend=idEmpreend, nmEmpreend=nmEmpreend)

@app.route('/salvar_alteracao_agenda', methods=['POST'])
def salvar_alteracao_agenda():

    print('------- salvar_alteracao_agenda INICIO --------')
    nmEmpreend = request.form.get("nmEmpreend")

    t = agenda ()
    t.setIdAgenda (request.form.get('idAgenda'))
    t.setIdEmpreend (request.form.get('idEmpreend'))
    t.setNmAgenda (request.form.get('nmAgenda'))
    t.setQtUnidade (request.form.get('qtUnidade'))

    print('------- salvar_alteracao_agenda --------')
    idEmpreend = request.form.get('idEmpreend')
    print(idEmpreend)

    agendaC = agendaController()
    agendaC.salvarAgenda(t)

    agendaS = agendaC.consultarAgendas (idEmpreend)
    return render_template("lista_agendas.html", idEmpreend=idEmpreend, nmEmpreend=nmEmpreend, agendaS=agendaS)

@app.route('/consultar_agenda')
def consultar_agenda():

    modo = request.args.get("modo")
    idT = request.args.get("idAgenda")
    idEmpreend = request.args.get("idEmpreend")
    nmEmpreend = request.args.get("nmEmpreend")


    print('------ consultar_agenda --------')
    print(modo, idT,idEmpreend,nmEmpreend)

    agendac = agendaController ()
    agenda = agendac.consultarAgendaPeloId (idT)
    print(agenda)

    print('------ consultar_agenda --------')
    print(modo)

    return render_template("agenda.html", agenda=agenda, modo=modo, idEmpreend=idEmpreend, nmEmpreend=nmEmpreend)

@app.route('/excluir_agenda')
def excluir_agenda():

    idAgenda = request.args.get('idAgenda')
    idEmpreend = request.args.get('idEmpreend')
    nmEmpreend = request.args.get('nmEmpreend')

    print('--------------excluir_agenda -------------')
    print (idAgenda, idEmpreend)

    agendaC = agendaController()
    agendaC.excluirAgenda(idAgenda)
    agendaS = agendaC.consultarAgendas (idEmpreend)

    if len(agendaS) == 0:
        empc = empreendimentoController ()
        emps = empc.consultarEmpreendimentos ()
        return render_template("home.html", empreends=emps)
    else:
        return render_template("lista_agendas.html", agendaS=agendaS, idEmpreend=idEmpreend, nmEmpreend=nmEmpreend)

############ GRAFICOS ######################

@app.route('/obter_grafico', methods=['GET'])
def obter_grafico():

    grafNome = request.args.get("grafNome")

    print ('------------ obter_grafico -------------')
    print (grafNome)
    return send_file(grafNome, mimetype='image/png')


@app.route('/graf_orcamento_liberacao', methods=['GET'])
def graf_orcamento_liberacao():

    tipo = request.args.get("tipo")
    idEmpreend = IdEmpreend().get()
    dtCarga = request.args.get("dtCarga")
    mes = request.args.get("mesV")
    ano = request.args.get("anoV")
    print ('==============>', mes, ano)

    medC = orcamentoController ()
    medS = medC.consultarOrcamentoPelaData (idEmpreend, dtCarga)

    fisico = []
    financeiro = []
    orcado = []
    index = []

    for m in medS:
        index.append(m.getItem())

        if tipo == "valor":
            fisico.append(float(0 if m.getFisicoValor() is None else m.getFisicoValor()))
            financeiro.append(float(0 if m.getFinanceiroValor() is None else m.getFinanceiroValor()))
            orcado.append(float(0 if m.getOrcadoValor() is None else m.getOrcadoValor()))
        else:
            fisico.append(float(m.getFisicoPercentual()))
            financeiro.append(float(m.getFinanceiroPercentual()))

#    plt.title("\Medição Física da Obra x Liberação Financeira (em %)", fontdict={'family': 'serif', 'color': 'black', 'weight': 'bold', 'size': 12}, loc='center')
        if tipo == "valor":
            df = pd.DataFrame({'Físico': fisico, 'Financeiro': financeiro, 'Orçado': orcado}, index=index)
        else:
            df = pd.DataFrame({'Físico': fisico, 'Financeiro': financeiro}, index=index)

    ax = df.plot.barh()
    ax.set_xlabel('Valor em milhões')
    plt.legend(loc='lower left', bbox_to_anchor=(0,-0.2), fontsize=8,ncols=3) # Adicionar a legenda fora do gráfico

    grafC = graficoController (app)

    diretorio = grafC.montaDir(idEmpreend, mes, ano)
    grafC.criaDir(diretorio)

    if tipo == "valor":
        grafNome = diretorio + 'graf_orcamento_liberacao_valor.png'
    else:
        grafNome = diretorio + 'graf_orcamento_liberacao_percentual.png'

    plt.savefig(grafNome, bbox_inches='tight')

    return render_template("orcamento_liberacao.html", grafNome=grafNome, version=random.randint(1,100000))

@app.route('/graf_progresso_obra', methods=['GET'])
def graf_progresso_obra():

# Gráfico de linhas
# PROGRESSO FÍSICO DA OBRA (Previsto x Realizado)

    idEmpreend = 55
    mes = "12"
    ano = "2024"
    mesVigenciaIni = '05'
    anoVigenciaIni = '2024'
    mesVigenciaFim = '12'
    anoVigenciaFim = '2024'


    geral = geralController (app)
    preC = medicaoController ()
    preS = preC.consultarMedicoesPorPeriodo (idEmpreend, mesVigenciaIni, anoVigenciaIni, mesVigenciaFim, anoVigenciaFim)

    fig, ax = plt.subplots(1, 1)

    x1 = []
    x2 = []
    y1 = []
    y2 = []
    for p in preS:
#        dd = []
        periodo = geral.formatammmaa(p.getMesVigencia(),p.getAnoVigencia())
        x1.append(periodo)
        y1.append(p.getPercPrevistoAcumulado())
        if p.getPercRealizadoAcumulado() > 0:
            y2.append(p.getPercRealizadoAcumulado())
            x2.append(periodo)

    plt.figure(figsize=(25, 10))     # Determina o tamanho da figura
    plt.plot(x1, y1, label='Previsto', linewidth=4, marker='o') # espessura da linha =4
    plt.plot(x2, y2, label='Realizado', linewidth=4, marker='o') # marker indica o ponto xy

    annotationsy1 = y1
    annotationsy2 = y2

    plt.scatter(x1, y1, s=20)   # Determina caracteristicas dos pontos x/y no gráfico
    plt.scatter(x2, y2, s=20)
    plt.ylim(-5, 120)            # Força os valores do eixo Y
    plt.tick_params(labelsize=14) # tamanho da letra nos eixos X e Y

    plt.title("PROGRESSO FÍSICO DA OBRA (Previsto x Realizado)", fontdict={'family': 'serif', 'color': 'black', 'weight': 'bold', 'size': 28}, loc='center')

    for xi, yi, text in zip(x1, y1, annotationsy1):
        plt.annotate(text, xy=(xi, yi), xycoords='data', xytext=(3, 10), textcoords='offset points', fontsize=14)
    for xi, yi, text in zip(x2, y2, annotationsy2):
        plt.annotate(text, xy=(xi, yi), xycoords='data', xytext=(3, -20), textcoords='offset points', fontsize=14)

    plt.legend(fontsize=20, loc="upper left")
#    plt.xlabel(fontsize=14)
#    plt.ylabel(fontsize=14)

    grafC = graficoController (app)

    idEmpreend = str(55)            ###### preciso montar esse informação
    mes = "12"
    ano = "2024"

    diretorio = grafC.montaDir(idEmpreend, mes, ano)
    grafC.criaDir(diretorio)
    grafNome = diretorio + 'graf_progresso_obra.png'

    plt.savefig(grafNome) # , bbox_inches='tight')

    return

@app.route('/graf_indices_garantia_I', methods=['GET'])
def graf_indices_garantia_I():
# ÍNDICES DE GARANTIA

    idEmpreend = 55
    mes = "12"
    ano = "2024"
    mesVigenciaIni = '01'
    anoVigenciaIni = '2024'
    mesVigenciaFim = '04'
    anoVigenciaFim = '2024'

    geral = geralController (app)
    empC = empreendimentoController ()
    empS = empC.consultarEmpreendimentoPeloId (idEmpreend)
    uniC = unidadeController ()
    uniS = uniC.consultarUnidadeRecebibeis (idEmpreend)

    x1 = ['jan', 'fev', 'mar', 'abr']
    y1 = [ 1.20, 1.20, 1.20, 1.20]
    y2 = [ 1.00, 1.23, 1.29, 1.42]

    linhas = [1.00, 1.10, 1.20, 1.30, 1.40, 1.50, 1.60]
    plt.hlines(linhas, 0, 3, '#9feafc')

    plt.plot(x1, y1, label='IC Estipulado em contrato')
    plt.plot(x1, y2, label='IC Recebiveis + estoque')

    annotationsy1 = y1
    annotationsy2 = y2

    plt.scatter(x1, y1, s=20)
    plt.scatter(x1, y2, s=20)

    plt.ylim(0.9, 1.6)

    plt.title("Índices de garantia previsto x existente", fontdict={'family': 'serif', 'color': 'black', 'weight': 'bold', 'size': 12}, loc='center')

    for xi, yi, text in zip(x1, y1, annotationsy1):
        plt.annotate(text, xy=(xi, yi), xycoords='data', xytext=(3, 10), textcoords='offset points')
    for xi, yi, text in zip(x1, y2, annotationsy2):
        plt.annotate(text, xy=(xi, yi), xycoords='data', xytext=(3, -10), textcoords='offset points')

    plt.legend(loc='lower left', bbox_to_anchor=(0,-0.2), fontsize=8,ncols=2) # Adicionar a legenda fora do gráfico
    plt.tight_layout()    # Ajustar o layout para evitar cortes
    plt.margins(0.1,0.1)  # Ajustar margens da caixa x gráfico

    grafC = graficoController (app)

    idEmpreend = str(55)            ###### preciso montar esse informação
    mes = "12"
    ano = "2024"

    diretorio = grafC.montaDir(idEmpreend, mes, ano)
    grafC.criaDir(diretorio)
    grafNome = diretorio + 'graf_indices_garantia_I.png'

    plt.savefig(grafNome) # , bbox_inches='tight')

    return

@app.route('/graf_indices_garantia_II', methods=['GET'])
def graf_indices_garantia_II():
# ÍNDICES DE GARANTIA

    idEmpreend = 55
    mes = "12"
    ano = "2024"
    mesVigenciaIni = '01'
    anoVigenciaIni = '2024'
    mesVigenciaFim = '04'
    anoVigenciaFim = '2024'

    geral = geralController (app)
    preC = medicaoController ()
    preS = preC.consultarMedicoesPorPeriodo (idEmpreend, mesVigenciaIni, anoVigenciaIni, mesVigenciaFim, anoVigenciaFim)

    x1 = ['jan', 'fev', 'mar', 'abr']
    y3 = [ 0.10, 0.15, 0.20, 0.29]
    y4 = [ 0.90, 1.08, 1.09, 1.13]

    linhas = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.00, 1.10, 1.20]

    plt.hlines(linhas, 0, 3, '#9feafc')
    plt.plot(x1, y3, label='IC Recebiveis')
    plt.plot(x1, y4, label='IC Estoque')

    annotationsy3 = y3
    annotationsy4 = y4

    plt.scatter(x1, y3, s=20)
    plt.scatter(x1, y4, s=20)

    plt.ylim(0.0, 1.2)

    plt.title("Índices de garantia previsto x existente", fontdict={'family': 'serif', 'color': 'black', 'weight': 'bold', 'size': 12}, loc='center')

    for xi, yi, text in zip(x1, y3, annotationsy3):
        plt.annotate(text, xy=(xi, yi), xycoords='data', xytext=(3, 10), textcoords='offset points')
    for xi, yi, text in zip(x1, y4, annotationsy4):
        plt.annotate(text, xy=(xi, yi), xycoords='data', xytext=(3, -10), textcoords='offset points')

    plt.legend(loc='lower left', bbox_to_anchor=(0,-0.2), fontsize=8,ncols=2) # Adicionar a legenda fora do gráfico
    plt.tight_layout()    # Ajustar o layout para evitar cortes
    plt.margins(0.1,0.1)  # Ajustar margens da caixa x gráfico

    grafC = graficoController (app)

    idEmpreend = str(55)            ###### preciso montar esse informação
    mes = "12"
    ano = "2024"

    diretorio = grafC.montaDir(idEmpreend, mes, ano)
    grafC.criaDir(diretorio)
    grafNome = diretorio + 'graf_indices_garantia_II.png'

    plt.savefig(grafNome) # , bbox_inches='tight')

    return

@app.route('/graf_vendas', methods=['GET'])
def graf_vendas():
# Gráfico de rosca
# ÍNDICES DE VENDAS

    idEmpreend = str(55)            ###### preciso montar esse informação
    mes = "12"
    ano = "2024"
    unidc = unidadeController ()
    unid = unidc.consultarUnidadeVendas(idEmpreend)

    fig, ax = plt.subplots(figsize=(6, 3), subplot_kw=dict(aspect="equal"))

    tpStatus = []
    data = []
    soma = 0

    for n in unid:
        soma += n.getTtStatus()
        data.append(n.getTtStatus())

    recipe = []

    for n in unid:
        perc = round((n.getTtStatus()/soma)*100)
        texto = str(n.getTtStatus()) + " " + n.getStatus() + " (" + str(perc) + "%)"
        recipe.append(texto)

    wedges, texts = ax.pie(data, wedgeprops=dict(width=0.5), startangle=-40)

    bbox_props = dict(boxstyle="square,pad=0.3", fc="w", ec="k", lw=0.72)
    kw = dict(arrowprops=dict(arrowstyle="-"), bbox=bbox_props, zorder=0, va="center")

    for i, p in enumerate(wedges):
        ang = (p.theta2 - p.theta1)/2. + p.theta1
        y = np.sin(np.deg2rad(ang))
        x = np.cos(np.deg2rad(ang))
        horizontalalignment = {-1: "right", 1: "left"}[int(np.sign(x))]
        connectionstyle = f"angle,angleA=0,angleB={ang}"
        kw["arrowprops"].update({"connectionstyle": connectionstyle})
        ax.annotate(recipe[i], xy=(x, y), xytext=(1.35*np.sign(x), 1.4*y),
                    horizontalalignment=horizontalalignment, **kw)

    ax.set_title("Vendas", fontdict={'family': 'serif', 'color': 'black', 'weight': 'bold', 'size': 12}, loc='center')

    grafC = graficoController (app)

    diretorio = grafC.montaDir(idEmpreend, mes, ano)
    grafC.criaDir(diretorio)
    grafNome = diretorio + 'graf_vendas.png'

    plt.savefig(grafNome) # , bbox_inches='tight')

    return

@app.route('/graf_chaves', methods=['GET'])
def graf_chaves():
# ÍNDICES DE CHAVES

    idEmpreend = str(55)            ###### preciso montar esse informação
    mes = "12"
    ano = "2024"
    unidc = unidadeController ()
    unid = unidc.consultarUnidadeChaves(idEmpreend)

    labels = ['Chaves', 'Pré-chaves', 'Pós-chaves']

    total = unid.getTtChaves() + unid.getTtPreChaves() + unid.getTtPosChaves()

    perChave = unid.getTtChaves() / total
    perPreChave = unid.getTtPreChaves() / total
    perPosChave = unid.getTtPosChaves() / total

    sizes = [perChave, perPreChave, perPosChave]
#    print('sizes = ', sizes)

    fig1, ax1 = plt.subplots()

    ax1.pie(sizes, labels=labels, autopct='%1.1f%%', shadow=False, startangle=90, textprops={'fontsize': 16})

    ax1.axis('equal')

    grafC = graficoController (app)

    idEmpreend = str(55)            ###### preciso montar esse informação
    mes = "12"
    ano = "2024"

    diretorio = grafC.montaDir(idEmpreend, mes, ano)
    grafC.criaDir(diretorio)
    grafNome = diretorio + 'graf_chaves.png'

    plt.savefig(grafNome) # , bbox_inches='tight')
    return

############ TABELAS ######################

@app.route('/tab_inadimplencia')
def tab_inadimplencia():

#    tipo = request.args.get("tipo")
#    idEmpreend = request.args.get("idEmpreend")
#    dtCarga = request.args.get("dtCarga")

    idEmpreend = 55
    mesIni = '10'
    anoIni = '2024'
    mesFim = '01'
    anoFim = '2025'

    geral = geralController (app)
    inaC = inadimplenciaController ()
    inaS = inaC.consultarInadimplenciaPelaData (idEmpreend, mesIni, anoIni, mesFim, anoFim)

    column_labels = []
    mesTeste = ''
    anoTeste = ''
    atrasoTeste = True

    column_labels.append('Atraso')

    for m in inaS:
        if m.getOrdem() == 1:
            column_labels.append(geral.formatammmaa(m.getMesVigencia(), m.getAnoVigencia()))
        else:
            break

#    print('++++++++ column_labels', column_labels )

    data = []

    periodoTeste = True
    ordemTeste = 1
    dd = []
    tamanho = len(inaS)
#    print ('===============> ', tamanho)
    posicao = 0

    while posicao < tamanho:
        print ('a ', posicao, tamanho)
        m=inaS[posicao]
        print ('b ',ordemTeste, m.getOrdem())
        if ordemTeste == m.getOrdem():
            if len(dd) == 0:
                dd.append(m.getPeriodo())
            dd.append(m.getQtUnidades())
        else:
            data.append(dd)
            dd=[]
            dd.append(m.getPeriodo())
            dd.append(m.getQtUnidades())
            ordemTeste += 1
        posicao += 1
    data.append(dd)

#    print('++++++++ Data', data )

    title_text = 'Inadimplência'
    fig, ax = plt.subplots(1, 1)

    # Definir tamanho das células
    cell_width = 0.6  # Largura de cada célula
    cell_height = 0.2  # Altura de cada célula
    # Calcular o tamanho total da figura com base no número de células
    num_rows = len(data) + 1  # +1 para incluir os cabeçalhos
    num_cols = len(column_labels)
    fig_width = num_cols * cell_width
    fig_height = num_rows * cell_height
    # Criar a figura com o tamanho calculado
    fig, ax = plt.subplots(figsize=(fig_width, fig_height))

    ax.axis("off")          #  Remove os eixos do gráfico, deixando apenas a tabela visível.
    tabela = ax.table(cellText=data, colLabels=column_labels, loc="center")
    tabela.auto_set_font_size(False)  # Desativa o ajuste automático do tamanho da fonte. Isso permite que você defina manualmente o tamanho da fonte.
    tabela.set_fontsize(8)
#    tabela.scale(2,1)

#   Ajustando o tamanho das colunas
    for x in range(0,num_cols):
        tabela.auto_set_column_width(x)
#   colocando cor de fundo no cabeçalho
    for (row, col), cell in tabela.get_celld().items():
        if row == 0:
            cell.set_facecolor("lightblue")

    grafC = graficoController (app)

    idEmpreend = 55            ###### preciso montar esse informação
    mes = "12"
    ano = "2024"

    diretorio = grafC.montaDir(idEmpreend, mes, ano)
    grafC.criaDir(diretorio)
    grafNome = diretorio + 'tab_inadimplencia.png'

#    plt.savefig(grafNome, edgecolor=fig.get_edgecolor(), facecolor=fig.get_facecolor(), dpi=150 )
    plt.savefig(grafNome) # , bbox_inches='tight')

    return

@app.route('/tab_notas')
def tab_notas():

#    tipo = request.args.get("tipo")
#    idEmpreend = request.args.get("idEmpreend")
#    dtCarga = request.args.get("dtCarga")

    idEmpreend = 55
    dtCarga = '2024-12-30 16:57:31'
    mes = "12"                            ###### preciso montar esse informação
    ano = "2024"

    geral = geralController (app)
    notC = notaController ()
    notS = notC.consultarNotaPelaData (idEmpreend, dtCarga)

    fig, ax = plt.subplots(1, 1)

    data = []
    somaVlNotaFiscal = 0
    somaVlEstoque = 0

    for n in notS:
        dd = []
        dd.append(n.getItem())
        somaVlNotaFiscal += n.getVlNotaFiscal()
        dd.append(geral.formataNumero(n.getVlNotaFiscal()))
        somaVlEstoque += n.getVlEstoque()
        dd.append(geral.formataNumero(n.getVlEstoque()))
        data.append(dd)

    # incluindo a linha de totais
    dd = []
    dd.append('Estoque em '+ mes + '/' + ano )
    dd.append(' ')
    dd.append(geral.formataNumero(somaVlEstoque))
    data.append(dd)

    column_labels = ["Produtos", "Valor da NF", "Estoque"]

    # Definir tamanho das células
    cell_width = 2.5  # Largura de cada célula
    cell_height = 0.2  # Altura de cada célula
    # Calcular o tamanho total da figura com base no número de células
    num_rows = len(data) + 1  # +1 para incluir os cabeçalhos
    num_cols = len(column_labels)
    fig_width = num_cols * cell_width
    fig_height = num_rows * cell_height
    # Criar a figura com o tamanho calculado
    fig, ax = plt.subplots(figsize=(fig_width, fig_height))

    ax.axis("off")          #  Remove os eixos do gráfico, deixando apenas a tabela visível.
    tabela = ax.table(cellText=data, colLabels=column_labels, loc="center")
    tabela.auto_set_font_size(False)  # Desativa o ajuste automático do tamanho da fonte. Isso permite que você defina manualmente o tamanho da fonte.
    tabela.set_fontsize(8)
#    tabela.scale(2,1)

#   Ajustando o tamanho das colunas
    for x in range(0,num_cols):
        tabela.auto_set_column_width(x)

#   colocando cor de fundo no cabeçalho
    for (row, col), cell in tabela.get_celld().items():
        if row == 0 or row == num_rows-1:
            cell.set_facecolor("lightblue") # campos em azul encima e embaixo
            if row == 0:
                cell.set_text_props(ha='center', va='center')  # Alinhar 1ª linha no centro
            else:
                if col == 0:
                   cell.set_text_props(ha='left', va='center')  # Alinhar coluna 1 da ultima linha à esquerda
        else:  # Demais itens da tabela
            if col == 0:
               cell.set_text_props(ha='left', va='center')  # Alinhar à esquerda

    grafC = graficoController (app)

    diretorio = grafC.montaDir(idEmpreend, mes, ano)
    grafC.criaDir(diretorio)
    grafNome = diretorio + 'tab_notas.png'

    plt.savefig(grafNome)

@app.route('/tab_conta_corrente')
def tab_conta_corrente():

    fig, ax = plt.subplots(1, 1)

#    tipo = request.args.get("tipo")
#    idEmpreend = request.args.get("idEmpreend")
#    dtCarga = request.args.get("dtCarga")

    idEmpreend = 55
    dtCarga = '2024-12-30 16:57:31'
    ###### preciso montar esse informação
    mes = "12"
    ano = "2024"

    geral = geralController (app)
    conC = contaController ()
    conS = conC.consultarConta (idEmpreend)

    data = []

    for c in conS:
        dd = []
        periodo = geral.formatammmaa(c.getMesVigencia(),c.getAnoVigencia())
        dd.append(periodo)
        dd.append(geral.formataNumero(c.getVlLiberacao()))
#        dd.append(geral.formataNumero(c.getVlMaterialEstoque()))
        dd.append(geral.formataNumero(c.getVlAporteConstrutora()))
        dd.append(geral.formataNumero(c.getVlReceitaRecebiveis()))
        dd.append(geral.formataNumero(c.getVlPagtoObra()))
        dd.append(geral.formataNumero(c.getVlPagtoRh()))
        dd.append(geral.formataNumero(c.getVlDiferenca()))
        dd.append(geral.formataNumero(c.getVlSaldo()))
        data.append(dd)

#    column_labels = ["Mês", "Liberação P.E.", "Mat. em estoque", "Aporte construtora", "Receita revebiveis", "Pagto obra", "Pagto RH", "Dif. encontradas", "Saldo"]
    column_labels = ["Mês", "Liberação P.E.", "Aporte construtora", "Receita revebiveis", "Pagto obra", "Pagto RH", "Dif. encontradas", "Saldo"]

    # Definir tamanho das células
    cell_width = 1.0   # Largura de cada célula
    cell_height = 0.2  # Altura de cada célula
    # Calcular o tamanho total da figura com base no número de células
    num_rows = len(data) + 1  # +1 para incluir os cabeçalhos
    num_cols = len(column_labels)
    fig_width = num_cols * cell_width
    fig_height = num_rows * cell_height
    # Criar a figura com o tamanho calculado
    fig, ax = plt.subplots(figsize=(fig_width, fig_height))

    ax.axis("off")          #  Remove os eixos do gráfico, deixando apenas a tabela visível.
    tabela = ax.table(cellText=data, colLabels=column_labels, loc="center")
    tabela.auto_set_font_size(False)  # Desativa o ajuste automático do tamanho da fonte. Isso permite que você defina manualmente o tamanho da fonte.
    tabela.set_fontsize(8)
#    tabela.scale(2,1)

#   Ajustando o tamanho das colunas
    for x in range(0,num_cols):
        tabela.auto_set_column_width(x)

#   colocando cor de fundo no cabeçalho
    for (row, col), cell in tabela.get_celld().items():
        if row == 0:
            cell.set_facecolor("lightblue")
            cell.set_text_props(ha='center', va='center')  # Alinhar no centro
        else:  # Demais itens da tabela
            cell.set_text_props(ha='right', va='center')  # Alinhar à esquerda

    grafC = graficoController (app)

    diretorio = grafC.montaDir(idEmpreend, mes, ano)
    grafC.criaDir(diretorio)
    grafNome = diretorio + 'tab_conta_corrente.png'

    plt.savefig(grafNome)

@app.route('/tab_garantias_geral')
def tab_garantias_geral():

#    tipo = request.args.get("tipo")
#    idEmpreend = request.args.get("idEmpreend")
#    dtCarga = request.args.get("dtCarga")

    idEmpreend = 55
    dtCarga = '2024-12-30 16:57:31'
    tipo = 'Geral'

    geral = geralController (app)
    ponC = pontoController ()
    ponS = ponC.consultarPontosPelaData (idEmpreend, dtCarga, tipo)

    fig, ax = plt.subplots(1, 1)

    data = []

    for p in ponS:
        dd = []
        dd.append(p.getHistorico())
        dd.append(p.getStatus())
        dd.append(p.getObservacao())
        data.append(dd)

    column_labels = ["Histórico", "Status", "Obs"]

    # Definir tamanho das células
    cell_width = 2.0  # Largura de cada célula
    cell_height = 0.2  # Altura de cada célula
    # Calcular o tamanho total da figura com base no número de células
    num_rows = len(data) + 1  # +1 para incluir os cabeçalhos
    num_cols = len(column_labels)
    fig_width = num_cols * cell_width
    fig_height = num_rows * cell_height
    # Criar a figura com o tamanho calculado
    fig, ax = plt.subplots(figsize=(fig_width, fig_height))

    ax.axis("off")          #  Remove os eixos do gráfico, deixando apenas a tabela visível.
    tabela = ax.table(cellText=data, colLabels=column_labels, loc="center")
    tabela.auto_set_font_size(False)  # Desativa o ajuste automático do tamanho da fonte. Isso permite que você defina manualmente o tamanho da fonte.
    tabela.set_fontsize(8)
#    tabela.scale(2,1)

#   Ajustando o tamanho das colunas
    for x in range(0,num_cols):
        tabela.auto_set_column_width(x)
#   colocando cor de fundo no cabeçalho
    for (row, col), cell in tabela.get_celld().items():
        cell.set_edgecolor("none")  # Define a cor da borda como "none" (sem borda)
        if row == 0:
            cell.set_facecolor("lightblue")
            cell.set_text_props(ha='center', va='center')  # Alinhar no centro
        else:  # Demais itens da tabela
            cell.set_text_props(ha='left', va='center')  # Alinhar à esquerda

    grafC = graficoController (app)

    idEmpreend = str(55)            ###### preciso montar esse informação
    mes = "12"
    ano = "2024"

    diretorio = grafC.montaDir(idEmpreend, mes, ano)
    grafC.criaDir(diretorio)
    grafNome = diretorio + 'tab_garantias_geral.png'

    plt.savefig(grafNome)

@app.route('/tab_garantias_obra')
def tab_garantias_obra():

#    tipo = request.args.get("tipo")
#    idEmpreend = request.args.get("idEmpreend")
#    dtCarga = request.args.get("dtCarga")

    idEmpreend = 55
    dtCarga = '2024-12-30 16:57:31'
    tipo = 'Obra'

    geral = geralController (app)
    ponC = pontoController ()
    ponS = ponC.consultarPontosPelaData (idEmpreend, dtCarga, tipo)

    fig, ax = plt.subplots(1, 1)

    data = []

    for p in ponS:
        dd = []
        dd.append(p.getHistorico())
        dd.append(p.getStatus())
        dd.append(p.getObservacao())
        data.append(dd)

    column_labels = ["Histórico", "Status", "Obs"]

    # Definir tamanho das células
    cell_width = 2.0  # Largura de cada célula
    cell_height = 0.2  # Altura de cada célula
    # Calcular o tamanho total da figura com base no número de células
    num_rows = len(data) + 1  # +1 para incluir os cabeçalhos
    num_cols = len(column_labels)
    fig_width = num_cols * cell_width
    fig_height = num_rows * cell_height
    # Criar a figura com o tamanho calculado
    fig, ax = plt.subplots(figsize=(fig_width, fig_height))

    ax.axis("off")          #  Remove os eixos do gráfico, deixando apenas a tabela visível.
    tabela = ax.table(cellText=data, colLabels=column_labels, loc="center")
    tabela.auto_set_font_size(False)  # Desativa o ajuste automático do tamanho da fonte. Isso permite que você defina manualmente o tamanho da fonte.
    tabela.set_fontsize(8)
#    tabela.scale(2,1)

#   Ajustando o tamanho das colunas
    for x in range(0,num_cols):
        tabela.auto_set_column_width(x)
#   colocando cor de fundo no cabeçalho
    for (row, col), cell in tabela.get_celld().items():
        cell.set_edgecolor("none")  # Define a cor da borda como "none" (sem borda)
        if row == 0:
            cell.set_facecolor("lightblue")
            cell.set_text_props(ha='center', va='center')  # Alinhar no centro
        else:  # Demais itens da tabela
            cell.set_text_props(ha='left', va='center')  # Alinhar à esquerda

    grafC = graficoController (app)

    idEmpreend = str(55)            ###### preciso montar esse informação
    mes = "12"
    ano = "2024"

    diretorio = grafC.montaDir(idEmpreend, mes, ano)
    grafC.criaDir(diretorio)
    grafNome = diretorio + 'tab_garantias_obra.png'

    plt.savefig(grafNome)

@app.route('/tab_certidoes')
def tab_garantias_certidoes():

#    tipo = request.args.get("tipo")
#    idEmpreend = request.args.get("idEmpreend")
#    dtCarga = request.args.get("dtCarga")

    idEmpreend = 55
    dtCarga = '2024-12-30 16:57:31'
    tipo = 'Dcto'

    geral = geralController (app)
    ponC = pontoController ()
    ponS = ponC.consultarPontosPelaData (idEmpreend, dtCarga, tipo)

    fig, ax = plt.subplots(1, 1)

    data = []

    for p in ponS:
        dd = []
        dd.append(p.getHistorico())
        dd.append(p.getStatus())
        dd.append(p.getObservacao())
        data.append(dd)

    column_labels = ["Doc. Fiscal", "Status", "Validade"]

    # Definir tamanho das células
    cell_width = 0.8  # Largura de cada célula
    cell_height = 0.2  # Altura de cada célula
    # Calcular o tamanho total da figura com base no número de células
    num_rows = len(data) + 1  # +1 para incluir os cabeçalhos
    num_cols = len(column_labels)
    fig_width = num_cols * cell_width
    fig_height = num_rows * cell_height
    # Criar a figura com o tamanho calculado
    fig, ax = plt.subplots(figsize=(fig_width, fig_height))

    ax.axis("off")          #  Remove os eixos do gráfico, deixando apenas a tabela visível.
    tabela = ax.table(cellText=data, colLabels=column_labels, loc="center")
    tabela.auto_set_font_size(False)  # Desativa o ajuste automático do tamanho da fonte. Isso permite que você defina manualmente o tamanho da fonte.
    tabela.set_fontsize(8)
#    tabela.scale(2,1)

#   Ajustando o tamanho das colunas
    for x in range(0,num_cols):
        tabela.auto_set_column_width(x)
#   colocando cor de fundo no cabeçalho
    for (row, col), cell in tabela.get_celld().items():
        cell.set_edgecolor("none")  # Define a cor da borda como "none" (sem borda)
        if row == 0:
            cell.set_facecolor("lightblue")
            cell.set_text_props(ha='center', va='center')  # Alinhar no centro
        else:  # Demais itens da tabela
            cell.set_text_props(ha='left', va='center')  # Alinhar à esquerda

    grafC = graficoController (app)

    idEmpreend = str(55)            ###### preciso montar esse informação
    mes = "12"
    ano = "2024"

    diretorio = grafC.montaDir(idEmpreend, mes, ano)
    grafC.criaDir(diretorio)
    grafNome = diretorio + 'tab_certidoes.png'

    plt.savefig(grafNome)

@app.route('/tab_acomp_financeiro')
def tab_acomp_financeiro():

#    tipo = request.args.get("tipo")
#    idEmpreend = request.args.get("idEmpreend")
#    dtCarga = request.args.get("dtCarga")

    idEmpreend = 55
    dtCarga = '2024-12-30 16:57:31'

    geral = geralController (app)
    finC = financeiroController ()
    finS = finC.consultarFinanceiroPelaData (idEmpreend, dtCarga)
    fig, ax = plt.subplots(1, 1)

    data = []

    for m in finS:
        dd = []
        dd.append(m.getHistorico())
        dd.append(geral.formataPerc(m.getPercFinanceiro(),0))
        dd.append(geral.formataNumero(m.getVlFinanceiro(),'R$'))
        data.append(dd)

    column_labels = ["                            ", "         ", "                "]

    # Definir tamanho das células
    cell_width = 1.2   # Largura de cada célula
    cell_height = 0.2  # Altura de cada célula
    # Calcular o tamanho total da figura com base no número de células
    num_rows = len(data) + 1  # +1 para incluir os cabeçalhos
    num_cols = len(column_labels)
    fig_width = num_cols * cell_width
    fig_height = num_rows * cell_height
    # Criar a figura com o tamanho calculado
    fig, ax = plt.subplots(figsize=(fig_width, fig_height))

    ax.axis("off")          #  Remove os eixos do gráfico, deixando apenas a tabela visível.
    tabela = ax.table(cellText=data, colLabels=column_labels, loc="center")
    tabela.auto_set_font_size(False)  # Desativa o ajuste automático do tamanho da fonte. Isso permite que você defina manualmente o tamanho da fonte.
    tabela.set_fontsize(8)
#    tabela.scale(2,1)

#   Ajustando o tamanho das colunas
    for x in range(0,num_cols):
        tabela.auto_set_column_width(x)
#   colocando cor de fundo no cabeçalho
    for (row, col), cell in tabela.get_celld().items():
        cell.set_edgecolor("none")  # Define a cor da borda como "none" (sem borda)
#        if row == 0:
#            cell.set_facecolor("lightblue")
#            cell.set_text_props(ha='center', va='center')  # Alinhar no centro
#        else:  # Demais itens da tabela
        cell.set_text_props(ha='left', va='center')  # Alinhar à esquerda

    grafC = graficoController (app)

    idEmpreend = str(55)            ###### preciso montar esse informação
    mes = "12"
    ano = "2024"

    diretorio = grafC.montaDir(idEmpreend, mes, ano)
    grafC.criaDir(diretorio)
    grafNome = diretorio + 'tab_acomp_financeiro.png'

    plt.savefig(grafNome)

@app.route('/prev_realizado')
def tab_prev_realizado():

#    tipo = request.args.get("tipo")
#    idEmpreend = request.args.get("idEmpreend")

    idEmpreend = 55
    mes = "12"
    ano = "2024"

    geral = geralController (app)
    preC = medicaoController ()
    preS = preC.consultarMedicoes (idEmpreend)

    fig, ax = plt.subplots(1, 1)

    data = []

    for p in preS:
        dd = []
        dd.append(str(p.getNrMedicao())+'ª')
        periodo = geral.formatammmaa(p.getMesVigencia(),p.getAnoVigencia())
        dd.append(periodo)
        dd.append(geral.formataNumero(p.getPercPrevistoAcumulado()))
        dd.append(geral.formataNumero(p.getPercRealizadoAcumulado()))
        if p.getPercRealizadoAcumulado() != 0:
            dd.append(geral.formataNumero(p.getPercRealizadoAcumulado()-p.getPercPrevistoAcumulado()))
        else:
            dd.append('')
        dd.append(geral.formataNumero(p.getPercPrevistoPeriodo()))
        data.append(dd)

#    print (data)
    column_labels = ["Medição", "Período", "Previsto acum.", "Realizado acum.", "Diferença","Previsto período"]

    # Definir tamanho das células
    cell_width = 1.2  # Largura de cada célula
    cell_height = 0.2  # Altura de cada célula
    # Calcular o tamanho total da figura com base no número de células
    num_rows = len(data) + 1  # +1 para incluir os cabeçalhos
    num_cols = len(column_labels)
    fig_width = num_cols * cell_width
    fig_height = num_rows * cell_height
#    print ('===============>>>>', num_rows, num_cols)
    # Criar a figura com o tamanho calculado
    fig, ax = plt.subplots(figsize=(fig_width, fig_height))

    ax.axis("off")          #  Remove os eixos do gráfico, deixando apenas a tabela visível.
    tabela = ax.table(cellText=data, colLabels=column_labels, loc="center")
    tabela.auto_set_font_size(False)  # Desativa o ajuste automático do tamanho da fonte. Isso permite que você defina manualmente o tamanho da fonte.
    tabela.set_fontsize(8)
#    tabela.scale(2,1)

#   Ajustando o tamanho das colunas
    for x in range(0,num_cols):
        tabela.auto_set_column_width(x)
#   colocando cor de fundo no cabeçalho
    for (row, col), cell in tabela.get_celld().items():
        if row == 0:
            cell.set_facecolor("lightblue")

    grafC = graficoController (app)

    diretorio = grafC.montaDir(idEmpreend, mes, ano)
    grafC.criaDir(diretorio)
    grafNome = diretorio + 'tab_prev_realizado.png'

    plt.savefig(grafNome)

@app.route('/tab_orcamento_liberacao')
def tab_orcamento_liberacao():

    idEmpreend = IdEmpreend().get()
    dtCarga = request.args.get("dtCarga")
    mes = request.args.get("mesV")
    ano = request.args.get("anoV")

#    idEmpreend = 45
#    dtCarga = '2025-02-26 22:36:33'
    ###### preciso montar esse informação

    geral = geralController (app)
    medC = orcamentoController ()
    medS = medC.consultarOrcamentoPelaData (idEmpreend, dtCarga)
    fig, ax = plt.subplots(1, 1)

    data = []
    somaOrcadoValor = 0
    somaFisicoValor = 0
    somaFisicoSaldo = 0
    somaFinanceiroValor = 0
    somaFinanceiroSaldo = 0

    for m in medS:
        dd = []
        dd.append(m.getItem())
        somaOrcadoValor += 0 if m.getOrcadoValor() is None else m.getOrcadoValor()
        dd.append(geral.formataNumero(m.getOrcadoValor()))
        dd.append(' ')
        somaFisicoValor += 0 if m.getFisicoValor() is None else m.getFisicoValor()
        dd.append(geral.formataNumero(m.getFisicoValor()))
        dd.append(geral.formataNumero(m.getFisicoPercentual()))
        somaFisicoSaldo += 0 if m.getFisicoSaldo() is None else m.getFisicoSaldo()
        dd.append(geral.formataNumero(m.getFisicoSaldo()))
        dd.append(' ')
        somaFinanceiroValor += 0 if m.getFinanceiroValor() is None else m.getFinanceiroValor()
        dd.append(geral.formataNumero(m.getFinanceiroValor()))
        dd.append(geral.formataNumero(m.getFinanceiroPercentual()))
        somaFinanceiroSaldo += 0 if m.getFinanceiroSaldo() is None else m.getFinanceiroSaldo()
        dd.append(geral.formataNumero(m.getFinanceiroSaldo()))
        data.append(dd)

    # incluindo a linha de totais
    dd = []
    dd.append('Total do Orçamento')
    dd.append(geral.formataNumero(somaOrcadoValor))
    dd.append(' ')
    dd.append(geral.formataNumero(somaFisicoValor))
    somaFisicoPercentual = somaFisicoValor/somaOrcadoValor*100
    dd.append(geral.formataNumero(somaFisicoPercentual))
    dd.append(geral.formataNumero(somaFisicoSaldo))
    dd.append(' ')
    dd.append(geral.formataNumero(somaFinanceiroValor))
    somaFinanceiroPercentual = somaFinanceiroValor/somaOrcadoValor*100
    dd.append(geral.formataNumero(somaFinanceiroPercentual))
    dd.append(geral.formataNumero(somaFinanceiroSaldo))
    data.append(dd)

    column_labels = ['Descrição', 'Orçamento (R$)', ' ', 'Medição física acumulado (R$)', '(%)', 'Saldo (R$)', ' ', 'Liberação financ acumulado (R$)', '(%)', 'Saldo (R$)']

    # Definir tamanho das células
    cell_width = 1.2  # Largura de cada célula
    cell_height = 0.2  # Altura de cada célula
    # Calcular o tamanho total da figura com base no número de células
    num_rows = len(data) + 1  # +1 para incluir os cabeçalhos
    num_cols = len(column_labels)

    fig_width = num_cols * cell_width
    fig_height = num_rows * cell_height
    # Criar a figura com o tamanho calculado
    fig, ax = plt.subplots(figsize=(fig_width, fig_height))

    ax.axis("off")          #  Remove os eixos do gráfico, deixando apenas a tabela visível.
    tabela = ax.table(cellText=data, colLabels=column_labels, loc="center")
    tabela.auto_set_font_size(False)  # Desativa o ajuste automático do tamanho da fonte. Isso permite que você defina manualmente o tamanho da fonte.
    tabela.set_fontsize(8)
#    tabela.scale(2,1)

#   Ajustando o tamanho das colunas
    for x in range(0,num_cols):
        tabela.auto_set_column_width(x)

    for (row, col), cell in tabela.get_celld().items():
        if row == 0 or row == num_rows-1:     # pinta a 1ª 1 ultima linhas
            cell.set_facecolor("lightblue")
        if col == 2 or col == 6:                     # pinta as colunas de divisão
            cell.set_facecolor("lightblue")
        if row > 0 and col == 0 :
            cell.set_text_props(ha='left', va='center')  # Alinhar à esquerda

    grafC = graficoController (app)

    diretorio = grafC.montaDir(idEmpreend, mes, ano)
    grafC.criaDir(diretorio)
    grafNome = diretorio + 'tab_orcamento_liberacao.png'

    plt.savefig(grafNome)

#    plt.savefig(grafNome, bbox_inches='tight')

    return render_template("orcamento_liberacao.html", grafNome=grafNome, version=random.randint(1, 100000))

############ PDF ######################

@app.route('/gerar_relatorio', methods=['GET'])
def gerar_relatorio():

    grafC = graficoController (app)

    idEmpreend = request.args.get("idEmpreend")
    apelido    = request.args.get("apelido")
    mes        = request.args.get("mes")
    ano        = request.args.get("ano")

    # monta o diretório onde estão os gráficos e fotos
    diretorio = grafC.montaDir(idEmpreend, mes, ano)
    erros = grafC.verificaArqRelatorio(diretorio)

    # monta o diretório onde ficam todos os relatórios
    dirRelatorio = grafC.montaDir(idEmpreend, mes, ano, relatorio = True)
    grafC.criaDir(dirRelatorio)
    nomePdf = apelido + "-" + ano + "-" + mes + ".pdf"

    if grafC.verificaDir(diretorio) == False:
        # Verifica se o diretório de graficos e fotos foi criado
        mensagem="Não existem dados para o relatório"
    else:
        # Verifica se existem graficos e fotos para o relatório
        if  len(erros) > 0:
            mensagem = ''
            for n in erros:
                mensagem =  mensagem + ' # ' + n
        else:
            c = canvas.Canvas(dirRelatorio + nomePdf)

            pagina = 1
            grafC.pdfPag1(c, diretorio, pagina)
            c.showPage()
            pagina += 1
            grafC.pdfPag2(c, diretorio, pagina)
            c.showPage()
            pagina += 1
            grafC.pdfPag3(c, diretorio, pagina)
            c.showPage()
            pagina += 1
            grafC.pdfPag4(c, diretorio, pagina)
            c.showPage()
            pagina += 1
            grafC.pdfPag5(c, diretorio, pagina)
            c.showPage()
            pagina += 1
            grafC.pdfPag6(c, diretorio, pagina)
            c.showPage()
            pagina += 1
            grafC.pdfPag7(c, diretorio, pagina)
            c.showPage()
            if os.path.isfile(diretorio+"foto_1.jpeg"):
                pagina += 1
                grafC.pdfPag8(c, diretorio, pagina)
                c.showPage()
                if os.path.isfile(diretorio+"foto_7.jpeg"):
                    pagina += 1
                    grafC.pdfPag9(c, diretorio, pagina)
                    c.showPage()
                    if os.path.isfile(diretorio+"foto_13.jpeg"):
                        pagina += 1
                        grafC.pdfPag10(c, diretorio, pagina)
                        c.showPage()
                        if os.path.isfile(diretorio+"foto_19.jpeg"):
                            pagina += 1
                            grafC.pdfPag11(c, diretorio, pagina)
                            c.showPage()

            pagina += 1
            grafC.pdfPag12(c, diretorio, pagina)
            c.showPage()
            c.save()
            mensagem="RELATORIO GERADO COM SUCESSO"


    gerC = geralController (app)
    arqS = gerC.listar_arquivos_com_prefixo(dirRelatorio, apelido)

    meses = ['  ','01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
    anos = ['    ','2025', '2026', '2027', '2028', '2029', '2030']

    return render_template("relatorio.html", arquivos=arqS, listaMes = meses, listaAno = anos, apelido=apelido, idEmpreend=idEmpreend, mensagem=mensagem)

############ FOTOS ######################

@app.route('/upload_fotos')
def upload_fotos():
    return render_template("upload_fotos.html")

@app.route('/upload_arquivo_fotos', methods=['POST'])
def upload_arquivo_fotos():

    grafC = graficoController (app)

# verifique se a solicitação de postagem tem a parte do arquivo
    if 'file' not in request.files:
        mensagem = "Erro no upload do arquivo. No file part."
        return render_template("erro.html", mensagem=mensagem)

    id_empreend = str(42)
    anoMes = "2024_12"

    diretorio = app.config['DIRSYS'] + id_empreend + app.config['BARRADIR'] + anoMes + app.config['BARRADIR']
    grafC.criaDir(diretorio)

    files = request.files.getlist("file")

    for file in files:
        file.save(diretorio + file.filename)
#        file.save(app.config['UPLOAD_FOLDER'] + '\\' + file.filename)

#    print('é aqui Rodrigo !!!!!!!!')

    return render_template("erro.html", mensagem=mensagem)

############ MOBILE ######################

@app.route('/download_arquivo', methods=['GET'])
def download_arquivo():
    arquivo = request.args.get('arquivo')
    diretorio = "c://GFC//Relatorios"
    print ('+++++++++++++', arquivo)
    return send_from_directory(diretorio, arquivo, as_attachment=True)

########## FILTROS PARA TEMPLATE #########
@app.template_filter('to_date')
def format_datetime(value):
  if value is not None and value != '--' and isinstance(value, datetime):
    return value.strftime('%d/%m/%Y')
  elif isinstance(value, str):
    return converter.converterStrDateTimeToDateFormat(value)
  return value

@app.template_filter('to_datetime')
def format_datetime(value):
  if value is not None and value != '--' and isinstance(value, datetime):
    return value.strftime('%d/%m/%Y %H:%M:%S')
  elif isinstance(value, str):
    return converter.converterStrDateTimeFormatBr(value)
  return value

@app.template_filter('to_currency')
def format_datetime(value):
  if value is not None and value != '--' and converter.isNumber(value):
    return converter.converterFloatToCurrency(value)
  return value

@app.template_filter('to_cpf_cnpj')
def format_cpf(value):
  if value is  None or value == '--' or not isinstance(value, str):
    return value
  elif len(value) == 11:
    cpf = value.zfill(11)
    return f'{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}'
  elif len(value) == 14:
    cnpj = value.zfill(14)
    return f'{cnpj[:2]}.{cnpj[2:5]}.{cnpj[5:8]}/{cnpj[8:12]}-{cnpj[12:]}'
  return value

@app.template_filter('to_cel_tel')
def format_tel_cel(value):
  if value is  None or value == '--' or not isinstance(value, str):
    return value
  elif len(value) == 8 or len(value) == 9:
    tel = value.zfill(len(value))
    return f'{tel[:4]}-{tel[4:]}' if len(value) == 8 else f'{tel[:5]}-{tel[5:]}'
  elif len(value) == 10 or len(value) == 11:
    telCp = value.zfill(len(value))
    return f'({telCp[:2]}) {telCp[2:6]}-{telCp[6:]}' if len(value) == 10 else f'({telCp[:2]}) {telCp[2:7]}-{telCp[7:]}'
  return value


if __name__ == "__main__":
  init(app)
  app.run()
  #app.run(host="192.168.0.11",port=5000)
  #app.run(host="177.195.148.38",port=80)
  #app.run(host='2804:14d:32a2:8564:a16e:bd9f:ad8b:9c76',port=80)
