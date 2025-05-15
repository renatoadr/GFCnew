from flask import Blueprint, request, render_template

from controller.graficoController import graficoController
from controller.geralController import geralController
from decorators.login_riquired import login_required
from reportlab.pdfgen import canvas
import os

relatorio_bp = Blueprint('relatorios', __name__)


@relatorio_bp.route('/gerar_relatorio', methods=['GET'])
@login_required
def gerar_relatorio():

    grafC = graficoController()

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
            if os.path.isfile(diretorio+"foto_1.jpeg") or os.path.isfile(diretorio+"foto_1.png"):
                pagina += 1
                grafC.pdfPag8(c, diretorio, pagina)
                c.showPage()
                if os.path.isfile(diretorio+"foto_7.jpeg") or os.path.isfile(diretorio+"foto_7.png"):
                    pagina += 1
                    grafC.pdfPag9(c, diretorio, pagina)
                    c.showPage()
                    if os.path.isfile(diretorio+"foto_13.jpeg") or os.path.isfile(diretorio+"foto_13.png"):
                        pagina += 1
                        grafC.pdfPag10(c, diretorio, pagina)
                        c.showPage()
                        if os.path.isfile(diretorio+"foto_19.jpeg") or os.path.isfile(diretorio+"foto_19.png"):
                            pagina += 1
                            grafC.pdfPag11(c, diretorio, pagina)
                            c.showPage()
    
            pagina += 1
            grafC.pdfPag12(c, diretorio, pagina, idEmpreend, mes, ano)
            c.showPage()
            c.save()
            mensagem = "RELATORIO GERADO COM SUCESSO"

    gerC = geralController()
    arqS = gerC.listar_arquivos_com_prefixo(dirRelatorio, apelido)

    meses = ['  ', '01', '02', '03', '04', '05',
             '06', '07', '08', '09', '10', '11', '12']
    anos = ['    ', '2025', '2026', '2027', '2028', '2029', '2030']

    return render_template("relatorio.html", arquivos=arqS, listaMes=meses, listaAno=anos, apelido=apelido, idEmpreend=idEmpreend, mensagem=mensagem)


#@relatorio_bp.route('/tratar_graficos_tabelas')
#@login_required
#def tratar_graficos_tabelas():
#    idEmpreend = request.args.get("idEmpreend")
#    nmEmpreend = request.args.get("nmEmpreend")
#
#    if (idEmpreend is None and not IdEmpreend().has()) or (nmEmpreend is None and not NmEmpreend().has()):
#        return redirect('/home')
#
#    if idEmpreend is None:
#        idEmpreend = IdEmpreend().get()
#    else:
#        IdEmpreend().set(idEmpreend)
#
#    if nmEmpreend is None:
#        nmEmpreend = NmEmpreend().get()
#    else:
#        NmEmpreend().set(nmEmpreend)
#
#    ctrl = garantiaController()
#    items = ctrl.list(idEmpreend)
#
#    if not items:
#        return redirect('/atualizar_garantia')
#
#    obras = filter(lambda it: it.tipo == 'Obra', items)
#    gerais = filter(lambda it: it.tipo == 'Geral', items)
#
#    return render_template('graf_tab.html', obras=obras, gerais=gerais)
