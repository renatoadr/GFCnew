Use db_gfc;
-- create database db_gfc

/*create table tb_empreendimentos (
	id_empreendimento int not null auto_increment,
    nm_empreendimento varchar(100),
    nm_banco varchar(100),
	nm_incorporador varchar(100),
	nm_construtor varchar(100),
	logradouro varchar(100),
    bairro varchar(50),
    cidade varchar(50),
    estado varchar(2),
    cep varchar(8),
    nm_engenheiro varchar(100),
	vl_plano_empresario decimal (10,2),
    indice_garantia decimal (3,2),
    previsao_entrega date,
    primary key (id_empreendimento));
*/

/*create table tb_usuarios (
    email varchar(50),
    senha varchar(12),
    nm_usuario varchar(100),
    tp_usuario  varchar (15),     					-- visitante/usario/administrador
*/

/*create table tb_torres (
id_torre int not null auto_increment,
id_empreendimento int,
nm_torre varchar(20),
qt_unidade int,
primary key (id_torre));

create index idx_torres
on tb_torres (id_empreendimento, id_torre);
*/

/*create table tb_gastos (
id_empreendimento int,
dt_evento date,
vlr_medicao decimal (10,2),
vlr_compras decimal (10,2),
vlr_rh_adm decimal (10,2),
primary key (id_empreendimento, dt_evento));
*/

/*create table tb_unidades (
	id_unidade int,
	id_empreendimento int,
    id_torre int,
    unidade varchar(5),
    mes_vigencia varchar(2),
    ano_vigencia varchar(4),
	vl_unidade decimal (10,2),
	status varchar(8),
	nm_comprador varchar(100),
    vl_pago decimal (10,2),
    dt_ocorrencia date,
    financiado varchar(3),
    vl_chaves decimal (10,2)),
    primary key (id_unidade);
*/
 
/* create table tb_orcamentos (
	id_empreendimento int,
    mes_vigencia varchar(2),
    ano_vigencia varchar(4),
    dt_carga datetime,
    item varchar(50),
    fisico_percentual decimal (5,2),
	fisico_valor decimal (15,2),
    fisico_saldo decimal (15,2),
    financeiro_percentual decimal (5,2),
	financeiro_valor decimal (15,2),
    financeiro_saldo decimal (15,2),
	orcado_valor decimal (15,2),
    primary key (id_empreendimento, mes_vigencia, ano_vigencia, dt_carga, item));
*/

/*create table tb_clientes (
	cpf_cnpj varchar(15),
	tp_cpf_cnpj varchar(4),
    nm_cliente varchar(100),
    ddd varchar(3),
	tel varchar(9),
	email varchar(50),
    primary key (cpf_cnpj));
*/    

/*create table tb_agendas (
    id_empreendimento int, 
    mes_vigencia varchar (2),
    ano_vigencia varchar (4),
    id_atividade varchar (7), 
    status varchar (9),               				-- pendente/concluido
    dt_atividade date, 
    nm_resp_atividade varchar (100), 
    dt_baixa date,
    nm_resp_baixa varchar (100),
    primary key (id_empreendimento, mes_vigencia, ano_vigencia, id_atividade));
*/  

/*create table tb_agendas_param (
	id_empreendimento int,  
	id_atividade varchar (7),
	dia_agenda varchar (2),
	status  varchar (9),                           	-- ativo/inativo
	dt_cadastro date,								-- timestemp  
	dt_inicio date,									-- data de ativação do parâmetro
	dt_fim date,									-- data da inativação do parâmetro
    primary key(id_empreendimento, id_atividade));	
*/
 
 /*create table tb_agendas_atividades (
	id_atividade varchar (7),
	descr_atividade varchar (100),
	primary key(id_atividade));	
*/
    
/* create table tb_laudos (				-- pontos de atenção
	id_empreendimento int,
    mes_vigencia varchar(2),
    ano_vigencia varchar(4),
	descricao varchar(100),
	status varchar(10), 
    observacao varchar(100),
    primary key(id_empreendimento, mes_vigencia, ano_vigencia, descricao));	
*/
    
/* create table tb_documentos ( 		-- Obrigações Formais 
	id_empreendimento int,
    doc_fiscal varchar(15),				-- SRF/INSS - Trabalhista - Municipal - Estadual - FGTS 
    status varchar(10), 				-- pendente/negativa/positiva
    dt_validade date,
    primary key(id_empreendimento, doc_fiscal, status))	
*/

/*
 create table tb_notas (
	id_empreendimento int,
    mes_vigencia varchar(2),
    ano_vigencia varchar(4),
    dt_carga datetime,
    item varchar(100),
    vl_nota_fiscal decimal (15,2),
	vl_estoque decimal (15,2),
    primary key (id_empreendimento, mes_vigencia, ano_vigencia, dt_carga, item));
*/
/*
 Create table tb_medicoes (
	id_empreendimento int,
    mes_vigencia varchar(2),
    ano_vigencia varchar(4),
    nr_medicao int,
    perc_previsto_acumulado decimal (5,2),
	perc_realizado_acumulado decimal (5,2),
    perc_previsto_periodo decimal (5,2),
    primary key (id_empreendimento, nr_medicao, mes_vigencia, ano_vigencia))
 */ 
 /*
 create table tb_conta (
	id_empreendimento int,
    mes_vigencia varchar(2),
    ano_vigencia varchar(4),
	vl_liberacao decimal (15,2),
    vl_material_estoque decimal (15,2),
    vl_aporte_construtora decimal (15,2),
    vl_receita_recebiveis decimal (15,2), 
    vl_pagto_obra decimal (15,2),
    vl_pagto_rh decimal (15,2),
    vl_diferencas decimal (15,2),
	vl_saldo decimal (15,2),
	primary key (id_empreendimento, mes_vigencia, ano_vigencia))
   */
   
-- drop table tb_pagto_fornecedores;    