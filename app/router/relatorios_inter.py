from flask import Blueprint, request, render_template
from controller.graficoInterController import graficoInterController
from controller.geralController import geralController
from utils.flash_message import flash_message
from utils.security import login_required
from reportlab.pdfgen import canvas
from reportlab.lib.colors import red, blue, green, black
import os

relatorio_inter_bp = Blueprint('relatorios_inter', __name__)

@relatorio_inter_bp.route('/gerar_relatorio_inter', methods=['GET'])
@login_required
def gerar_relatorio_inter():

    grafC = graficoInterController()

    ###idEmpreend = request.args.get("idEmpreend")
    ###apelido = request.args.get("apelido")
    ###mes = request.args.get("mes")
    ###ano = request.args.get("ano")
    idEmpreend = '59'
    mes = '05'
    ano = '2025'
    apelido = 'TESTE'

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

    meses = ['  ', '01', '02', '03', '04', '05',
             '06', '07', '08', '09', '10', '11', '12']
    anos = ['    ', '2025', '2026', '2027', '2028', '2029', '2030']

    return render_template("relatorio.html", arquivos=arqS, listaMes=meses, listaAno=anos, apelido=apelido, idEmpreend=idEmpreend)
