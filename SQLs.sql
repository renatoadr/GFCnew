Use db_gfc;


 select * from tb_empreendimentos;

--  select * from tb_gastos;PRIMARY
-- select * from tb_unidades;
-- select * from tb_medicoes where id_empreendimento = 55;
-- select * from tb_torres; 
-- select * from tb_clientes;
-- select * from tb_atividades;
-- select * from tb_agendas_param;
-- select * from tb_agendas_atividades;
-- select * from tb_agendas;
-- select * from tb_notas;
 select * from tb_usuario_empreendimento;
 
 select * from tb_contas;
 

--  select mes_vigencia, ano_vigencia, dt_carga from tb_medicoes where id_empreendimento = 42
--      group by mes_vigencia, ano_vigencia, dt_carga;
--  select * from tb_medicoes where id_empreendimento = 42 and dt_carga = '2024-10-18 00:00:00' 
--      group by mes_vigencia, ano_vigencia, dt_carga;
-- select * from tb_torres where id_empreendimento = 42
-- order by nm_torre; 

-- delete from tb_empreendimentos where id_empreendimento > 0 ;
-- delete from tb_gastos where id_empreendimento > 0;

-- create public synonym tb_empreendimentos for db_gfc.tb_empreendimentos;

-- INSERT INTO tb_unidades ( id_empreendimento, id_torre, unidade, mes_vigencia, ano_vigencia, vl_unidade, status, nm_comprador, vl_pago,  dt_ocorrencia, financiado, vl_chaves )

-- insert into  tb_torres (id_empreendimento, nm_torre, qt_apto)
-- 		Values (42, 'Torre D', 50);

-- insert into tb_clientes (cpf_cnpj, tp_cpf_cnpj, nm_cliente, ddd, tel, email)
-- 		Values ('12345678901234', 'CPF', 'Bill Gates', '11', '345678901', 'bill@gmail.com');
-- 		Values ('23456789012345', 'CPF', 'Ana Maria Braga', '11', '234567890', 'aninha@gmail.com');
-- 		Values ('34567890123456', 'CPF', 'Pedro Alvares Cabral', '11', '123456789', 'caca@gmail.com'); 

-- insert into  tb_agendas_atividades (id_atividade, descr_atividade)
-- 		Values ('POSINA', 'Solicitar posição de inadimplência')
-- 		Values ('MOVCC', 'Solicitar movimentação de conta corrente')
-- 		Values ('PTATEN', 'Cadastrar pontos de atenção')
-- 		Values ('IMGOBRA', 'Cadastrar imagens da obra')
-- 		Values ('IMG3D', 'Cadastrar imagens 3D')
-- 		Values ('DOCFIS', 'Validar posição de documentos fiscais')
-- 		Values ('PAGFOR', 'Cadastrar posição de pagamento a fornecedores')
-- 		Values ('VISTOR', 'Fazer vistoria')
-- 		Values ('GEREL', 'Gerar relatório')

-- insert into tb_agendas_param (id_empreendimento, id_atividade, dia_agenda, status, dt_cadastro, dt_inicio, dt_fim)
--        Values (42, 'VISTOR', '05', 'Ativo', '2024-11-25', '2024-11-25', '2050-11-25')
--        Values (42, 'PAGFOR', '10', 'Ativo', '2024-11-25', '2024-11-25', '2050-11-25')
--        Values (42, 'IMGOBRA', '07', 'Ativo', '2024-11-25', '2024-11-25', '2050-11-25')

-- insert into tb_agendas (id_empreendimento, mes_vigencia, ano_vigencia, id_atividade, status, dt_atividade, nm_resp_atividade, dt_baixa, nm_resp_baixa)
-- values (42, '12', '2024', 'VISTOR', 'Pendente', null, null, null, null)
-- values (42, '12', '2024', 'PAGFOR', 'Pendente', null, null, null, null)
-- values (42, '12', '2024', 'IMGOBRA', 'Pendente', null, null, null, null)

