from flask import Blueprint, request, render_template, redirect
from controller.contaController import contaController
from utils.helper import allowed_file
from utils.CtrlSessao import IdEmpreend, NmEmpreend, DtCarga, AnoVigencia, MesVigencia
from utils.converter import converterStrToFloat
from decorators.login_riquired import login_required
from dto.conta import conta

contas_corrente_bp = Blueprint('contas_corrente', __name__)


@contas_corrente_bp.route('/upload_arquivo_contas', methods=['POST'])
def upload_arquivo_contas():

    # check if the post request has the file part
    if 'file' not in request.files:
        mensagem = "Erro no upload do arquivo. No file part."
        return render_template("erro.html", mensagem=mensagem)
    file = request.files['file']
    if file:
        if file.filename == '':
            mensagem = "Erro no upload do arquivo. Nome do arquivo='" + file.filename + "'."
        elif not allowed_file(file.filename):
            mensagem = "Erro no upload do arquivo. Arquivo: '"
            mensagem += file.filename + "' não possui uma das extensões permitidas."
        else:
            notC = contaController()
            notC.carregar_contas(file, IdEmpreend().get())
            return redirect("/tratar_contas")
    else:
        mensagem = "Erro no upload do arquivo. Você precisa selecionar um arquivo."
    return render_template("erro.html", mensagem=mensagem)


@contas_corrente_bp.route('/tratar_contas')
@login_required
def tratar_contas():

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

    print('-----tratar_contas----')
    print(idEmpreend, nmEmpreend)

    contC = contaController()
    contS = contC.consultarContas(idEmpreend)

    if len(contS) == 0:
        return render_template(
            "lista_contas_agrupadas.html",
            mensagem="Conta não Cadastrada, importar o arquivo Excel!!!",
            contas=contS
        )
    else:
        return render_template("lista_contas_agrupadas.html", contas=contS)


@contas_corrente_bp.route('/consultar_conta_data')
@login_required
def consultar_conta():
    data = request.args.get('dtCarga')
    ano = request.args.get('anoV')
    mes = request.args.get('mesV')

    if data is None and not DtCarga().has():
        return redirect('/tratar_contas')
    if data is None:
        data = DtCarga().get()
        ano = AnoVigencia().get()
        mes = MesVigencia().get()
    else:
        AnoVigencia().set(ano)
        MesVigencia().set(mes)
        DtCarga().set(data)

    contC = contaController()
    contS = contC.listaContas(IdEmpreend().get(), data, mes, ano)
    return render_template("lista_contas.html", contas=contS)


@contas_corrente_bp.route('/editar_conta')
@login_required
def editar_conta():
    id = request.args.get('id')
    contC = contaController()
    conta = contC.conta_por_id(id)
    return render_template("cad_conta.html", conta=conta)


@contas_corrente_bp.route('/abrir_cad_conta')
@login_required
def cadastrar_conta():
    return render_template("cad_conta.html")


@contas_corrente_bp.route('/salvar_conta', methods=['POST'])
def salvar_conta():
    ct = get_conta_cadastro()
    contC = contaController()
    contC.salvar_conta(ct)
    return redirect("/consultar_conta_data")


@contas_corrente_bp.route('/criar_conta', methods=['POST'])
def criar_conta():
    ct = get_conta_cadastro()
    ct.setAnoVigencia(AnoVigencia().get())
    ct.setMesVigencia(MesVigencia().get())
    ct.setDtCarga(DtCarga().get())
    ct.setIdEmpreend(IdEmpreend().get())
    contC = contaController()
    contC.inserir_conta(ct)
    return redirect("/consultar_conta_data")


@contas_corrente_bp.route('/excluir_conta_carga')
@login_required
def excluir_conta_carga():
    mes = request.args.get('mesV')
    ano = request.args.get('anoV')
    data = request.args.get('dtCarga')
    contC = contaController()
    contC.excluir_por_data(IdEmpreend().get(), data, mes, ano)
    return redirect('/tratar_contas')


@contas_corrente_bp.route('/excluir_conta')
@login_required
def excluir_conta():
    id = request.args.get('idConta')
    contC = contaController()
    contC.excluir_conta(id)
    return redirect('/consultar_conta_data')


def get_conta_cadastro():
    idConta = request.form.get('idConta')
    vlSaldo = converterStrToFloat(request.form.get('vlSaldo'))
    vlReceita = converterStrToFloat(request.form.get('vlReceita'))
    vlLiberacao = converterStrToFloat(request.form.get('vlLiberacao'))
    vlPagamento = converterStrToFloat(request.form.get('vlPagamento'))
    vlPagamentoObra = converterStrToFloat(request.form.get('vlPagamentoObra'))
    vlAporteConstrutora = converterStrToFloat(
        request.form.get('vlAporteConstrutora')
    )

    ct = conta()
    ct.setIdConta(idConta)
    ct.setVlReceitaRecebiveis(vlReceita)
    ct.setVlLiberacao(vlLiberacao)
    ct.setVlPagtoObra(vlPagamentoObra)
    ct.setVlAporteConstrutora(vlAporteConstrutora)
    ct.setVlPagtoRh(vlPagamento)
    ct.setVlSaldo(vlSaldo)
    ct.setVlDiferenca(
        (vlLiberacao + vlAporteConstrutora + vlReceita) -
        (vlPagamentoObra + vlPagamento) - vlSaldo
    )
    return ct
