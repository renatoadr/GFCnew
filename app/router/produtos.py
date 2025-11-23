from flask import Blueprint, request, render_template, redirect
from controller.categoriasController import categoriasController
from controller.produtosController import produtosController
from utils.security import login_required, login_required_api


produtos_bp = Blueprint('produtos', __name__)

catCtrl = categoriasController()
prodCtrl = produtosController()


@produtos_bp.route('/itens_produtos')
@login_required
def tratar_produtos():
    categorias_pai = catCtrl.lista_categorias_pai()
    agrupadores = catCtrl.listar_agrupadores()

    pagProd = request.args.get('pagProd', 1, type=int)
    fPCat = request.args.get('spcat', None)
    fPDesc = request.args.get('spdesc', None)
    produtos = prodCtrl.todos_produtos((fPCat, fPDesc), pagProd, 25)

    pagCat = request.args.get('pagCat', 1, type=int)
    filtroCat = request.args.get('scat', None)
    filtroGrp = request.args.get('sgroup', None)
    categorias = catCtrl.todas_categorias((filtroCat, filtroGrp), pagCat, 25)

    return render_template(
        "lista_produtos.html",
        categorias=categorias[0],
        pagCat_totais=categorias[1],
        pagCat_atual=pagCat,
        produtos=produtos[0],
        pagProd_totais=produtos[1],
        pagProd_atual=pagProd,
        hideVig=True,
        cats_pai=categorias_pai,
        agrupadores=agrupadores
    )


@produtos_bp.route('/cadastrar_categoria', methods=['POST'])
@login_required
def cadastrar_categoria():
    cat_pai = request.form.get('categoria_pai')
    descricao = request.form.get('categoria')
    agrupador = request.form.get('agrupador')
    ativo = request.form.get('ativo') == 'Sim'
    agrupador = agrupador if agrupador != "" else None
    cat_pai = cat_pai if cat_pai != "Não Informado" else None
    catCtrl.cadastrar_categoria(cat_pai, descricao, agrupador, ativo)
    return redirect('/itens_produtos#cat')


@produtos_bp.route('/excluir_categoria', methods=['GET'])
@login_required
def excluir_categoria():
    id = request.args.get('id')
    catCtrl.deletar_categoria(id)
    return redirect('/itens_produtos#cat')


@produtos_bp.route('/editar_categoria', methods=['POST'])
@login_required
def editar_categoria():
    id = request.form.get('id')
    cat_pai = request.form.get('categoria_pai')
    descricao = request.form.get('categoria')
    agrupador = request.form.get('agrupador')
    ativo = request.form.get('ativo') == 'Sim'
    agrupador = agrupador if agrupador != "" else None
    cat_pai = cat_pai if cat_pai != "Não Informado" else None
    catCtrl.atualizar_categoria(id, cat_pai, descricao, agrupador, ativo)
    return redirect('/itens_produtos#cat')


@produtos_bp.route('/obter_dados_categoria', methods=['GET'])
@login_required_api
def obter_dados_categoria():
    id = request.args.get('id')
    categoria = catCtrl.obter_categoria_por_id(id)
    if categoria:
        return {
            "id": categoria.getId(),
            "id_cat_pai": categoria.getIdCategoriaPai(),
            "descricao": categoria.getDescricao(),
            "agrupador": categoria.getAgrupador(),
            "ativo": categoria.getAtivo()
        }
    else:
        return {}


@produtos_bp.route('/obter_dados_produto', methods=['GET'])
@login_required_api
def obter_dados_produto():
    id = request.args.get('id')
    produto = prodCtrl.obter_produto_por_id(id)
    if produto is not None:
        return {
            "id": produto.getId(),
            "descricao": produto.getDescricao(),
            "categoria_id": produto.getIdCategoria(),
            "ativo": produto.getAtivo(),
            "unidade": produto.getUnidade(),
            "codigo": produto.getCodigo()
        }
    else:
        return {}


@produtos_bp.route('/deletar_produto', methods=['GET'])
@login_required
def deletar_produto():
    id = request.args.get('id')
    prodCtrl.deletar_produto(id)
    return redirect('/itens_produtos#prod')


@produtos_bp.route('/editar_produto', methods=['POST'])
@login_required
def editar_produto():
    id = request.args.get('id')
    descricao = request.form.get('desc_prod')
    cat_id = request.form.get('categoria_prod')
    ativo = request.form.get('ativo_prod') == 'Sim'
    unidade = request.form.get('unidade_prod')
    codigo = request.form.get('cod_prod', None)
    cat_id = cat_id if cat_id != "Não Informado" else None
    codigo = codigo if codigo != "" else None
    prodCtrl.atualizar_produto(id, cat_id, codigo, unidade, ativo, descricao)
    return redirect('/itens_produtos#prod')


@produtos_bp.route('/cadastrar_produto', methods=['POST'])
@login_required
def cadastrar_produto():
    descricao = request.form.get('desc_prod')
    cat_id = request.form.get('categoria_prod')
    ativo = request.form.get('ativo_prod') == 'Sim'
    unidade = request.form.get('unidade_prod')
    codigo = request.form.get('cod_prod')
    cat_id = cat_id if cat_id != "Não Informado" else None
    prodCtrl.cadastrar_produto(cat_id, descricao, unidade, codigo, ativo)
    return redirect('/itens_produtos#prod')