-- insert into tb_medicoes (id_empreendimento, mes_vigencia, ano_vigencia, dt_carga, item, orcado_valor, fisico_valor, fisico_percentual, fisico_saldo, financeiro_valor, financeiro_percentual, financeiro_saldo)
-- values (55, '12', '2024', '2024-12-30 16:57:31', 'Serviços iniciais', 357777.17, 357777.17, 100.00,  0.00, 357777.17, 100.00, 0.00)
-- values (55, '12', '2024', '2024-12-30 16:57:31', 'Serviços gerais', 									4633930.07 ,   644211.15,  13.90,  3989718.92,   644211.15, 13.90, 3989718.92)
-- values (55, '12', '2024', '2024-12-30 16:57:31', 'Infra-estrutura', 									1537793.40 ,   968071.43,  62.95,   569721.97,   968071.43, 62.95,    569721.97)
-- values (55, '12', '2024', '2024-12-30 16:57:31', 'Supra-estrutura',	 								3745250.48 ,   0.00,      0.00,  3745250.48,        0.00,      0.00, 3745250.48)
-- values (55, '12', '2024', '2024-12-30 16:57:31', 'Alvenaria', 												724226.99  ,  0.00,      0.00,   724226.99,       0.00,      0.00, 724226.99)
-- values (55, '12', '2024', '2024-12-30 16:57:31', 'Esquadrias', 											2052002.70 , 0.00,      0.00,  2052002.70,       0.00,      0.00, 2052002.70)
-- values (55, '12', '2024', '2024-12-30 16:57:31', 'Revestimentos', 										1794736.27 , 0.00,      0.00,  1794736.27,       0.00,      0.00, 1794736.27)
-- values (55, '12', '2024', '2024-12-30 16:57:31', 'Pavimentação', 										611558.33  , 0.00,      0.00,   611558.33,       0.00,      0.00, 611558.33)
-- values (55, '12', '2024', '2024-12-30 16:57:31', 'Peitoris/soleiras/rodapé/muretas', 359139.40  , 0.00,      0.00,   359139.40,       0.00,      0.00, 359139.40)
-- values (55, '12', '2024', '2024-12-30 16:57:31', 'Pintura', 													656334.94  , 0.00,      0.00,   656334.94,       0.00,      0.00, 656334.94)
-- values (55, '12', '2024', '2024-12-30 16:57:31', 'Cobertura', 												     0.00  , 0.00,      0.00,        0.00,       0.00,      0.00,     0.00)
-- values (55, '12', '2024', '2024-12-30 16:57:31', 'Impermeabilização', 								619290.80  , 0.00,      0.00,   619290.80,       0.00,      0.00, 619290.80)
-- values (55, '12', '2024', '2024-12-30 16:57:31', 'Instalações', 											3485827.38 , 0.00,      0.00,  3485827.38,       0.00,      0.00, 3485827.38)
-- values (55, '12', '2024', '2024-12-30 16:57:31', 'Bancas/louças/metais/guarnições', 	398139.90  , 0.00,      0.00,   398139.90,       0.00,      0.00, 398139.90)
-- values (55, '12', '2024', '2024-12-30 16:57:31', 'Complementação da obra', 					468606.53  , 0.00,      0.00,   468606.53,       0.00,      0.00, 468606.53)


-- update tb_unidades set id_torre = 12 where id_unidade > 3 and id_unidade < 12 
 
-- select id_unidade, id_empreendimento, id_torre, unidade from tb_unidades where id_empreendimento = 42 order by id_torre, unidade
-- select unidade, nm_torre from tb_unidades inner join tb_torres on tb_unidades.id_torre = tb_torres.id_torre where tb_unidades.id_empreendimento=42 order by tb_torres.nm_torre, tb_unidades.unidade
-- select A.id_unidade AS id_unidade, A.id_empreendimento AS id_empreendimento, A.id_torre AS id_torre, A.unidade AS unidade, B.nm_torre AS nm_torre from tb_unidades A, tb_torres B where A.id_torre = B.id_torre AND A.id_empreendimento = 42 order by A.id_torre, A.unidade 
-- select id_empreendimento, mes_vigencia, ano_vigencia, dt_carga, item, fisico_percentual, fisico_valor, financeiro_percentual, financeiro_valor from db_gfc.tb_medicoes where id_empreendimento = '42' and dt_carga = '2024-11-06 19:22:01' order by item

