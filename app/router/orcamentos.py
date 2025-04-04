from flask import Blueprint, request, render_template, redirect, session, current_app
from utils.CtrlSessao import IdEmpreend, DtCarga, MesVigencia, AnoVigencia, NmEmpreend, IdOrca
from controller.orcamentoController import orcamentoController
from dto.orcamento import orcamento

import os
import utils.converter as converter
from utils.helper import protectedPage, allowed_file

orca_bp = Blueprint('orcamentos', __name__)


@orca_bp.route('/abrir_cad_orcamento')
def abrir_cad_orcamento():
    return render_template("Orcamento_item.html", idEmpreend=IdEmpreend().get())


@orca_bp.route('/tratar_orcamentos')
def tratar_orcamentos():
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

    print('-----tratar_orcamentos----')
    print(idEmpreend, nmEmpreend)

    medC = orcamentoController()
    medS = medC.consultarOrcamentos(idEmpreend)

    if len(medS) == 0:
        return render_template("lista_orcamentos.html", mensagem="Medição não Cadastrada, importar o arquivo Excel!!!", orcamentos=medS)
    else:
        return render_template("lista_orcamentos.html", orcamentos=medS)


@orca_bp.route('/consultar_orcamento_data')
def consultar_orcamento_data():
    dtCarga = request.args.get("dtCarga")
    ano = request.args.get("anoV")
    mes = request.args.get("mesV")

    if dtCarga is None and not DtCarga().has():
        return redirect('/tratar_orcamentos')
    elif dtCarga is None:
        dtCarga = DtCarga().get()
    else:
        DtCarga().set(dtCarga)
        MesVigencia().set(mes)
        AnoVigencia().set(ano)

    medC = orcamentoController()
    medS = medC.consultarOrcamentoPelaData(IdEmpreend().get(), dtCarga)

    return render_template("orcamentos_itens.html", orcamentos=medS)


@orca_bp.route('/upload_arquivo_orcamentos', methods=['POST'])
def upload_arquivo_orcamentos():
    if 'file' not in request.files:
        mensagem = "Erro no upload do arquivo. No file part."
        return render_template("erro.html", mensagem=mensagem)
    file = request.files['file']
    if file:
        if file.filename == '':
            mensagem = "Erro no upload do arquivo. Nome do arquivo='" + file.filename + "'."
        elif not allowed_file(file.filename):
            mensagem = "Erro no upload do arquivo. Arquivo='" + \
                file.filename + "' não possui uma das extensões permitidas."
        else:
            orcC = orcamentoController()
            orcC.carregar_orcamentos(file, IdEmpreend().get())
            return redirect("/tratar_orcamentos")
    else:
        mensagem = "Erro no upload do arquivo. Você precisa selecionar um arquivo."
        return render_template("erro.html", mensagem=mensagem)


@orca_bp.route('/editar_item_orcamento', methods=['GET'])
def editar_item_orcamento():
    idOrc = request.args.get("idOrcamento")
    orcC = orcamentoController()
    item = orcC.consultarOrcamentoPeloId(idOrc)
    return render_template("Orcamento_item.html", item=item)


@orca_bp.route('/excluir_item_orcamento')
def excluir_item_orcamento():
    idOrc = request.args.get("idOrcamento")
    orcC = orcamentoController()
    orcC.excluirItemOrcamento(idOrc)
    return redirect('/consultar_orcamento_data')


@orca_bp.route('/excluir_orcamento')
def excluir_orcamento():
    idEmpreend = IdEmpreend().get()
    mes = request.args.get('mesV')
    ano = request.args.get('anoV')
    data = request.args.get('dtCarga')
    orcC = orcamentoController()
    orcC.excluirOrcamento(idEmpreend, mes, ano, data)
    return redirect('/tratar_orcamentos')


@orca_bp.route('/salvar_item_orcamento', methods=['POST'])
def salvar_item_orcamento():
    item = get_orcamento_form()
    orcC = orcamentoController()
    orcC.salvarItemOrcamento(item)

    return redirect("/consultar_orcamento_data")


@orca_bp.route('/incluir_item_orcamento', methods=['POST'])
def incluir_item_orcamento():
    item = get_orcamento_form()
    orcC = orcamentoController()
    orcC.inserirOrcamento(item)

    return redirect("/consultar_orcamento_data")


def get_orcamento_form() -> orcamento:
    valorOrcado = converter.converterStrToFloat(
        request.form.get('orcadoValor'))
    fisicoPercent = converter.converterStrToFloat(
        request.form.get('fisicoPercentual'), 1)
    valorFinanceiro = converter.converterStrToFloat(
        request.form.get('financeiroValor'))
    financeiroPercentual = valorFinanceiro / valorOrcado * 100
    fisicoValor = valorOrcado * fisicoPercent / 100

    item = orcamento()
    item.setIdOrcamento(request.form.get('idOrcamento'))
    item.setIdEmpreend(IdEmpreend().get())
    item.setMesVigencia(MesVigencia().get())
    item.setAnoVigencia(AnoVigencia().get())
    item.setDtCarga(DtCarga().get())
    item.setItem(request.form.get('item'))
    item.setOrcadoValor(valorOrcado)
    item.setFisicoPercentual(fisicoPercent)
    item.setFinanceiroValor(valorFinanceiro)

    item.setFinanceiroPercentual(financeiroPercentual)
    item.setFinanceiroSaldo(valorOrcado - valorFinanceiro)
    item.setFisicoValor(fisicoValor)
    item.setFisicoSaldo(valorOrcado - fisicoValor)
    return item
