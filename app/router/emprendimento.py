from flask import Blueprint, request, render_template, redirect
from controller.empreendimentoController import empreendimentoController
from dto.empreendimento import empreendimento
import utils.converter as converter

empreend_bp = Blueprint('empreendimentos', __name__)

@empreend_bp.route('/home', methods=['POST','GET'])
def abrir_home():
  empc = empreendimentoController ()
  emps = empc.consultarEmpreendimentos ()
  return render_template("home.html", empreends=emps)

@empreend_bp.route('/abrir_cad_empreend')
def abrir_cad_empreend():
    return render_template("cad_empreend.html")

@empreend_bp.route('/efetuar_cad_empreend', methods=['POST'])
def efetuar_cad_empreend():
    empreend = empreendimento ()
    empreend.setApelido(request.form.get('apelido'))
    empreend.setNmEmpreend (request.form.get('nmEmpreendimento'))
    empreend.setNmBanco (request.form.get('nmBanco'))
    empreend.setNmIncorp (request.form.get('nmIncorp'))
    empreend.setNmConstrutor (request.form.get('nmConstrutor'))
    empreend.setLogradouro (request.form.get('logradouro'))
    empreend.setBairro (request.form.get('bairro'))
    empreend.setCidade (request.form.get('cidade'))
    empreend.setEstado (request.form.get('estado'))
    empreend.setCep (converter.removeAlpha(request.form.get('cep')))
    empreend.setCpfCnpjEngenheiro (request.form.get('cpfCnpjEngenheiro'))
    empreend.setVlPlanoEmp (converter.converterStrToFloat(request.form.get('vlPlanoEmp')))
    empreend.setIndiceGarantia (converter.converterStrToFloat(request.form.get('indiceGarantia')))
    empreend.setPrevisaoEntrega (request.form.get('previsaoEntrega'))

    empc = empreendimentoController()
    empc.inserirEmpreendimento(empreend)
    return redirect("/home")

@empreend_bp.route('/excluir_empreend')
def excluir_empreend():
    idEmpreend = request.args.get('idEmpreend')
    print (idEmpreend)
    empc = empreendimentoController()
    empc.excluirEmpreendimento(idEmpreend)

    emps = empc.consultarEmpreendimentos ()
    return render_template("home.html", empreends=emps)

@empreend_bp.route('/abrir_edicao_empreend')
def abrir_edicao_empreend():

    idEmpreend = request.args.get('idEmpreend')
    print (idEmpreend)
    empc = empreendimentoController ()
    empreend = empc.consultarEmpreendimentoPeloId (idEmpreend)

    print(empreend)
    return render_template("cad_empreend.html", empreend=empreend)

@empreend_bp.route('/salvar_empreend', methods=['POST'])
def salvar_empreend():
    empreend = empreendimento ()
    empreend.setApelido(request.form.get('apelido'))
    empreend.setIdEmpreend (int(request.form.get('idEmpreendimento')))
    empreend.setNmEmpreend (request.form.get('nmEmpreendimento'))
    empreend.setNmBanco (request.form.get('nmBanco'))
    empreend.setNmIncorp (request.form.get('nmIncorp'))
    empreend.setNmConstrutor (request.form.get('nmConstrutor'))
    empreend.setLogradouro (request.form.get('logradouro'))
    empreend.setBairro (request.form.get('bairro'))
    empreend.setCidade (request.form.get('cidade'))
    empreend.setEstado (request.form.get('estado'))
    empreend.setCep (converter.removeAlpha(request.form.get('cep')))
    empreend.setCpfCnpjEngenheiro (request.form.get('cpfCnpjEngenheiro'))
    empreend.setVlPlanoEmp (converter.converterStrToFloat(request.form.get('vlPlanoEmp')))
    empreend.setIndiceGarantia (converter.converterStrToFloat(request.form.get('indiceGarantia')))
    empreend.setPrevisaoEntrega (request.form.get('previsaoEntrega'))

    empc = empreendimentoController()
    empc.salvarEmpreendimento(empreend)
    return redirect("/home")
