CREATE DATABASE IF NOT EXISTS `db_gfc`;
USE `db_gfc`;

CREATE TABLE IF NOT EXISTS `tb_agendas` (
  `id_empreendimento` int NOT NULL,
  `mes_vigencia` varchar(2) NOT NULL,
  `ano_vigencia` varchar(4) NOT NULL,
  `id_atividade` varchar(7) NOT NULL,
  `status` varchar(9) DEFAULT NULL,
  `dt_atividade` date DEFAULT NULL,
  `nm_resp_atividade` varchar(100) DEFAULT NULL,
  `dt_baixa` date DEFAULT NULL,
  `nm_resp_baixa` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id_empreendimento`,`mes_vigencia`,`ano_vigencia`,`id_atividade`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE IF NOT EXISTS `tb_agendas_atividades` (
  `id_atividade` varchar(7) NOT NULL,
  `descr_atividade` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id_atividade`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE IF NOT EXISTS `tb_agendas_param` (
  `id_empreendimento` int NOT NULL,
  `id_atividade` varchar(7) NOT NULL,
  `dia_agenda` varchar(2) DEFAULT NULL,
  `status` varchar(9) DEFAULT NULL,
  `dt_cadastro` date DEFAULT NULL,
  `dt_inicio` date DEFAULT NULL,
  `dt_fim` date DEFAULT NULL,
  PRIMARY KEY (`id_empreendimento`,`id_atividade`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE IF NOT EXISTS `tb_certidoes` (
  `id_empreendimento` int NOT NULL,
  `estadual_status` varchar(8) DEFAULT NULL,
  `estadual_validade` date DEFAULT NULL,
  `fgts_status` varchar(8) DEFAULT NULL,
  `fgts_validade` date DEFAULT NULL,
  `municipal_status` varchar(8) DEFAULT NULL,
  `municipal_validade` date DEFAULT NULL,
  `srf_inss_status` varchar(8) DEFAULT NULL,
  `srf_inss_validade` date DEFAULT NULL,
  `trabalhista_status` varchar(8) DEFAULT NULL,
  `trabalhista_validade` date DEFAULT NULL,
  PRIMARY KEY (`id_empreendimento`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE IF NOT EXISTS `tb_clientes` (
  `cpf_cnpj` varchar(15) NOT NULL,
  `tp_cpf_cnpj` varchar(4) DEFAULT NULL,
  `nm_cliente` varchar(100) DEFAULT NULL,
  `ddd` varchar(3) DEFAULT NULL,
  `tel` varchar(9) DEFAULT NULL,
  `email` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`cpf_cnpj`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE IF NOT EXISTS `tb_contas` (
  `id_conta` int NOT NULL AUTO_INCREMENT,
  `id_empreendimento` int NOT NULL,
  `mes_vigencia` varchar(2) NOT NULL,
  `ano_vigencia` varchar(4) NOT NULL,
  `dt_carga` datetime DEFAULT NULL,
  `vl_liberacao` decimal(15,2) DEFAULT NULL,
  `vl_aporte_construtora` decimal(15,2) DEFAULT NULL,
  `vl_receita_recebiveis` decimal(15,2) DEFAULT NULL,
  `vl_pagto_obra` decimal(15,2) DEFAULT NULL,
  `vl_pagto_rh` decimal(15,2) DEFAULT NULL,
  `vl_diferenca` decimal(15,2) DEFAULT NULL,
  `vl_saldo` decimal(15,2) DEFAULT NULL,
  PRIMARY KEY (`id_conta`)
) ENGINE=InnoDB AUTO_INCREMENT=51 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE IF NOT EXISTS `tb_empreendimentos` (
  `id_empreendimento` int NOT NULL AUTO_INCREMENT,
  `nm_empreendimento` varchar(100) DEFAULT NULL,
  `apelido` varchar(10) DEFAULT NULL,
  `cod_banco` int NOT NULL,
  `nm_incorporador` varchar(100) DEFAULT NULL,
  `nm_construtor` varchar(100) DEFAULT NULL,
  `logradouro` varchar(100) DEFAULT NULL,
  `bairro` varchar(50) DEFAULT NULL,
  `cidade` varchar(50) DEFAULT NULL,
  `estado` varchar(2) DEFAULT NULL,
  `cep` varchar(8) DEFAULT NULL,
  `cpf_cnpj_engenheiro` varchar(15) DEFAULT NULL,
  `vl_plano_empresario` decimal(10,2) DEFAULT NULL,
  `indice_garantia` decimal(3,2) DEFAULT NULL,
  `previsao_entrega` date DEFAULT NULL,
  PRIMARY KEY (`id_empreendimento`)
) ENGINE=InnoDB AUTO_INCREMENT=57 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE IF NOT EXISTS `tb_financeiro` (
  `id_empreendimento` int NOT NULL,
  `mes_vigencia` varchar(2) NOT NULL,
  `ano_vigencia` varchar(4) NOT NULL,
  `ordem` int NOT NULL,
  `historico` varchar(50) DEFAULT NULL,
  `perc_financeiro` decimal(5,2) DEFAULT NULL,
  `vl_financeiro` decimal(15,2) DEFAULT NULL,
  PRIMARY KEY (`id_empreendimento`,`mes_vigencia`,`ano_vigencia`,`ordem`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE IF NOT EXISTS `tb_garantias` (
  `id_empreendimento` int NOT NULL,
  `tipo` varchar(5) NOT NULL,
  `historico` varchar(50) NOT NULL,
  `status` varchar(10) NOT NULL,
  `observacao` varchar(50) DEFAULT NULL,
  `id_garantia` int NOT NULL AUTO_INCREMENT,
  `criado_em` datetime NOT NULL,
  PRIMARY KEY (`id_garantia`)
) ENGINE=InnoDB AUTO_INCREMENT=97 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE IF NOT EXISTS `tb_inadimplencias` (
  `id_empreendimento` int NOT NULL,
  `mes_vigencia` varchar(2) NOT NULL,
  `ano_vigencia` varchar(4) NOT NULL,
  `ordem` int NOT NULL,
  `periodo` varchar(10) DEFAULT NULL,
  `qt_unidades` int DEFAULT NULL,
  PRIMARY KEY (`id_empreendimento`,`mes_vigencia`,`ano_vigencia`,`ordem`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE IF NOT EXISTS  IF NOT EXISTS `tb_laudos` (
  `id_empreendimento` int NOT NULL,
  `mes_vigencia` varchar(2) NOT NULL,
  `ano_vigencia` varchar(4) NOT NULL,
  `descricao` varchar(100) NOT NULL,
  `status` varchar(10) DEFAULT NULL,
  `observacao` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id_empreendimento`,`mes_vigencia`,`ano_vigencia`,`descricao`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE IF NOT EXISTS `tb_medicoes` (
  `id_medicao` int NOT NULL AUTO_INCREMENT,
  `id_empreendimento` int NOT NULL,
  `mes_vigencia` varchar(2) NOT NULL,
  `ano_vigencia` varchar(4) NOT NULL,
  `dt_carga` datetime DEFAULT NULL,
  `nr_medicao` varchar(4) NOT NULL,
  `perc_previsto_acumulado` decimal(5,2) DEFAULT NULL,
  `perc_realizado_acumulado` decimal(5,2) DEFAULT NULL,
  `perc_diferenca` decimal(5,2) DEFAULT NULL,
  `perc_previsto_periodo` decimal(5,2) DEFAULT NULL,
  `perc_realizado_periodo` decimal(5,2) DEFAULT NULL,
  PRIMARY KEY (`id_medicao`),
  KEY `idx_medicoes` (`id_empreendimento`,`mes_vigencia`,`ano_vigencia`) /*!80000 INVISIBLE */
) ENGINE=InnoDB AUTO_INCREMENT=466 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE IF NOT EXISTS `tb_notas` (
  `id_nota` int NOT NULL AUTO_INCREMENT,
  `id_empreendimento` int NOT NULL,
  `mes_vigencia` varchar(2) NOT NULL,
  `ano_vigencia` varchar(4) NOT NULL,
  `dt_carga` datetime NOT NULL,
  `produto` varchar(100) DEFAULT NULL,
  `vl_nota_fiscal` decimal(15,2) DEFAULT NULL,
  `vl_estoque` decimal(15,2) DEFAULT NULL,
  PRIMARY KEY (`id_nota`),
  KEY `idx_nota` (`dt_carga`,`id_empreendimento`,`mes_vigencia`,`ano_vigencia`)
) ENGINE=InnoDB AUTO_INCREMENT=117 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE IF NOT EXISTS `tb_orcamentos` (
  `id_orcamento` int NOT NULL AUTO_INCREMENT,
  `id_empreendimento` int DEFAULT NULL,
  `mes_vigencia` varchar(2) DEFAULT NULL,
  `ano_vigencia` varchar(4) DEFAULT NULL,
  `dt_carga` datetime DEFAULT NULL,
  `item` varchar(50) DEFAULT NULL,
  `orcado_valor` decimal(15,2) DEFAULT NULL,
  `fisico_valor` decimal(15,2) DEFAULT NULL,
  `fisico_percentual` decimal(6,2) DEFAULT NULL,
  `fisico_saldo` decimal(15,2) DEFAULT NULL,
  `financeiro_valor` decimal(15,2) DEFAULT NULL,
  `financeiro_percentual` decimal(6,2) DEFAULT NULL,
  `financeiro_saldo` decimal(15,2) DEFAULT NULL,
  PRIMARY KEY (`id_orcamento`)
) ENGINE=InnoDB AUTO_INCREMENT=396 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE IF NOT EXISTS `tb_torres` (
  `id_torre` int NOT NULL AUTO_INCREMENT,
  `id_empreendimento` int NOT NULL,
  `nm_torre` varchar(20) NOT NULL,
  `qt_unidade` int NOT NULL,
  `qt_andar` int NOT NULL,
  `qt_coberturas` int DEFAULT NULL,
  `prefix_cobertura` varchar(20) DEFAULT NULL,
  `num_apt_um_andar_um` int NOT NULL,
  `vl_unidade` DECIMAL(15,2) NULL,
  `vl_cobertura` DECIMAL(15,2) NULL,
  PRIMARY KEY (`id_torre`),
  KEY `idx_torres` (`id_empreendimento`,`id_torre`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

  CREATE TABLE IF NOT EXISTS `tb_unidades` (
  `id_unidade` int NOT NULL AUTO_INCREMENT,
  `id_empreendimento` int NOT NULL,
  `id_torre` int NOT NULL,
  `unidade` varchar(15) NOT NULL,
  `mes_vigencia` varchar(2) NOT NULL,
  `ano_vigencia` varchar(4) NOT NULL,
  `vl_unidade` decimal(10,2) DEFAULT NULL,
  `status` varchar(8) NOT NULL,
  `cpf_cnpj_comprador` varchar(15) DEFAULT NULL,
  `vl_receber` decimal(10,2) DEFAULT NULL,
  `dt_ocorrencia` datetime DEFAULT CURRENT_TIMESTAMP,
  `financiado` varchar(3) DEFAULT NULL,
  `vl_chaves` decimal(15,2) DEFAULT NULL,
  `vl_pre_chaves` decimal(15,2) DEFAULT NULL,
  `vl_pos_chaves` decimal(15,2) DEFAULT NULL,
  `ac_historico` varchar(15) DEFAULT NULL,
  PRIMARY KEY (`id_unidade`),
  KEY `idx_unidades` (`id_empreendimento`,`id_torre`,`unidade`,`mes_vigencia`,`ano_vigencia`)
) ENGINE=InnoDB AUTO_INCREMENT=31 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE IF NOT EXISTS `tb_usuarios` (
  `id_usuario` int NOT NULL AUTO_INCREMENT,
  `email` varchar(50) UNIQUE DEFAULT NULL,
  `senha` varchar(100) DEFAULT NULL,
  `tp_acesso` varchar(15) DEFAULT NULL,
  `nm_usuario` varchar(100) DEFAULT NULL,
  `cod_banco` int null,
  PRIMARY KEY (`id_usuario`),
  KEY `idx_email` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE IF NOT EXISTS  `tb_consideracoes` (
  `id` int NOT NULL AUTO_INCREMENT,
  `campo` varchar(20) NOT NULL,
  `texto` varchar(120) NOT NULL,
  `dt_criado` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `ac_historico` varchar(45) DEFAULT NULL,
  `id_empreendimento` int NOT NULL,
  `dt_editado` timestamp NULL DEFAULT NULL,
  `mes_vigencia` varchar(2) NOT NULL,
  `ano_vigencia` int NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=30 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE IF NOT EXISTS  `tb_bancos` (
  `codigo` int(3) NOT NULL,
  `ispb` varchar(10) DEFAULT NULL,
  `descricao` varchar(60) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `descricao_completa` varchar(150) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  PRIMARY KEY (`codigo`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


CREATE TABLE IF NOT EXISTS `tb_aspectos` (
  `id` INT AUTO_INCREMENT NOT NULL,
  `status` VARCHAR(100) NOT NULL,
  `descricao` VARCHAR(500) NULL,
  `id_empreendimento` INT NOT NULL,
  `id_pergunta_aspecto` INT NOT NULL,
  `mes_vigencia` VARCHAR(2) NOT NULL,
  `ano_vigencia` INT NOT NULL,
   PRIMARY KEY (`id`)
) ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS `tb_perguntas_aspectos` (
  `id` INT AUTO_INCREMENT NOT NULL,
  `pergunta` VARCHAR(350) NOT NULL,
  `grupo` VARCHAR(100) NOT NULL,
  `opcoes` VARCHAR(500) NOT NULL,
   PRIMARY KEY (`id`)
) ENGINE = InnoDB;

INSERT INTO Query (id, pergunta, grupo, opcoes) VALUES (1, 'A execução obedece o projeto?', 'Projeto', 'Sim;Não');
INSERT INTO Query (id, pergunta, grupo, opcoes) VALUES (2, 'Houve modificação em alguma unidade?', 'Projeto', 'Sim;Não');
INSERT INTO Query (id, pergunta, grupo, opcoes) VALUES (3, 'Utilização de Equipamentos Individuais', 'Segurança', 'Sim;Não');
INSERT INTO Query (id, pergunta, grupo, opcoes) VALUES (4, 'Utilização de Equipamentos Coletivos', 'Segurança', 'Sim;Não');
INSERT INTO Query (id, pergunta, grupo, opcoes) VALUES (5, 'Estrutura (Prumo, presença de nichos)', 'Qualidade', 'Baixo;Normal;Bom');
INSERT INTO Query (id, pergunta, grupo, opcoes) VALUES (6, 'Paredes (Prumo, Alinhamento, Modulação e etc.)', 'Qualidade', 'Baixo;Normal;Bom');
INSERT INTO Query (id, pergunta, grupo, opcoes) VALUES (7, 'Instalações de Portas e Janelas', 'Qualidade', 'Baixo;Normal;Bom');
INSERT INTO Query (id, pergunta, grupo, opcoes) VALUES (8, 'Contrapiso', 'Qualidade', 'Baixo;Normal;Bom');
INSERT INTO Query (id, pergunta, grupo, opcoes) VALUES (9, 'Revestimento Interno', 'Qualidade', 'Baixo;Normal;Bom');
INSERT INTO Query (id, pergunta, grupo, opcoes) VALUES (10, 'Revestimento Externo', 'Qualidade', 'Baixo;Normal;Bom');
INSERT INTO Query (id, pergunta, grupo, opcoes) VALUES (11, 'Escadas', 'Qualidade', 'Baixo;Normal;Bom');
INSERT INTO Query (id, pergunta, grupo, opcoes) VALUES (12, 'Instalações Elétricas e Hidráulicas', 'Qualidade', 'Baixo;Normal;Bom');
INSERT INTO Query (id, pergunta, grupo, opcoes) VALUES (13, 'Forros', 'Qualidade', 'Baixo;Normal;Bom');
INSERT INTO Query (id, pergunta, grupo, opcoes) VALUES (14, 'Pintura', 'Qualidade', 'Baixo;Normal;Bom');
INSERT INTO Query (id, pergunta, grupo, opcoes) VALUES (15, 'Uso de Ferramentas adequadas ao serviço', 'Qualidade', 'Baixo;Normal;Bom');
INSERT INTO Query (id, pergunta, grupo, opcoes) VALUES (16, 'Planejamento', 'Qualidade', 'Baixo;Normal;Bom');
INSERT INTO Query (id, pergunta, grupo, opcoes) VALUES (17, 'Limpeza', 'Qualidade', 'Baixo;Normal;Bom');
INSERT INTO Query (id, pergunta, grupo, opcoes) VALUES (18, 'Logística de Canteiro', 'Qualidade', 'Baixo;Normal;Bom');
INSERT INTO Query (id, pergunta, grupo, opcoes) VALUES (19, 'Outro', 'Qualidade', 'Baixo;Normal;Bom');


INSERT INTO `db_gfc`.`tb_consideracoes`(`email`, `senha`, `tp_acesso`, `nm_usuario`)
VALUES (`adm@gfcpro.com.br`, `$2b$06$S0KOp/YN3wdyzc6JlF68Eugmhjh5wIzLmO9PVDGtildPudAtsQqTq`, `RT`, `Renato Adriano`)


INSERT INTO `db_gfc`.`tb_bancos`(`ispb`, `descricao`, `codigo`, `descricao_completa`)
values (`00000000`,`BCO DO BRASIL S.A.`,1,`Banco do Brasil S.A.`),
(`00000208`,`BRB - BCO DE BRASILIA S.A.`,70,`BRB - BANCO DE BRASILIA S.A.`),
(`00122327`,`SANTINVEST S.A. - CFI`,539,`SANTINVEST S.A. - CREDITO, FINANCIAMENTO E INVESTIMENTOS`),
(`00204963`,`CCR SEARA`,430,`COOPERATIVA DE CREDITO RURAL SEARA - CREDISEARA`),
(`00315557`,`CONF NAC COOP CENTRAIS UNICRED`,136,`CONFEDERAÇÃO NACIONAL DAS COOPERATIVAS CENTRAIS UNICRED LTDA. - UNICRED DO BRASI`),
(`00360305`,`CAIXA ECONOMICA FEDERAL`,104,`CAIXA ECONOMICA FEDERAL`),
(`00416968`,`BANCO INTER`,77,`Banco Inter S.A.`),
(`00517645`,`BCO RIBEIRAO PRETO S.A.`,741,`BANCO RIBEIRAO PRETO S.A.`),
(`00556603`,`BANCO BARI S.A.`,330,`BANCO BARI DE INVESTIMENTOS E FINANCIAMENTOS S.A.`),
(`00558456`,`BCO CETELEM S.A.`,739,`Banco Cetelem S.A.`),
(`00795423`,`BANCO SEMEAR`,743,`Banco Semear S.A.`),
(`01023570`,`BCO RABOBANK INTL BRASIL S.A.`,747,`Banco Rabobank International Brasil S.A.`),
(`01181521`,`BCO COOPERATIVO SICREDI S.A.`,748,`BANCO COOPERATIVO SICREDI S.A.`),
(`01522368`,`BCO BNP PARIBAS BRASIL S A`,752,`Banco BNP Paribas Brasil S.A.`),
(`01658426`,`CECM COOPERFORTE`,379,`COOPERFORTE - COOPERATIVA DE ECONOMIA E CRÉDITO MÚTUO DE FUNCIONÁRIOS DE INSTITU`),
(`01701201`,`KIRTON BANK`,399,`Kirton Bank S.A. - Banco Múltiplo`),
(`01852137`,`BCO BRASILEIRO DE CRÉDITO S.A.`,378,`BANCO BRASILEIRO DE CRÉDITO SOCIEDADE ANÔNIMA`),
(`01858774`,`BCO BV S.A.`,413,`BANCO BV S.A.`),
(`02038232`,`BANCO SICOOB S.A.`,756,`BANCO COOPERATIVO SICOOB S.A. - BANCO SICOOB`),
(`02318507`,`BCO KEB HANA DO BRASIL S.A.`,757,`BANCO KEB HANA DO BRASIL S.A.`),
(`02801938`,`BCO MORGAN STANLEY S.A.`,66,`BANCO MORGAN STANLEY S.A.`),
(`03012230`,`HIPERCARD BM S.A.`,62,`Hipercard Banco Múltiplo S.A.`),
(`03017677`,`BCO. J.SAFRA S.A.`,74,`Banco J. Safra S.A.`),
(`03046391`,`UNIPRIME COOPCENTRAL LTDA.`,99,`UNIPRIME CENTRAL NACIONAL - CENTRAL NACIONAL DE COOPERATIVA DE CREDITO`),
(`03215790`,`BCO TOYOTA DO BRASIL S.A.`,387,`Banco Toyota do Brasil S.A.`),
(`03311443`,`PARATI - CFI S.A.`,326,`PARATI - CREDITO, FINANCIAMENTO E INVESTIMENTO S.A.`),
(`03323840`,`BCO ALFA S.A.`,25,`Banco Alfa S.A.`),
(`03532415`,`BCO ABN AMRO S.A.`,75,`Banco ABN Amro S.A.`),
(`03609817`,`BCO CARGILL S.A.`,40,`Banco Cargill S.A.`),
(`03844699`,`CECM DOS TRAB.PORT. DA G.VITOR`,385,`COOPERATIVA DE ECONOMIA E CREDITO MUTUO DOS TRABALHADORES PORTUARIOS DA GRANDE V`),
(`03881423`,`SOCINAL S.A. CFI`,425,`SOCINAL S.A. - CRÉDITO, FINANCIAMENTO E INVESTIMENTO`),
(`04184779`,`BANCO BRADESCARD`,63,`Banco Bradescard S.A.`),
(`04307598`,`FIDUCIA SCMEPP LTDA`,382,`FIDÚCIA SOCIEDADE DE CRÉDITO AO MICROEMPREENDEDOR E À EMPRESA DE PEQUENO PORTE L`),
(`04332281`,`GOLDMAN SACHS DO BRASIL BM S.A`,64,`GOLDMAN SACHS DO BRASIL BANCO MULTIPLO S.A.`),
(`04632856`,`CREDISIS CENTRAL DE COOPERATIVAS DE CRÉDITO LTDA.`,97,`Credisis - Central de Cooperativas de Crédito Ltda.`),
(`04814563`,`BCO AFINZ S.A. - BM`,299,`BANCO AFINZ S.A. - BANCO MÚLTIPLO`),
(`04831810`,`CECM SERV PUBL PINHÃO`,471,`COOPERATIVA DE ECONOMIA E CREDITO MUTUO DOS SERVIDORES PUBLICOS DE PINHÃO - CRES`),
(`04862600`,`PORTOSEG S.A. CFI`,468,`PORTOSEG S.A. - CREDITO, FINANCIAMENTO E INVESTIMENTO`),
(`04866275`,`BANCO INBURSA`,12,`Banco Inbursa S.A.`),
(`04902979`,`BCO DA AMAZONIA S.A.`,3,`BANCO DA AMAZONIA S.A.`),
(`04913711`,`BCO DO EST. DO PA S.A.`,37,`Banco do Estado do Pará S.A.`),
(`05192316`,`VIA CERTA FINANCIADORA S.A. - CFI`,411,`Via Certa Financiadora S.A. - Crédito, Financiamento e Investimentos`),
(`05351887`,`ZEMA CFI S/A`,359,`ZEMA CRÉDITO, FINANCIAMENTO E INVESTIMENTO S/A`),
(`05442029`,`CASA CREDITO S.A. SCM`,159,`Casa do Crédito S.A. Sociedade de Crédito ao Microempreendedor`),
(`05463212`,`COOPCENTRAL AILOS`,85,`Cooperativa Central de Crédito - Ailos`),
(`05676026`,`CREDIARE CFI S.A.`,429,`Crediare S.A. - Crédito, financiamento e investimento`),
(`05684234`,`PLANNER SOCIEDADE DE CRÉDITO DIRETO`,410,`PLANNER SOCIEDADE DE CRÉDITO DIRETO S.A.`),
(`06271464`,`BCO BBI S.A.`,36,`Banco Bradesco BBI S.A.`),
(`07207996`,`BCO BRADESCO FINANC. S.A.`,394,`Banco Bradesco Financiamentos S.A.`),
(`07237373`,`BCO DO NORDESTE DO BRASIL S.A.`,4,`Banco do Nordeste do Brasil S.A.`),
(`07450604`,`BCO CCB BRASIL S.A.`,320,`China Construction Bank (Brasil) Banco Múltiplo S/A`),
(`07512441`,`HS FINANCEIRA`,189,`HS FINANCEIRA S/A CREDITO, FINANCIAMENTO E INVESTIMENTOS`),
(`07652226`,`LECCA CFI S.A.`,105,`Lecca Crédito, Financiamento e Investimento S/A`),
(`07656500`,`BCO KDB BRASIL S.A.`,76,`Banco KDB do Brasil S.A.`),
(`07679404`,`BANCO TOPÁZIO S.A.`,82,`BANCO TOPÁZIO S.A.`),
(`07693858`,`HSCM SCMEPP LTDA.`,312,`HSCM - SOCIEDADE DE CRÉDITO AO MICROEMPREENDEDOR E À EMPRESA DE PEQUENO PORTE LT`),
(`07799277`,`VALOR SCD S.A.`,195,`VALOR SOCIEDADE DE CRÉDITO DIRETO S.A.`),
(`07945233`,`POLOCRED SCMEPP LTDA.`,93,`PÓLOCRED   SOCIEDADE DE CRÉDITO AO MICROEMPREENDEDOR E À EMPRESA DE PEQUENO PORT`),
(`08240446`,`CCR DE IBIAM`,391,`COOPERATIVA DE CREDITO RURAL DE IBIAM - SULCREDI/IBIAM`),
(`08357240`,`BCO CSF S.A.`,368,`Banco CSF S.A.`),
(`09210106`,`SOCRED SA - SCMEPP`,183,`SOCRED S.A. - SOCIEDADE DE CRÉDITO AO MICROEMPREENDEDOR E À EMPRESA DE PEQUENO P`),
(`09274232`,`STATE STREET BR S.A. BCO COMERCIAL`,14,`STATE STREET BRASIL S.A. - BANCO COMERCIAL`),
(`09313766`,`CARUANA SCFI`,130,`CARUANA S.A. - SOCIEDADE DE CRÉDITO, FINANCIAMENTO E INVESTIMENTO`),
(`09464032`,`MIDWAY S.A. - SCFI`,358,`MIDWAY S.A. - CRÉDITO, FINANCIAMENTO E INVESTIMENTO`),
(`09516419`,`PICPAY BANK - BANCO MÚLTIPLO S.A`,79,`PICPAY BANK - BANCO MÚLTIPLO S.A`),
(`09526594`,`MASTER BI S.A.`,141,`BANCO MASTER DE INVESTIMENTO S.A.`),
(`10264663`,`BANCOSEGURO S.A.`,81,`BancoSeguro S.A.`),
(`10371492`,`BCO YAMAHA MOTOR S.A.`,475,`Banco Yamaha Motor do Brasil S.A.`),
(`10398952`,`CRESOL CONFEDERAÇÃO`,133,`CONFEDERAÇÃO NACIONAL DAS COOPERATIVAS CENTRAIS DE CRÉDITO E ECONOMIA FAMILIAR E`),
(`10664513`,`BCO AGIBANK S.A.`,121,`Banco Agibank S.A.`),
(`10690848`,`BCO DA CHINA BRASIL S.A.`,83,`Banco da China Brasil S.A.`),
(`10866788`,`BCO BANDEPE S.A.`,24,`Banco Bandepe S.A.`),
(`11165756`,`GLOBAL SCM LTDA`,384,`GLOBAL FINANÇAS SOCIEDADE DE CRÉDITO AO MICROEMPREENDEDOR E À EMPRESA DE PEQUENO`),
(`11285104`,`NEON FINANCEIRA - CFI S.A.`,426,`NEON FINANCEIRA - CRÉDITO, FINANCIAMENTO E INVESTIMENTO S.A.`),
(`11476673`,`BANCO RANDON S.A.`,88,`BANCO RANDON S.A.`),
(`11581339`,`BMP SCMEPP LTDA`,274,`BMP SOCIEDADE DE CRÉDITO AO MICROEMPREENDEDOR E A EMPRESA DE PEQUENO PORTE LTDA.`),
(`11758741`,`BANCO FINAXIS`,94,`Banco Finaxis S.A.`),
(`11760553`,`GAZINCRED S.A. SCFI`,478,`GAZINCRED S.A. SOCIEDADE DE CRÉDITO, FINANCIAMENTO E INVESTIMENTO`),
(`11970623`,`BCO SENFF S.A.`,276,`BANCO SENFF S.A.`),
(`13009717`,`BCO DO EST. DE SE S.A.`,47,`Banco do Estado de Sergipe S.A.`),
(`13220493`,`BR PARTNERS BI`,126,`BR Partners Banco de Investimento S.A.`),
(`13720915`,`BCO WESTERN UNION`,119,`Banco Western Union do Brasil S.A.`),
(`14388334`,`PARANA BCO S.A.`,254,`PARANÁ BANCO S.A.`),
(`14511781`,`BARI CIA HIPOTECÁRIA`,268,`BARI COMPANHIA HIPOTECÁRIA`),
(`15114366`,`BCO BOCOM BBM S.A.`,107,`Banco Bocom BBM S.A.`),
(`15124464`,`BANCO BESA S.A.`,334,`BANCO BESA S.A.`),
(`15173776`,`SOCIAL BANK S/A`,412,`SOCIAL BANK BANCO MÚLTIPLO S/A`),
(`15357060`,`BCO WOORI BANK DO BRASIL S.A.`,124,`Banco Woori Bank do Brasil S.A.`),
(`15581638`,`FACTA S.A. CFI`,149,`Facta Financeira S.A. - Crédito Financiamento e Investimento`),
(`17184037`,`BCO MERCANTIL DO BRASIL S.A.`,389,`Banco Mercantil do Brasil S.A.`),
(`17298092`,`BCO ITAÚ BBA S.A.`,184,`Banco Itaú BBA S.A.`),
(`17351180`,`BCO TRIANGULO S.A.`,634,`BANCO TRIANGULO S.A.`),
(`17453575`,`ICBC DO BRASIL BM S.A.`,132,`ICBC do Brasil Banco Múltiplo S.A.`),
(`17826860`,`BMS SCD S.A.`,377,`BMS SOCIEDADE DE CRÉDITO DIRETO S.A.`),
(`18188384`,`CREFAZ SCMEPP LTDA`,321,`CREFAZ SOCIEDADE DE CRÉDITO AO MICROEMPREENDEDOR E A EMPRESA DE PEQUENO PORTE LT`),
(`18236120`,`NU PAGAMENTOS - IP`,260,`NU PAGAMENTOS S.A. - INSTITUIÇÃO DE PAGAMENTO`),
(`18394228`,`CDC SCD S.A.`,470,`CDC SOCIEDADE DE CRÉDITO DIRETO S.A.`),
(`18520834`,`UBS BRASIL BI S.A.`,129,`UBS Brasil Banco de Investimento S.A.`),
(`19324634`,`LAMARA SCD S.A.`,416,`LAMARA SOCIEDADE DE CRÉDITO DIRETO S.A.`),
(`20855875`,`NEON PAGAMENTOS S.A. IP`,536,`NEON PAGAMENTOS S.A. - INSTITUIÇÃO DE PAGAMENTO`),
(`21018182`,`EBANX IP LTDA.`,383,`EBANX INSTITUICAO DE PAGAMENTOS LTDA.`),
(`21332862`,`CARTOS SCD S.A.`,324,`CARTOS SOCIEDADE DE CRÉDITO DIRETO S.A.`),
(`22610500`,`VORTX DTVM LTDA.`,310,`VORTX DISTRIBUIDORA DE TITULOS E VALORES MOBILIARIOS LTDA.`),
(`23862762`,`WILL FINANCEIRA S.A.CFI`,280,`WILL FINANCEIRA S.A. CRÉDITO, FINANCIAMENTO E INVESTIMENTO`),
(`24537861`,`FFA SCMEPP LTDA.`,343,`FFA SOCIEDADE DE CRÉDITO AO MICROEMPREENDEDOR E À EMPRESA DE PEQUENO PORTE LTDA.`),
(`27098060`,`BANCO DIGIO`,335,`Banco Digio S.A.`),
(`27214112`,`AL5 S.A. CFI`,349,`AL5 S.A. CRÉDITO, FINANCIAMENTO E INVESTIMENTO`),
(`27302181`,`CRED-UFES`,427,`COOPERATIVA DE CREDITO DOS SERVIDORES DA UNIVERSIDADE FEDERAL DO ESPIRITO SANTO`),
(`27351731`,`REALIZE CFI S.A.`,374,`REALIZE CRÉDITO, FINANCIAMENTO E INVESTIMENTO S.A.`),
(`28127603`,`BCO BANESTES S.A.`,21,`BANESTES S.A. BANCO DO ESTADO DO ESPIRITO SANTO`),
(`28195667`,`BCO ABC BRASIL S.A.`,246,`Banco ABC Brasil S.A.`),
(`29030467`,`SCOTIABANK BRASIL`,751,`Scotiabank Brasil S.A. Banco Múltiplo`),
(`30306294`,`BANCO BTG PACTUAL S.A.`,208,`Banco BTG Pactual S.A.`),
(`30680829`,`NU FINANCEIRA S.A. CFI`,386,`NU FINANCEIRA S.A. - Sociedade de Crédito, Financiamento e Investimento`),
(`30723886`,`BCO MODAL S.A.`,746,`Banco Modal S.A.`),
(`31597552`,`BCO CLASSICO S.A.`,241,`BANCO CLASSICO S.A.`),
(`31872495`,`BCO C6 S.A.`,336,`Banco C6 S.A.`),
(`31880826`,`BCO GUANABARA S.A.`,612,`Banco Guanabara S.A.`),
(`31895683`,`BCO INDUSTRIAL DO BRASIL S.A.`,604,`Banco Industrial do Brasil S.A.`),
(`32062580`,`BCO CREDIT SUISSE S.A.`,505,`Banco Credit Suisse (Brasil) S.A.`),
(`32402502`,`QI SCD S.A.`,329,`QI Sociedade de Crédito Direto S.A.`),
(`32997490`,`CREDITAS SCD`,342,`Creditas Sociedade de Crédito Direto S.A.`),
(`33042151`,`BCO LA NACION ARGENTINA`,300,`Banco de la Nacion Argentina`),
(`33042953`,`CITIBANK N.A.`,477,`Citibank N.A.`),
(`33132044`,`BCO CEDULA S.A.`,266,`BANCO CEDULA S.A.`),
(`33147315`,`BCO BRADESCO BERJ S.A.`,122,`Banco Bradesco BERJ S.A.`),
(`33172537`,`BCO J.P. MORGAN S.A.`,376,`BANCO J.P. MORGAN S.A.`),
(`33264668`,`BCO XP S.A.`,348,`Banco XP S.A.`),
(`33466988`,`BCO CAIXA GERAL BRASIL S.A.`,473,`Banco Caixa Geral - Brasil S.A.`),
(`33479023`,`BCO CITIBANK S.A.`,745,`Banco Citibank S.A.`),
(`33603457`,`BCO RODOBENS S.A.`,120,`BANCO RODOBENS S.A.`),
(`33644196`,`BCO FATOR S.A.`,265,`Banco Fator S.A.`),
(`33657248`,`BNDES`,7,`BANCO NACIONAL DE DESENVOLVIMENTO ECONOMICO E SOCIAL`),
(`33885724`,`BANCO ITAÚ CONSIGNADO S.A.`,29,`Banco Itaú Consignado S.A.`),
(`33923798`,`BANCO MASTER`,243,`BANCO MASTER S/A`),
(`34088029`,`LISTO SCD S.A.`,397,`LISTO SOCIEDADE DE CREDITO DIRETO S.A.`),
(`34111187`,`HAITONG BI DO BRASIL S.A.`,78,`Haitong Banco de Investimento do Brasil S.A.`),
(`34335592`,`ÓTIMO SCD S.A.`,355,`ÓTIMO SOCIEDADE DE CRÉDITO DIRETO S.A.`),
(`35551187`,`PLANTAE CFI`,445,`PLANTAE S.A. - CRÉDITO, FINANCIAMENTO E INVESTIMENTO`),
(`35977097`,`UP.P SEP S.A.`,373,`UP.P SOCIEDADE DE EMPRÉSTIMO ENTRE PESSOAS S.A.`),
(`36583700`,`QISTA S.A. CFI`,516,`QISTA S.A. - CRÉDITO, FINANCIAMENTO E INVESTIMENTO`),
(`36586946`,`BONUSPAGO SCD S.A.`,408,`BONUSPAGO SOCIEDADE DE CRÉDITO DIRETO S.A.`),
(`36947229`,`COBUCCIO S.A. SCFI`,402,`COBUCCIO S/A - SOCIEDADE DE CRÉDITO, FINANCIAMENTO E INVESTIMENTOS`),
(`37229413`,`SCFI EFÍ S.A.`,507,`SOCIEDADE DE CRÉDITO, FINANCIAMENTO E INVESTIMENTO EFÍ S.A.`),
(`37241230`,`SUMUP SCD S.A.`,404,`SUMUP SOCIEDADE DE CRÉDITO DIRETO S.A.`),
(`37414009`,`ZIPDIN SCD S.A.`,418,`ZIPDIN SOLUÇÕES DIGITAIS SOCIEDADE DE CRÉDITO DIRETO S/A`),
(`37526080`,`LEND SCD S.A.`,414,`LEND SOCIEDADE DE CRÉDITO DIRETO S.A.`),
(`37555231`,`DM`,449,`DM SOCIEDADE DE CRÉDITO DIRETO S.A.`),
(`37679449`,`MERCADO CRÉDITO SCFI S.A.`,518,`MERCADO CRÉDITO SOCIEDADE DE CRÉDITO, FINANCIAMENTO E INVESTIMENTO S.A.`),
(`37715993`,`ACCREDITO SCD S.A.`,406,`ACCREDITO - SOCIEDADE DE CRÉDITO DIRETO S.A.`),
(`37880206`,`CORA SCD S.A.`,403,`CORA SOCIEDADE DE CRÉDITO DIRETO S.A.`),
(`38129006`,`NUMBRS SCD S.A.`,419,`NUMBRS SOCIEDADE DE CRÉDITO DIRETO S.A.`),
(`38224857`,`DELCRED SCD S.A.`,435,`DELCRED SOCIEDADE DE CRÉDITO DIRETO S.A.`),
(`39416705`,`CREDIHOME SCD`,443,`CREDIHOME SOCIEDADE DE CRÉDITO DIRETO S.A.`),
(`39519944`,`MARU SCD S.A.`,535,`MARÚ SOCIEDADE DE CRÉDITO DIRETO S.A.`),
(`39587424`,`UY3 SCD S/A`,457,`UY3 SOCIEDADE DE CRÉDITO DIRETO S/A`),
(`39664698`,`CREDSYSTEM SCD S.A.`,428,`CREDSYSTEM SOCIEDADE DE CRÉDITO DIRETO S.A.`),
(`39676772`,`CREDIFIT SCD S.A.`,452,`CREDIFIT SOCIEDADE DE CRÉDITO DIRETO S.A.`),
(`39738065`,`FFCRED SCD S.A.`,510,`FFCRED SOCIEDADE DE CRÉDITO DIRETO S.A..`),
(`39908427`,`STARK SCD S.A.`,462,`STARK SOCIEDADE DE CRÉDITO DIRETO S.A.`),
(`40083667`,`CAPITAL CONSIG SCD S.A.`,465,`CAPITAL CONSIG SOCIEDADE DE CRÉDITO DIRETO S.A.`),
(`40303299`,`PORTOPAR DTVM LTDA`,306,`PORTOPAR DISTRIBUIDORA DE TITULOS E VALORES MOBILIARIOS LTDA.`),
(`40475846`,`J17 - SCD S/A`,451,`J17 - SOCIEDADE DE CRÉDITO DIRETO S/A`),
(`40654622`,`TRINUS SCD S.A.`,444,`TRINUS SOCIEDADE DE CRÉDITO DIRETO S.A.`),
(`42047025`,`UNAVANTI SCD S/A`,460,`UNAVANTI SOCIEDADE DE CRÉDITO DIRETO S/A`),
(`42259084`,`SBCASH SCD`,482,`SBCASH SOCIEDADE DE CRÉDITO DIRETO S.A.`),
(`42272526`,`BNY MELLON BCO S.A.`,17,`BNY Mellon Banco S.A.`),
(`43180355`,`PEFISA S.A. - C.F.I.`,174,`PEFISA S.A. - CRÉDITO, FINANCIAMENTO E INVESTIMENTO`),
(`43599047`,`SUPERLÓGICA SCD S.A.`,481,`SUPERLÓGICA SOCIEDADE DE CRÉDITO DIRETO S.A.`),
(`44019481`,`PEAK SEP S.A.`,521,`PEAK SOCIEDADE DE EMPRÉSTIMO ENTRE PESSOAS S.A.`),
(`44189447`,`BCO LA PROVINCIA B AIRES BCE`,495,`Banco de La Provincia de Buenos Aires`),
(`44292580`,`HR DIGITAL SCD`,523,`HR DIGITAL - SOCIEDADE DE CRÉDITO DIRETO S/A`),
(`44478623`,`ATICCA SCD S.A.`,527,`ATICCA - SOCIEDADE DE CRÉDITO DIRETO S.A.`),
(`44683140`,`MAGNUM SCD`,511,`MAGNUM SOCIEDADE DE CRÉDITO DIRETO S.A.`),
(`44728700`,`ATF CREDIT SCD S.A.`,513,`ATF CREDIT SOCIEDADE DE CRÉDITO DIRETO S.A.`),
(`45246410`,`BANCO GENIAL`,125,`BANCO GENIAL S.A.`),
(`45745537`,`EAGLE SCD S.A.`,532,`EAGLE SOCIEDADE DE CRÉDITO DIRETO S.A.`),
(`45756448`,`MICROCASH SCMEPP LTDA.`,537,`MICROCASH SOCIEDADE DE CRÉDITO AO MICROEMPREENDEDOR E À EMPRESA DE PEQUENO PORTE`),
(`46026562`,`MONETARIE SCD`,526,`MONETARIE SOCIEDADE DE CRÉDITO DIRETO S.A.`),
(`46518205`,`JPMORGAN CHASE BANK`,488,`JPMorgan Chase Bank, National Association`),
(`47593544`,`RED SCD S.A.`,522,`RED SOCIEDADE DE CRÉDITO DIRETO S.A.`),
(`47873449`,`SER FINANCE SCD S.A.`,530,`SER FINANCE SOCIEDADE DE CRÉDITO DIRETO S.A.`),
(`48795256`,`BCO ANDBANK S.A.`,65,`Banco AndBank (Brasil) S.A.`),
(`50585090`,`BCV - BCO, CRÉDITO E VAREJO S.A.`,250,`BCV - BANCO DE CRÉDITO E VAREJO S.A.`),
(`53518684`,`BCO HSBC S.A.`,269,`BANCO HSBC S.A.`),
(`54403563`,`BCO ARBI S.A.`,213,`Banco Arbi S.A.`),
(`55230916`,`INTESA SANPAOLO BRASIL S.A. BM`,139,`Intesa Sanpaolo Brasil S.A. - Banco Múltiplo`),
(`57839805`,`BCO TRICURY S.A.`,18,`Banco Tricury S.A.`),
(`58160789`,`BCO SAFRA S.A.`,422,`Banco Safra S.A.`),
(`58497702`,`BCO LETSBANK S.A.`,630,`BANCO LETSBANK S.A.`),
(`58616418`,`BCO FIBRA S.A.`,224,`Banco Fibra S.A.`),
(`59109165`,`BCO VOLKSWAGEN S.A`,393,`Banco Volkswagen S.A.`),
(`59118133`,`BCO LUSO BRASILEIRO S.A.`,600,`Banco Luso Brasileiro S.A.`),
(`59274605`,`BCO GM S.A.`,390,`BANCO GM S.A.`),
(`59285411`,`BANCO PAN`,623,`Banco Pan S.A.`),
(`59588111`,`BCO VOTORANTIM S.A.`,655,`Banco Votorantim S.A.`),
(`60394079`,`BCO ITAUBANK S.A.`,479,`Banco ItauBank S.A.`),
(`60498557`,`BCO MUFG BRASIL S.A.`,456,`Banco MUFG Brasil S.A.`),
(`60518222`,`BCO SUMITOMO MITSUI BRASIL S.A.`,464,`Banco Sumitomo Mitsui Brasileiro S.A.`),
(`60701190`,`ITAÚ UNIBANCO S.A.`,341,`ITAÚ UNIBANCO S.A.`),
(`60746948`,`BCO BRADESCO S.A.`,237,`Banco Bradesco S.A.`),
(`60814191`,`BCO MERCEDES-BENZ S.A.`,381,`BANCO MERCEDES-BENZ DO BRASIL S.A.`),
(`60850229`,`OMNI BANCO S.A.`,613,`Omni Banco S.A.`),
(`60889128`,`BCO SOFISA S.A.`,637,`BANCO SOFISA S.A.`),
(`61024352`,`BANCO VOITER`,653,`BANCO VOITER S.A.`),
(`61033106`,`BCO CREFISA S.A.`,69,`Banco Crefisa S.A.`),
(`61088183`,`BCO MIZUHO S.A.`,370,`Banco Mizuho do Brasil S.A.`),
(`61182408`,`BANCO INVESTCRED UNIBANCO S.A.`,249,`Banco Investcred Unibanco S.A.`),
(`61186680`,`BCO BMG S.A.`,318,`Banco BMG S.A.`),
(`61348538`,`BCO C6 CONSIG`,626,`BANCO C6 CONSIGNADO S.A.`),
(`61533584`,`BCO SOCIETE GENERALE BRASIL`,366,`BANCO SOCIETE GENERALE BRASIL S.A.`),
(`61820817`,`BCO PAULISTA S.A.`,611,`Banco Paulista S.A.`),
(`62073200`,`BOFA MERRILL LYNCH BM S.A.`,755,`Bank of America Merrill Lynch Banco Múltiplo S.A.`),
(`62144175`,`BCO PINE S.A.`,643,`Banco Pine S.A.`),
(`62232889`,`BCO DAYCOVAL S.A`,707,`Banco Daycoval S.A.`),
(`62331228`,`DEUTSCHE BANK S.A.BCO ALEMAO`,487,`DEUTSCHE BANK S.A. - BANCO ALEMAO`),
(`62421979`,`BANCO CIFRA`,233,`Banco Cifra S.A.`),
(`68900810`,`BCO RENDIMENTO S.A.`,633,`Banco Rendimento S.A.`),
(`71027866`,`BCO BS2 S.A.`,218,`Banco BS2 S.A.`),
(`74828799`,`NOVO BCO CONTINENTAL S.A. - BM`,753,`Novo Banco Continental S.A. - Banco Múltiplo`),
(`75647891`,`BCO CRÉDIT AGRICOLE BR S.A.`,222,`BANCO CRÉDIT AGRICOLE BRASIL S.A.`),
(`76543115`,`BANCO SISTEMA`,754,`Banco Sistema S.A.`),
(`78626983`,`BCO VR S.A.`,610,`Banco VR S.A.`),
(`78632767`,`BCO OURINVEST S.A.`,712,`Banco Ourinvest S.A.`),
(`80271455`,`BCO RNX S.A.`,720,`BANCO RNX S.A.`),
(`81723108`,`CREDICOAMO`,10,`CREDICOAMO CREDITO RURAL COOPERATIVA`),
(`90400888`,`BCO SANTANDER (BRASIL) S.A.`,33,`BANCO SANTANDER (BRASIL) S.A.`),
(`91884981`,`BANCO JOHN DEERE S.A.`,217,`Banco John Deere S.A.`),
(`92702067`,`BCO DO ESTADO DO RS S.A.`,41,`Banco do Estado do Rio Grande do Sul S.A.`),
(`92874270`,`BCO DIGIMAIS S.A.`,654,`BANCO DIGIMAIS S.A.`),
(`92894922`,`BANCO ORIGINAL`,212,`Banco Original S.A.`);
