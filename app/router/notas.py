from flask import Blueprint, request, render_template, redirect

from utils.CtrlSessao import IdEmpreend, NmEmpreend, DtCarga, AnoVigencia, MesVigencia
from utils.security import login_required
from controller.notaController import notaController
from utils.converter import converterStrToFloat
from utils.helper import allowed_file
from dto.nota import nota

nota_bp = Blueprint('notas', __name__)


@nota_bp.route('/upload_arquivo_notas', methods=['POST'])
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
            mensagem = "Erro no upload do arquivo. Arquivo '"
            mensagem += file.filename + "' não possui uma das extensões permitidas."
        else:
            idEmpreend = IdEmpreend().get()
            notC = notaController()
            notC.carregar_notas(file, idEmpreend)
            return redirect("/tratar_notas")
    else:
        mensagem = "Erro no upload do arquivo. Você precisa selecionar um arquivo."
    return render_template("erro.html", mensagem=mensagem)


@nota_bp.route('/tratar_notas')
@login_required
def tratar_notas():

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

    print('-----tratar_notas----')
    print(idEmpreend, nmEmpreend)

    notC = notaController()
    notS = notC.consultarNotas(idEmpreend)

    return render_template("lista_notas_agrupadas.html", notas=notS, idEmpreend=idEmpreend)


@nota_bp.route('/excluir_nota_carga')
@login_required
def excluir_nota_carga():
    mes = request.args.get('mesV')
    ano = request.args.get('anoV')
    data = request.args.get('dtCarga')
    contC = notaController()
    contC.excluir_por_data(IdEmpreend().get(), data, mes, ano)
    return redirect('/tratar_notas')


@nota_bp.route('/consultar_nota_data')
@login_required
def consultar_nota_data():
    data = request.args.get('dtCarga')
    ano = request.args.get('anoV')
    mes = request.args.get('mesV')

    if data is None and not DtCarga().has():
        return redirect('/tratar_notas')
    if data is None:
        data = DtCarga().get()
        ano = AnoVigencia().get()
        mes = MesVigencia().get()
    else:
        AnoVigencia().set(ano)
        MesVigencia().set(mes)
        DtCarga().set(data)

    notaC = notaController()
    notaS = notaC.listaNotas(IdEmpreend().get(), data, mes, ano)
    return render_template("lista_notas.html", notas=notaS)


@nota_bp.route('/excluir_nota')
@login_required
def excluir_nota():
    id = request.args.get('idNota')
    contC = notaController()
    contC.excluir_nota(id)
    return redirect('/consultar_nota_data')


@nota_bp.route('/editar_nota')
@login_required
def editar_nota():
    id = request.args.get('idConta')
    contC = notaController()
    nota = contC.nota_por_id(id)
    return render_template("cad_nota.html", nota=nota)


@nota_bp.route('/abrir_cad_nota')
@login_required
def cadastrar_nota():
    return render_template("cad_nota.html")


@nota_bp.route('/salvar_nota', methods=['POST'])
def salvar_nota():
    ct = get_nota_cadastro()
    contC = notaController()
    contC.salvar_nota(ct)
    return redirect("/consultar_nota_data")


@nota_bp.route('/criar_nota', methods=['POST'])
def criar_nota():
    ct = get_nota_cadastro()
    ct.setAnoVigencia(AnoVigencia().get())
    ct.setMesVigencia(MesVigencia().get())
    ct.setDtCarga(DtCarga().get())
    ct.setIdEmpreend(IdEmpreend().get())
    contC = notaController()
    contC.inserir_nota(ct)
    return redirect("/consultar_nota_data")


def get_nota_cadastro() -> nota:
    idNota = request.form.get('idNota')
    produto = request.form.get('produto')
    vlNotaFiscal = converterStrToFloat(request.form.get('vlNotaFiscal'))
    vlEstoque = converterStrToFloat(request.form.get('vlEstoque'))

    ct = nota()
    ct.setIdNota(idNota)
    ct.setProduto(produto)
    ct.setVlNotaFiscal(vlNotaFiscal)
    ct.setVlEstoque(vlEstoque)

    return ct
