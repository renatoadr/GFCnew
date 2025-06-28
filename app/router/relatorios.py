from flask import Blueprint, request, render_template, redirect, current_app, send_from_directory, url_for
from controller.graficoInterController import graficoInterController
from utils.CtrlSessao import IdEmpreend, NmEmpreend, CodBanco
from controller.graficoController import graficoController
from controller.geralController import geralController
from utils.flash_message import flash_message
from utils.security import login_required
from reportlab.pdfgen import canvas
from datetime import datetime
import os

relatorios_bp = Blueprint('relatorios', __name__)


@relatorios_bp.route('/gerar_relatorio')
@login_required
def gerar_relatorio():
    vigencia = request.args.get('vigencia')

    if not vigencia:
        return redirect('/lista_relatorios')

    vig = vigencia.split('-')

    idEmpreend = request.args.get("idEmpreend")
    apelido = request.args.get("apelido")
    mes = vig[1]
    ano = vig[0]

    idEmpreend = request.args.get("idEmpreend")
    codBanco = CodBanco().get()

    if codBanco == 77:  # Banco Inter
        return relatorio_inter(idEmpreend, apelido, mes, ano)
    else:
        return relatorio_padrao(idEmpreend, apelido, mes, ano)


@relatorios_bp.route('/lista_relatorios')
def lista_relatorios():
    idEmpreend = request.args.get('idEmpreend')
    apelido = request.args.get('apelido')
    vigencia = request.args.get('vigencia')
    codBanco = int(request.args.get('codBanco')
                   ) if request.args.get('codBanco') else None

    if not vigencia:
        vigencia = datetime.now().strftime('%Y-%m')

    if (idEmpreend is None and not IdEmpreend().has()) or (apelido is None and not NmEmpreend().has()):
        return redirect('/home')

    if idEmpreend is None:
        idEmpreend = IdEmpreend().get()
    else:
        IdEmpreend().set(idEmpreend)

    if apelido is None:
        apelido = NmEmpreend().get()
    else:
        NmEmpreend().set(apelido)

    if codBanco is None:
        codBanco = CodBanco().get()
    else:
        CodBanco().set(codBanco)

    mobile = request.form.get('mobile', 'false').lower() == 'true'

    gerC = geralController()
    diretorio = os.path.join(current_app.config['DIRSYS'], 'Relatorios')
    arqS = gerC.listar_arquivos_com_prefixo(
        os.path.normpath(diretorio), apelido)

    if mobile:
        return render_template("mobile/download.html", arquivos=arqS)
    else:
        return render_template(
            "relatorio.html",
            arquivos=arqS,
            minDate='2000-01',
            maxDate=datetime.now().strftime('%Y-%m'),
            vigencia=vigencia,
            apelido=apelido,
            idEmpreend=idEmpreend
        )


@relatorios_bp.route('/download_arquivo')
def download_arquivo():
    arquivo = request.args.get('arquivo')
    diretorio = os.path.join(current_app.config['DIRSYS'], 'Relatorios')
    print('+++++++++++++', arquivo)
    return send_from_directory(os.path.normpath(diretorio), arquivo, as_attachment=True)


