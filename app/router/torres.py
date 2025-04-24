from decorators.login_riquired import login_required
from flask import Blueprint, request, render_template, redirect, flash

from controller.torreController import torreController
from controller.unidadeController import unidadeController
from utils.CtrlSessao import IdEmpreend, NmEmpreend
from dto.torre import torre

torre_bp = Blueprint('torres', __name__)


@torre_bp.route('/tratar_torres')
@login_required
def tratartorres():

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

    print('-----tratar_torres----')
    print(idEmpreend, nmEmpreend)

    torreC = torreController()
    torreS = torreC.consultarTorres(idEmpreend)

    if len(torreS) == 0:
        return render_template("lista_torres.html", mensagem="Torre não cadastrada!!!", torreS=torreS)
    else:
        return render_template("lista_torres.html", torreS=torreS)


@torre_bp.route('/abrir_cad_torre')
@login_required
def abrir_cad_torre():

    idEmpreend = request.form.get("idEmpreend")
    nmEmpreend = request.form.get("nmEmpreend")

    print('-----------abrir_cad_torre-----------')
    print(idEmpreend)

    return render_template("torre.html", idEmpreend=idEmpreend, nmEmpreend=nmEmpreend)


@torre_bp.route('/cadastrar_torre', methods=['POST'])
def cadastrar_torre():
    t = torre()
    t.setIdEmpreend(IdEmpreend().get())
    t.setNmTorre(request.form.get('nmTorre'))
    t.setQtUnidade(request.form.get('qtUnidade'))
    t.setQtAndar(request.form.get('qtdAndar'))
    t.setQtCobertura(request.form.get('qtdCoberturas')
                     if request.form.get('qtdCoberturas') else 0)
    t.setPrefixCobertura(request.form.get('prefixCobertura')
                         if request.form.get('prefixCobertura') else 'Cobertura')
    t.setNumAptUmAndarUm(request.form.get('numApUmAdrUm'))

    torreC = torreController()
    torreC.inserirTorre(t)

    return redirect("/tratar_torres")


# @torre_bp.route('/editar_torre')
# def editar_torre():

#     idT = request.args.get("idTorre")
#     idEmpreend = request.args.get("idEmpreend")
#     nmEmpreend = request.args.get("nmEmpreend")

#     print('------ editar_torre --------')
#     print(idT, nmEmpreend)

#     torreC = torreController()
#     torre = torreC.consultarTorrePeloId(idT)

#     print(torre)
#     return render_template("torre.html", torre=torre, idEmpreend=idEmpreend, nmEmpreend=nmEmpreend)


# @torre_bp.route('/salvar_alteracao_torre', methods=['POST'])
# def salvar_alteracao_torre():
#     print('------- salvar_alteracao_torre INICIO --------')

#     t = torre()
#     t.setIdTorre(request.form.get('idTorre'))
#     t.setIdEmpreend(IdEmpreend().get())
#     t.setNmTorre(request.form.get('nmTorre'))
#     t.setQtUnidade(request.form.get('qtUnidade'))
#     t.setQtAndar(request.form.get('qtdAndar'))
#     t.setQtCobertura(request.form.get('qtdCoberturas'))
#     t.setPrefixCobertura(request.form.get('prefixCobertura'))
#     t.setNumAptUmAndarUm(request.form.get('numApUmAdrUm'))

#     print('------- salvar_alteracao_torre --------')

#     torreC = torreController()
#     torreC.salvarTorre(t)

#     return redirect("/tratar_torres")


@torre_bp.route('/excluir_torre')
@login_required
def excluir_torre():
    torreC = torreController()
    idTorre = request.args.get('idTorre')
    ctrlUnid = unidadeController()
    unidades = ctrlUnid.existeUnidadesPorTorre(idTorre)
    nome = torreC.consultarNomeTorre(idTorre)

    if unidades:
        flash('Existem unidades cadastradas e não é possível remover a torre: ' + nome,
              category='error')
        return redirect('/tratar_torres')

    torreC.excluirTorre(idTorre)
    return redirect("/tratar_torres")


@torre_bp.route('/copiar_torre')
@login_required
def editar_torre():
    idT = request.args.get("idTorre")

    torreC = torreController()
    torre = torreC.consultarTorrePeloId(idT)

    torre.setIdTorre(None)
    torre.setNmTorre('')

    print(torre)
    return render_template("torre.html", torre=torre)
