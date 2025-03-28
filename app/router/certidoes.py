from flask import Blueprint, request, render_template, redirect
from controller.certidaoController import certidaoController
from utils.CtrlSessao import IdEmpreend, NmEmpreend
from utils.helper import protectedPage
from dto.certidao import certidao

cert_bp = Blueprint('certidoes', __name__)

@cert_bp.route('/tratar_certidoes')
def tratar_certidoes():
  protectedPage()

  idEmpreend = request.args.get("idEmpreend")
  nmEmpreend = request.args.get("nmEmpreend")

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

  print('-----tratar_certidoes---')
  print('tratar_certidoes ',idEmpreend)

  certC = certidaoController ()
  certS = certC.consultarCertidoes (idEmpreend)

  print('-----tratar_certidoes 2 ---')
  print('tratar_certidoes ',idEmpreend)

  if len(certS) == 0:
    return render_template("certidoes.html", mensagem="Certidões não Cadastradas!!!", certidoes=certS)
  else:
    return render_template("certidoes.html", certidoes=certS[0])

@cert_bp.route('/efetuar_cad_certidoes', methods=['POST'])
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

@cert_bp.route('/salvar_certidoes', methods=['POST'])
def salvar_item_orcamento():

    item = certidao ()
    item.setIdEmpreend (request.form.get('idEmpreend'))
    item.setEstadualStatus (request.form.get('estadualStatus'))
    item.setEstadualValidade (request.form.get('estadualValidade'))
    item.setFgtsStatus (request.form.get('fgtsStatus'))
    item.setFgtsValidade (request.form.get('fgtsValidade'))
    item.setMunicipalStatus (request.form.get('municipalStatus'))
    item.setMunicipalValidade (request.form.get('municipalValidade'))
    item.setSrfInssStatus (request.form.get('srfInssStatus'))
    item.setSrfInssValidade (request.form.get('srfInssValidade'))
    item.setTrabalhistaStatus (request.form.get('trabalhistaStatus'))
    item.setTrabalhistaValidade (request.form.get('trabalhistaValidade'))

    certC = certidaoController()
    certC.salvarCertidoes(item)

    return redirect("/tratar_certidoes")
