Use db_gfc;

 select * from tb_empreendimentos;
--  select * from tb_gastos;PRIMARY
-- select * from tb_unidades;
-- select * from tb_medicoes where id_empreendimento = 55;
-- select * from tb_medicoes;
-- select * from tb_torres; 
-- select * from tb_garantias;
 
-- select * from tb_clientes;
-- select * from tb_atividades;
-- select * from tb_agendas_param;
-- select * from tb_agendas_atividades;
-- select * from tb_agendas;
-- select * from tb_notas;
-- select * from tb_laudos;
-- select * from tb_orcamentos;
-- select * from tb_pontos_atencao;
 select * from tb_contas;
-- select* from tb_financeiro;
-- select * from tb_inadimplencias;
-- select * from tb_certidoes ;
-- select * from tb_garantias; 
 
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


-- update tb_unidades set id_torre = 12 where id_unidade > 3 and id_unidade < 12 
 
-- select id_unidade, id_empreendimento, id_torre, unidade from tb_unidades where id_empreendimento = 42 order by id_torre, unidade
-- select unidade, nm_torre from tb_unidades inner join tb_torres on tb_unidades.id_torre = tb_torres.id_torre where tb_unidades.id_empreendimento=42 order by tb_torres.nm_torre, tb_unidades.unidade
-- select A.id_unidade AS id_unidade, A.id_empreendimento AS id_empreendimento, A.id_torre AS id_torre, A.unidade AS unidade, B.nm_torre AS nm_torre from tb_unidades A, tb_torres B where A.id_torre = B.id_torre AND A.id_empreendimento = 42 order by A.id_torre, A.unidade 
-- select id_empreendimento, mes_vigencia, ano_vigencia, dt_carga, item, fisico_percentual, fisico_valor, financeiro_percentual, financeiro_valor from db_gfc.tb_medicoes where id_empreendimento = '42' and dt_carga = '2024-11-06 19:22:01' order by item

-- insert into tb_previsto_realizado (id_empreendimento, nr_medicao, mes_vigencia, ano_vigencia, perc_previsto_acumulado, perc_realizado_acumulado, perc_previsto_periodo)
-- values (55, '1',  '05', '2024',   4.00,   5.52,  4.00)
/*
select id_empreendimento, mes_vigencia, ano_vigencia, ordem, periodo, qt_unidades 
from tb_inadimpencia 
where id_empreendimento = 55 and (mes_vigencia => '11' and ano_vigencia => '2024') and (mes_vigencia <= '12' and ano_vigencia <= '2024')
*/
/*
 select * from tb_inadimplencias where id_empreendimento = 55 and (ano_vigencia = '2024' and mes_vigencia >= '10') or
                                                                  (ano_vigencia = '2025' and mes_vigencia <= '01') order by ordem, ano_vigencia, mes_vigencia
*/
-- select mes_vigencia, ano_vigencia from tb_inadimplencias where id_empreendimento = 55 and (mes_vigencia >= '11' and ano_vigencia <= '2024') and (mes_vigencia <= ' 1' and ano_vigencia <= '2025') group by ano_vigencia, mes_vigencia
-- select * from tb_inadimplencias where id_empreendimento = 55

 
-- select count(id_unidade), sum(vl_chaves), sum(vl_pre_chaves), sum(vl_pos_chaves) from tb_unidades where id_empreendimento = 55 and status != 'distrato';
-- select status, sum(vl_pago), sum(vl_unidade) from tb_unidades where id_empreendimento = 55 and status in ('vendido', 'estoque') group  by status;
-- select* from tb_usuario_empreendimento;
-- select* from tb_usuarios
-- select id_usuario, email, senha, tp_acesso, nm_usuario from db_gfc.tb_usuarios  where email = 'XXX' and senha = 'SSS';
-- select mes_vigencia, ano_vigencia, dt_carga  from db_gfc.tb_notas where id_empreendimento = 39 group by mes_vigencia, ano_vigencia, dt_carga;

-- select id_empreendimento, ano_vigencia, dt_carga from db_gfc.tb_orcamentos where id_empreendimento = 39 group by mes_vigencia, ano_vigencia, dt_carga 

-- select id_garantia, id_empreendimento, criado_em, tipo, historico, status, observacao from tb_garantias where id_empreendimento = 57 and tipo = 'Obra'   AND criado_em = (SELECT MAX(criado_em) FROM tb_garantias WHERE id_empreendimento = 57 AND tipo = 'Obra');