-- insert into tb_notas (id_empreendimento, mes_vigencia, ano_vigencia, dt_carga, item, vl_nota_fiscal, vl_estoque)
-- values (55, '12', '2024', '2024-12-30 16:57:31', 'Cabo Cobre Isolado EPR, 90ºC, 1kV - 120,0mm, Classe 2, preto', 					17530.74, 17530.74)                                                        
-- values (55, '12', '2024', '2024-12-30 16:57:31', 'Caixa Metálica para BEP com barramento, padrão CELESC, 350x450x200mm', 		138.25, 138.25)
-- values (55, '12', '2024', '2024-12-30 16:57:31', 'Fusível de média tensão tipo HH, alta capacidade de ruptura, 25A', 			1995.00, 1995.00)
-- values (55, '12', '2024', '2024-12-30 16:57:31', 'Luminária Sobrepor a Prova de Explosão p/ Lâmpada halógena, soquete E-27', 306.78, 306.78)
-- values (55, '12', '2024', '2024-12-30 16:57:31', 'Tapete Isolante 76x60 mm, Classe II (20 kV)', 															801.00, 801.00)
-- values (55, '12', '2024', '2024-12-30 16:57:31', 'Cabo 10mm 750v (Bombas Casa de Máquinas)',																		 0, 0)  
-- values (55, '12', '2024', '2024-12-30 16:57:31', 'Preto – 150mts', 																													547.50, 547.50)
-- values (55, '12', '2024', '2024-12-30 16:57:31', 'Branco – 230mts',																												 839.50, 839.50)
-- values (55, '12', '2024', '2024-12-30 16:57:31', 'Vermelho – 130mt',																												 474.50, 474.50)
-- values (55, '12', '2024', '2024-12-30 16:57:31', 'Cabo 2,5mm 750v', 																															0,0)   
-- values (55, '12', '2024', '2024-12-30 16:57:31', 'Azul – 200 mts',																													 182.00, 182.00)
-- values (55, '12', '2024', '2024-12-30 16:57:31', 'Bomba Inferior', 																															0, 0)   
-- values (55, '12', '2024', '2024-12-30 16:57:31', 'Cabo PP 2x1,5 – 290mts',																								 462.55, 462.55)  
 -- values (55, '12', '2024', '2024-12-30 16:57:31', 'DIVERSOS',																																		 0, 0)    
-- values (55, '12', '2024', '2024-12-30 16:57:31', 'Cimento', 																																367.50, 367.50) 
-- values (55, '12', '2024', '2024-12-30 16:57:31', 'Areia', 																																	151.96, 151.96) 
-- values (55, '12', '2024', '2024-12-30 16:57:31', 'Brita', 																																	229.90, 229.90) 
-- values (55, '12', '2024', '2024-12-30 16:57:31', 'Tinta',																															 	3000.00, 3000.00) 
-- values (55, '12', '2024', '2024-12-30 16:57:31', 'Massa corrida',																													 66.00, 66.00)  
-- values (55, '12', '2024', '2024-12-30 16:57:31', 'Acabamento de registro',																							 6648.00, 6648.00)  
-- values (55, '12', '2024', '2024-12-30 16:57:31', 'Torneira',																														 4480.00, 4480.00)  
-- values (55, '12', '2024', '2024-12-30 16:57:31', 'Esquadria da substação',																								 700.00, 700.00)  
-- values (55, '12', '2024', '2024-12-30 16:57:31', 'Materiais para gas e preventivo',																	 11000.00, 11000.00)  
-- values (55, '12', '2024', '2024-12-30 16:57:31', 'ESTOQUE em 31/07/2019', 		 																						0, 49921.18)     
																							                                                           


