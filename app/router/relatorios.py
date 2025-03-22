from flask import Blueprint, request, render_template, current_app
from controller.graficoController import graficoController
from controller.geralController import geralController
from reportlab.pdfgen import canvas
import os

relatorio_bp = Blueprint('relatorios', __name__)

@relatorio_bp.route('/gerar_relatorio', methods=['GET'])
def gerar_relatorio():

    grafC = graficoController(current_app)

    idEmpreend = request.args.get("idEmpreend")
    apelido = request.args.get("apelido")
    mes = request.args.get("mes")
    ano = request.args.get("ano")

    # monta o diretório onde estão os gráficos e fotos
    diretorio = grafC.montaDir(idEmpreend, mes, ano)
    erros = grafC.verificaArqRelatorio(diretorio)

    # monta o diretório onde ficam todos os relatórios
    dirRelatorio = grafC.montaDir(idEmpreend, mes, ano, relatorio=True)
    grafC.criaDir(dirRelatorio)
    nomePdf = apelido + "-" + ano + "-" + mes + ".pdf"

    if grafC.verificaDir(diretorio) == False:
        # Verifica se o diretório de graficos e fotos foi criado
        mensagem = "Não existem dados para o relatório"
    else:
        # Verifica se existem graficos e fotos para o relatório
        if len(erros) > 0:
            mensagem = ''
            for n in erros:
                mensagem = mensagem + ' # ' + n
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
            mensagem = "RELATORIO GERADO COM SUCESSO"

    gerC = geralController(current_app)
    arqS = gerC.listar_arquivos_com_prefixo(dirRelatorio, apelido)

    meses = ['  ', '01', '02', '03', '04', '05',
             '06', '07', '08', '09', '10', '11', '12']
    anos = ['    ', '2025', '2026', '2027', '2028', '2029', '2030']

    return render_template("relatorio.html", arquivos=arqS, listaMes=meses, listaAno=anos, apelido=apelido, idEmpreend=idEmpreend, mensagem=mensagem)
