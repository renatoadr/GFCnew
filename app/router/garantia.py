from flask import Blueprint, request, render_template, redirect, flash
from controller.garantiaController import garantiaController
from utils.CtrlSessao import IdEmpreend, NmEmpreend
from decorators.login_riquired import login_required
from datetime import datetime

garantia_bp = Blueprint('garantias', __name__)

obrasDocs = [
    "Comprometimento com Cronograma",
    "Efetivo",
    "Estoque de Material",
    "Evoluçao Financeira/Evoluçao da obra"
]

geralDocs = [
    "Garantias Contratuais",
    "Movimentação financeira na C/C.",
    "Obrigações Fiscais",
    "Vendas"
]


def getGarantia(garantias, campo):
    for gar in garantias:
        if gar.documento == campo:
            return gar
    return None


@garantia_bp.route('/tratar_garantias')
@login_required
def tratar_garantias():
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

    ctrl = garantiaController()
    items = ctrl.list(idEmpreend)

    if not items:
        return redirect('/atualizar_garantia')

    obras = filter(lambda it: it.tipo == 'Obra', items)
    gerais = filter(lambda it: it.tipo == 'Geral', items)

    return render_template('garantias.html', obras=obras, gerais=gerais)


@garantia_bp.route('/atualizar_garantia')
@login_required
def atualizar_garantia():
    ctrl = garantiaController()
    items = ctrl.list(IdEmpreend().get())
    return render_template('cad_garantia.html', camposObra=obrasDocs, camposGeral=geralDocs, garantias=items, getGarantia=getGarantia)


@garantia_bp.route('/cadastrar_garantia', methods=['POST'])
def cadastrar_garantia():
    date = datetime.now()
    docsObra = request.form.getlist('obraDocumento')
    stsObra = request.form.getlist('obraStatus')
    obsObra = request.form.getlist('obraObservacao')
    docsGeral = request.form.getlist('geralDocumento')
    stsGeral = request.form.getlist('geralStatus')
    obsGeral = request.form.getlist('geralObservacao')
    temErro = False

    if not stsObra or not stsGeral:
        flash('Existe campos obrigatórios não preenchidos', category='error')
        return redirect('/atualizar_garantia')

    for idx in range(0, len(stsObra)):
        if not stsObra[idx]:
            temErro = True
            flash('O status do documento de obra: ' +
                  docsObra[idx] + ' não foi informado', category='error')

    for idx in range(0, len(stsGeral)):
        if not stsGeral[idx]:
            temErro = True
            flash('O status do documento geral: ' +
                  docsGeral[idx] + ' não foi informado', category='error')

    if temErro:
        return redirect('/atualizar_garantia')

    formObras = prepareList(IdEmpreend().get(), 'Obra',
                            date, docsObra, stsObra, obsObra)
    formGeral = prepareList(IdEmpreend().get(), 'Geral',
                            date, docsGeral, stsGeral, obsGeral)

    ctrl = garantiaController()
    ctrl.insert_garantias(formObras + formGeral)
    return redirect('/tratar_garantias')


def prepareList(idEmpreend, tipo, date, docsList, stsList, obsList):
    result = []
    for idx in range(0, len(docsList)):
        temp = []
        temp.append(idEmpreend)
        temp.append(tipo)
        temp.append(docsList[idx])
        temp.append(stsList[idx])
        temp.append(obsList[idx])
        temp.append(date)
        result.append(tuple(temp))
    return tuple(result)


@garantia_bp.route('/gerar_relatorio_garantia', methods=['POST'])
def gerar_relatorio_garantia():
    idEmpreend = IdEmpreend().get()
    tipo = request.form.get('tipo')
    mesVigencia = str(request.form.get('mesVigencia')).zfill(2)
    anoVigencia = request.form.get('anoVigencia')
    if tipo == 'Geral':
        return redirect('/tab_garantias_geral?tipo=' + tipo + '&idEmpreend=' + idEmpreend + '&mesVigencia=' + mesVigencia + '&anoVigencia=' + anoVigencia)
    else:
        return redirect('/tab_garantias_obra?tipo=' + tipo + '&idEmpreend=' + idEmpreend + '&mesVigencia=' + mesVigencia + '&anoVigencia=' + anoVigencia)
