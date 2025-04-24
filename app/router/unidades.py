from flask import Blueprint, request, render_template, redirect
from controller.unidadeController import unidadeController
from controller.torreController import torreController
from decorators.login_riquired import login_required
from utils.CtrlSessao import IdEmpreend, NmEmpreend
import utils.converter as converter
from dto.unidade import unidade

unidade_bp = Blueprint('unidades', __name__)


@unidade_bp.route('/tratar_unidades')
@login_required
def tratarunidades():

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

    unidC = unidadeController()
    unidS = unidC.consultarUnidades(idEmpreend)

    if len(unidS) == 0:
        return render_template("lista_unidades.html",  mensagem="Unidade não Cadastrada.", unidades=unidS)
    else:
        return render_template("lista_unidades.html", unidades=unidS)


# @unidade_bp.route('/abrir_cad_unidade')
# def abrir_cad_unidade():

#     #    idEmpreend = request.args.get("idEmpreend")
#     #    IdEmpreend().set(idEmpreend)

#     ctrlTorre = torreController()
#     listaTorres = ctrlTorre.consultarTorres(IdEmpreend().get())
#     return render_template("unidade.html", listaTorres=listaTorres, current_date=date.today())


@unidade_bp.route('/cadastrar_unidade', methods=['POST'])
def cadastrar_unidade():
    un = unidade()
    un.setIdTorre(request.form.get('idTorre'))
    un.setIdUnidade(request.form.get('idUnidade'))
    un.setIdEmpreend(IdEmpreend().get())
    un.setUnidade(request.form.get('unidade'))
    un.setMesVigencia(request.form.get('mesVigencia'))
    un.setAnoVigencia(request.form.get('anoVigencia'))
    un.setVlUnidade(converter.converterStrToFloat(
        request.form.get('vlUnidade')))
    un.setStatus(request.form.get('status'))
    un.setCpfComprador(request.form.get('cpfCnpjCliente'))
    un.setVlPago(converter.converterStrToFloat(request.form.get('vlPago')))
    un.setDtOcorrencia(request.form.get('dtOcorrencia'))
    un.setFinanciado(request.form.get('financiado'))
    un.setVlChaves(converter.converterStrToFloat(request.form.get('vlChaves')))
    un.setVlPreChaves(converter.converterStrToFloat(
        request.form.get('vlPreChaves')))
    un.setVlPosChaves(converter.converterStrToFloat(
        request.form.get('vlPosChaves')))

    unid = unidadeController()

    if un.getIdUnidade():
        unid.mudarHistoricoEditado(un.getIdUnidade())

    if un.getStatus() == 'Distrato':
        un.setCpfComprador(None)
        un.setFinanciado(None)
        un.setVlPago(None)
        un.setVlChaves(None)
        un.setVlPosChaves(None)
        un.setVlPreChaves(None)
        un.setStatus('Estoque')

    unid.inserirUnidade(un)

    return redirect("/tratar_unidades")


@unidade_bp.route('/editar_unidade')
@login_required
def editar_unidade():
    idUni = request.args.get("idUnidade")

    ctrlTorre = torreController()
    unidc = unidadeController()

    listaTorres = ctrlTorre.consultarTorres(IdEmpreend().get())
    uni = unidc.consultarUnidadePeloId(idUni)
    sts = uni.getStatus()

    listaStatus = []
    if sts == 'Estoque':
        listaStatus = ['Estoque', 'Quitado', 'Vendido']
    elif sts == 'Vendido':
        listaStatus = ['Vendido', 'Quitado', 'Distrato']
    elif sts == 'Quitado':
        listaStatus = ['Quitado']
    elif sts == 'Distrato':
        listaStatus = ['Distrato']

    return render_template(
        "unidade.html",
        unidade=uni,
        listaTorres=listaTorres,
        listaStatus=listaStatus
    )


@unidade_bp.route('/consultar_unidade')
@login_required
def consultar_unidade():

    ctrlTorre = torreController()
    listaTorres = ctrlTorre.consultarTorres(IdEmpreend().get())
    modo = request.args.get("modo")
    idUni = request.args.get("idUnidade")

    print('------ consultar_unidade --------')
    print(modo)
    print(idUni)

    unidc = unidadeController()
    unidade = unidc.consultarUnidadePeloId(idUni)
    print(unidade)

    print('------ consultar_unidade --------')
    print(modo)

    return render_template("unidade.html", unidade=unidade,  listaTorres=listaTorres, modo=modo)


@unidade_bp.route('/excluir_unidade')
@login_required
def excluir_unidade():
    idUnidade = request.args.get('idUnidade')
    unidc = unidadeController()
    unidc.excluirUnidade(idUnidade)
    return redirect("/tratar_unidades")
