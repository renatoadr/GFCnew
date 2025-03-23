from flask import Blueprint, request, render_template, redirect
from controller.unidadeController import unidadeController
from controller.unidadeController import unidadeController
from controller.torreController import torreController
from controller.torreController import torreController
from utils.CtrlSessao import IdEmpreend, NmEmpreend
from utils.helper import protectedPage
import utils.converter as converter
from dto.unidade import unidade
from datetime import date


unidade_bp = Blueprint('unidades', __name__)

@unidade_bp.route('/tratar_unidades')
def tratarunidades():

  protectedPage()

  idEmpreend = request.args.get("idEmpreend")
  nmEmpreend = request.args.get("nmEmpreend")

  if (idEmpreend is None and not IdEmpreend().has()) or (nmEmpreend is None and not NmEmpreend().has()):
    redirect('/home')

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

@unidade_bp.route('/abrir_cad_unidade')
def abrir_cad_unidade():

#    idEmpreend = request.args.get("idEmpreend")
#    IdEmpreend().set(idEmpreend)

    ctrlTorre = torreController()
    listaTorres = ctrlTorre.consultarTorres(IdEmpreend().get())
    return render_template("unidade.html", listaTorres=listaTorres, current_date=date.today())

@unidade_bp.route('/cadastrar_unidade', methods=['POST'])
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

@unidade_bp.route('/editar_unidade')
def editar_unidade():
    ctrlTorre = torreController()
    listaTorres = ctrlTorre.consultarTorres(IdEmpreend().get())
    idUni = request.args.get("idUnidade")
    print('------ editar_unidade --------')
    print (idUni)
    unidc = unidadeController ()
    unidade = unidc.consultarUnidadePeloId (idUni)
    return render_template("unidade.html", unidade=unidade, listaTorres=listaTorres)

@unidade_bp.route('/salvar_alteracao_unidade', methods=['POST'])
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

@unidade_bp.route('/consultar_unidade')
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

@unidade_bp.route('/excluir_unidade')
def excluir_unidade():
    idUnidade = request.args.get('idUnidade')
    unidc = unidadeController()
    unidc.excluirUnidade(idUnidade)
    return redirect("/tratar_unidades")
