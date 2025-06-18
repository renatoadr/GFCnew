from flask import Blueprint, request, render_template, redirect, url_for, send_file
from controller.unidadeController import unidadeController
from controller.clienteController import clienteController
from controller.torreController import torreController
from utils.CtrlSessao import IdEmpreend, NmEmpreend
from utils.converter import converterStrToFloat, maskCpfOrCnpj
from utils.flash_message import flash_message
from utils.security import login_required
from utils.helper import allowed_file
import utils.converter as converter
from dto.unidade import unidade
from datetime import datetime
from io import BytesIO
import pandas as pd
import xlsxwriter
import math
import re

unidades_bp = Blueprint('unidades', __name__)


@unidades_bp.route('/tratar_unidades')
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


@unidades_bp.route('/exportar_planilha_unidades')
@login_required
def export_planilha():
    unidC = unidadeController()
    unidS = unidC.consultarUnidades(IdEmpreend().get())
    nome_arquivo = f"gfc_valores_unidades_{NmEmpreend().get().replace(' ', '_')}.xlsx"
    fileBytes = BytesIO()
    workbook = xlsxwriter.Workbook(fileBytes, {'in_memory': True})
    worksheet = workbook.add_worksheet("unidades")

    worksheet.protect('PgFc432')

    worksheet.set_column('A:B', width=13, options={'auto_size': True})
    worksheet.set_column('C:H', width=25, options={'auto_size': True})
    worksheet.set_row(0, height=20)
    header_format = workbook.add_format({'bold': True, 'align': 'center'})
    header_format.set_align('vcenter')
    headers = [
        {'header': 'Torre', 'header_format': header_format},
        {'header': 'Unidade', 'header_format': header_format},
        {'header': 'CPF/CNPJ Cliente', 'header_format': header_format},
        {'header': 'Vigência', 'header_format': header_format},
        {'header': 'Valor da Unidade', 'header_format': header_format},
        {'header': 'Valor da Pré Chaves', 'header_format': header_format},
        {'header': 'Valor das Chaves', 'header_format': header_format},
        {'header': 'Valor do Pós Chaves', 'header_format': header_format}
    ]

    formato_moeda = workbook.add_format(
        {'num_format': '#,##0.00', "locked": False})
    formato_data = workbook.add_format(
        {'num_format': 'dd/mm/yyyy', "locked": False})
    for idx in range(0, len(unidS)):
        uni = unidS[idx]
        cel = idx + 2
        worksheet.write_string(f'A{cel}', uni.getNmTorre())
        worksheet.write_string(f'B{cel}', uni.getUnidade())
        worksheet.write_string(
            f'C{cel}', maskCpfOrCnpj(uni.getCpfComprador()) if uni.getCpfComprador(
            ) and uni.getCpfComprador() != 'None' else '',
            workbook.add_format({"locked": False}))
        worksheet.write_datetime(
            f'D{cel}', datetime(int(uni.getAnoVigencia()), int(uni.getMesVigencia()), 1), formato_data)
        worksheet.write_number(
            f'E{cel}', converterStrToFloat(uni.getVlUnidade()), formato_moeda)
        worksheet.write_number(
            f'F{cel}', converterStrToFloat(uni.getVlPreChaves()), formato_moeda)
        worksheet.write_number(
            f'G{cel}', converterStrToFloat(uni.getVlChaves()), formato_moeda)
        worksheet.write_number(
            f'H{cel}', converterStrToFloat(uni.getVlPosChaves()), formato_moeda)

    worksheet.add_table('A1:H10000', {'columns': headers})
    workbook.close()
    fileBytes.seek(0)
    return send_file(
        fileBytes,
        mimetype='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
        as_attachment=True,
        download_name=nome_arquivo
    )


@unidades_bp.route('/importar_planilha_unidades', methods=['POST'])
@login_required
def importar_planilha():
    if 'file' not in request.files:
        flash_message.error("Erro no upload do arquivo. No file part.")
        return redirect("/tratar_unidades")

    file = request.files['file']
    if file and not allowed_file(file.filename):
        flash_message.error("Este arquivo não é uma planilha")
        return redirect("/tratar_unidades")

    sheetData = pd.read_excel(file.stream)
    dictList = sheetData.to_dict()
    total = len(dictList['Torre'])
    for idx in range(0, total):
        keyRecord = f'Torre: {dictList['Torre'][idx]} e unidade: {dictList['Torre'][idx]}'
        id_torre = unidadeController.idTorrePeloNomeeUnidade(
            dictList['Unidade'][idx],
            dictList['Torre'][idx],
            IdEmpreend().get()
        )
        if not id_torre:
            flash_message.error(
                f'Não foi encontrado o id da torre. {keyRecord}')
            continue
        if isinstance(dictList['Vigência'][0], datetime):
            mes = format(dictList['Vigência'][0], '%m')
            ano = format(dictList['Vigência'][0], '%Y')
        else:
            flash_message.error(f'Vigência não é válida para {keyRecord}')
            continue

        vlUnidade = converterStrToFloat(dictList['Valor da Unidade'][idx])
        vlPreChaves = converterStrToFloat(dictList['Valor da Pré Chaves'][idx])
        vlChaves = converterStrToFloat(dictList['Valor das Chaves'][idx])
        vlPosChaves = converterStrToFloat(dictList['Valor do Pós Chaves'][idx])
        vlReceber = vlPreChaves + vlChaves + vlPosChaves
        comprador = dictList['CPF/CNPJ Cliente'][idx]
        status = 'Estoque'

        if vlReceber > 0:
            status = 'Vendido'

        if vlReceber > 0 and vlReceber >= vlUnidade:
            status = 'Quitado'

        if comprador and isinstance(comprador, str):
            comprador = re.sub(r'\D', '', comprador)
            existe = clienteController.getCliente(comprador)
            if not existe:
                comprador = None
        else:
            comprador = None

        if not flash_message.has_error():
            unidadeController.atualizarValoresUnidade((
                IdEmpreend().get(),
                id_torre,
                dictList['Unidade'][idx],
                status,
                mes,
                ano,
                comprador,
                vlUnidade,
                vlPreChaves,
                vlChaves,
                vlPosChaves,
                vlReceber,
            ))

    return redirect("/tratar_unidades")


