from flask import Blueprint, request, render_template, redirect
from controller.garantiaController import garantiaController
from utils.CtrlSessao import IdEmpreend, NmEmpreend
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

@garantia_bp.route('/tratar_garantias')
def obter_grafico():
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
  obras = filter(lambda it: it.tipo == 'Obra', items)
  gerais = filter(lambda it: it.tipo == 'Geral', items)

  return render_template('garantias.html', obras=obras, gerais=gerais)


@garantia_bp.route('/atualizar_garantia')
def atualizar_garantia():
  return render_template('cad_garantia.html', camposObra = obrasDocs, camposGeral=geralDocs)


@garantia_bp.route('/salvar_garantia', methods=['POST'])
def salvar_garantia():
  pass

@garantia_bp.route('/cadastrar_garantia', methods=['POST'])
def cadastrar_garantia():
  date = datetime.now()
  mesVig = request.form.get('mesVig')
  anoVig = request.form.get('anoVig')

  docsObra = request.form.getlist('obraDocumento')
  stsObra = request.form.getlist('obraStatus')
  obsObra = request.form.getlist('obraObservacao')

  docsGeral = request.form.getlist('geralDocumento')
  stsGeral = request.form.getlist('geralStatus')
  obsGeral = request.form.getlist('geralObservacao')

  formObras = prepareList(IdEmpreend().get(), 'Obra', mesVig, anoVig, date, docsObra, stsObra, obsObra)
  formGeral = prepareList(IdEmpreend().get(), 'Geral', mesVig, anoVig, date, docsGeral, stsGeral, obsGeral)

  ctrl = garantiaController()
  ctrl.insert_garantias(formObras + formGeral)
  return redirect('/tratar_garantias')

def prepareList(idEmpreend, tipo, mesv, anov, date, docsList, stsList, obsList):
  result = []
  for idx in range(0, len(docsList)):
    temp = []
    temp.append(idEmpreend)
    temp.append(mesv)
    temp.append(anov)
    temp.append(tipo)
    temp.append(docsList[idx])
    temp.append(stsList[idx])
    temp.append(obsList[idx])
    temp.append(date)
    result.append(tuple(temp))
  return tuple(result)