def relatorio_padrao(idEmpreend, apelido, mes, ano):

    grafC = graficoController()

    # monta o diretório onde estão os gráficos e fotos
    diretorio = grafC.montaDir(idEmpreend, mes, ano)
    erros = grafC.verificaArqRelatorio(diretorio, idEmpreend, f"{ano}-{mes}")

    # monta o diretório onde ficam todos os relatórios
    dirRelatorio = grafC.montaDir(idEmpreend, mes, ano, relatorio=True)
    grafC.criaDir(dirRelatorio)
    nomePdf = apelido + "-" + ano + "-" + mes + ".pdf"

    if grafC.verificaDir(diretorio) == False:
        flash_message.info("Não existem dados para o relatório")
    else:
        # Verifica se existem graficos e fotos para o relatório
        if len(erros) > 0:
            for n in erros:
                flash_message.error(n)
        else:
            c = canvas.Canvas(os.path.join(dirRelatorio, nomePdf))
            pagina = 1
            grafC.pdfPag1(c, diretorio, pagina, idEmpreend)
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

            foto1 = os.path.normpath(f"{diretorio}/foto_1")
            if os.path.isfile(f"{foto1}.jpeg") or os.path.isfile(f"{foto1}.png"):
                pagina += 1
                grafC.pdfPag8(c, diretorio, pagina)
                c.showPage()

                foto7 = os.path.normpath(f"{diretorio}/foto_7")
                if os.path.isfile(f"{foto7}.jpeg") or os.path.isfile(f"{foto7}.png"):
                    pagina += 1
                    grafC.pdfPag9(c, diretorio, pagina)
                    c.showPage()

                    foto13 = os.path.normpath(f"{diretorio}/foto_13")
                    if os.path.isfile(f"{foto13}.jpeg") or os.path.isfile(f"{foto13}.png"):
                        pagina += 1
                        grafC.pdfPag10(c, diretorio, pagina)
                        c.showPage()

                        foto19 = os.path.normpath(f"{diretorio}/foto_19")
                        if os.path.isfile(f"{foto19}.jpeg") or os.path.isfile(f"{foto19}.png"):
                            pagina += 1
                            grafC.pdfPag11(c, diretorio, pagina)
                            c.showPage()

            pagina += 1
            grafC.pdfPag12(c, diretorio, pagina, idEmpreend, mes, ano)
            c.showPage()
            c.save()
            flash_message.success("RELATORIO GERADO COM SUCESSO")

    gerC = geralController()
    arqS = gerC.listar_arquivos_com_prefixo(dirRelatorio, apelido)

    return redirect(
        url_for(
            'relatorios.lista_relatorios',
            arquivos=arqS,
            minDate='2000-01',
            maxDate=datetime.now().strftime('%Y-%m'),
            apelido=apelido,
            vigencia=f"{ano}-{mes}",
            idEmpreend=idEmpreend
        )
    )


def relatorio_inter(idEmpreend, apelido, mes, ano):

    grafC = graficoInterController()

    # monta o diretório onde estão os gráficos e fotos
    diretorio = grafC.montaDir(idEmpreend, mes, ano)
    erros = grafC.verificaArqRelatorio(diretorio)

    # monta o diretório onde ficam todos os relatórios
    dirRelatorio = grafC.montaDir(idEmpreend, mes, ano, relatorio=True)
    grafC.criaDir(dirRelatorio)
    nomePdf = apelido + "-" + ano + "-" + mes + ".pdf"

    if grafC.verificaDir(diretorio) == False:
        flash_message.info("Não existem dados para o relatório")
    else:
        # Verifica se existem graficos e fotos para o relatório
        if len(erros) > 0:
            for n in erros:
                flash_message.error(n)
        else:
            c = canvas.Canvas(os.path.join(dirRelatorio, nomePdf))
            pagina = 1
            grafC.pdfPag1(c, diretorio, pagina, idEmpreend)
            c.showPage()
            pagina += 1
            grafC.pdfPag2(c, diretorio, pagina)
            c.showPage()
            pagina += 1
            grafC.pdfPag2a(c, diretorio, pagina)
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

            foto1 = os.path.normpath(f"{diretorio}/foto_1")
            if os.path.isfile(f"{foto1}.jpeg") or os.path.isfile(f"{foto1}.png"):
                pagina += 1
                grafC.pdfPag8(c, diretorio, pagina)
                c.showPage()

                foto7 = os.path.normpath(f"{diretorio}/foto_7")
                if os.path.isfile(f"{foto7}.jpeg") or os.path.isfile(f"{foto7}.png"):
                    pagina += 1
                    grafC.pdfPag9(c, diretorio, pagina)
                    c.showPage()

                    foto13 = os.path.normpath(f"{diretorio}/foto_13")
                    if os.path.isfile(f"{foto13}.jpeg") or os.path.isfile(f"{foto13}.png"):
                        pagina += 1
                        grafC.pdfPag10(c, diretorio, pagina)
                        c.showPage()

                        foto19 = os.path.normpath(f"{diretorio}/foto_19")
                        if os.path.isfile(f"{foto19}.jpeg") or os.path.isfile(f"{foto19}.png"):
                            pagina += 1
                            grafC.pdfPag11(c, diretorio, pagina)
                            c.showPage()

            pagina += 1
            grafC.pdfPag12(c, diretorio, pagina, idEmpreend, mes, ano)
            c.showPage()
            c.save()
            flash_message.success("RELATORIO GERADO COM SUCESSO")

    gerC = geralController()
    arqS = gerC.listar_arquivos_com_prefixo(dirRelatorio, apelido)

    return redirect(
        url_for(
            'relatorios.lista_relatorios',
            arquivos=arqS,
            minDate='2000-01',
            maxDate=datetime.now().strftime('%Y-%m'),
            apelido=apelido,
            vigencia=f"{ano}-{mes}",
            idEmpreend=idEmpreend
        )
    )