@unidades_bp.route('/cadastrar_unidade', methods=['POST'])
def cadastrar_unidade():
    vigencia = request.form.get('vigencia')

    if vigencia:
        vigencia = vigencia.split('-')
    else:
        return redirect(url_for('unidades.editar_unidade', idUnidade=request.form.get('idUnidade')))

    un = unidade()
    un.setIdTorre(request.form.get('idTorre'))
    un.setIdUnidade(request.form.get('idUnidade'))
    un.setIdEmpreend(IdEmpreend().get())
    un.setUnidade(request.form.get('unidade'))
    un.setMesVigencia(vigencia[1])
    un.setAnoVigencia(vigencia[0])
    un.setVlUnidade(converter.converterStrToFloat(
        request.form.get('vlUnidade')))
    un.setStatus(request.form.get('status'))
    un.setCpfComprador(request.form.get('cpfCnpjCliente'))
    un.setDtOcorrencia(request.form.get('dtOcorrencia'))
    un.setFinanciado(request.form.get('financiado'))
    un.setVlChaves(converter.converterStrToFloat(request.form.get('vlChaves')))
    un.setVlPreChaves(converter.converterStrToFloat(
        request.form.get('vlPreChaves')))
    un.setVlPosChaves(converter.converterStrToFloat(
        request.form.get('vlPosChaves')))
    un.setVlReceber(somaVlReceber(un))

    unid = unidadeController()

    if un.getIdUnidade():
        unid.mudarHistoricoEditado(un.getIdUnidade())

    if un.getStatus() == 'Distrato':
        un.setCpfComprador(None)
        un.setFinanciado(None)
        un.setVlReceber(None)
        un.setVlChaves(None)
        un.setVlPosChaves(None)
        un.setVlPreChaves(None)
        un.setStatus('Estoque')

    unid.inserirUnidade(un)

    return redirect("/tratar_unidades")


@unidades_bp.route('/editar_unidade')
@login_required
def editar_unidade():
    idUni = request.args.get("idUnidade")

    ctrlTorre = torreController()
    unidc = unidadeController()

    listaTorres = ctrlTorre.consultarTorres(IdEmpreend().get())
    uni = unidc.consultarUnidadePeloId(idUni)
    uni.setVlReceber(somaVlReceber(uni))

    listaStatus = prepListaStatus(uni.getStatus())
    vigencia = f"{uni.getAnoVigencia()}-{uni.getMesVigencia()}"

    return render_template(
        "unidade.html",
        unidade=uni,
        listaTorres=listaTorres,
        listaStatus=listaStatus,
        vigencia=vigencia
    )


@unidades_bp.route('/consultar_unidade')
@login_required
def consultar_unidade():
    ctrlTorre = torreController()
    listaTorres = ctrlTorre.consultarTorres(IdEmpreend().get())
    modo = request.args.get("modo")
    idUni = request.args.get("idUnidade")

    unidc = unidadeController()
    uni = unidc.consultarUnidadePeloId(idUni)

    listaStatus = prepListaStatus(uni.getStatus())
    vigencia = f"{uni.getAnoVigencia()}-{uni.getMesVigencia()}"

    return render_template(
        "unidade.html",
        modo=modo,
        unidade=uni,
        listaTorres=listaTorres,
        listaStatus=listaStatus,
        vigencia=vigencia
    )


@unidades_bp.route('/excluir_unidade')
@login_required
def excluir_unidade():
    idUnidade = request.args.get('idUnidade')
    unidc = unidadeController()
    unidc.excluirUnidade(idUnidade)
    return redirect("/tratar_unidades")


def somaVlReceber(uni: unidade) -> float:
    vlChaves = converter.converterStrToFloat(uni.getVlChaves())
    vlPreChaves = converter.converterStrToFloat(uni.getVlPreChaves())
    vlPosChaves = converter.converterStrToFloat(uni.getVlPosChaves())
    return vlChaves + vlPosChaves + vlPreChaves


def prepListaStatus(sts: str) -> list[str]:
    listaStatus = []
    if sts == 'Estoque':
        listaStatus = ['Estoque', 'Quitado', 'Vendido']
    elif sts == 'Vendido':
        listaStatus = ['Vendido', 'Quitado', 'Distrato']
    elif sts == 'Quitado':
        listaStatus = ['Quitado']
    elif sts == 'Distrato':
        listaStatus = ['Distrato']
    return listaStatus
