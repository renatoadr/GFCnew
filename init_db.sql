CREATE TABLE  IF NOT EXISTS `tb_agendas` (
  `id` INT AUTO_INCREMENT NOT NULL,
  `id_empreendimento` INT NOT NULL,
  `mes_vigencia` VARCHAR(2) NOT NULL,
  `ano_vigencia` VARCHAR(4) NOT NULL,
  `id_atividade` VARCHAR(7) NOT NULL,
  `status` VARCHAR(15) NULL,
  `dt_atividade` DATE NULL,
  `nm_resp_atividade` VARCHAR(100) NULL,
  `dt_baixa` DATE NULL,
  `nm_resp_baixa` VARCHAR(100) NULL,
   PRIMARY KEY (`id`)
)
ENGINE = InnoDB;
CREATE TABLE  IF NOT EXISTS `tb_agendas_atividades` (
  `id_atividade` VARCHAR(7) NOT NULL,
  `descr_atividade` VARCHAR(100) NULL,
   PRIMARY KEY (`id_atividade`)
)
ENGINE = InnoDB;
CREATE TABLE  IF NOT EXISTS `tb_aspectos` (
  `id` INT AUTO_INCREMENT NOT NULL,
  `status` VARCHAR(100) NOT NULL,
  `descricao` VARCHAR(500) NULL,
  `id_empreendimento` INT NOT NULL,
  `id_pergunta_aspecto` INT NOT NULL,
  `mes_vigencia` VARCHAR(2) NOT NULL,
  `ano_vigencia` INT NOT NULL,
   PRIMARY KEY (`id`)
)
ENGINE = InnoDB;
CREATE TABLE  IF NOT EXISTS `tb_bancos` (
  `ispb` VARCHAR(10) NULL,
  `codigo` INT NOT NULL,
  `descricao` VARCHAR(60) NOT NULL,
  `descricao_completa` VARCHAR(150) NULL,
   PRIMARY KEY (`codigo`)
)
ENGINE = MyISAM;
CREATE TABLE  IF NOT EXISTS `tb_certidoes` (
  `id_empreendimento` INT NOT NULL,
  `estadual_status` VARCHAR(8) NULL,
  `estadual_validade` DATE NULL,
  `fgts_status` VARCHAR(8) NULL,
  `fgts_validade` DATE NULL,
  `municipal_status` VARCHAR(8) NULL,
  `municipal_validade` DATE NULL,
  `srf_inss_status` VARCHAR(8) NULL,
  `srf_inss_validade` DATE NULL,
  `trabalhista_status` VARCHAR(8) NULL,
  `trabalhista_validade` DATE NULL,
   PRIMARY KEY (`id_empreendimento`)
)
ENGINE = InnoDB;
CREATE TABLE  IF NOT EXISTS `tb_clientes` (
  `cpf_cnpj` VARCHAR(15) NOT NULL,
  `tp_cpf_cnpj` VARCHAR(4) NULL,
  `nm_cliente` VARCHAR(100) NULL,
  `ddd` VARCHAR(3) NULL,
  `tel` VARCHAR(9) NULL,
  `email` VARCHAR(50) NULL,
   PRIMARY KEY (`cpf_cnpj`)
)
ENGINE = InnoDB;
CREATE TABLE  IF NOT EXISTS `tb_consideracoes` (
  `id` INT AUTO_INCREMENT NOT NULL,
  `campo` VARCHAR(20) NOT NULL,
  `texto` VARCHAR(120) NOT NULL,
  `dt_criado` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ,
  `ac_historico` VARCHAR(45) NULL,
  `id_empreendimento` INT NOT NULL,
  `dt_editado` TIMESTAMP NULL,
  `mes_vigencia` VARCHAR(2) NOT NULL,
  `ano_vigencia` INT NOT NULL,
   PRIMARY KEY (`id`)
)
ENGINE = MyISAM;
CREATE TABLE  IF NOT EXISTS `tb_contas` (
  `id_conta` INT AUTO_INCREMENT NOT NULL,
  `id_empreendimento` INT NOT NULL,
  `id_empreed_elonet` INT NULL,
  `id_conta_elonet` INT NULL,
  `mes_vigencia` VARCHAR(2) NOT NULL,
  `ano_vigencia` VARCHAR(4) NOT NULL,
  `dt_carga` DATETIME NULL,
  `vl_liberacao` DECIMAL(15,2) NULL,
  `vl_aporte_construtora` DECIMAL(15,2) NULL,
  `vl_receita_recebiveis` DECIMAL(15,2) NULL,
  `vl_pagto_obra` DECIMAL(15,2) NULL,
  `vl_pagto_rh` DECIMAL(15,2) NULL,
  `vl_diferenca` DECIMAL(15,2) NULL,
  `vl_saldo` DECIMAL(15,2) NULL,
   PRIMARY KEY (`id_conta`)
)
ENGINE = InnoDB;
CREATE TABLE  IF NOT EXISTS `tb_empreendimentos` (
  `id_empreendimento` INT AUTO_INCREMENT NOT NULL,
  `id_empreed_elonet` INT NULL,
  `nm_empreendimento` VARCHAR(100) NULL,
  `apelido` VARCHAR(10) NULL,
  `nm_incorporador` VARCHAR(100) NULL,
  `nm_construtor` VARCHAR(100) NULL,
  `logradouro` VARCHAR(100) NULL,
  `bairro` VARCHAR(50) NULL,
  `cidade` VARCHAR(50) NULL,
  `estado` VARCHAR(2) NULL,
  `cep` VARCHAR(8) NULL,
  `cpf_cnpj_engenheiro` VARCHAR(15) NULL,
  `vl_plano_empresario` DECIMAL(15,2) NULL,
  `indice_garantia` DECIMAL(3,2) NULL,
  `previsao_entrega` DATE NULL,
  `cod_banco` INT NOT NULL,
   PRIMARY KEY (`id_empreendimento`)
)
ENGINE = InnoDB;
CREATE TABLE  IF NOT EXISTS `tb_financeiro` (
  `id_empreendimento` INT NOT NULL,
  `mes_vigencia` VARCHAR(2) NOT NULL,
  `ano_vigencia` VARCHAR(4) NOT NULL,
  `ordem` INT NOT NULL,
  `historico` VARCHAR(50) NULL,
  `perc_financeiro` DECIMAL(5,2) NULL,
  `vl_financeiro` DECIMAL(15,2) NULL,
   PRIMARY KEY (`id_empreendimento`, `mes_vigencia`, `ano_vigencia`, `ordem`)
)
ENGINE = InnoDB;
CREATE TABLE  IF NOT EXISTS `tb_garantias` (
  `id_empreendimento` INT NOT NULL,
  `tipo` VARCHAR(5) NOT NULL,
  `historico` VARCHAR(50) NOT NULL,
  `status` VARCHAR(10) NOT NULL,
  `observacao` VARCHAR(50) NULL,
  `id_garantia` INT AUTO_INCREMENT NOT NULL,
  `criado_em` DATETIME NOT NULL,
   PRIMARY KEY (`id_garantia`)
)
ENGINE = InnoDB;
CREATE TABLE  IF NOT EXISTS `tb_inadimplencias` (
  `id_empreendimento` INT NOT NULL,
  `mes_vigencia` VARCHAR(2) NOT NULL,
  `ano_vigencia` VARCHAR(4) NOT NULL,
  `ordem` INT NOT NULL,
  `periodo` VARCHAR(10) NULL,
  `qt_unidades` INT NULL,
   PRIMARY KEY (`id_empreendimento`, `mes_vigencia`, `ano_vigencia`, `ordem`)
)
ENGINE = InnoDB;
CREATE TABLE  IF NOT EXISTS `tb_medicoes` (
  `id_medicao` INT AUTO_INCREMENT NOT NULL,
  `id_empreendimento` INT NOT NULL,
  `mes_vigencia` VARCHAR(2) NOT NULL,
  `ano_vigencia` VARCHAR(4) NOT NULL,
  `dt_carga` DATETIME NULL,
  `nr_medicao` VARCHAR(4) NOT NULL,
  `perc_previsto_acumulado` DECIMAL(5,2) NULL,
  `perc_realizado_acumulado` DECIMAL(5,2) NULL,
  `perc_diferenca` DECIMAL(5,2) NULL,
  `perc_previsto_periodo` DECIMAL(5,2) NULL,
  `perc_realizado_periodo` DECIMAL(5,2) NULL,
  'dt_medicao' DATE NULL,
   PRIMARY KEY (`id_medicao`)
)
ENGINE = InnoDB;
CREATE TABLE  IF NOT EXISTS `tb_notas` (
  `id_nota` INT AUTO_INCREMENT NOT NULL,
  `id_empreendimento` INT NOT NULL,
  `mes_vigencia` VARCHAR(2) NOT NULL,
  `ano_vigencia` VARCHAR(4) NOT NULL,
  `dt_carga` DATETIME NOT NULL,
  `produto` VARCHAR(100) NULL,
  `vl_nota_fiscal` DECIMAL(15,2) NULL,
  `vl_estoque` DECIMAL(15,2) NULL,
   PRIMARY KEY (`id_nota`)
)
ENGINE = InnoDB;
CREATE TABLE  IF NOT EXISTS `tb_orcamentos` (
  `id_orcamento` INT AUTO_INCREMENT NOT NULL,
  `id_empreendimento` INT NULL,
  `mes_vigencia` VARCHAR(2) NULL,
  `ano_vigencia` VARCHAR(4) NULL,
  `dt_carga` DATETIME NULL,
  `item` VARCHAR(50) NULL,
  `orcado_valor` DECIMAL(15,2) NULL,
  `fisico_valor` DECIMAL(15,2) NULL,
  `fisico_percentual` DECIMAL(6,2) NULL,
  `fisico_saldo` DECIMAL(15,2) NULL,
  `financeiro_valor` DECIMAL(15,2) NULL,
  `financeiro_percentual` DECIMAL(6,2) NULL,
  `financeiro_saldo` DECIMAL(15,2) NULL,
   PRIMARY KEY (`id_orcamento`)
)
ENGINE = InnoDB;
CREATE TABLE  IF NOT EXISTS `tb_perguntas_aspectos` (
  `id` INT AUTO_INCREMENT NOT NULL,
  `pergunta` VARCHAR(350) NOT NULL,
  `grupo` VARCHAR(100) NOT NULL,
  `opcoes` VARCHAR(500) NOT NULL,
   PRIMARY KEY (`id`)
)
ENGINE = InnoDB;
CREATE TABLE  IF NOT EXISTS `tb_torres` (
  `id_torre` INT AUTO_INCREMENT NOT NULL,
  `id_empreendimento` INT NOT NULL,
  `id_empreed_elonet` INT NULL,
  `id_torre_elonet` INT NULL,
  `nm_torre` VARCHAR(20) NOT NULL,
  `qt_unidade` INT NOT NULL,
  `qt_andar` INT NOT NULL,
  `qt_coberturas` INT NULL,
  `prefix_cobertura` VARCHAR(20) NULL,
  `num_apt_um_andar_um` INT NULL,
  `vl_unidade` DECIMAL(15,2) NULL,
  `vl_cobertura` DECIMAL(15,2) NULL,
   PRIMARY KEY (`id_torre`)
)
ENGINE = InnoDB;
CREATE TABLE  IF NOT EXISTS `tb_unidades` (
  `id_unidade` INT AUTO_INCREMENT NOT NULL,
  `id_empreendimento` INT NOT NULL,
  `id_torre` INT NOT NULL,
  `id_empreed_elonet` INT NULL,
  `id_torre_elonet` INT NULL,
  `unidade` VARCHAR(15) NOT NULL,
  `mes_vigencia` VARCHAR(2) NOT NULL,
  `ano_vigencia` VARCHAR(4) NOT NULL,
  `vl_unidade` DECIMAL(10,2) NULL,
  `status` VARCHAR(8) NOT NULL,
  `cpf_cnpj_comprador` VARCHAR(15) NULL,
  `vl_receber` DECIMAL(10,2) NULL,
  `dt_ocorrencia` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ,
  `financiado` VARCHAR(3) NULL,
  `vl_chaves` DECIMAL(15,2) NULL,
  `vl_pre_chaves` DECIMAL(15,2) NULL,
  `vl_pos_chaves` DECIMAL(15,2) NULL,
  `ac_historico` VARCHAR(15) NULL,
   PRIMARY KEY (`id_unidade`)
)
ENGINE = InnoDB;
CREATE TABLE  IF NOT EXISTS `tb_usuarios` (
  `id_usuario` INT AUTO_INCREMENT NOT NULL,
  `email` VARCHAR(50) NULL,
  `senha` VARCHAR(100) NULL,
  `tp_acesso` VARCHAR(15) NULL,
  `nm_usuario` VARCHAR(100) NULL,
  `cod_banco` INT NULL,
   PRIMARY KEY (`id_usuario`),
  CONSTRAINT `email` UNIQUE (`email`)
)
ENGINE = InnoDB;
CREATE TABLE `tb_sinapi_item` (
  `id` int NOT NULL AUTO_INCREMENT,
  `dt_criacao` date NOT NULL,
  `dt_vigencia` date NOT NULL,
  `cod_item` int DEFAULT NULL,
  `cod_composicao` int NOT NULL,
  `nm_grupo` text NOT NULL,
  `tp_item` text CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci,
  `desc_item` text NOT NULL,
  `tp_unidade` text NOT NULL,
  `vl_coeficiente` decimal(11,7) DEFAULT NULL,
  `dt_emissao` date NOT NULL,
  PRIMARY KEY (`id`),
  KEY `idx_sinapi_item_desc` (`desc_item`(250)),
  KEY `idx_sinapi_item_comp_dt` (`cod_composicao`,`dt_vigencia`),
  KEY `idx_sinapi_item_cod_comp_dt` (`cod_item`,`cod_composicao`,`dt_vigencia`)
) ENGINE=MyISAM AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
CREATE TABLE `tb_sinapi_custo` (
  `id` int NOT NULL AUTO_INCREMENT,
  `dt_criacao` date NOT NULL,
  `dt_vigencia` date NOT NULL,
  `cod_item` int NOT NULL,
  `nm_tipo` text NOT NULL,
  `vl_ac` decimal(10,2) NOT NULL,
  `vl_al` decimal(10,2) NOT NULL,
  `vl_am` decimal(10,2) NOT NULL,
  `vl_ap` decimal(10,2) NOT NULL,
  `vl_ba` decimal(10,2) NOT NULL,
  `vl_ce` decimal(10,2) NOT NULL,
  `vl_df` decimal(10,2) NOT NULL,
  `vl_es` decimal(10,2) NOT NULL,
  `vl_go` decimal(10,2) NOT NULL,
  `vl_ma` decimal(10,2) NOT NULL,
  `vl_mg` decimal(10,2) NOT NULL,
  `vl_ms` decimal(10,2) NOT NULL,
  `vl_mt` decimal(10,2) NOT NULL,
  `vl_pa` decimal(10,2) NOT NULL,
  `vl_pb` decimal(10,2) NOT NULL,
  `vl_pe` decimal(10,2) NOT NULL,
  `vl_pi` decimal(10,2) NOT NULL,
  `vl_pr` decimal(10,2) NOT NULL,
  `vl_rj` decimal(10,2) NOT NULL,
  `vl_rn` decimal(10,2) NOT NULL,
  `vl_ro` decimal(10,2) NOT NULL,
  `vl_rr` decimal(10,2) NOT NULL,
  `vl_rs` decimal(10,2) NOT NULL,
  `vl_sc` decimal(10,2) NOT NULL,
  `vl_se` decimal(10,2) NOT NULL,
  `vl_sp` decimal(10,2) NOT NULL,
  `vl_to` decimal(10,2) NOT NULL,
  `dt_emissao` date NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
CREATE TABLE `tb_opcoes` (
  `id` int NOT NULL AUTO_INCREMENT,
  `chave` varchar(40) NOT NULL,
  `valor` text,
  PRIMARY KEY (`id`),
  UNIQUE KEY `tb_opcoes_chave_unique` (`chave`)
) ENGINE=MyISAM AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
CREATE TABLE `tb_itens_produtos` (
  `id` int NOT NULL AUTO_INCREMENT,
  `id_cat` int NOT NULL,
  `descricao` varchar(500) NOT NULL,
  `codigo` int DEFAULT NULL,
  `unidade` varchar(10) DEFAULT NULL,
  `ativo` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
CREATE TABLE `tb_categorias` (
  `id` int NOT NULL AUTO_INCREMENT,
  `id_cat_pai` int DEFAULT NULL,
  `descricao` varchar(250) NOT NULL,
  `agrupador` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `ativo` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `tb_categorias_agrupador_IDX` (`agrupador`) USING BTREE,
  KEY `tb_categorias_descricao_IDX` (`descricao`) USING BTREE
) ENGINE=MyISAM AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
CREATE TABLE `tb_sync_elonet` (
  `id` int NOT NULL AUTO_INCREMENT,
  `chave_dominio` varchar(50) NOT NULL,
  `nm_campo` varchar(100) NOT NULL,
  `valor_antigo` text,
  `novo_valor` text,
  `ts_sync` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
CREATE TABLE IF NOT EXISTS `tb_contabil_empreendimentos` (
  `id` int NOT NULL AUTO_INCREMENT,
  `id_empreendimento` int NOT NULL,
  `id_empreendimento_elonet` int DEFAULT NULL,
  `dt_criado` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `dt_vigencia` date NOT NULL,
  `vlr_liberado` decimal(15,2) NOT NULL,
  `vlr_a_liberar` decimal(15,2) NOT NULL,
  `vlr_estoque` decimal(15,2) NOT NULL,
  `vlr_recebivel` decimal(15,2) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `empreend_vigencia` (`id_empreendimento_elonet`,`dt_vigencia`)
) ENGINE=MyISAM AUTO_INCREMENT=26 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
CREATE INDEX `idx_medicoes`
ON `tb_medicoes` (
  `id_empreendimento` ASC,
  `mes_vigencia` ASC,
  `ano_vigencia` ASC
);
CREATE INDEX `idx_nota`
ON `tb_notas` (
  `dt_carga` ASC,
  `id_empreendimento` ASC,
  `mes_vigencia` ASC,
  `ano_vigencia` ASC
);
CREATE INDEX `idx_torres`
ON `tb_torres` (
  `id_empreendimento` ASC,
  `id_torre` ASC
);
CREATE INDEX `idx_unidades`
ON `tb_unidades` (
  `id_empreendimento` ASC,
  `id_torre` ASC,
  `unidade` ASC,
  `mes_vigencia` ASC,
  `ano_vigencia` ASC
);
CREATE INDEX `idx_email`
ON `tb_usuarios` (
  `email` ASC
);
SET FOREIGN_KEY_CHECKS = 0;
CREATE UNIQUE INDEX uq_chave ON db_gfc.tb_opcoes(chave);

INSERT INTO `tb_agendas_atividades` (`id_atividade`, `descr_atividade`) VALUES ('DOCFIS', 'Validar posição de documentos fiscais');
INSERT INTO `tb_agendas_atividades` (`id_atividade`, `descr_atividade`) VALUES ('GEREL', 'Gerar relatório');
INSERT INTO `tb_agendas_atividades` (`id_atividade`, `descr_atividade`) VALUES ('IMG3D', 'Cadastrar imagens 3D');
INSERT INTO `tb_agendas_atividades` (`id_atividade`, `descr_atividade`) VALUES ('IMGOBRA', 'Cadastrar imagens da obra');
INSERT INTO `tb_agendas_atividades` (`id_atividade`, `descr_atividade`) VALUES ('MOVCC', 'Solicitar movimentação de conta corrente');
INSERT INTO `tb_agendas_atividades` (`id_atividade`, `descr_atividade`) VALUES ('PAGFOR', 'Cadastrar posição de pagamento a fornecedores');
INSERT INTO `tb_agendas_atividades` (`id_atividade`, `descr_atividade`) VALUES ('POSINA', 'Solicitar posição de inadimplência');
INSERT INTO `tb_agendas_atividades` (`id_atividade`, `descr_atividade`) VALUES ('PTATEN', 'Cadastrar pontos de atenção');
INSERT INTO `tb_agendas_atividades` (`id_atividade`, `descr_atividade`) VALUES ('VISTOR', 'Fazer vistoria');
INSERT INTO `tb_bancos` (`ispb`, `codigo`, `descricao`, `descricao_completa`) VALUES ('00000000', 1, 'BCO DO BRASIL S.A.', 'Banco do Brasil S.A.');
INSERT INTO `tb_bancos` (`ispb`, `codigo`, `descricao`, `descricao_completa`) VALUES ('00000208', 70, 'BRB - BCO DE BRASILIA S.A.', 'BRB - BANCO DE BRASILIA S.A.');
INSERT INTO `tb_bancos` (`ispb`, `codigo`, `descricao`, `descricao_completa`) VALUES ('00122327', 539, 'SANTINVEST S.A. - CFI', 'SANTINVEST S.A. - CREDITO, FINANCIAMENTO E INVESTIMENTOS');
INSERT INTO `tb_bancos` (`ispb`, `codigo`, `descricao`, `descricao_completa`) VALUES ('00204963', 430, 'CCR SEARA', 'COOPERATIVA DE CREDITO RURAL SEARA - CREDISEARA');
INSERT INTO `tb_bancos` (`ispb`, `codigo`, `descricao`, `descricao_completa`) VALUES ('00315557', 136, 'CONF NAC COOP CENTRAIS UNICRED', 'CONFEDERAÇÃO NACIONAL DAS COOPERATIVAS CENTRAIS UNICRED LTDA. - UNICRED DO BRASI');
INSERT INTO `tb_bancos` (`ispb`, `codigo`, `descricao`, `descricao_completa`) VALUES ('00360305', 104, 'CAIXA ECONOMICA FEDERAL', 'CAIXA ECONOMICA FEDERAL');
INSERT INTO `tb_bancos` (`ispb`, `codigo`, `descricao`, `descricao_completa`) VALUES ('00416968', 77, 'BANCO INTER', 'Banco Inter S.A.');
INSERT INTO `tb_bancos` (`ispb`, `codigo`, `descricao`, `descricao_completa`) VALUES ('00517645', 741, 'BCO RIBEIRAO PRETO S.A.', 'BANCO RIBEIRAO PRETO S.A.');
INSERT INTO `tb_bancos` (`ispb`, `codigo`, `descricao`, `descricao_completa`) VALUES ('00556603', 330, 'BANCO BARI S.A.', 'BANCO BARI DE INVESTIMENTOS E FINANCIAMENTOS S.A.');
INSERT INTO `tb_bancos` (`ispb`, `codigo`, `descricao`, `descricao_completa`) VALUES ('00558456', 739, 'BCO CETELEM S.A.', 'Banco Cetelem S.A.');
INSERT INTO `tb_bancos` (`ispb`, `codigo`, `descricao`, `descricao_completa`) VALUES ('00795423', 743, 'BANCO SEMEAR', 'Banco Semear S.A.');
INSERT INTO `tb_bancos` (`ispb`, `codigo`, `descricao`, `descricao_completa`) VALUES ('01023570', 747, 'BCO RABOBANK INTL BRASIL S.A.', 'Banco Rabobank International Brasil S.A.');
INSERT INTO `tb_bancos` (`ispb`, `codigo`, `descricao`, `descricao_completa`) VALUES ('01181521', 748, 'BCO COOPERATIVO SICREDI S.A.', 'BANCO COOPERATIVO SICREDI S.A.');
INSERT INTO `tb_bancos` (`ispb`, `codigo`, `descricao`, `descricao_completa`) VALUES ('01522368', 752, 'BCO BNP PARIBAS BRASIL S A', 'Banco BNP Paribas Brasil S.A.');
INSERT INTO `tb_bancos` (`ispb`, `codigo`, `descricao`, `descricao_completa`) VALUES ('01658426', 379, 'CECM COOPERFORTE', 'COOPERFORTE - COOPERATIVA DE ECONOMIA E CRÉDITO MÚTUO DE FUNCIONÁRIOS DE INSTITU');
INSERT INTO `tb_bancos` (`ispb`, `codigo`, `descricao`, `descricao_completa`) VALUES ('01701201', 399, 'KIRTON BANK', 'Kirton Bank S.A. - Banco Múltiplo');
INSERT INTO `tb_bancos` (`ispb`, `codigo`, `descricao`, `descricao_completa`) VALUES ('01852137', 378, 'BCO BRASILEIRO DE CRÉDITO S.A.', 'BANCO BRASILEIRO DE CRÉDITO SOCIEDADE ANÔNIMA');
INSERT INTO `tb_bancos` (`ispb`, `codigo`, `descricao`, `descricao_completa`) VALUES ('01858774', 413, 'BCO BV S.A.', 'BANCO BV S.A.');
INSERT INTO `tb_bancos` (`ispb`, `codigo`, `descricao`, `descricao_completa`) VALUES ('02038232', 756, 'BANCO SICOOB S.A.', 'BANCO COOPERATIVO SICOOB S.A. - BANCO SICOOB');
INSERT INTO `tb_bancos` (`ispb`, `codigo`, `descricao`, `descricao_completa`) VALUES ('02318507', 757, 'BCO KEB HANA DO BRASIL S.A.', 'BANCO KEB HANA DO BRASIL S.A.');
INSERT INTO `tb_bancos` (`ispb`, `codigo`, `descricao`, `descricao_completa`) VALUES ('02801938', 66, 'BCO MORGAN STANLEY S.A.', 'BANCO MORGAN STANLEY S.A.');
INSERT INTO `tb_bancos` (`ispb`, `codigo`, `descricao`, `descricao_completa`) VALUES ('03012230', 62, 'HIPERCARD BM S.A.', 'Hipercard Banco Múltiplo S.A.');
INSERT INTO `tb_bancos` (`ispb`, `codigo`, `descricao`, `descricao_completa`) VALUES ('03017677', 74, 'BCO. J.SAFRA S.A.', 'Banco J. Safra S.A.');
INSERT INTO `tb_bancos` (`ispb`, `codigo`, `descricao`, `descricao_completa`) VALUES ('03046391', 99, 'UNIPRIME COOPCENTRAL LTDA.', 'UNIPRIME CENTRAL NACIONAL - CENTRAL NACIONAL DE COOPERATIVA DE CREDITO');
INSERT INTO `tb_bancos` (`ispb`, `codigo`, `descricao`, `descricao_completa`) VALUES ('03215790', 387, 'BCO TOYOTA DO BRASIL S.A.', 'Banco Toyota do Brasil S.A.');
INSERT INTO `tb_bancos` (`ispb`, `codigo`, `descricao`, `descricao_completa`) VALUES ('03311443', 326, 'PARATI - CFI S.A.', 'PARATI - CREDITO, FINANCIAMENTO E INVESTIMENTO S.A.');
INSERT INTO `tb_bancos` (`ispb`, `codigo`, `descricao`, `descricao_completa`) VALUES ('03323840', 25, 'BCO ALFA S.A.', 'Banco Alfa S.A.');
INSERT INTO `tb_bancos` (`ispb`, `codigo`, `descricao`, `descricao_completa`) VALUES ('03532415', 75, 'BCO ABN AMRO S.A.', 'Banco ABN Amro S.A.');
INSERT INTO `tb_bancos` (`ispb`, `codigo`, `descricao`, `descricao_completa`) VALUES ('03609817', 40, 'BCO CARGILL S.A.', 'Banco Cargill S.A.');
INSERT INTO `tb_bancos` (`ispb`, `codigo`, `descricao`, `descricao_completa`) VALUES ('03844699', 385, 'CECM DOS TRAB.PORT. DA G.VITOR', 'COOPERATIVA DE ECONOMIA E CREDITO MUTUO DOS TRABALHADORES PORTUARIOS DA GRANDE V');
INSERT INTO `tb_bancos` (`ispb`, `codigo`, `descricao`, `descricao_completa`) VALUES ('03881423', 425, 'SOCINAL S.A. CFI', 'SOCINAL S.A. - CRÉDITO, FINANCIAMENTO E INVESTIMENTO');
INSERT INTO `tb_bancos` (`ispb`, `codigo`, `descricao`, `descricao_completa`) VALUES ('04184779', 63, 'BANCO BRADESCARD', 'Banco Bradescard S.A.');
INSERT INTO `tb_bancos` (`ispb`, `codigo`, `descricao`, `descricao_completa`) VALUES ('04307598', 382, 'FIDUCIA SCMEPP LTDA', 'FIDÚCIA SOCIEDADE DE CRÉDITO AO MICROEMPREENDEDOR E À EMPRESA DE PEQUENO PORTE L');
INSERT INTO `tb_bancos` (`ispb`, `codigo`, `descricao`, `descricao_completa`) VALUES ('04332281', 64, 'GOLDMAN SACHS DO BRASIL BM S.A', 'GOLDMAN SACHS DO BRASIL BANCO MULTIPLO S.A.');
INSERT INTO `tb_bancos` (`ispb`, `codigo`, `descricao`, `descricao_completa`) VALUES ('04632856', 97, 'CREDISIS CENTRAL DE COOPERATIVAS DE CRÉDITO LTDA.', 'Credisis - Central de Cooperativas de Crédito Ltda.');
INSERT INTO `tb_bancos` (`ispb`, `codigo`, `descricao`, `descricao_completa`) VALUES ('04814563', 299, 'BCO AFINZ S.A. - BM', 'BANCO AFINZ S.A. - BANCO MÚLTIPLO');
INSERT INTO `tb_bancos` (`ispb`, `codigo`, `descricao`, `descricao_completa`) VALUES ('04831810', 471, 'CECM SERV PUBL PINHÃO', 'COOPERATIVA DE ECONOMIA E CREDITO MUTUO DOS SERVIDORES PUBLICOS DE PINHÃO - CRES');
INSERT INTO `tb_bancos` (`ispb`, `codigo`, `descricao`, `descricao_completa`) VALUES ('04862600', 468, 'PORTOSEG S.A. CFI', 'PORTOSEG S.A. - CREDITO, FINANCIAMENTO E INVESTIMENTO');
INSERT INTO `tb_bancos` (`ispb`, `codigo`, `descricao`, `descricao_completa`) VALUES ('04866275', 12, 'BANCO INBURSA', 'Banco Inbursa S.A.');
INSERT INTO `tb_bancos` (`ispb`, `codigo`, `descricao`, `descricao_completa`) VALUES ('04902979', 3, 'BCO DA AMAZONIA S.A.', 'BANCO DA AMAZONIA S.A.');
INSERT INTO `tb_bancos` (`ispb`, `codigo`, `descricao`, `descricao_completa`) VALUES ('04913711', 37, 'BCO DO EST. DO PA S.A.', 'Banco do Estado do Pará S.A.');
INSERT INTO `tb_bancos` (`ispb`, `codigo`, `descricao`, `descricao_completa`) VALUES ('05192316', 411, 'VIA CERTA FINANCIADORA S.A. - CFI', 'Via Certa Financiadora S.A. - Crédito, Financiamento e Investimentos');
INSERT INTO `tb_bancos` (`ispb`, `codigo`, `descricao`, `descricao_completa`) VALUES ('05351887', 359, 'ZEMA CFI S/A', 'ZEMA CRÉDITO, FINANCIAMENTO E INVESTIMENTO S/A');
INSERT INTO `tb_bancos` (`ispb`, `codigo`, `descricao`, `descricao_completa`) VALUES ('05442029', 159, 'CASA CREDITO S.A. SCM', 'Casa do Crédito S.A. Sociedade de Crédito ao Microempreendedor');
INSERT INTO `tb_bancos` (`ispb`, `codigo`, `descricao`, `descricao_completa`) VALUES ('05463212', 85, 'COOPCENTRAL AILOS', 'Cooperativa Central de Crédito - Ailos');
INSERT INTO `tb_bancos` (`ispb`, `codigo`, `descricao`, `descricao_completa`) VALUES ('05676026', 429, 'CREDIARE CFI S.A.', 'Crediare S.A. - Crédito, financiamento e investimento');
INSERT INTO `tb_bancos` (`ispb`, `codigo`, `descricao`, `descricao_completa`) VALUES ('05684234', 410, 'PLANNER SOCIEDADE DE CRÉDITO DIRETO', 'PLANNER SOCIEDADE DE CRÉDITO DIRETO S.A.');
INSERT INTO `tb_bancos` (`ispb`, `codigo`, `descricao`, `descricao_completa`) VALUES ('06271464', 36, 'BCO BBI S.A.', 'Banco Bradesco BBI S.A.');
INSERT INTO `tb_bancos` (`ispb`, `codigo`, `descricao`, `descricao_completa`) VALUES ('07207996', 394, 'BCO BRADESCO FINANC. S.A.', 'Banco Bradesco Financiamentos S.A.');
INSERT INTO `tb_bancos` (`ispb`, `codigo`, `descricao`, `descricao_completa`) VALUES ('07237373', 4, 'BCO DO NORDESTE DO BRASIL S.A.', 'Banco do Nordeste do Brasil S.A.');
INSERT INTO `tb_bancos` (`ispb`, `codigo`, `descricao`, `descricao_completa`) VALUES ('07450604', 320, 'BCO CCB BRASIL S.A.', 'China Construction Bank (Brasil) Banco Múltiplo S/A');
INSERT INTO `tb_bancos` (`ispb`, `codigo`, `descricao`, `descricao_completa`) VALUES ('07512441', 189, 'HS FINANCEIRA', 'HS FINANCEIRA S/A CREDITO, FINANCIAMENTO E INVESTIMENTOS');
INSERT INTO `tb_bancos` (`ispb`, `codigo`, `descricao`, `descricao_completa`) VALUES ('07652226', 105, 'LECCA CFI S.A.', 'Lecca Crédito, Financiamento e Investimento S/A');
INSERT INTO `tb_bancos` (`ispb`, `codigo`, `descricao`, `descricao_completa`) VALUES ('07656500', 76, 'BCO KDB BRASIL S.A.', 'Banco KDB do Brasil S.A.');
INSERT INTO `tb_bancos` (`ispb`, `codigo`, `descricao`, `descricao_completa`) VALUES ('07679404', 82, 'BANCO TOPÁZIO S.A.', 'BANCO TOPÁZIO S.A.');
INSERT INTO `tb_bancos` (`ispb`, `codigo`, `descricao`, `descricao_completa`) VALUES ('07693858', 312, 'HSCM SCMEPP LTDA.', 'HSCM - SOCIEDADE DE CRÉDITO AO MICROEMPREENDEDOR E À EMPRESA DE PEQUENO PORTE LT');
INSERT INTO `tb_bancos` (`ispb`, `codigo`, `descricao`, `descricao_completa`) VALUES ('07799277', 195, 'VALOR SCD S.A.', 'VALOR SOCIEDADE DE CRÉDITO DIRETO S.A.');
INSERT INTO `tb_bancos` (`ispb`, `codigo`, `descricao`, `descricao_completa`) VALUES ('07945233', 93, 'POLOCRED SCMEPP LTDA.', 'PÓLOCRED   SOCIEDADE DE CRÉDITO AO MICROEMPREENDEDOR E À EMPRESA DE PEQUENO PORT');
INSERT INTO `tb_bancos` (`ispb`, `codigo`, `descricao`, `descricao_completa`) VALUES ('08240446', 391, 'CCR DE IBIAM', 'COOPERATIVA DE CREDITO RURAL DE IBIAM - SULCREDI/IBIAM');
INSERT INTO `tb_bancos` (`ispb`, `codigo`, `descricao`, `descricao_completa`) VALUES ('08357240', 368, 'BCO CSF S.A.', 'Banco CSF S.A.');
INSERT INTO `tb_bancos` (`ispb`, `codigo`, `descricao`, `descricao_completa`) VALUES ('09210106', 183, 'SOCRED SA - SCMEPP', 'SOCRED S.A. - SOCIEDADE DE CRÉDITO AO MICROEMPREENDEDOR E À EMPRESA DE PEQUENO P');
INSERT INTO `tb_bancos` (`ispb`, `codigo`, `descricao`, `descricao_completa`) VALUES ('09274232', 14, 'STATE STREET BR S.A. BCO COMERCIAL', 'STATE STREET BRASIL S.A. - BANCO COMERCIAL');
INSERT INTO `tb_bancos` (`ispb`, `codigo`, `descricao`, `descricao_completa`) VALUES ('09313766', 130, 'CARUANA SCFI', 'CARUANA S.A. - SOCIEDADE DE CRÉDITO, FINANCIAMENTO E INVESTIMENTO');
INSERT INTO `tb_bancos` (`ispb`, `codigo`, `descricao`, `descricao_completa`) VALUES ('09464032', 358, 'MIDWAY S.A. - SCFI', 'MIDWAY S.A. - CRÉDITO, FINANCIAMENTO E INVESTIMENTO');
INSERT INTO `tb_bancos` (`ispb`, `codigo`, `descricao`, `descricao_completa`) VALUES ('09516419', 79, 'PICPAY BANK - BANCO MÚLTIPLO S.A', 'PICPAY BANK - BANCO MÚLTIPLO S.A');
INSERT INTO `tb_bancos` (`ispb`, `codigo`, `descricao`, `descricao_completa`) VALUES ('09526594', 141, 'MASTER BI S.A.', 'BANCO MASTER DE INVESTIMENTO S.A.');
INSERT INTO `tb_bancos` (`ispb`, `codigo`, `descricao`, `descricao_completa`) VALUES ('10264663', 81, 'BANCOSEGURO S.A.', 'BancoSeguro S.A.');
INSERT INTO `tb_bancos` (`ispb`, `codigo`, `descricao`, `descricao_completa`) VALUES ('10371492', 475, 'BCO YAMAHA MOTOR S.A.', 'Banco Yamaha Motor do Brasil S.A.');
INSERT INTO `tb_bancos` (`ispb`, `codigo`, `descricao`, `descricao_completa`) VALUES ('10398952', 133, 'CRESOL CONFEDERAÇÃO', 'CONFEDERAÇÃO NACIONAL DAS COOPERATIVAS CENTRAIS DE CRÉDITO E ECONOMIA FAMILIAR E');
INSERT INTO `tb_bancos` (`ispb`, `codigo`, `descricao`, `descricao_completa`) VALUES ('10664513', 121, 'BCO AGIBANK S.A.', 'Banco Agibank S.A.');
INSERT INTO `tb_bancos` (`ispb`, `codigo`, `descricao`, `descricao_completa`) VALUES ('10690848', 83, 'BCO DA CHINA BRASIL S.A.', 'Banco da China Brasil S.A.');
INSERT INTO `tb_bancos` (`ispb`, `codigo`, `descricao`, `descricao_completa`) VALUES ('10866788', 24, 'BCO BANDEPE S.A.', 'Banco Bandepe S.A.');
INSERT INTO `tb_bancos` (`ispb`, `codigo`, `descricao`, `descricao_completa`) VALUES ('11165756', 384, 'GLOBAL SCM LTDA', 'GLOBAL FINANÇAS SOCIEDADE DE CRÉDITO AO MICROEMPREENDEDOR E À EMPRESA DE PEQUENO');
INSERT INTO `tb_bancos` (`ispb`, `codigo`, `descricao`, `descricao_completa`) VALUES ('11285104', 426, 'NEON FINANCEIRA - CFI S.A.', 'NEON FINANCEIRA - CRÉDITO, FINANCIAMENTO E INVESTIMENTO S.A.');
INSERT INTO `tb_bancos` (`ispb`, `codigo`, `descricao`, `descricao_completa`) VALUES ('11476673', 88, 'BANCO RANDON S.A.', 'BANCO RANDON S.A.');
INSERT INTO `tb_bancos` (`ispb`, `codigo`, `descricao`, `descricao_completa`) VALUES ('11581339', 274, 'BMP SCMEPP LTDA', 'BMP SOCIEDADE DE CRÉDITO AO MICROEMPREENDEDOR E A EMPRESA DE PEQUENO PORTE LTDA.');
INSERT INTO `tb_bancos` (`ispb`, `codigo`, `descricao`, `descricao_completa`) VALUES ('11758741', 94, 'BANCO FINAXIS', 'Banco Finaxis S.A.');
INSERT INTO `tb_bancos` (`ispb`, `codigo`, `descricao`, `descricao_completa`) VALUES ('11760553', 478, 'GAZINCRED S.A. SCFI', 'GAZINCRED S.A. SOCIEDADE DE CRÉDITO, FINANCIAMENTO E INVESTIMENTO');
INSERT INTO `tb_bancos` (`ispb`, `codigo`, `descricao`, `descricao_completa`) VALUES ('11970623', 276, 'BCO SENFF S.A.', 'BANCO SENFF S.A.');
INSERT INTO `tb_bancos` (`ispb`, `codigo`, `descricao`, `descricao_completa`) VALUES ('13009717', 47, 'BCO DO EST. DE SE S.A.', 'Banco do Estado de Sergipe S.A.');
INSERT INTO `tb_bancos` (`ispb`, `codigo`, `descricao`, `descricao_completa`) VALUES ('13220493', 126, 'BR PARTNERS BI', 'BR Partners Banco de Investimento S.A.');
INSERT INTO `tb_bancos` (`ispb`, `codigo`, `descricao`, `descricao_completa`) VALUES ('13720915', 119, 'BCO WESTERN UNION', 'Banco Western Union do Brasil S.A.');
INSERT INTO `tb_bancos` (`ispb`, `codigo`, `descricao`, `descricao_completa`) VALUES ('14388334', 254, 'PARANA BCO S.A.', 'PARANÁ BANCO S.A.');
INSERT INTO `tb_bancos` (`ispb`, `codigo`, `descricao`, `descricao_completa`) VALUES ('14511781', 268, 'BARI CIA HIPOTECÁRIA', 'BARI COMPANHIA HIPOTECÁRIA');
INSERT INTO `tb_bancos` (`ispb`, `codigo`, `descricao`, `descricao_completa`) VALUES ('15114366', 107, 'BCO BOCOM BBM S.A.', 'Banco Bocom BBM S.A.');
INSERT INTO `tb_bancos` (`ispb`, `codigo`, `descricao`, `descricao_completa`) VALUES ('15124464', 334, 'BANCO BESA S.A.', 'BANCO BESA S.A.');
INSERT INTO `tb_bancos` (`ispb`, `codigo`, `descricao`, `descricao_completa`) VALUES ('15173776', 412, 'SOCIAL BANK S/A', 'SOCIAL BANK BANCO MÚLTIPLO S/A');
INSERT INTO `tb_bancos` (`ispb`, `codigo`, `descricao`, `descricao_completa`) VALUES ('15357060', 124, 'BCO WOORI BANK DO BRASIL S.A.', 'Banco Woori Bank do Brasil S.A.');
INSERT INTO `tb_bancos` (`ispb`, `codigo`, `descricao`, `descricao_completa`) VALUES ('15581638', 149, 'FACTA S.A. CFI', 'Facta Financeira S.A. - Crédito Financiamento e Investimento');
INSERT INTO `tb_bancos` (`ispb`, `codigo`, `descricao`, `descricao_completa`) VALUES ('17184037', 389, 'BCO MERCANTIL DO BRASIL S.A.', 'Banco Mercantil do Brasil S.A.');
INSERT INTO `tb_bancos` (`ispb`, `codigo`, `descricao`, `descricao_completa`) VALUES ('17298092', 184, 'BCO ITAÚ BBA S.A.', 'Banco Itaú BBA S.A.');
INSERT INTO `tb_bancos` (`ispb`, `codigo`, `descricao`, `descricao_completa`) VALUES ('17351180', 634, 'BCO TRIANGULO S.A.', 'BANCO TRIANGULO S.A.');
INSERT INTO `tb_bancos` (`ispb`, `codigo`, `descricao`, `descricao_completa`) VALUES ('17453575', 132, 'ICBC DO BRASIL BM S.A.', 'ICBC do Brasil Banco Múltiplo S.A.');
INSERT INTO `tb_bancos` (`ispb`, `codigo`, `descricao`, `descricao_completa`) VALUES ('17826860', 377, 'BMS SCD S.A.', 'BMS SOCIEDADE DE CRÉDITO DIRETO S.A.');
INSERT INTO `tb_bancos` (`ispb`, `codigo`, `descricao`, `descricao_completa`) VALUES ('18188384', 321, 'CREFAZ SCMEPP LTDA', 'CREFAZ SOCIEDADE DE CRÉDITO AO MICROEMPREENDEDOR E A EMPRESA DE PEQUENO PORTE LT');
INSERT INTO `tb_bancos` (`ispb`, `codigo`, `descricao`, `descricao_completa`) VALUES ('18236120', 260, 'NU PAGAMENTOS - IP', 'NU PAGAMENTOS S.A. - INSTITUIÇÃO DE PAGAMENTO');
INSERT INTO `tb_bancos` (`ispb`, `codigo`, `descricao`, `descricao_completa`) VALUES ('18394228', 470, 'CDC SCD S.A.', 'CDC SOCIEDADE DE CRÉDITO DIRETO S.A.');
INSERT INTO `tb_bancos` (`ispb`, `codigo`, `descricao`, `descricao_completa`) VALUES ('18520834', 129, 'UBS BRASIL BI S.A.', 'UBS Brasil Banco de Investimento S.A.');
INSERT INTO `tb_bancos` (`ispb`, `codigo`, `descricao`, `descricao_completa`) VALUES ('19324634', 416, 'LAMARA SCD S.A.', 'LAMARA SOCIEDADE DE CRÉDITO DIRETO S.A.');
INSERT INTO `tb_bancos` (`ispb`, `codigo`, `descricao`, `descricao_completa`) VALUES ('20855875', 536, 'NEON PAGAMENTOS S.A. IP', 'NEON PAGAMENTOS S.A. - INSTITUIÇÃO DE PAGAMENTO');
INSERT INTO `tb_bancos` (`ispb`, `codigo`, `descricao`, `descricao_completa`) VALUES ('21018182', 383, 'EBANX IP LTDA.', 'EBANX INSTITUICAO DE PAGAMENTOS LTDA.');
INSERT INTO `tb_bancos` (`ispb`, `codigo`, `descricao`, `descricao_completa`) VALUES ('21332862', 324, 'CARTOS SCD S.A.', 'CARTOS SOCIEDADE DE CRÉDITO DIRETO S.A.');
INSERT INTO `tb_bancos` (`ispb`, `codigo`, `descricao`, `descricao_completa`) VALUES ('22610500', 310, 'VORTX DTVM LTDA.', 'VORTX DISTRIBUIDORA DE TITULOS E VALORES MOBILIARIOS LTDA.');
INSERT INTO `tb_bancos` (`ispb`, `codigo`, `descricao`, `descricao_completa`) VALUES ('23862762', 280, 'WILL FINANCEIRA S.A.CFI', 'WILL FINANCEIRA S.A. CRÉDITO, FINANCIAMENTO E INVESTIMENTO');
INSERT INTO `tb_bancos` (`ispb`, `codigo`, `descricao`, `descricao_completa`) VALUES ('24537861', 343, 'FFA SCMEPP LTDA.', 'FFA SOCIEDADE DE CRÉDITO AO MICROEMPREENDEDOR E À EMPRESA DE PEQUENO PORTE LTDA.');
INSERT INTO `tb_bancos` (`ispb`, `codigo`, `descricao`, `descricao_completa`) VALUES ('27098060', 335, 'BANCO DIGIO', 'Banco Digio S.A.');
INSERT INTO `tb_bancos` (`ispb`, `codigo`, `descricao`, `descricao_completa`) VALUES ('27214112', 349, 'AL5 S.A. CFI', 'AL5 S.A. CRÉDITO, FINANCIAMENTO E INVESTIMENTO');
INSERT INTO `tb_bancos` (`ispb`, `codigo`, `descricao`, `descricao_completa`) VALUES ('27302181', 427, 'CRED-UFES', 'COOPERATIVA DE CREDITO DOS SERVIDORES DA UNIVERSIDADE FEDERAL DO ESPIRITO SANTO');
INSERT INTO `tb_bancos` (`ispb`, `codigo`, `descricao`, `descricao_completa`) VALUES ('27351731', 374, 'REALIZE CFI S.A.', 'REALIZE CRÉDITO, FINANCIAMENTO E INVESTIMENTO S.A.');
INSERT INTO `tb_bancos` (`ispb`, `codigo`, `descricao`, `descricao_completa`) VALUES ('28127603', 21, 'BCO BANESTES S.A.', 'BANESTES S.A. BANCO DO ESTADO DO ESPIRITO SANTO');
INSERT INTO `tb_bancos` (`ispb`, `codigo`, `descricao`, `descricao_completa`) VALUES ('28195667', 246, 'BCO ABC BRASIL S.A.', 'Banco ABC Brasil S.A.');
INSERT INTO `tb_bancos` (`ispb`, `codigo`, `descricao`, `descricao_completa`) VALUES ('29030467', 751, 'SCOTIABANK BRASIL', 'Scotiabank Brasil S.A. Banco Múltiplo');
INSERT INTO `tb_bancos` (`ispb`, `codigo`, `descricao`, `descricao_completa`) VALUES ('30306294', 208, 'BANCO BTG PACTUAL S.A.', 'Banco BTG Pactual S.A.');
INSERT INTO `tb_bancos` (`ispb`, `codigo`, `descricao`, `descricao_completa`) VALUES ('30680829', 386, 'NU FINANCEIRA S.A. CFI', 'NU FINANCEIRA S.A. - Sociedade de Crédito, Financiamento e Investimento');
INSERT INTO `tb_bancos` (`ispb`, `codigo`, `descricao`, `descricao_completa`) VALUES ('30723886', 746, 'BCO MODAL S.A.', 'Banco Modal S.A.');
INSERT INTO `tb_bancos` (`ispb`, `codigo`, `descricao`, `descricao_completa`) VALUES ('31597552', 241, 'BCO CLASSICO S.A.', 'BANCO CLASSICO S.A.');
INSERT INTO `tb_bancos` (`ispb`, `codigo`, `descricao`, `descricao_completa`) VALUES ('31872495', 336, 'BCO C6 S.A.', 'Banco C6 S.A.');
INSERT INTO `tb_bancos` (`ispb`, `codigo`, `descricao`, `descricao_completa`) VALUES ('31880826', 612, 'BCO GUANABARA S.A.', 'Banco Guanabara S.A.');
INSERT INTO `tb_bancos` (`ispb`, `codigo`, `descricao`, `descricao_completa`) VALUES ('31895683', 604, 'BCO INDUSTRIAL DO BRASIL S.A.', 'Banco Industrial do Brasil S.A.');
INSERT INTO `tb_bancos` (`ispb`, `codigo`, `descricao`, `descricao_completa`) VALUES ('32062580', 505, 'BCO CREDIT SUISSE S.A.', 'Banco Credit Suisse (Brasil) S.A.');
INSERT INTO `tb_bancos` (`ispb`, `codigo`, `descricao`, `descricao_completa`) VALUES ('32402502', 329, 'QI SCD S.A.', 'QI Sociedade de Crédito Direto S.A.');
INSERT INTO `tb_bancos` (`ispb`, `codigo`, `descricao`, `descricao_completa`) VALUES ('32997490', 342, 'CREDITAS SCD', 'Creditas Sociedade de Crédito Direto S.A.');
INSERT INTO `tb_bancos` (`ispb`, `codigo`, `descricao`, `descricao_completa`) VALUES ('33042151', 300, 'BCO LA NACION ARGENTINA', 'Banco de la Nacion Argentina');
INSERT INTO `tb_bancos` (`ispb`, `codigo`, `descricao`, `descricao_completa`) VALUES ('33042953', 477, 'CITIBANK N.A.', 'Citibank N.A.');
INSERT INTO `tb_bancos` (`ispb`, `codigo`, `descricao`, `descricao_completa`) VALUES ('33132044', 266, 'BCO CEDULA S.A.', 'BANCO CEDULA S.A.');
INSERT INTO `tb_bancos` (`ispb`, `codigo`, `descricao`, `descricao_completa`) VALUES ('33147315', 122, 'BCO BRADESCO BERJ S.A.', 'Banco Bradesco BERJ S.A.');
INSERT INTO `tb_bancos` (`ispb`, `codigo`, `descricao`, `descricao_completa`) VALUES ('33172537', 376, 'BCO J.P. MORGAN S.A.', 'BANCO J.P. MORGAN S.A.');
INSERT INTO `tb_bancos` (`ispb`, `codigo`, `descricao`, `descricao_completa`) VALUES ('33264668', 348, 'BCO XP S.A.', 'Banco XP S.A.');
INSERT INTO `tb_bancos` (`ispb`, `codigo`, `descricao`, `descricao_completa`) VALUES ('33466988', 473, 'BCO CAIXA GERAL BRASIL S.A.', 'Banco Caixa Geral - Brasil S.A.');
INSERT INTO `tb_bancos` (`ispb`, `codigo`, `descricao`, `descricao_completa`) VALUES ('33479023', 745, 'BCO CITIBANK S.A.', 'Banco Citibank S.A.');
INSERT INTO `tb_bancos` (`ispb`, `codigo`, `descricao`, `descricao_completa`) VALUES ('33603457', 120, 'BCO RODOBENS S.A.', 'BANCO RODOBENS S.A.');
INSERT INTO `tb_bancos` (`ispb`, `codigo`, `descricao`, `descricao_completa`) VALUES ('33644196', 265, 'BCO FATOR S.A.', 'Banco Fator S.A.');
INSERT INTO `tb_bancos` (`ispb`, `codigo`, `descricao`, `descricao_completa`) VALUES ('33657248', 7, 'BNDES', 'BANCO NACIONAL DE DESENVOLVIMENTO ECONOMICO E SOCIAL');
INSERT INTO `tb_bancos` (`ispb`, `codigo`, `descricao`, `descricao_completa`) VALUES ('33885724', 29, 'BANCO ITAÚ CONSIGNADO S.A.', 'Banco Itaú Consignado S.A.');
INSERT INTO `tb_bancos` (`ispb`, `codigo`, `descricao`, `descricao_completa`) VALUES ('33923798', 243, 'BANCO MASTER', 'BANCO MASTER S/A');
INSERT INTO `tb_bancos` (`ispb`, `codigo`, `descricao`, `descricao_completa`) VALUES ('34088029', 397, 'LISTO SCD S.A.', 'LISTO SOCIEDADE DE CREDITO DIRETO S.A.');
INSERT INTO `tb_bancos` (`ispb`, `codigo`, `descricao`, `descricao_completa`) VALUES ('34111187', 78, 'HAITONG BI DO BRASIL S.A.', 'Haitong Banco de Investimento do Brasil S.A.');
INSERT INTO `tb_bancos` (`ispb`, `codigo`, `descricao`, `descricao_completa`) VALUES ('34335592', 355, 'ÓTIMO SCD S.A.', 'ÓTIMO SOCIEDADE DE CRÉDITO DIRETO S.A.');
INSERT INTO `tb_bancos` (`ispb`, `codigo`, `descricao`, `descricao_completa`) VALUES ('35551187', 445, 'PLANTAE CFI', 'PLANTAE S.A. - CRÉDITO, FINANCIAMENTO E INVESTIMENTO');
INSERT INTO `tb_bancos` (`ispb`, `codigo`, `descricao`, `descricao_completa`) VALUES ('35977097', 373, 'UP.P SEP S.A.', 'UP.P SOCIEDADE DE EMPRÉSTIMO ENTRE PESSOAS S.A.');
INSERT INTO `tb_bancos` (`ispb`, `codigo`, `descricao`, `descricao_completa`) VALUES ('36583700', 516, 'QISTA S.A. CFI', 'QISTA S.A. - CRÉDITO, FINANCIAMENTO E INVESTIMENTO');
INSERT INTO `tb_bancos` (`ispb`, `codigo`, `descricao`, `descricao_completa`) VALUES ('36586946', 408, 'BONUSPAGO SCD S.A.', 'BONUSPAGO SOCIEDADE DE CRÉDITO DIRETO S.A.');
INSERT INTO `tb_bancos` (`ispb`, `codigo`, `descricao`, `descricao_completa`) VALUES ('36947229', 402, 'COBUCCIO S.A. SCFI', 'COBUCCIO S/A - SOCIEDADE DE CRÉDITO, FINANCIAMENTO E INVESTIMENTOS');
INSERT INTO `tb_bancos` (`ispb`, `codigo`, `descricao`, `descricao_completa`) VALUES ('37229413', 507, 'SCFI EFÍ S.A.', 'SOCIEDADE DE CRÉDITO, FINANCIAMENTO E INVESTIMENTO EFÍ S.A.');
INSERT INTO `tb_bancos` (`ispb`, `codigo`, `descricao`, `descricao_completa`) VALUES ('37241230', 404, 'SUMUP SCD S.A.', 'SUMUP SOCIEDADE DE CRÉDITO DIRETO S.A.');
INSERT INTO `tb_bancos` (`ispb`, `codigo`, `descricao`, `descricao_completa`) VALUES ('37414009', 418, 'ZIPDIN SCD S.A.', 'ZIPDIN SOLUÇÕES DIGITAIS SOCIEDADE DE CRÉDITO DIRETO S/A');
INSERT INTO `tb_bancos` (`ispb`, `codigo`, `descricao`, `descricao_completa`) VALUES ('37526080', 414, 'LEND SCD S.A.', 'LEND SOCIEDADE DE CRÉDITO DIRETO S.A.');
INSERT INTO `tb_bancos` (`ispb`, `codigo`, `descricao`, `descricao_completa`) VALUES ('37555231', 449, 'DM', 'DM SOCIEDADE DE CRÉDITO DIRETO S.A.');
INSERT INTO `tb_bancos` (`ispb`, `codigo`, `descricao`, `descricao_completa`) VALUES ('37679449', 518, 'MERCADO CRÉDITO SCFI S.A.', 'MERCADO CRÉDITO SOCIEDADE DE CRÉDITO, FINANCIAMENTO E INVESTIMENTO S.A.');
INSERT INTO `tb_bancos` (`ispb`, `codigo`, `descricao`, `descricao_completa`) VALUES ('37715993', 406, 'ACCREDITO SCD S.A.', 'ACCREDITO - SOCIEDADE DE CRÉDITO DIRETO S.A.');
INSERT INTO `tb_bancos` (`ispb`, `codigo`, `descricao`, `descricao_completa`) VALUES ('37880206', 403, 'CORA SCD S.A.', 'CORA SOCIEDADE DE CRÉDITO DIRETO S.A.');
INSERT INTO `tb_bancos` (`ispb`, `codigo`, `descricao`, `descricao_completa`) VALUES ('38129006', 419, 'NUMBRS SCD S.A.', 'NUMBRS SOCIEDADE DE CRÉDITO DIRETO S.A.');
INSERT INTO `tb_bancos` (`ispb`, `codigo`, `descricao`, `descricao_completa`) VALUES ('38224857', 435, 'DELCRED SCD S.A.', 'DELCRED SOCIEDADE DE CRÉDITO DIRETO S.A.');
INSERT INTO `tb_bancos` (`ispb`, `codigo`, `descricao`, `descricao_completa`) VALUES ('39416705', 443, 'CREDIHOME SCD', 'CREDIHOME SOCIEDADE DE CRÉDITO DIRETO S.A.');
INSERT INTO `tb_bancos` (`ispb`, `codigo`, `descricao`, `descricao_completa`) VALUES ('39519944', 535, 'MARU SCD S.A.', 'MARÚ SOCIEDADE DE CRÉDITO DIRETO S.A.');
INSERT INTO `tb_bancos` (`ispb`, `codigo`, `descricao`, `descricao_completa`) VALUES ('39587424', 457, 'UY3 SCD S/A', 'UY3 SOCIEDADE DE CRÉDITO DIRETO S/A');
INSERT INTO `tb_bancos` (`ispb`, `codigo`, `descricao`, `descricao_completa`) VALUES ('39664698', 428, 'CREDSYSTEM SCD S.A.', 'CREDSYSTEM SOCIEDADE DE CRÉDITO DIRETO S.A.');
INSERT INTO `tb_bancos` (`ispb`, `codigo`, `descricao`, `descricao_completa`) VALUES ('39676772', 452, 'CREDIFIT SCD S.A.', 'CREDIFIT SOCIEDADE DE CRÉDITO DIRETO S.A.');
INSERT INTO `tb_bancos` (`ispb`, `codigo`, `descricao`, `descricao_completa`) VALUES ('39738065', 510, 'FFCRED SCD S.A.', 'FFCRED SOCIEDADE DE CRÉDITO DIRETO S.A..');
INSERT INTO `tb_bancos` (`ispb`, `codigo`, `descricao`, `descricao_completa`) VALUES ('39908427', 462, 'STARK SCD S.A.', 'STARK SOCIEDADE DE CRÉDITO DIRETO S.A.');
INSERT INTO `tb_bancos` (`ispb`, `codigo`, `descricao`, `descricao_completa`) VALUES ('40083667', 465, 'CAPITAL CONSIG SCD S.A.', 'CAPITAL CONSIG SOCIEDADE DE CRÉDITO DIRETO S.A.');
INSERT INTO `tb_bancos` (`ispb`, `codigo`, `descricao`, `descricao_completa`) VALUES ('40303299', 306, 'PORTOPAR DTVM LTDA', 'PORTOPAR DISTRIBUIDORA DE TITULOS E VALORES MOBILIARIOS LTDA.');
INSERT INTO `tb_bancos` (`ispb`, `codigo`, `descricao`, `descricao_completa`) VALUES ('40475846', 451, 'J17 - SCD S/A', 'J17 - SOCIEDADE DE CRÉDITO DIRETO S/A');
INSERT INTO `tb_bancos` (`ispb`, `codigo`, `descricao`, `descricao_completa`) VALUES ('40654622', 444, 'TRINUS SCD S.A.', 'TRINUS SOCIEDADE DE CRÉDITO DIRETO S.A.');
INSERT INTO `tb_bancos` (`ispb`, `codigo`, `descricao`, `descricao_completa`) VALUES ('42047025', 460, 'UNAVANTI SCD S/A', 'UNAVANTI SOCIEDADE DE CRÉDITO DIRETO S/A');
INSERT INTO `tb_bancos` (`ispb`, `codigo`, `descricao`, `descricao_completa`) VALUES ('42259084', 482, 'SBCASH SCD', 'SBCASH SOCIEDADE DE CRÉDITO DIRETO S.A.');
INSERT INTO `tb_bancos` (`ispb`, `codigo`, `descricao`, `descricao_completa`) VALUES ('42272526', 17, 'BNY MELLON BCO S.A.', 'BNY Mellon Banco S.A.');
INSERT INTO `tb_bancos` (`ispb`, `codigo`, `descricao`, `descricao_completa`) VALUES ('43180355', 174, 'PEFISA S.A. - C.F.I.', 'PEFISA S.A. - CRÉDITO, FINANCIAMENTO E INVESTIMENTO');
INSERT INTO `tb_bancos` (`ispb`, `codigo`, `descricao`, `descricao_completa`) VALUES ('43599047', 481, 'SUPERLÓGICA SCD S.A.', 'SUPERLÓGICA SOCIEDADE DE CRÉDITO DIRETO S.A.');
INSERT INTO `tb_bancos` (`ispb`, `codigo`, `descricao`, `descricao_completa`) VALUES ('44019481', 521, 'PEAK SEP S.A.', 'PEAK SOCIEDADE DE EMPRÉSTIMO ENTRE PESSOAS S.A.');
INSERT INTO `tb_bancos` (`ispb`, `codigo`, `descricao`, `descricao_completa`) VALUES ('44189447', 495, 'BCO LA PROVINCIA B AIRES BCE', 'Banco de La Provincia de Buenos Aires');
INSERT INTO `tb_bancos` (`ispb`, `codigo`, `descricao`, `descricao_completa`) VALUES ('44292580', 523, 'HR DIGITAL SCD', 'HR DIGITAL - SOCIEDADE DE CRÉDITO DIRETO S/A');
INSERT INTO `tb_bancos` (`ispb`, `codigo`, `descricao`, `descricao_completa`) VALUES ('44478623', 527, 'ATICCA SCD S.A.', 'ATICCA - SOCIEDADE DE CRÉDITO DIRETO S.A.');
INSERT INTO `tb_bancos` (`ispb`, `codigo`, `descricao`, `descricao_completa`) VALUES ('44683140', 511, 'MAGNUM SCD', 'MAGNUM SOCIEDADE DE CRÉDITO DIRETO S.A.');
INSERT INTO `tb_bancos` (`ispb`, `codigo`, `descricao`, `descricao_completa`) VALUES ('44728700', 513, 'ATF CREDIT SCD S.A.', 'ATF CREDIT SOCIEDADE DE CRÉDITO DIRETO S.A.');
INSERT INTO `tb_bancos` (`ispb`, `codigo`, `descricao`, `descricao_completa`) VALUES ('45246410', 125, 'BANCO GENIAL', 'BANCO GENIAL S.A.');
INSERT INTO `tb_bancos` (`ispb`, `codigo`, `descricao`, `descricao_completa`) VALUES ('45745537', 532, 'EAGLE SCD S.A.', 'EAGLE SOCIEDADE DE CRÉDITO DIRETO S.A.');
INSERT INTO `tb_bancos` (`ispb`, `codigo`, `descricao`, `descricao_completa`) VALUES ('45756448', 537, 'MICROCASH SCMEPP LTDA.', 'MICROCASH SOCIEDADE DE CRÉDITO AO MICROEMPREENDEDOR E À EMPRESA DE PEQUENO PORTE');
INSERT INTO `tb_bancos` (`ispb`, `codigo`, `descricao`, `descricao_completa`) VALUES ('46026562', 526, 'MONETARIE SCD', 'MONETARIE SOCIEDADE DE CRÉDITO DIRETO S.A.');
INSERT INTO `tb_bancos` (`ispb`, `codigo`, `descricao`, `descricao_completa`) VALUES ('46518205', 488, 'JPMORGAN CHASE BANK', 'JPMorgan Chase Bank, National Association');
INSERT INTO `tb_bancos` (`ispb`, `codigo`, `descricao`, `descricao_completa`) VALUES ('47593544', 522, 'RED SCD S.A.', 'RED SOCIEDADE DE CRÉDITO DIRETO S.A.');
INSERT INTO `tb_bancos` (`ispb`, `codigo`, `descricao`, `descricao_completa`) VALUES ('47873449', 530, 'SER FINANCE SCD S.A.', 'SER FINANCE SOCIEDADE DE CRÉDITO DIRETO S.A.');
INSERT INTO `tb_bancos` (`ispb`, `codigo`, `descricao`, `descricao_completa`) VALUES ('48795256', 65, 'BCO ANDBANK S.A.', 'Banco AndBank (Brasil) S.A.');
INSERT INTO `tb_bancos` (`ispb`, `codigo`, `descricao`, `descricao_completa`) VALUES ('50585090', 250, 'BCV - BCO, CRÉDITO E VAREJO S.A.', 'BCV - BANCO DE CRÉDITO E VAREJO S.A.');
INSERT INTO `tb_bancos` (`ispb`, `codigo`, `descricao`, `descricao_completa`) VALUES ('53518684', 269, 'BCO HSBC S.A.', 'BANCO HSBC S.A.');
INSERT INTO `tb_bancos` (`ispb`, `codigo`, `descricao`, `descricao_completa`) VALUES ('54403563', 213, 'BCO ARBI S.A.', 'Banco Arbi S.A.');
INSERT INTO `tb_bancos` (`ispb`, `codigo`, `descricao`, `descricao_completa`) VALUES ('55230916', 139, 'INTESA SANPAOLO BRASIL S.A. BM', 'Intesa Sanpaolo Brasil S.A. - Banco Múltiplo');
INSERT INTO `tb_bancos` (`ispb`, `codigo`, `descricao`, `descricao_completa`) VALUES ('57839805', 18, 'BCO TRICURY S.A.', 'Banco Tricury S.A.');
INSERT INTO `tb_bancos` (`ispb`, `codigo`, `descricao`, `descricao_completa`) VALUES ('58160789', 422, 'BCO SAFRA S.A.', 'Banco Safra S.A.');
INSERT INTO `tb_bancos` (`ispb`, `codigo`, `descricao`, `descricao_completa`) VALUES ('58497702', 630, 'BCO LETSBANK S.A.', 'BANCO LETSBANK S.A.');
INSERT INTO `tb_bancos` (`ispb`, `codigo`, `descricao`, `descricao_completa`) VALUES ('58616418', 224, 'BCO FIBRA S.A.', 'Banco Fibra S.A.');
INSERT INTO `tb_bancos` (`ispb`, `codigo`, `descricao`, `descricao_completa`) VALUES ('59109165', 393, 'BCO VOLKSWAGEN S.A', 'Banco Volkswagen S.A.');
INSERT INTO `tb_bancos` (`ispb`, `codigo`, `descricao`, `descricao_completa`) VALUES ('59118133', 600, 'BCO LUSO BRASILEIRO S.A.', 'Banco Luso Brasileiro S.A.');
INSERT INTO `tb_bancos` (`ispb`, `codigo`, `descricao`, `descricao_completa`) VALUES ('59274605', 390, 'BCO GM S.A.', 'BANCO GM S.A.');
INSERT INTO `tb_bancos` (`ispb`, `codigo`, `descricao`, `descricao_completa`) VALUES ('59285411', 623, 'BANCO PAN', 'Banco Pan S.A.');
INSERT INTO `tb_bancos` (`ispb`, `codigo`, `descricao`, `descricao_completa`) VALUES ('59588111', 655, 'BCO VOTORANTIM S.A.', 'Banco Votorantim S.A.');
INSERT INTO `tb_bancos` (`ispb`, `codigo`, `descricao`, `descricao_completa`) VALUES ('60394079', 479, 'BCO ITAUBANK S.A.', 'Banco ItauBank S.A.');
INSERT INTO `tb_bancos` (`ispb`, `codigo`, `descricao`, `descricao_completa`) VALUES ('60498557', 456, 'BCO MUFG BRASIL S.A.', 'Banco MUFG Brasil S.A.');
INSERT INTO `tb_bancos` (`ispb`, `codigo`, `descricao`, `descricao_completa`) VALUES ('60518222', 464, 'BCO SUMITOMO MITSUI BRASIL S.A.', 'Banco Sumitomo Mitsui Brasileiro S.A.');
INSERT INTO `tb_bancos` (`ispb`, `codigo`, `descricao`, `descricao_completa`) VALUES ('60701190', 341, 'ITAÚ UNIBANCO S.A.', 'ITAÚ UNIBANCO S.A.');
INSERT INTO `tb_bancos` (`ispb`, `codigo`, `descricao`, `descricao_completa`) VALUES ('60746948', 237, 'BCO BRADESCO S.A.', 'Banco Bradesco S.A.');
INSERT INTO `tb_bancos` (`ispb`, `codigo`, `descricao`, `descricao_completa`) VALUES ('60814191', 381, 'BCO MERCEDES-BENZ S.A.', 'BANCO MERCEDES-BENZ DO BRASIL S.A.');
INSERT INTO `tb_bancos` (`ispb`, `codigo`, `descricao`, `descricao_completa`) VALUES ('60850229', 613, 'OMNI BANCO S.A.', 'Omni Banco S.A.');
INSERT INTO `tb_bancos` (`ispb`, `codigo`, `descricao`, `descricao_completa`) VALUES ('60889128', 637, 'BCO SOFISA S.A.', 'BANCO SOFISA S.A.');
INSERT INTO `tb_bancos` (`ispb`, `codigo`, `descricao`, `descricao_completa`) VALUES ('61024352', 653, 'BANCO VOITER', 'BANCO VOITER S.A.');
INSERT INTO `tb_bancos` (`ispb`, `codigo`, `descricao`, `descricao_completa`) VALUES ('61033106', 69, 'BCO CREFISA S.A.', 'Banco Crefisa S.A.');
INSERT INTO `tb_bancos` (`ispb`, `codigo`, `descricao`, `descricao_completa`) VALUES ('61088183', 370, 'BCO MIZUHO S.A.', 'Banco Mizuho do Brasil S.A.');
INSERT INTO `tb_bancos` (`ispb`, `codigo`, `descricao`, `descricao_completa`) VALUES ('61182408', 249, 'BANCO INVESTCRED UNIBANCO S.A.', 'Banco Investcred Unibanco S.A.');
INSERT INTO `tb_bancos` (`ispb`, `codigo`, `descricao`, `descricao_completa`) VALUES ('61186680', 318, 'BCO BMG S.A.', 'Banco BMG S.A.');
INSERT INTO `tb_bancos` (`ispb`, `codigo`, `descricao`, `descricao_completa`) VALUES ('61348538', 626, 'BCO C6 CONSIG', 'BANCO C6 CONSIGNADO S.A.');
INSERT INTO `tb_bancos` (`ispb`, `codigo`, `descricao`, `descricao_completa`) VALUES ('61533584', 366, 'BCO SOCIETE GENERALE BRASIL', 'BANCO SOCIETE GENERALE BRASIL S.A.');
INSERT INTO `tb_bancos` (`ispb`, `codigo`, `descricao`, `descricao_completa`) VALUES ('61820817', 611, 'BCO PAULISTA S.A.', 'Banco Paulista S.A.');
INSERT INTO `tb_bancos` (`ispb`, `codigo`, `descricao`, `descricao_completa`) VALUES ('62073200', 755, 'BOFA MERRILL LYNCH BM S.A.', 'Bank of America Merrill Lynch Banco Múltiplo S.A.');
INSERT INTO `tb_bancos` (`ispb`, `codigo`, `descricao`, `descricao_completa`) VALUES ('62144175', 643, 'BCO PINE S.A.', 'Banco Pine S.A.');
INSERT INTO `tb_bancos` (`ispb`, `codigo`, `descricao`, `descricao_completa`) VALUES ('62232889', 707, 'BCO DAYCOVAL S.A', 'Banco Daycoval S.A.');
INSERT INTO `tb_bancos` (`ispb`, `codigo`, `descricao`, `descricao_completa`) VALUES ('62331228', 487, 'DEUTSCHE BANK S.A.BCO ALEMAO', 'DEUTSCHE BANK S.A. - BANCO ALEMAO');
INSERT INTO `tb_bancos` (`ispb`, `codigo`, `descricao`, `descricao_completa`) VALUES ('62421979', 233, 'BANCO CIFRA', 'Banco Cifra S.A.');
INSERT INTO `tb_bancos` (`ispb`, `codigo`, `descricao`, `descricao_completa`) VALUES ('68900810', 633, 'BCO RENDIMENTO S.A.', 'Banco Rendimento S.A.');
INSERT INTO `tb_bancos` (`ispb`, `codigo`, `descricao`, `descricao_completa`) VALUES ('71027866', 218, 'BCO BS2 S.A.', 'Banco BS2 S.A.');
INSERT INTO `tb_bancos` (`ispb`, `codigo`, `descricao`, `descricao_completa`) VALUES ('74828799', 753, 'NOVO BCO CONTINENTAL S.A. - BM', 'Novo Banco Continental S.A. - Banco Múltiplo');
INSERT INTO `tb_bancos` (`ispb`, `codigo`, `descricao`, `descricao_completa`) VALUES ('75647891', 222, 'BCO CRÉDIT AGRICOLE BR S.A.', 'BANCO CRÉDIT AGRICOLE BRASIL S.A.');
INSERT INTO `tb_bancos` (`ispb`, `codigo`, `descricao`, `descricao_completa`) VALUES ('76543115', 754, 'BANCO SISTEMA', 'Banco Sistema S.A.');
INSERT INTO `tb_bancos` (`ispb`, `codigo`, `descricao`, `descricao_completa`) VALUES ('78626983', 610, 'BCO VR S.A.', 'Banco VR S.A.');
INSERT INTO `tb_bancos` (`ispb`, `codigo`, `descricao`, `descricao_completa`) VALUES ('78632767', 712, 'BCO OURINVEST S.A.', 'Banco Ourinvest S.A.');
INSERT INTO `tb_bancos` (`ispb`, `codigo`, `descricao`, `descricao_completa`) VALUES ('80271455', 720, 'BCO RNX S.A.', 'BANCO RNX S.A.');
INSERT INTO `tb_bancos` (`ispb`, `codigo`, `descricao`, `descricao_completa`) VALUES ('81723108', 10, 'CREDICOAMO', 'CREDICOAMO CREDITO RURAL COOPERATIVA');
INSERT INTO `tb_bancos` (`ispb`, `codigo`, `descricao`, `descricao_completa`) VALUES ('90400888', 33, 'BCO SANTANDER (BRASIL) S.A.', 'BANCO SANTANDER (BRASIL) S.A.');
INSERT INTO `tb_bancos` (`ispb`, `codigo`, `descricao`, `descricao_completa`) VALUES ('91884981', 217, 'BANCO JOHN DEERE S.A.', 'Banco John Deere S.A.');
INSERT INTO `tb_bancos` (`ispb`, `codigo`, `descricao`, `descricao_completa`) VALUES ('92702067', 41, 'BCO DO ESTADO DO RS S.A.', 'Banco do Estado do Rio Grande do Sul S.A.');
INSERT INTO `tb_bancos` (`ispb`, `codigo`, `descricao`, `descricao_completa`) VALUES ('92874270', 654, 'BCO DIGIMAIS S.A.', 'BANCO DIGIMAIS S.A.');
INSERT INTO `tb_bancos` (`ispb`, `codigo`, `descricao`, `descricao_completa`) VALUES ('92894922', 212, 'BANCO ORIGINAL', 'Banco Original S.A.');
INSERT INTO `tb_perguntas_aspectos` (`id`, `pergunta`, `grupo`, `opcoes`) VALUES (1, 'A execução obedece o projeto?', 'Projeto', 'Sim;Não');
INSERT INTO `tb_perguntas_aspectos` (`id`, `pergunta`, `grupo`, `opcoes`) VALUES (2, 'Houve modificação em alguma unidade?', 'Projeto', 'Sim;Não');
INSERT INTO `tb_perguntas_aspectos` (`id`, `pergunta`, `grupo`, `opcoes`) VALUES (3, 'Utilização de Equipamentos Individuais', 'Segurança', 'Sim;Não');
INSERT INTO `tb_perguntas_aspectos` (`id`, `pergunta`, `grupo`, `opcoes`) VALUES (4, 'Utilização de Equipamentos Coletivos', 'Segurança', 'Sim;Não');
INSERT INTO `tb_perguntas_aspectos` (`id`, `pergunta`, `grupo`, `opcoes`) VALUES (5, 'Estrutura (Prumo, presença de nichos)', 'Qualidade', 'Baixo;Normal;Bom');
INSERT INTO `tb_perguntas_aspectos` (`id`, `pergunta`, `grupo`, `opcoes`) VALUES (6, 'Paredes (Prumo, Alinhamento, Modulação e etc.)', 'Qualidade', 'Baixo;Normal;Bom');
INSERT INTO `tb_perguntas_aspectos` (`id`, `pergunta`, `grupo`, `opcoes`) VALUES (7, 'Instalações de Portas e Janelas', 'Qualidade', 'Baixo;Normal;Bom');
INSERT INTO `tb_perguntas_aspectos` (`id`, `pergunta`, `grupo`, `opcoes`) VALUES (8, 'Contrapiso', 'Qualidade', 'Baixo;Normal;Bom');
INSERT INTO `tb_perguntas_aspectos` (`id`, `pergunta`, `grupo`, `opcoes`) VALUES (9, 'Revestimento Interno', 'Qualidade', 'Baixo;Normal;Bom');
INSERT INTO `tb_perguntas_aspectos` (`id`, `pergunta`, `grupo`, `opcoes`) VALUES (10, 'Revestimento Externo', 'Qualidade', 'Baixo;Normal;Bom');
INSERT INTO `tb_perguntas_aspectos` (`id`, `pergunta`, `grupo`, `opcoes`) VALUES (11, 'Escadas', 'Qualidade', 'Baixo;Normal;Bom');
INSERT INTO `tb_perguntas_aspectos` (`id`, `pergunta`, `grupo`, `opcoes`) VALUES (12, 'Instalações Elétricas e Hidráulicas', 'Qualidade', 'Baixo;Normal;Bom');
INSERT INTO `tb_perguntas_aspectos` (`id`, `pergunta`, `grupo`, `opcoes`) VALUES (13, 'Forros', 'Qualidade', 'Baixo;Normal;Bom');
INSERT INTO `tb_perguntas_aspectos` (`id`, `pergunta`, `grupo`, `opcoes`) VALUES (14, 'Pintura', 'Qualidade', 'Baixo;Normal;Bom');
INSERT INTO `tb_perguntas_aspectos` (`id`, `pergunta`, `grupo`, `opcoes`) VALUES (15, 'Uso de Ferramentas adequadas ao serviço', 'Qualidade', 'Baixo;Normal;Bom');
INSERT INTO `tb_perguntas_aspectos` (`id`, `pergunta`, `grupo`, `opcoes`) VALUES (16, 'Planejamento', 'Qualidade', 'Baixo;Normal;Bom');
INSERT INTO `tb_perguntas_aspectos` (`id`, `pergunta`, `grupo`, `opcoes`) VALUES (17, 'Limpeza', 'Qualidade', 'Baixo;Normal;Bom');
INSERT INTO `tb_perguntas_aspectos` (`id`, `pergunta`, `grupo`, `opcoes`) VALUES (18, 'Logística de Canteiro', 'Qualidade', 'Baixo;Normal;Bom');
INSERT INTO `tb_perguntas_aspectos` (`id`, `pergunta`, `grupo`, `opcoes`) VALUES (19, 'Outro', 'Qualidade', 'Baixo;Normal;Bom');
INSERT INTO `tb_perguntas_aspectos` (`id`, `pergunta`, `grupo`, `opcoes`) VALUES (20, 'Quanto ao prazo a obra está', 'Situação', 'Adiantada;Atrasada;No prazo');

INSERT INTO `tb_usuarios` (`id_usuario`, `email`, `senha`, `tp_acesso`, `nm_usuario`, `cod_banco`) VALUES (1, 'adm@gfcpro.com.br', '$2b$06$S0KOp/YN3wdyzc6JlF68Eugmhjh5wIzLmO9PVDGtildPudAtsQqTq', 'RT', 'Renato Adriano', 0);

INSERT INTO db_gfc.tb_itens_produtos (id_cat,descricao,codigo,unidade,ativo) VALUES
	 (16,'Projeto arquitetônico de prefeitura',NULL,'vb',1),
	 (16,'Projeto arquitetônico execução',NULL,'vb',1),
	 (16,'Projeto de Geotecnia',NULL,'vb',1),
	 (16,'Projeto de Fundação',NULL,'vb',1),
	 (16,'Projeto de Estrutura',NULL,'vb',1),
	 (16,'Projeto de Instalações Prediais',NULL,'vb',1),
	 (16,'Projeto de Instalações Mecânicas',NULL,'vb',1),
	 (16,'Projeto de Incêndio',NULL,'vb',1),
	 (16,'Projeto de Custo de Construção (Orçamento)',NULL,'vb',1),
	 (16,'Consultoria em Tecnologia do Concreto',NULL,'vb',1);
INSERT INTO db_gfc.tb_itens_produtos (id_cat,descricao,codigo,unidade,ativo) VALUES
	 (16,'Consultoria de Fundações',NULL,'vb',1),
	 (16,'Consultoria de Esquadrias de Alumínio',NULL,'vb',1),
	 (16,'Laudo vistoria vizinhos',NULL,'vb',1),
	 (16,'PCMSO',NULL,'vb',1),
	 (16,'PPRA',NULL,'vb',1),
	 (16,'PCMAT',NULL,'vb',1),
	 (17,'TOPOGRAFO COM ENCARGOS COMPLEMENTARES',90781,'H',1),
	 (17,'TOPOGRAFO COM ENCARGOS COMPLEMENTARES',94296,'MES',1),
	 (17,'AUXILIAR DE TOPÓGRAFO COM ENCARGOS COMPLEMENTARES',88253,'H',1),
	 (17,'AUXILIAR DE TOPÓGRAFO COM ENCARGOS COMPLEMENTARES',101389,'MES',1);
INSERT INTO db_gfc.tb_itens_produtos (id_cat,descricao,codigo,unidade,ativo) VALUES
	 (17,'LIMPEZA MANUAL DE VEGETAÇÃO EM TERRENO COM ENXADA. AF_03/2024',98524,'M2',1),
	 (17,'Sondagem',NULL,'vb',1),
	 (18,'LOCAÇÃO CONVENCIONAL DE OBRA, UTILIZANDO GABARITO DE TÁBUAS CORRIDAS PONTALETADAS A CADA 1,50M - 2 UTILIZAÇÕES. AF_03/2024',105009,'M',1),
	 (18,'FORNECIMENTO E INSTALAÇÃO DE PLACA DE OBRA COM CHAPA GALVANIZADA E ESTRUTURA DE MADEIRA. AF_03/2022_PS',103689,'M2',1),
	 (18,'EXTINTOR DE INCÊNDIO PORTÁTIL COM CARGA DE CO2 DE 6 KG, CLASSE BC - FORNECIMENTO E INSTALAÇÃO. AF_10/2020_PE',101907,'UN',1),
	 (18,'EXTINTOR DE INCÊNDIO PORTÁTIL COM CARGA DE PQS DE 6 KG, CLASSE BC - FORNECIMENTO E INSTALAÇÃO. AF_10/2020_PE',101909,'UN',1),
	 (18,'EXTINTOR DE INCÊNDIO PORTÁTIL COM CARGA DE ÁGUA PRESSURIZADA DE 10 L, CLASSE A - FORNECIMENTO E INSTALAÇÃO. AF_10/2020_PE',101905,'UN',1),
	 (18,'FORNECIMENTO E INSTALAÇÃO DE PLACA DE SINALIZAÇÃO EM CHAPA DE ALUMÍNIO EM SUPORTE DE CONCRETO. AF_03/2022',103702,'M2',1),
	 (18,'KIT CAVALETE PARA MEDIÇÃO DE ÁGUA - ENTRADA PRINCIPAL, EM PVC 20 MM (1/2") - FORNECIMENTO E INSTALAÇÃO (EXCLUSIVE HIDRÔMETRO). AF_03/2024',95634,'UN',1),
	 (18,'Inst Prov Hidrômetro MAT MO',NULL,'vb',1);
INSERT INTO db_gfc.tb_itens_produtos (id_cat,descricao,codigo,unidade,ativo) VALUES
	 (18,'Inst Prov Entr Energia MAT MO',NULL,'vb',1),
	 (18,'Inst Prov Sanitários MAT MO',NULL,'vb',1),
	 (18,'Inst Prov Distribuição Obra MAT MO',NULL,'vb',1),
	 (19,'PAREDE DE MADEIRA COMPENSADA PARA CONSTRUÇÃO TEMPORÁRIA EM CHAPA SIMPLES, EXTERNA, COM ÁREA LÍQUIDA MAIOR OU IGUAL A 6 M², COM VÃO. AF_03/2024',98445,'M2',1),
	 (19,'PAREDE DE MADEIRA COMPENSADA PARA CONSTRUÇÃO TEMPORÁRIA EM CHAPA SIMPLES, EXTERNA, COM ÁREA LÍQUIDA MENOR QUE 6 M², COM VÃO. AF_03/2024',98446,'M2',1),
	 (19,'PAREDE DE MADEIRA COMPENSADA PARA CONSTRUÇÃO TEMPORÁRIA EM CHAPA SIMPLES, EXTERNA, SEM VÃO. AF_03/2024',98441,'M2',1),
	 (19,'PAREDE DE MADEIRA COMPENSADA PARA CONSTRUÇÃO TEMPORÁRIA EM CHAPA SIMPLES, INTERNA, COM ÁREA LÍQUIDA MAIOR OU IGUAL A 6 M², COM VÃO. AF_03/2024',98447,'M2',1),
	 (19,'PAREDE DE MADEIRA COMPENSADA PARA CONSTRUÇÃO TEMPORÁRIA EM CHAPA SIMPLES, INTERNA, COM ÁREA LÍQUIDA MENOR QUE 6 M², COM VÃO. AF_03/2024',98448,'M2',1),
	 (19,'PAREDE DE MADEIRA COMPENSADA PARA CONSTRUÇÃO TEMPORÁRIA EM CHAPA SIMPLES, INTERNA, SEM VÃO. AF_03/2024',98443,'M2',1),
	 (19,'TAPUME COM TELHA METÁLICA. AF_03/2024',98459,'M2',1);
INSERT INTO db_gfc.tb_itens_produtos (id_cat,descricao,codigo,unidade,ativo) VALUES
	 (19,'EXECUÇÃO DE PILARETES PARA TAPUMES E CONSTRUÇÕES TEMPORÁRIAS. AF_03/2024',105130,'M',1),
	 (19,'PISO PARA CONSTRUÇÃO TEMPORÁRIA EM MADEIRA, SEM REAPROVEITAMENTO. AF_03/2024',98460,'M2',1),
	 (19,'Mobiliario escritorio, bebedouro, computadores,etc',NULL,'vb',1),
	 (20,'SERRA CIRCULAR DE BANCADA COM MOTOR ELÉTRICO POTÊNCIA DE 5HP, COM COIFA PARA DISCO 10" - CHP DIURNO. AF_08/2015',91692,'CHP',1),
	 (20,'BETONEIRA CAPACIDADE NOMINAL DE 600 L, CAPACIDADE DE MISTURA 360 L, MOTOR ELÉTRICO TRIFÁSICO POTÊNCIA DE 4 CV, SEM CARREGADOR - CHP DIURNO. AF_05/2023',89225,'CHP',1),
	 (20,'FURADEIRA ELETROMAGNÉTICA, VELOCIDADE (SEM CARGA/ COM CARGA) 450/ 270 RPM, ESPESSURA MÁXIMA DA CHAPA A SER FURADA 50 MM, PORÇA DE ADESÃO MAGNÉTICA 17000 N, POTÊNCIA 1100 W, ALIMENTÇÃO 220 - 60 HZ, MONOFÁSICA - CHP DIURNO. AF_08/2019',102934,'CHP',1),
	 (20,'MINICARREGADEIRA SOBRE RODAS, POTÊNCIA LÍQUIDA DE 47 HP, CAPACIDADE NOMINAL DE OPERAÇÃO DE 646 KG - CHP DIURNO. AF_06/2015',90692,'CHP',1),
	 (20,'MINIESCAVADEIRA SOBRE ESTEIRAS, POTÊNCIA LÍQUIDA DE *30* HP, PESO OPERACIONAL DE *3.500* KG - CHP DIURNO. AF_04/2017',96245,'CHP',1),
	 (20,'MARTELETE OU ROMPEDOR PNEUMÁTICO MANUAL, 28 KG, COM SILENCIADOR - CHP DIURNO. AF_07/2016',5795,'CHP',1),
	 (20,'ESCAVADEIRA HIDRÁULICA DE BRAÇO LONGO (LONGO ALCANCE) SOBRE ESTEIRAS, CAÇAMBA 0,52 M3, PESO OPERACIONAL 24 T, POTÊNCIA LÍQUIDA 155 HP - CHP DIURNO. AF_06/2023',104716,'CHP',1);
INSERT INTO db_gfc.tb_itens_produtos (id_cat,descricao,codigo,unidade,ativo) VALUES
	 (20,'COMPACTADOR DE SOLOS DE PERCUSÃO (SOQUETE) COM MOTOR A GASOLINA, POTÊNCIA 3 CV - CHP DIURNO. AF_09/2016',95264,'CHP',1),
	 (20,'BOMBA SUBMERSÍVEL ELÉTRICA TRIFÁSICA, POTÊNCIA 2,96 HP, Ø ROTOR 144 MM SEMI-ABERTO, BOCAL DE SAÍDA Ø 2", HM/Q = 2 MCA / 38,8 M3/H A 28 MCA / 5 M3/H - CHP DIURNO. AF_06/2014',89021,'CHP',1),
	 (20,'MISTURADOR DE ARGAMASSA, EIXO HORIZONTAL, CAPACIDADE DE MISTURA 160 KG, MOTOR ELÉTRICO POTÊNCIA 3 CV - CHP DIURNO. AF_05/2023',88399,'CHP',1),
	 (20,'ASCENSÃO DE GRUA ASCENSIONAL. AF_03/2024',105110,'M',1),
	 (20,'ASCENSÃO E DESCIDA DE ELEVADOR DE CREMALHEIRA. AF_03/2024',105103,'M',1),
	 (20,'GRUA ASCENCIONAL, LANCA DE 42 M, CAPACIDADE DE 1,5 T A 30 M, ALTURA ATE 39 M - CHP DIURNO. AF_05/2023',95212,'CHP',1),
	 (20,'MONTAGEM E DESMONTAGEM DE GRUA ASCENSIONAL, UTILIZAÇÃO DE GUINDASTE DERRICK. AF_03/2024',105108,'UN',1),
	 (20,'MONTAGEM E DESMONTAGEM DE TRECHO INICIAL DE ELEVADOR DE CREMALHEIRA, CABINE DUPLA - EXCLUSO FUNDAÇÕES. AF_03/2024',105107,'UN',1),
	 (20,'MONTAGEM E DESMONTAGEM DE ANDAIME MODULAR FACHADEIRO, COM PISO METÁLICO, PARA EDIFÍCIOS COM MULTIPLOS PAVIMENTOS (EXCLUSIVE ANDAIME E LIMPEZA). AF_03/2024',97063,'M2',1),
	 (20,'Aluguel de Andaime Fachadeiro',NULL,'mês',1);
INSERT INTO db_gfc.tb_itens_produtos (id_cat,descricao,codigo,unidade,ativo) VALUES
	 (20,'Aluguel de Elevador Cremalheira',NULL,'mês',1),
	 (21,'Manutenção canteiro de obra.',NULL,'mês',1),
	 (21,'Carretos',NULL,'un/mês',1),
	 (21,'Retirada de entulho c/ caçamba.',NULL,'un',1),
	 (21,'Higiene de obra',NULL,'mês',1),
	 (21,'Medicamentos e Primeiros Socorros',NULL,'mês',1),
	 (21,'Plotagem.',NULL,'mês',1),
	 (21,'Despesas de deslocamento',NULL,'mês',1),
	 (21,'Limpeza Alojamento engenharia',NULL,'mês',1),
	 (21,'Limpeza alojamento encarregados',NULL,'mês',1);
INSERT INTO db_gfc.tb_itens_produtos (id_cat,descricao,codigo,unidade,ativo) VALUES
	 (21,'Mobiliário Alojamento',NULL,'vb',1),
	 (21,'Consumo de água/esgoto',NULL,'mês',1),
	 (21,'Consumo de luz',NULL,'mês',1),
	 (21,'Consumo de telefone e internet',NULL,'mês',1),
	 (21,'Seguro de obra (0,2% custo raso)',NULL,'vb',1),
	 (21,'Despesas com vizinhos',NULL,'vb',1),
	 (21,'Despesas c/ Combustivel',NULL,'mês',1),
	 (21,'Material de escritório',NULL,'mês',1),
	 (21,'Caixinha da obra',NULL,'mês',1),
	 (21,'Fumacê',NULL,'un',1);
INSERT INTO db_gfc.tb_itens_produtos (id_cat,descricao,codigo,unidade,ativo) VALUES
	 (21,'Fumacê',NULL,'un',1),
	 (21,'Laudo de Potabilidade de Água',NULL,'un',1),
	 (21,'Dedetização contra carrapatos',NULL,'m²',1),
	 (21,'Dedetização/ Desratização',NULL,'mês',1),
	 (22,'ENGENHEIRO CIVIL DE OBRA JUNIOR COM ENCARGOS COMPLEMENTARES',90777,'H',1),
	 (22,'ENGENHEIRO CIVIL DE OBRA JUNIOR COM ENCARGOS COMPLEMENTARES',93565,'MES',1),
	 (22,'ENGENHEIRO CIVIL DE OBRA PLENO COM ENCARGOS COMPLEMENTARES',90778,'H',1),
	 (22,'ENGENHEIRO CIVIL DE OBRA PLENO COM ENCARGOS COMPLEMENTARES',93567,'MES',1),
	 (22,'ENGENHEIRO CIVIL DE OBRA SENIOR COM ENCARGOS COMPLEMENTARES',90779,'H',1),
	 (22,'ENGENHEIRO CIVIL DE OBRA SENIOR COM ENCARGOS COMPLEMENTARES',93568,'MES',1);
INSERT INTO db_gfc.tb_itens_produtos (id_cat,descricao,codigo,unidade,ativo) VALUES
	 (22,'MESTRE DE OBRAS COM ENCARGOS COMPLEMENTARES',94295,'MES',1),
	 (22,'ALMOXARIFE COM ENCARGOS COMPLEMENTARES',93563,'MES',1),
	 (22,'ENCARREGADO GERAL DE OBRAS COM ENCARGOS COMPLEMENTARES',93572,'MES',1),
	 (22,'OPERADOR DE BETONEIRA ESTACIONÁRIA COM ENCARGOS COMPLEMENTARES',101428,'MES',1),
	 (22,'OPERADOR DE GUINCHO OU GUINCHEIRO COM ENCARGOS COMPLEMENTARES',101432,'MES',1),
	 (22,'PEDREIRO COM ENCARGOS COMPLEMENTARES',101445,'MES',1),
	 (22,'SERVENTE DE OBRAS COM ENCARGOS COMPLEMENTARES',101452,'MES',1),
	 (22,'TECNICO DE EDIFICACOES COM ENCARGOS COMPLEMENTARES',100534,'MES',1),
	 (22,'APONTADOR OU APROPRIADOR COM ENCARGOS COMPLEMENTARES',93564,'MES',1),
	 (22,'AUXILIAR DE ESCRITORIO COM ENCARGOS COMPLEMENTARES',93566,'MES',1);
INSERT INTO db_gfc.tb_itens_produtos (id_cat,descricao,codigo,unidade,ativo) VALUES
	 (22,'CARPINTEIRO DE FORMAS COM ENCARGOS COMPLEMENTARES',101397,'MES',1),
	 (22,'Estagiário',NULL,'mês',1),
	 (22,'Hora Extra',NULL,'vb',1),
	 (23,'PLATAFORMA DE PROTEÇÃO PRINCIPAL (PRIMÁRIA) PARA COLETA DE RESÍDUOS COM ESTRUTURA METÁLICA E FORRAÇÃO EM TÁBUA DE MADEIRA SERRADA - 1 MONTAGEM POR OBRA. AF_03/2024',96997,'M',1),
	 (23,'PLATAFORMA DE PROTEÇÃO SECUNDÁRIA PARA COLETA DE RESÍDUOS COM ESTRUTURA METÁLICA E FORRAÇÃO EM TÁBUA DE MADEIRA SERRADA - 1 MONTAGEM POR OBRA. AF_03/2024',97001,'M',1),
	 (23,'LINHA DE VIDA TIPO VARAL DE SEGURANÇA COM CABO DE AÇO PARA PROTEÇÃO DE PERIFERIA PARA EDIFÍCIOS ACIMA DE 8 PAVIMENTOS. AF_03/2024',97045,'M',1),
	 (23,'LINHA DE VIDA TIPO VARAL DE SEGURANÇA COM CABO DE AÇO PARA PROTEÇÃO DE PERIFERIA PARA EDIFÍCIOS DE 5 A 8 PAVIMENTOS. AF_03/2024',97044,'M',1),
	 (23,'GUARDA-CORPO EM LAJE PÓS-DESFÔRMA COM ESCORAS DE MADEIRA ESTRONCADAS NA ESTRUTURA, TRAVESSÕES DE MADEIRA E FECHAMENTO EM TELA DE POLIPROPILENO PARA EDIFÍCIOS ACIMA DE 4 PAVIMENTOS (2 MONTAGENS). AF_03/2024',97032,'M',1),
	 (23,'INSTALAÇÃO DE GAMBIARRA PARA SINALIZAÇÃO, INCLUINDO LÂMPADA, E SINALIZADOR. AF_03/2024',97052,'UN',1),
	 (23,'COLOCAÇÃO DE TELA FACHADEIRA PERIMETRAL. AF_03/2024',97061,'M2',1);
INSERT INTO db_gfc.tb_itens_produtos (id_cat,descricao,codigo,unidade,ativo) VALUES
	 (24,'ENGENHEIRO CIVIL DE OBRA JUNIOR COM ENCARGOS COMPLEMENTARES',90777,'H',1),
	 (24,'ENGENHEIRO CIVIL DE OBRA JUNIOR COM ENCARGOS COMPLEMENTARES',93565,'MES',1),
	 (24,'ENGENHEIRO CIVIL DE OBRA PLENO COM ENCARGOS COMPLEMENTARES',90778,'H',1),
	 (24,'ENGENHEIRO CIVIL DE OBRA PLENO COM ENCARGOS COMPLEMENTARES',93567,'MES',1),
	 (24,'ENGENHEIRO CIVIL DE OBRA SENIOR COM ENCARGOS COMPLEMENTARES',90779,'H',1),
	 (24,'ENGENHEIRO CIVIL DE OBRA SENIOR COM ENCARGOS COMPLEMENTARES',93568,'MES',1),
	 (24,'MESTRE DE OBRAS COM ENCARGOS COMPLEMENTARES',94295,'MES',1),
	 (24,'ALMOXARIFE COM ENCARGOS COMPLEMENTARES',93563,'MES',1),
	 (24,'ENCARREGADO GERAL DE OBRAS COM ENCARGOS COMPLEMENTARES',93572,'MES',1),
	 (24,'OPERADOR DE BETONEIRA ESTACIONÁRIA COM ENCARGOS COMPLEMENTARES',101428,'MES',1);
INSERT INTO db_gfc.tb_itens_produtos (id_cat,descricao,codigo,unidade,ativo) VALUES
	 (24,'OPERADOR DE GUINCHO OU GUINCHEIRO COM ENCARGOS COMPLEMENTARES',101432,'MES',1),
	 (24,'PEDREIRO COM ENCARGOS COMPLEMENTARES',101445,'MES',1),
	 (24,'SERVENTE DE OBRAS COM ENCARGOS COMPLEMENTARES',101452,'MES',1),
	 (24,'TECNICO DE EDIFICACOES COM ENCARGOS COMPLEMENTARES',100534,'MES',1),
	 (24,'APONTADOR OU APROPRIADOR COM ENCARGOS COMPLEMENTARES',93564,'MES',1),
	 (24,'AUXILIAR DE ESCRITORIO COM ENCARGOS COMPLEMENTARES',93566,'MES',1),
	 (24,'CARPINTEIRO DE FORMAS COM ENCARGOS COMPLEMENTARES',101397,'MES',1),
	 (24,'Estagiário',NULL,'mês',1),
	 (25,'Ensaio de Compressão - Argamassa de assentamento',NULL,'vb',1),
	 (25,'Controle Tecnológico - Implant. E Coleta',NULL,'vb',1);
INSERT INTO db_gfc.tb_itens_produtos (id_cat,descricao,codigo,unidade,ativo) VALUES
	 (25,'Determinação da resistência - Argamassa',NULL,'vb',1),
	 (25,'Controle Tecnológico - Graute',NULL,'vb',1),
	 (25,'Controle Tecnológico - Concreto',NULL,'vb',1),
	 (25,'Controle Tecnológico - Prisma Oco',NULL,'vb',1),
	 (25,'Controle Tecnológico - Prisma Cheio',NULL,'vb',1),
	 (25,'Resist a Compres e Dimens (NBR 12118/13) - Bloco Cerâmico',NULL,'vb',1),
	 (25,'RAS',NULL,'vb',1),
	 (25,'Ensaios de Compactação do Solo',NULL,'vb',1),
	 (25,'Absorção e Umidade - Bloco Cerâmico',NULL,'vb',1),
	 (25,'Resist a Compres e Dimens (NBR 15270) - Bloco Cerâmico',NULL,'vb',1);
INSERT INTO db_gfc.tb_itens_produtos (id_cat,descricao,codigo,unidade,ativo) VALUES
	 (25,'Determ de massa seca e índ de absorção - Bloco Cerâmico',NULL,'vb',1),
	 (25,'Determ de área bruta e área líquida - Bloco Cerâmico',NULL,'vb',1),
	 (26,'ESCAVAÇÃO MANUAL PARA BLOCO DE COROAMENTO OU SAPATA (INCLUINDO ESCAVAÇÃO PARA COLOCAÇÃO DE FÔRMAS). AF_01/2024',96523,'M3',1),
	 (26,'ESCAVAÇÃO MANUAL PARA VIGA BALDRAME OU SAPATA CORRIDA (INCLUINDO ESCAVAÇÃO PARA COLOCAÇÃO DE FÔRMAS). AF_01/2024',96527,'M3',1),
	 (26,'ESCAVAÇÃO MECANIZADA PARA BLOCO DE COROAMENTO OU SAPATA COM RETROESCAVADEIRA (INCLUINDO ESCAVAÇÃO PARA COLOCAÇÃO DE FÔRMAS). AF_01/2024',96521,'M3',1),
	 (26,'ESCAVAÇÃO MECANIZADA PARA VIGA BALDRAME OU SAPATA CORRIDA COM MINI-ESCAVADEIRA (INCLUINDO ESCAVAÇÃO PARA COLOCAÇÃO DE FÔRMAS). AF_01/2024',96525,'M3',1),
	 (26,'ATERRO MANUAL DE VALAS COM SOLO ARGILO-ARENOSO. AF_08/2023',94319,'M3',1),
	 (26,'ATERRO MECANIZADO DE VALA COM ESCAVADEIRA HIDRÁULICA (CAPACIDADE DA CAÇAMBA: 0,8 M³ / POTÊNCIA: 111 HP), LARGURA ATÉ 2,5 M, PROFUNDIDADE ATÉ 1,5 M, COM SOLO ARGILO-ARENOSO. AF_08/2023',94304,'M3',1),
	 (26,'REATERRO MANUAL DE VALAS, COM PLACA VIBRATÓRIA. AF_08/2023',104737,'M3',1),
	 (26,'REATERRO MECANIZADO DE VALA COM ESCAVADEIRA HIDRÁULICA (CAPACIDADE DA CAÇAMBA: 0,8 M³/POTÊNCIA: 111 HP), LARGURA 1,5 A 2,5 M, PROFUNDIDADE 1,5 A 3,0 M, COM SOLO (SEM SUBSTITUIÇÃO) DE 1ª CATEGORIA, COM COMPACTADOR DE SOLOS DE PERCUSSÃO. AF_08/2023',93369,'M3',1);
INSERT INTO db_gfc.tb_itens_produtos (id_cat,descricao,codigo,unidade,ativo) VALUES
	 (26,'CAMADA SEPARADORA PARA EXECUÇÃO DE RADIER, PISO DE CONCRETO OU LAJE SOBRE SOLO, EM LONA PLÁSTICA. AF_09/2021',97087,'M2',1),
	 (27,'LASTRO DE CONCRETO MAGRO, APLICADO EM PISOS, LAJES SOBRE SOLO OU RADIERS. AF_01/2024',96620,'M3',1),
	 (27,'EXECUÇÃO DE LAJE SOBRE SOLO, ESPESSURA DE 10 CM, FCK = 30 MPA, COM USO DE FORMAS EM MADEIRA SERRADA. AF_09/2021',103076,'M2',1),
	 (27,'EXECUÇÃO DE LAJE SOBRE SOLO, ESPESSURA DE 15 CM, FCK = 30 MPA, COM USO DE FORMAS EM MADEIRA SERRADA. AF_09/2021',103077,'M2',1),
	 (27,'EXECUÇÃO DE LAJE SOBRE SOLO, ESPESSURA DE 20 CM, FCK = 30 MPA, COM USO DE FORMAS EM MADEIRA SERRADA. AF_09/2021',103078,'M2',1),
	 (27,'EXECUÇÃO DE LAJE SOBRE SOLO, ESPESSURA DE 25 CM, FCK = 30 MPA, COM USO DE FORMAS EM MADEIRA SERRADA. AF_09/2021',103079,'M2',1),
	 (27,'EXECUÇÃO DE LAJE SOBRE SOLO, ESPESSURA DE 30 CM, FCK = 30 MPA, COM USO DE FORMAS EM MADEIRA SERRADA. AF_09/2021',103080,'M2',1),
	 (27,'ARMAÇÃO PARA EXECUÇÃO DE RADIER, PISO DE CONCRETO OU LAJE SOBRE SOLO, COM USO DE TELA Q-113. AF_09/2021',97089,'KG',1),
	 (27,'ARMAÇÃO PARA EXECUÇÃO DE RADIER, PISO DE CONCRETO OU LAJE SOBRE SOLO, COM USO DE TELA Q-138. AF_09/2021',97090,'KG',1),
	 (27,'ARMAÇÃO PARA EXECUÇÃO DE RADIER, PISO DE CONCRETO OU LAJE SOBRE SOLO, COM USO DE TELA Q-159. AF_09/2021',97091,'KG',1);
INSERT INTO db_gfc.tb_itens_produtos (id_cat,descricao,codigo,unidade,ativo) VALUES
	 (27,'ARMAÇÃO PARA EXECUÇÃO DE RADIER, PISO DE CONCRETO OU LAJE SOBRE SOLO, COM USO DE TELA Q-196. AF_09/2021',97092,'KG',1),
	 (27,'ARMAÇÃO PARA EXECUÇÃO DE RADIER, PISO DE CONCRETO OU LAJE SOBRE SOLO, COM USO DE TELA Q-246. AF_09/2021',103053,'KG',1),
	 (27,'ARMAÇÃO PARA EXECUÇÃO DE RADIER, PISO DE CONCRETO OU LAJE SOBRE SOLO, COM USO DE TELA Q-283. AF_09/2021',97093,'KG',1),
	 (27,'ARMAÇÃO PARA EXECUÇÃO DE RADIER, PISO DE CONCRETO OU LAJE SOBRE SOLO, COM USO DE TELA Q-396. AF_09/2021',103054,'KG',1),
	 (27,'ARMAÇÃO PARA EXECUÇÃO DE RADIER, PISO DE CONCRETO OU LAJE SOBRE SOLO, COM USO DE TELA Q-92. AF_09/2021',97088,'KG',1),
	 (27,'ARMAÇÃO UTILIZANDO AÇO CA-25 DE 10,0 MM - MONTAGEM. AF_06/2022',92884,'KG',1),
	 (27,'ARMAÇÃO UTILIZANDO AÇO CA-25 DE 12,5 MM - MONTAGEM. AF_06/2022',92885,'KG',1),
	 (27,'ARMAÇÃO UTILIZANDO AÇO CA-25 DE 16,0 MM - MONTAGEM. AF_06/2022',92886,'KG',1),
	 (27,'ARMAÇÃO UTILIZANDO AÇO CA-25 DE 20,0 MM - MONTAGEM. AF_06/2022',92887,'KG',1),
	 (27,'ARMAÇÃO UTILIZANDO AÇO CA-25 DE 25,0 MM - MONTAGEM. AF_06/2022',92888,'KG',1);
INSERT INTO db_gfc.tb_itens_produtos (id_cat,descricao,codigo,unidade,ativo) VALUES
	 (27,'ARMAÇÃO UTILIZANDO AÇO CA-25 DE 6,3 MM - MONTAGEM. AF_06/2022',92882,'KG',1),
	 (27,'ARMAÇÃO UTILIZANDO AÇO CA-25 DE 8,0 MM - MONTAGEM. AF_06/2022',92883,'KG',1),
	 (27,'ARMAÇÃO UTILIZANDO AÇO CA-25 DE 8,0 MM - MONTAGEM. AF_06/2022',92883,'KG',1),
	 (28,'ESTACA RAIZ, DIÂMETRO DE 20 CM, SEM PRESENÇA DE ROCHA (EXCLUSIVE MOBILIZAÇÃO E DESMOBILIZAÇÃO). AF_03/2020',102645,'M',1),
	 (28,'ESTACA RAIZ, DIÂMETRO DE 31 CM, PERFURADA EM ROCHA (EXCLUSIVE MOBILIZAÇÃO E DESMOBILIZAÇÃO). AF_03/2020',102650,'M',1),
	 (28,'ESTACA RAIZ, DIÂMETRO DE 31 CM, SEM PRESENÇA DE ROCHA (EXCLUSIVE MOBILIZAÇÃO E DESMOBILIZAÇÃO). AF_03/2020',102646,'M',1),
	 (28,'ESTACA RAIZ, DIÂMETRO DE 40 CM, PERFURADA EM ROCHA (EXCLUSIVE MOBILIZAÇÃO E DESMOBILIZAÇÃO). AF_03/2020',102651,'M',1),
	 (28,'ESTACA RAIZ, DIÂMETRO DE 40 CM, SEM PRESENÇA DE ROCHA (EXCLUSIVE MOBILIZAÇÃO E DESMOBILIZAÇÃO). AF_03/2020',102647,'M',1),
	 (28,'ESTACA RAIZ, DIÂMETRO DE 45 CM, PERFURADA EM ROCHA (EXCLUSIVE MOBILIZAÇÃO E DESMOBILIZAÇÃO). AF_03/2020',102652,'M',1),
	 (28,'ESTACA RAIZ, DIÂMETRO DE 45 CM, SEM PRESENÇA DE ROCHA (EXCLUSIVE MOBILIZAÇÃO E DESMOBILIZAÇÃO). AF_03/2020',102648,'M',1);
INSERT INTO db_gfc.tb_itens_produtos (id_cat,descricao,codigo,unidade,ativo) VALUES
	 (28,'ESTACA HÉLICE CONTÍNUA, DIÂMETRO DE 30 CM, INCLUSO CONCRETO FCK=30MPA E ARMADURA MÍNIMA (EXCLUSIVE BOMBEAMENTO, MOBILIZAÇÃO E DESMOBILIZAÇÃO). AF_12/2019',100651,'M',1),
	 (28,'ESTACA HÉLICE CONTÍNUA, DIÂMETRO DE 50 CM, INCLUSO CONCRETO FCK=30MPA E ARMADURA MÍNIMA (EXCLUSIVE BOMBEAMENTO, MOBILIZAÇÃO E DESMOBILIZAÇÃO). AF_12/2019',100652,'M',1),
	 (28,'ESTACA HÉLICE CONTÍNUA, DIÂMETRO DE 70 CM, INCLUSO CONCRETO FCK=30MPA E ARMADURA MÍNIMA (EXCLUSIVE BOMBEAMENTO, MOBILIZAÇÃO E DESMOBILIZAÇÃO). AF_12/2019',100653,'M',1),
	 (28,'ESTACA HÉLICE CONTÍNUA, DIÂMETRO DE 80 CM, INCLUSO CONCRETO FCK=30MPA E ARMADURA MÍNIMA (EXCLUSIVE BOMBEAMENTO, MOBILIZAÇÃO E DESMOBILIZAÇÃO). AF_12/2019',100654,'M',1),
	 (28,'ESTACA HÉLICE CONTÍNUA, DIÂMETRO DE 90 CM, INCLUSO CONCRETO FCK=30MPA E ARMADURA MÍNIMA (EXCLUSIVE BOMBEAMENTO, MOBILIZAÇÃO E DESMOBILIZAÇÃO). AF_12/2019',100655,'M',1),
	 (28,'ARRASAMENTO MECANICO DE ESTACA DE CONCRETO ARMADO, DIAMETROS DE 101 CM A 150 CM. AF_05/2021',95605,'UN',1),
	 (28,'ARRASAMENTO MECANICO DE ESTACA DE CONCRETO ARMADO, DIAMETROS DE 41 CM A 60 CM. AF_05/2021',95602,'UN',1),
	 (28,'ARRASAMENTO MECANICO DE ESTACA DE CONCRETO ARMADO, DIAMETROS DE 61 CM A 80 CM. AF_05/2021',95603,'UN',1),
	 (28,'ARRASAMENTO MECANICO DE ESTACA DE CONCRETO ARMADO, DIAMETROS DE 81 CM A 100 CM. AF_05/2021',95604,'UN',1),
	 (28,'ARRASAMENTO MECANICO DE ESTACA DE CONCRETO ARMADO, DIAMETROS DE ATÉ 40 CM. AF_05/2021',95601,'UN',1);
INSERT INTO db_gfc.tb_itens_produtos (id_cat,descricao,codigo,unidade,ativo) VALUES
	 (29,'CONCRETAGEM DE PILARES, FCK = 25 MPA, COM USO DE BOMBA - LANÇAMENTO, ADENSAMENTO E ACABAMENTO. AF_02/2022_PS',103672,'M3',1),
	 (29,'CONCRETAGEM DE VIGAS E LAJES, FCK=25 MPA, PARA QUALQUER TIPO DE LAJE COM BALDES EM EDIFICAÇÃO DE MULTIPAVIMENTOS ATÉ 04 ANDARES - LANÇAMENTO, ADENSAMENTO E ACABAMENTO. AF_02/2022',103683,'M3',1),
	 (29,'LANÇAMENTO COM USO DE BOMBA, ADENSAMENTO E ACABAMENTO DE CONCRETO EM ESTRUTURAS. AF_02/2022',103673,'M3',1),
	 (30,'ESCORAMENTO DE FÔRMAS DE LAJE EM MADEIRA NÃO APARELHADA, PÉ-DIREITO SIMPLES, INCLUSO TRAVAMENTO, 4 UTILIZAÇÕES. AF_09/2020',101792,'M3',1),
	 (30,'MONTAGEM E DESMONTAGEM DE FÔRMA DE PILARES RETANGULARES E ESTRUTURAS SIMILARES, PÉ-DIREITO SIMPLES, EM CHAPA DE MADEIRA COMPENSADA RESINADA, 2 UTILIZAÇÕES. AF_09/2020',92415,'M2',1),
	 (30,'MONTAGEM E DESMONTAGEM DE FÔRMA DE VIGA, ESCORAMENTO COM GARFO DE MADEIRA, PÉ-DIREITO SIMPLES, EM CHAPA DE MADEIRA RESINADA, 2 UTILIZAÇÕES. AF_09/2020',92451,'M2',1),
	 (30,'MONTAGEM E DESMONTAGEM DE FÔRMA DE LAJE MACIÇA, PÉ-DIREITO SIMPLES, EM CHAPA DE MADEIRA COMPENSADA RESINADA E CIMBRAMENTO DE MADEIRA, 4 UTILIZAÇÕES. AF_03/2022',103761,'M2',1),
	 (31,'ARMAÇÃO UTILIZANDO AÇO CA-25 DE 10,0 MM - MONTAGEM. AF_06/2022',92884,'KG',1),
	 (31,'ARMAÇÃO UTILIZANDO AÇO CA-25 DE 12,5 MM - MONTAGEM. AF_06/2022',92885,'KG',1),
	 (31,'ARMAÇÃO UTILIZANDO AÇO CA-25 DE 16,0 MM - MONTAGEM. AF_06/2022',92886,'KG',1);
INSERT INTO db_gfc.tb_itens_produtos (id_cat,descricao,codigo,unidade,ativo) VALUES
	 (31,'ARMAÇÃO UTILIZANDO AÇO CA-25 DE 20,0 MM - MONTAGEM. AF_06/2022',92887,'KG',1),
	 (31,'ARMAÇÃO UTILIZANDO AÇO CA-25 DE 25,0 MM - MONTAGEM. AF_06/2022',92888,'KG',1),
	 (31,'ARMAÇÃO UTILIZANDO AÇO CA-25 DE 6,3 MM - MONTAGEM. AF_06/2022',92882,'KG',1),
	 (31,'ARMAÇÃO UTILIZANDO AÇO CA-25 DE 8,0 MM - MONTAGEM. AF_06/2022',92883,'KG',1),
	 (32,'ALVENARIA DE VEDAÇÃO DE BLOCOS CERÂMICOS FURADOS NA HORIZONTAL DE 14X19X29 CM (ESPESSURA 14 CM) E ARGAMASSA DE ASSENTAMENTO COM PREPARO EM BETONEIRA. AF_12/2021',103360,'M2',1),
	 (32,'ALVENARIA DE VEDAÇÃO DE BLOCOS CERÂMICOS FURADOS NA HORIZONTAL DE 14X19X39 CM (ESPESSURA 14 CM) E ARGAMASSA DE ASSENTAMENTO COM PREPARO EM BETONEIRA. AF_12/2021',103368,'M2',1),
	 (32,'ALVENARIA DE VEDAÇÃO DE BLOCOS CERÂMICOS FURADOS NA HORIZONTAL DE 14X9X19 CM (ESPESSURA 14 CM, BLOCO DEITADO) E ARGAMASSA DE ASSENTAMENTO COM PREPARO EM BETONEIRA. AF_12/2021',103334,'M2',1),
	 (32,'ALVENARIA DE VEDAÇÃO DE BLOCOS CERÂMICOS FURADOS NA HORIZONTAL DE 19X19X29 CM (ESPESSURA 19 CM) E ARGAMASSA DE ASSENTAMENTO COM PREPARO EM BETONEIRA. AF_12/2021',103362,'M2',1),
	 (32,'ALVENARIA DE VEDAÇÃO DE BLOCOS CERÂMICOS FURADOS NA HORIZONTAL DE 19X19X39 CM (ESPESSURA 19 CM) E ARGAMASSA DE ASSENTAMENTO COM PREPARO EM BETONEIRA. AF_12/2021',103370,'M2',1),
	 (32,'ALVENARIA DE VEDAÇÃO DE BLOCOS CERÂMICOS FURADOS NA HORIZONTAL DE 9X14X19 CM (ESPESSURA 9 CM) E ARGAMASSA DE ASSENTAMENTO COM PREPARO EM BETONEIRA. AF_12/2021',103332,'M2',1);
INSERT INTO db_gfc.tb_itens_produtos (id_cat,descricao,codigo,unidade,ativo) VALUES
	 (32,'ALVENARIA DE VEDAÇÃO DE BLOCOS CERÂMICOS FURADOS NA HORIZONTAL DE 9X14X24 CM (ESPESSURA 9 CM) E ARGAMASSA DE ASSENTAMENTO COM PREPARO EM BETONEIRA. AF_12/2021',103352,'M2',1),
	 (32,'ALVENARIA DE VEDAÇÃO DE BLOCOS CERÂMICOS FURADOS NA HORIZONTAL DE 9X19X19 CM (ESPESSURA 9 CM) E ARGAMASSA DE ASSENTAMENTO COM PREPARO EM BETONEIRA. AF_12/2021',103328,'M2',1),
	 (32,'ALVENARIA DE VEDAÇÃO DE BLOCOS CERÂMICOS FURADOS NA HORIZONTAL DE 9X19X29 CM (ESPESSURA 9 CM) E ARGAMASSA DE ASSENTAMENTO COM PREPARO EM BETONEIRA. AF_12/2021',103356,'M2',1),
	 (32,'ALVENARIA DE VEDAÇÃO DE BLOCOS CERÂMICOS FURADOS NA HORIZONTAL DE 9X19X39 CM (ESPESSURA 9 CM) E ARGAMASSA DE ASSENTAMENTO COM PREPARO EM BETONEIRA. AF_12/2021',103364,'M2',1),
	 (33,'ALVENARIA DE VEDAÇÃO DE BLOCOS VAZADOS DE CONCRETO DE 14X19X29 CM (ESPESSURA 14 CM) E ARGAMASSA DE ASSENTAMENTO COM PREPARO EM BETONEIRA. AF_12/2021',103342,'M2',1),
	 (33,'ALVENARIA DE VEDAÇÃO DE BLOCOS VAZADOS DE CONCRETO DE 14X19X39 CM (ESPESSURA 14 CM) E ARGAMASSA DE ASSENTAMENTO COM PREPARO EM BETONEIRA. AF_12/2021',103318,'M2',1),
	 (33,'ALVENARIA DE VEDAÇÃO DE BLOCOS VAZADOS DE CONCRETO DE 19X19X39 CM (ESPESSURA 19 CM) E ARGAMASSA DE ASSENTAMENTO COM PREPARO EM BETONEIRA. AF_12/2021',103320,'M2',1),
	 (33,'ALVENARIA DE VEDAÇÃO DE BLOCOS VAZADOS DE CONCRETO DE 9X19X39 CM (ESPESSURA 9 CM) E ARGAMASSA DE ASSENTAMENTO COM PREPARO EM BETONEIRA. AF_12/2021',103316,'M2',1),
	 (34,'ALVENARIA DE VEDAÇÃO COM ELEMENTO VAZADO DE CERÂMICA (COBOGÓ) DE 7X20X20CM E ARGAMASSA DE ASSENTAMENTO COM PREPARO EM BETONEIRA. AF_05/2020',101162,'M2',1),
	 (34,'VERGA PRÉ-MOLDADA COM ATÉ 1,5 M DE VÃO, ESPESSURA DE *10* CM. AF_03/2024',105022,'M',1);
INSERT INTO db_gfc.tb_itens_produtos (id_cat,descricao,codigo,unidade,ativo) VALUES
	 (34,'VERGA PRÉ-MOLDADA COM ATÉ 1,5 M DE VÃO, ESPESSURA DE *15* CM. AF_03/2024',105021,'M',1),
	 (34,'VERGA PRÉ-MOLDADA COM ATÉ 1,5 M DE VÃO, ESPESSURA DE *20* CM. AF_03/2024',93184,'M',1),
	 (34,'CONTRAVERGA PRÉ-MOLDADA, ESPESSURA DE *10* CM. AF_03/2024',105028,'M',1),
	 (34,'CONTRAVERGA PRÉ-MOLDADA, ESPESSURA DE *15* CM. AF_03/2024',105027,'M',1),
	 (34,'CONTRAVERGA PRÉ-MOLDADA, ESPESSURA DE *20* CM. AF_03/2024',93194,'M',1),
	 (34,'PAREDE COM SISTEMA EM CHAPAS DE GESSO PARA DRYWALL, USO INTERNO, COM DUAS FACES DUPLAS E ESTRUTURA METÁLICA COM GUIAS SIMPLES PARA PAREDES COM ÁREA LÍQUIDA MAIOR OU IGUAL A 6 M2, COM VÃOS. AF_07/2023_PS',96367,'M2',1),
	 (34,'PAREDE COM SISTEMA EM CHAPAS DE GESSO PARA DRYWALL, USO INTERNO, COM DUAS FACES DUPLAS E ESTRUTURA METÁLICA COM GUIAS SIMPLES PARA PAREDES COM ÁREA LÍQUIDA MENOR QUE 6 M2, COM VÃOS. AF_07/2023_PS',104722,'M2',1),
	 (35,'KIT DE PORTA DE MADEIRA PARA PINTURA, SEMI-OCA (LEVE OU MÉDIA), PADRÃO MÉDIO, 60X210CM, ESPESSURA DE 3,5CM, ITENS INCLUSOS: DOBRADIÇAS, MONTAGEM E INSTALAÇÃO DO BATENTE, FECHADURA COM EXECUÇÃO DO FURO - FORNECIMENTO E INSTALAÇÃO. AF_12/2019',90841,'UN',1),
	 (35,'KIT DE PORTA DE MADEIRA PARA PINTURA, SEMI-OCA (LEVE OU MÉDIA), PADRÃO MÉDIO, 70X210CM, ESPESSURA DE 3,5CM, ITENS INCLUSOS: DOBRADIÇAS, MONTAGEM E INSTALAÇÃO DO BATENTE, FECHADURA COM EXECUÇÃO DO FURO - FORNECIMENTO E INSTALAÇÃO. AF_12/2019',90842,'UN',1),
	 (35,'KIT DE PORTA DE MADEIRA PARA PINTURA, SEMI-OCA (LEVE OU MÉDIA), PADRÃO MÉDIO, 80X210CM, ESPESSURA DE 3,5CM, ITENS INCLUSOS: DOBRADIÇAS, MONTAGEM E INSTALAÇÃO DO BATENTE, FECHADURA COM EXECUÇÃO DO FURO - FORNECIMENTO E INSTALAÇÃO. AF_12/2019',90843,'UN',1);
INSERT INTO db_gfc.tb_itens_produtos (id_cat,descricao,codigo,unidade,ativo) VALUES
	 (35,'KIT DE PORTA DE MADEIRA PARA PINTURA, SEMI-OCA (LEVE OU MÉDIA), PADRÃO MÉDIO, 90X210CM, ESPESSURA DE 3,5CM, ITENS INCLUSOS: DOBRADIÇAS, MONTAGEM E INSTALAÇÃO DO BATENTE, FECHADURA COM EXECUÇÃO DO FURO - FORNECIMENTO E INSTALAÇÃO. AF_12/2019',90844,'UN',1),
	 (35,'ALIZAR DE 5X1,5CM PARA PORTA FIXADO COM PREGOS, PADRÃO MÉDIO - FORNECIMENTO E INSTALAÇÃO. AF_12/2019',100659,'M',1),
	 (36,'CONTRAMARCO DE ALUMÍNIO, FIXAÇÃO COM PARAFUSO - FORNECIMENTO E INSTALAÇÃO. AF_11/2024',94590,'M',1),
	 (36,'JANELA DE ALUMÍNIO DE CORRER COM 4 FOLHAS PARA VIDROS (VIDROS INCLUSOS), SEM BANDEIRA, BATENTE/ REQUADRO 6 A 14 CM, ACABAMENTO COM ACETATO OU BRILHANTE, FIXAÇÃO COM PARAFUSO, SEM GUARNIÇÃO/ ALIZAR, DIMENSÕES 150X120 CM, VEDAÇÃO COM SILICONE, EXCLUSIVE CONTRAMARCO - FORNECIMENTO E INSTALAÇÃO. AF_11/2024',105809,'M2',1),
	 (36,'JANELA DE ALUMÍNIO TIPO MAXIM-AR, BATENTE/ REQUADRO 3 A 14 CM, VIDRO INCLUSO, FIXAÇÃO COM PARAFUSO, SEM GUARNIÇÃO/ ALIZAR, DIMENSÕES 60X80 (A X L) CM, SEM ACABAMENTO, VEDAÇÃO COM SILICONE, EXCLUSIVE CONTRAMARCO - FORNECIMENTO E INSTALAÇÃO. AF_11/2024',94569,'M2',1),
	 (36,'GUARNIÇÃO DE ALUMÍNIO. AF_11/2024',105812,'M',1),
	 (36,'PORTA DE CORRER DE ALUMÍNIO, COM DUAS FOLHAS PARA VIDRO, INCLUSO VIDRO LISO INCOLOR, FECHADURA E PUXADOR, SEM ALIZAR. AF_12/2019',100702,'M2',1),
	 (36,'GUARDA-CORPO PANORÂMICO COM PERFIS DE ALUMÍNIO E VIDRO LAMINADO 8 MM, FIXADO COM CHUMBADOR MECÂNICO. AF_04/2019_PS',99841,'M',1),
	 (36,'GUARDA-CORPO DE AÇO GALVANIZADO DE 1,10M DE ALTURA, MONTANTES TUBULARES DE 1.1/2 ESPAÇADOS DE 1,20M, TRAVESSA SUPERIOR DE 2, GRADIL FORMADO POR BARRAS CHATAS EM FERRO DE 32X4,8MM, FIXADO COM CHUMBADOR MECÂNICO. AF_04/2019_PS',99839,'M',1),
	 (37,'PORTA CORTA-FOGO 90X210X4CM - FORNECIMENTO E INSTALAÇÃO. AF_12/2019',90838,'UN',1);
INSERT INTO db_gfc.tb_itens_produtos (id_cat,descricao,codigo,unidade,ativo) VALUES
	 (37,'GRELHA DE FERRO FUNDIDO SIMPLES COM REQUADRO, 150 X 1000 MM, ASSENTADA COM ARGAMASSA 1 : 3 CIMENTO: AREIA - FORNECIMENTO E INSTALAÇÃO. AF_05/2025',103001,'UN',1),
	 (37,'GRELHA DE FERRO FUNDIDO SIMPLES COM REQUADRO, 200 X 1000 MM, ASSENTADA COM ARGAMASSA 1 : 3 CIMENTO: AREIA - FORNECIMENTO E INSTALAÇÃO. AF_05/2025',103002,'UN',1),
	 (37,'GRELHA DE FERRO FUNDIDO SIMPLES COM REQUADRO, 300 X 1000 MM, ASSENTADA COM ARGAMASSA 1 : 3 CIMENTO: AREIA - FORNECIMENTO E INSTALAÇÃO. AF_05/2025',103003,'UN',1),
	 (37,'PORTA DE FERRO, DE ABRIR, TIPO GRADE COM CHAPA, COM GUARNIÇÕES. AF_12/2019',100701,'M2',1),
	 (37,'ESCADA TIPO MARINHEIRO EM TUBO AÇO GALVANIZADO 1 1/2", COM GUARDA-CORPO, PARA ALTURAS DE ATÉ 3 M, FIXADA COM CHUMBADOR MECÂNICO. AF_11/2020',102092,'M',1),
	 (39,'APLICAÇÃO DE GESSO PROJETADO COM EQUIPAMENTO DE PROJEÇÃO EM PAREDES, DESEMPENADO (SEM TALISCAS), ESPESSURA DE 1,0CM. AF_03/2023',87433,'M2',1),
	 (39,'FORRO EM PLACAS DE GESSO, PARA AMBIENTES COMERCIAIS. AF_08/2023_PS',96113,'M2',1),
	 (39,'FORRO EM PLACAS DE GESSO, PARA AMBIENTES RESIDENCIAIS. AF_08/2023_PS',96109,'M2',1),
	 (39,'ACABAMENTOS PARA FORRO (SANCA DE GESSO, MONTADA NA OBRA). AF_08/2023_PS',99054,'M2',1),
	 (39,'MASSA ÚNICA, EM ARGAMASSA TRAÇO 1:2:8, PREPARO MECÂNICO, APLICADA MANUALMENTE EM PAREDES INTERNAS DE AMBIENTES COM ÁREA ENTRE 5M² E 10M², E = 17,5MM, COM TALISCAS. AF_03/2024',87529,'M2',1);
INSERT INTO db_gfc.tb_itens_produtos (id_cat,descricao,codigo,unidade,ativo) VALUES
	 (39,'MASSA ÚNICA, EM ARGAMASSA TRAÇO 1:2:8, PREPARO MECÂNICO, APLICADA MANUALMENTE EM TETO, E = 10MM, COM TALISCAS. AF_03/2024',90408,'M2',1),
	 (39,'EMBOÇO, EM ARGAMASSA TRAÇO 1:2:8, PREPARO MECÂNICO, APLICADO MANUALMENTE EM PAREDES INTERNAS, PARA AMBIENTES COM ÁREA MENOR QUE 5M², E = 10MM, COM TALISCAS. AF_03/2024',87545,'M2',1),
	 (39,'EMBOÇO, EM ARGAMASSA TRAÇO 1:2:8, PREPARO MECÂNICO, APLICADO MANUALMENTE EM PAREDES INTERNAS DE AMBIENTES COM ÁREA ENTRE 5M² E 10M², E = 17,5MM, COM TALISCAS. AF_03/2024',87531,'M2',1),
	 (39,'CHAPISCO APLICADO EM ALVENARIA (COM PRESENÇA DE VÃOS) E ESTRUTURAS DE CONCRETO DE FACHADA, COM COLHER DE PEDREIRO. ARGAMASSA TRAÇO 1:3 COM PREPARO EM BETONEIRA 400L. AF_10/2022',87905,'M2',1),
	 (39,'REVESTIMENTO CERÂMICO PARA PAREDES INTERNAS COM PLACAS TIPO ESMALTADA DE DIMENSÕES 25X35 CM APLICADAS NA ALTURA INTEIRA DAS PAREDES. AF_02/2023_PE',87269,'M2',1),
	 (39,'REVESTIMENTO CERÂMICO PARA PAREDES INTERNAS COM PLACAS TIPO ESMALTADA DE DIMENSÕES 33X45 CM APLICADAS NA ALTURA INTEIRA DAS PAREDES. AF_02/2023_PE',87273,'M2',1),
	 (40,'EMBOÇO OU MASSA ÚNICA EM ARGAMASSA TRAÇO 1:2:8, PREPARO MECÂNICA COM BETONEIRA 400 L, APLICADA MANUALMENTE EM SUPERFÍCIES EXTERNAS DA SACADA, ESPESSURA DE 25 MM, ACESSO POR ANDAIME, SEM USO DE TELA METÁLICA. AF_08/2022',104249,'M2',1),
	 (40,'CHAPISCO APLICADO EM ALVENARIA (COM PRESENÇA DE VÃOS) E ESTRUTURAS DE CONCRETO DE FACHADA, COM EQUIPAMENTO DE PROJEÇÃO. ARGAMASSA TRAÇO 1:3 COM PREPARO MANUAL. AF_10/2022',87907,'M2',1),
	 (40,'REVESTIMENTO CERÂMICO PARA PAREDES EXTERNAS, COM PLACAS TIPO GRÊS OU SEMIGRÊS, FORMATO MENOR OU IGUAL A 200 CM2, DISPOSTAS EM AMARRAÇÃO. AF_02/2023',104590,'M2',1),
	 (41,'REVESTIMENTO CERÂMICO PARA PISO COM PLACAS TIPO PORCELANATO DE DIMENSÕES 60X60 CM APLICADA EM AMBIENTES DE ÁREA MAIOR QUE 10 M². AF_02/2023_PE',87263,'M2',1);
INSERT INTO db_gfc.tb_itens_produtos (id_cat,descricao,codigo,unidade,ativo) VALUES
	 (41,'REVESTIMENTO CERÂMICO PARA PISO COM PLACAS TIPO PORCELANATO DE DIMENSÕES 60X60 CM APLICADA EM AMBIENTES DE ÁREA MENOR QUE 5 M². AF_02/2023_PE',87261,'M2',1),
	 (41,'REVESTIMENTO CERÂMICO PARA PISO COM PLACAS TIPO PORCELANATO DE DIMENSÕES 80X80 CM APLICADA EM AMBIENTES DE ÁREA ENTRE 5 M² E 10 M². AF_02/2023_PE',104597,'M2',1),
	 (41,'REVESTIMENTO CERÂMICO PARA PISO COM PLACAS TIPO PORCELANATO DE DIMENSÕES 80X80 CM APLICADA EM AMBIENTES DE ÁREA MAIOR QUE 10 M². AF_02/2023_PE',104598,'M2',1),
	 (41,'REVESTIMENTO CERÂMICO PARA PISO COM PLACAS TIPO PORCELANATO DE DIMENSÕES 80X80 CM APLICADA EM AMBIENTES DE ÁREA MENOR QUE 5 M². AF_02/2023_PE',104596,'M2',1),
	 (41,'PISO VINÍLICO SEMI-FLEXÍVEL EM PLACAS, PADRÃO LISO, ESPESSURA 3,2 MM, FIXADO COM COLA. AF_09/2020',101727,'M2',1),
	 (41,'PISO LAMINADO EM AMBIENTES INTERNOS. AF_09/2020',98683,'M2',1),
	 (41,'PISO EM GRANITO APLICADO EM AMBIENTES INTERNOS. AF_09/2020',98671,'M2',1),
	 (41,'PISO CIMENTADO, TRAÇO 1:3 (CIMENTO E AREIA), ACABAMENTO LISO, ESPESSURA 4,0 CM, PREPARO MECÂNICO DA ARGAMASSA. AF_09/2020',101749,'M2',1),
	 (41,'PISO CIMENTADO, TRAÇO 1:3 (CIMENTO E AREIA), ACABAMENTO RÚSTICO, ESPESSURA 4,0 CM, PREPARO MECÂNICO DA ARGAMASSA. AF_09/2020',101750,'M2',1),
	 (41,'CONTRAPISO EM ARGAMASSA TRAÇO 1:4 (CIMENTO E AREIA), PREPARO MECÂNICO COM BETONEIRA 400 L, APLICADO EM ÁREAS SECAS SOBRE LAJE, NÃO ADERIDO, ACABAMENTO NÃO REFORÇADO, ESPESSURA 5CM. AF_07/2021',87690,'M2',1);
INSERT INTO db_gfc.tb_itens_produtos (id_cat,descricao,codigo,unidade,ativo) VALUES
	 (41,'CONTRAPISO EM ARGAMASSA TRAÇO 1:4 (CIMENTO E AREIA), PREPARO MECÂNICO COM BETONEIRA 400 L, APLICADO EM ÁREAS MOLHADAS SOBRE IMPERMEABILIZAÇÃO, ACABAMENTO NÃO REFORÇADO, ESPESSURA 4CM. AF_07/2021',87765,'M2',1),
	 (41,'PISO EM CONCRETO 20 MPA PREPARO MECÂNICO, ESPESSURA 7CM. AF_09/2020',101747,'M2',1),
	 (42,'RODAPÉ CERÂMICO DE 7CM DE ALTURA COM PLACAS TIPO ESMALTADA DE DIMENSÕES 60X60CM. AF_02/2023',88650,'M',1),
	 (42,'RODAPÉ CERÂMICO DE 7CM DE ALTURA COM PLACAS TIPO ESMALTADA DE DIMENSÕES 80X80CM. AF_02/2023',104619,'M',1),
	 (42,'RODAPÉ EM GRANITO, ALTURA 10 CM. AF_09/2020',98685,'M',1),
	 (42,'RODAPÉ EM POLIESTIRENO, ALTURA 5 CM. AF_09/2020',98688,'M',1),
	 (42,'RODAPÉ EM POLIESTIRENO, ALTURA 5 CM. AF_09/2020',98688,'M',1),
	 (43,'SOLEIRA EM GRANITO, LARGURA 15 CM, ESPESSURA 2,0 CM. AF_09/2020',98689,'M',1),
	 (43,'SOLEIRA EM MÁRMORE, LARGURA 15 CM, ESPESSURA 2,0 CM. AF_09/2020',98695,'M',1),
	 (44,'PEITORIL LINEAR EM CONCRETO PRÉ-MOLDADO, COMPRIMENTO DE ATÉ 2 M, ASSENTADO COM ARGAMASSA 1:6 COM ADITIVO. AF_11/2020',101967,'M',1);
INSERT INTO db_gfc.tb_itens_produtos (id_cat,descricao,codigo,unidade,ativo) VALUES
	 (44,'PEITORIL LINEAR EM CONCRETO PRÉ-MOLDADO, COMPRIMENTO MAIOR QUE 2 M, ASSENTADO COM ARGAMASSA 1:6 COM ADITIVO. AF_11/2020',101968,'M',1),
	 (44,'PEITORIL LINEAR EM GRANITO OU MÁRMORE, L = 15CM, ASSENTADO COM ARGAMASSA 1:6 COM ADITIVO. AF_11/2020',101965,'M',1),
	 (45,'Tento de granito',NULL,'m',1),
	 (46,'DIVISORIA SANITÁRIA, TIPO CABINE, EM GRANITO CINZA POLIDO, ESP = 3CM, ASSENTADO COM ARGAMASSA COLANTE AC III-E, EXCLUSIVE FERRAGENS. AF_01/2021',102253,'M2',1),
	 (46,'DIVISORIA SANITÁRIA, TIPO CABINE, EM MÁRMORE BRANCO POLIDO, ESP = 3CM, ASSENTADO COM ARGAMASSA COLANTE AC III-E, EXCLUSIVE FERRAGENS. AF_01/2021',102254,'M2',1),
	 (47,'EMASSAMENTO COM MASSA LÁTEX, APLICAÇÃO EM PAREDE, UMA DEMÃO, LIXAMENTO MECANIZADO. AF_04/2023',104646,'M2',1),
	 (47,'EMASSAMENTO COM MASSA LÁTEX, APLICAÇÃO EM TETO, UMA DEMÃO, LIXAMENTO MECANIZADO. AF_04/2023',104645,'M2',1),
	 (47,'FUNDO SELADOR ACRÍLICO, APLICAÇÃO MANUAL EM PAREDE, UMA DEMÃO. AF_04/2023',88485,'M2',1),
	 (47,'FUNDO SELADOR ACRÍLICO, APLICAÇÃO MANUAL EM TETO, UMA DEMÃO. AF_04/2023',88484,'M2',1),
	 (47,'PINTURA LÁTEX ACRÍLICA ECONÔMICA, APLICAÇÃO MANUAL EM PAREDES, DUAS DEMÃOS. AF_04/2023',104641,'M2',1);
INSERT INTO db_gfc.tb_itens_produtos (id_cat,descricao,codigo,unidade,ativo) VALUES
	 (47,'PINTURA LÁTEX ACRÍLICA ECONÔMICA, APLICAÇÃO MANUAL EM TETO, DUAS DEMÃOS. AF_04/2023',104639,'M2',1),
	 (47,'PINTURA LÁTEX ACRÍLICA PREMIUM, APLICAÇÃO MANUAL EM PAREDES, DUAS DEMÃOS. AF_04/2023',88489,'M2',1),
	 (47,'PINTURA LÁTEX ACRÍLICA PREMIUM, APLICAÇÃO MANUAL EM TETO, DUAS DEMÃOS. AF_04/2023',88488,'M2',1),
	 (47,'PINTURA LÁTEX ACRÍLICA STANDARD, APLICAÇÃO MANUAL EM PAREDES, DUAS DEMÃOS. AF_04/2023',104642,'M2',1),
	 (47,'PINTURA LÁTEX ACRÍLICA STANDARD, APLICAÇÃO MANUAL EM TETO, DUAS DEMÃOS. AF_04/2023',104640,'M2',1),
	 (47,'TEXTURA ACRÍLICA, APLICAÇÃO MANUAL EM PAREDE, UMA DEMÃO. AF_04/2023',95305,'M2',1),
	 (47,'TEXTURA ACRÍLICA, APLICAÇÃO MANUAL EM TETO, UMA DEMÃO. AF_04/2023',95306,'M2',1),
	 (47,'PINTURA DE DEMARCAÇÃO DE VAGA COM TINTA EPÓXI, E = 10 CM, APLICAÇÃO MANUAL. AF_05/2021',102507,'M',1),
	 (47,'PINTURA DE PISO COM TINTA EPÓXI, APLICAÇÃO MANUAL, 2 DEMÃOS, INCLUSO PRIMER EPÓXI. AF_05/2021',102494,'M2',1),
	 (47,'PINTURA DE RODAPÉ COM TINTA EPÓXI, APLICAÇÃO MANUAL, 2 DEMÃOS, INCLUSÃO PRIMER EPÓXI. AF_05/2021',102496,'M',1);
INSERT INTO db_gfc.tb_itens_produtos (id_cat,descricao,codigo,unidade,ativo) VALUES
	 (47,'PREPARO DO PISO CIMENTADO PARA PINTURA - LIXAMENTO E LIMPEZA. AF_05/2021',102488,'M2',1),
	 (47,'PINTURA TINTA DE ACABAMENTO (PIGMENTADA) ESMALTE SINTÉTICO FOSCO EM MADEIRA, 3 DEMÃOS. AF_01/2021',102228,'M2',1),
	 (48,'APLICAÇÃO MANUAL DE FUNDO SELADOR ACRÍLICO EM PANOS COM PRESENÇA DE VÃOS DE EDIFÍCIOS DE MÚLTIPLOS PAVIMENTOS. AF_03/2024',88411,'M2',1),
	 (48,'APLICAÇÃO MANUAL DE MASSA ACRÍLICA EM PANOS DE FACHADA COM PRESENÇA DE VÃOS, DE EDIFÍCIOS DE MÚLTIPLOS PAVIMENTOS, UMA DEMÃO. AF_03/2024',96126,'M2',1),
	 (48,'APLICAÇÃO MANUAL DE PINTURA COM TINTA TEXTURIZADA ACRÍLICA EM PANOS COM PRESENÇA DE VÃOS DE EDIFÍCIOS DE MÚLTIPLOS PAVIMENTOS, DUAS CORES. AF_03/2024',88424,'M2',1),
	 (48,'APLICAÇÃO MANUAL DE TINTA LÁTEX ACRÍLICA EM PAREDE EXTERNAS DE CASAS, DUAS DEMÃOS. AF_03/2024',95626,'M2',1),
	 (49,'RUFO EM CHAPA DE AÇO GALVANIZADO NÚMERO 24, CORTE DE 25 CM, INCLUSO TRANSPORTE VERTICAL. AF_07/2019',94231,'M',1),
	 (49,'TELHAMENTO COM TELHA ONDULADA DE FIBROCIMENTO E = 6 MM, COM RECOBRIMENTO LATERAL DE 1/4 DE ONDA PARA TELHADO COM INCLINAÇÃO MAIOR QUE 10°, COM ATÉ 2 ÁGUAS, INCLUSO IÇAMENTO. AF_07/2019',94207,'M2',1),
	 (49,'TELHAMENTO COM TELHA METÁLICA TERMOACÚSTICA E = 30 MM, COM ATÉ 2 ÁGUAS, INCLUSO IÇAMENTO. AF_07/2019',94216,'M2',1),
	 (49,'CUMEEIRA SHED PARA TELHA ONDULADA DE FIBROCIMENTO, E = 6 MM, INCLUSO ACESSÓRIOS DE FIXAÇÃO E IÇAMENTO. AF_07/2019',100325,'M',1);
INSERT INTO db_gfc.tb_itens_produtos (id_cat,descricao,codigo,unidade,ativo) VALUES
	 (49,'AMARRAÇÃO DE TELHAS CERÂMICAS OU DE CONCRETO. AF_07/2019',94232,'UN',1),
	 (49,'CALHA DE BEIRAL, SEMICIRCULAR DE PVC, DIAMETRO 125 MM, INCLUINDO CABECEIRAS, EMENDAS, BOCAIS, SUPORTES E VEDAÇÕES, EXCLUINDO CONDUTORES, INCLUSO TRANSPORTE VERTICAL. AF_07/2019',100434,'M',1),
	 (49,'CALHA EM CHAPA DE AÇO GALVANIZADO NÚMERO 24, DESENVOLVIMENTO DE 100 CM, INCLUSO TRANSPORTE VERTICAL. AF_07/2019',94229,'M',1),
	 (50,'IMPERMEABILIZAÇÃO COM MANTA ASFÁLTICA COLADA COM ASFALTO DERRETIDO, DUAS CAMADAS, E = 3MM E E=4MM. AF_09/2023',98549,'M2',1),
	 (50,'IMPERMEABILIZAÇÃO DE SUPERFÍCIE COM ARGAMASSA POLIMÉRICA / MEMBRANA ACRÍLICA, 4 DEMÃOS, REFORÇADA COM VÉU DE POLIÉSTER (MAV). AF_09/2023',98556,'M2',1),
	 (50,'PROTEÇÃO MECÂNICA DE SUPERFÍCIE HORIZONTAL COM ARGAMASSA DE CIMENTO E AREIA, TRAÇO 1:3, E=2CM. AF_09/2023',98563,'M2',1),
	 (50,'PROTEÇÃO MECÂNICA DE SUPERFÍCIE VERTICAL COM ARGAMASSA DE CIMENTO E AREIA, TRAÇO 1:3, E=2CM. AF_09/2023',98564,'M2',1),
	 (50,'TRATAMENTO DE JUNTA DE DILATAÇÃO COM MANTA ASFÁLTICA ADERIDA COM MAÇARICO. AF_09/2023',98576,'M',1),
	 (50,'TRATAMENTO DE RALO OU PONTO EMERGENTE COM ARGAMASSA POLIMÉRICA / MEMBRANA ACRÍLICA REFORÇADO COM TELA DE POLIÉSTER (MAV). AF_09/2023',98558,'UN',1),
	 (51,'CONJUNTO DE MANGUEIRA PARA COMBATE A INCÊNDIO EM FIBRA DE POLIESTER PURA, COM 1.1/2", REVESTIDA INTERNAMENTE, COMPRIMENTO DE 15M - FORNECIMENTO E INSTALAÇÃO. AF_10/2020',101915,'UN',1);
INSERT INTO db_gfc.tb_itens_produtos (id_cat,descricao,codigo,unidade,ativo) VALUES
	 (51,'Instalações especiais mat e mo emp',NULL,'vb',1),
	 (52,'Elevador.',NULL,'vb',1),
	 (52,'Elevador portadores de defic especiais.',NULL,'vb',1),
	 (52,'Pressurização de escada - mat e mo emp',NULL,'vb',1),
	 (52,'Instalação Infra ar cond tipo split - mat e mo emp',NULL,'UN',1),
	 (53,'Luminárias.',NULL,'vb',1),
	 (53,'Instalações prediais - mat e mo emp',NULL,'vb',1),
	 (54,'LAVATÓRIO LOUÇA BRANCA COM COLUNA, *44 X 35,5* CM, PADRÃO POPULAR - FORNECIMENTO E INSTALAÇÃO. AF_01/2020',86902,'UN',1),
	 (54,'VASO SANITÁRIO SIFONADO COM CAIXA ACOPLADA LOUÇA BRANCA - PADRÃO MÉDIO, INCLUSO ENGATE FLEXÍVEL EM METAL CROMADO, 1/2 X 40CM - FORNECIMENTO E INSTALAÇÃO. AF_01/2020',86932,'UN',1),
	 (54,'TANQUE DE LOUÇA BRANCA COM COLUNA, 30L OU EQUIVALENTE - FORNECIMENTO E INSTALAÇÃO. AF_01/2020',86872,'UN',1);
INSERT INTO db_gfc.tb_itens_produtos (id_cat,descricao,codigo,unidade,ativo) VALUES
	 (54,'CUBA DE EMBUTIR OVAL EM LOUÇA BRANCA, 35 X 50CM OU EQUIVALENTE, INCLUSO VÁLVULA E SIFÃO TIPO GARRAFA EM METAL CROMADO - FORNECIMENTO E INSTALAÇÃO. AF_01/2020',86938,'UN',1),
	 (54,'TORNEIRA CROMADA 1/2" OU 3/4" PARA TANQUE, PADRÃO POPULAR - FORNECIMENTO E INSTALAÇÃO. AF_01/2020',86913,'UN',1),
	 (54,'TORNEIRA CROMADA DE MESA, 1/2" OU 3/4", PARA LAVATÓRIO, PADRÃO MÉDIO - FORNECIMENTO E INSTALAÇÃO. AF_01/2020',86915,'UN',1),
	 (54,'TORNEIRA CROMADA TUBO MÓVEL, DE MESA, 1/2" OU 3/4", PARA PIA DE COZINHA, PADRÃO ALTO - FORNECIMENTO E INSTALAÇÃO. AF_01/2020',86909,'UN',1),
	 (54,'ACABAMENTO MONOCOMANDO PARA CHUVEIRO - FORNECIMENTO E INSTALAÇÃO. AF_01/2020',100857,'UN',1),
	 (54,'CUBA DE EMBUTIR RETANGULAR DE AÇO INOXIDÁVEL, 56 X 33 X 12 CM - FORNECIMENTO E INSTALAÇÃO. AF_01/2020',100852,'UN',1),
	 (54,'MICTÓRIO SIFONADO LOUÇA BRANCA - PADRÃO MÉDIO - FORNECIMENTO E INSTALAÇÃO. AF_01/2020',100858,'UN',1),
	 (54,'BARRA DE APOIO EM "L", EM ACO INOX POLIDO 70 X 70 CM, FIXADA NA PAREDE - FORNECIMENTO E INSTALACAO. AF_01/2020',100863,'UN',1),
	 (54,'BARRA DE APOIO EM "L", EM ACO INOX POLIDO 80 X 80 CM, FIXADA NA PAREDE - FORNECIMENTO E INSTALACAO. AF_01/2020',100864,'UN',1),
	 (54,'BARRA DE APOIO LATERAL ARTICULADA, COM TRAVA, EM ACO INOX POLIDO, FIXADA NA PAREDE - FORNECIMENTO E INSTALAÇÃO. AF_01/2020',100865,'UN',1);
INSERT INTO db_gfc.tb_itens_produtos (id_cat,descricao,codigo,unidade,ativo) VALUES
	 (54,'BARRA DE APOIO RETA, EM ACO INOX POLIDO, COMPRIMENTO 60CM, FIXADA NA PAREDE - FORNECIMENTO E INSTALAÇÃO. AF_01/2020',100866,'UN',1),
	 (54,'BARRA DE APOIO RETA, EM ACO INOX POLIDO, COMPRIMENTO 70 CM, FIXADA NA PAREDE - FORNECIMENTO E INSTALAÇÃO. AF_01/2020',100867,'UN',1),
	 (54,'BARRA DE APOIO RETA, EM ACO INOX POLIDO, COMPRIMENTO 80 CM, FIXADA NA PAREDE - FORNECIMENTO E INSTALAÇÃO. AF_01/2020',100868,'UN',1),
	 (54,'BARRA DE APOIO RETA, EM ACO INOX POLIDO, COMPRIMENTO 90 CM, FIXADA NA PAREDE - FORNECIMENTO E INSTALAÇÃO. AF_01/2020',100869,'UN',1),
	 (55,'BANCADA DE GRANITO CINZA POLIDO, DE 0,50 X 0,60 M, PARA LAVATÓRIO - FORNECIMENTO E INSTALAÇÃO. AF_01/2020',86895,'UN',1),
	 (55,'BANCADA DE GRANITO CINZA POLIDO, DE 1,50 X 0,60 M, PARA PIA DE COZINHA - FORNECIMENTO E INSTALAÇÃO. AF_01/2020',86889,'UN',1),
	 (55,'BANCADA DE MÁRMORE BRANCO POLIDO, DE 0,50 X 0,60 M, PARA LAVATÓRIO - FORNECIMENTO E INSTALAÇÃO. AF_01/2020',86899,'UN',1),
	 (55,'BANCADA DE MÁRMORE BRANCO POLIDO, DE 1,50 X 0,60 M, PARA PIA DE COZINHA - FORNECIMENTO E INSTALAÇÃO. AF_01/2020',86893,'UN',1),
	 (55,'BANCADA DE MÁRMORE SINTÉTICO 120 X 60CM, COM CUBA INTEGRADA, INCLUSO SIFÃO TIPO FLEXÍVEL EM PVC, VÁLVULA EM PLÁSTICO CROMADO TIPO AMERICANA E TORNEIRA CROMADA LONGA, DE PAREDE, PADRÃO POPULAR - FORNECIMENTO E INSTALAÇÃO. AF_01/2020',86934,'UN',1),
	 (56,'PLANTIO DE FORRAÇÃO. AF_07/2024',98505,'M2',1);
INSERT INTO db_gfc.tb_itens_produtos (id_cat,descricao,codigo,unidade,ativo) VALUES
	 (56,'PLANTIO DE GRAMA ESMERALDA OU SÃO CARLOS OU CURITIBANA, EM PLACAS. AF_07/2024',103946,'M2',1),
	 (56,'PLANTIO DE GRAMA EM PAVIMENTO CONCREGRAMA. AF_07/2024',98503,'M2',1),
	 (56,'PISO ASFÁLTICO PARA QUADRA POLIESPORTIVA - FORNECIMENTO E INSTALAÇÃO. AF_03/2022',103780,'M2',1),
	 (56,'PISO DE GRAMA SINTÉTICA PARA QUADRA POLIESPORTIVA - FORNECIMENTO E INSTALAÇÃO. AF_03/2022',103781,'M2',1),
	 (57,'Decoração',NULL,'vb',1),
	 (57,'Eventuais',NULL,'vb',1),
	 (57,'Manutenção pós obra (1% do custo total)',NULL,'vb',1),
	 (58,'PISO EM PEDRA PORTUGUESA ASSENTADO SOBRE ARGAMASSA SECA DE CIMENTO E AREIA, TRAÇO 1:3, REJUNTADO COM CIMENTO COMUM. AF_05/2020',101090,'M2',1),
	 (58,'ASSENTAMENTO DE GUIA (MEIO-FIO) EM TRECHO RETO, CONFECCIONADA EM CONCRETO PRÉ-FABRICADO, DIMENSÕES 100X15X13X20 CM (COMPRIMENTO X BASE INFERIOR X BASE SUPERIOR X ALTURA). AF_01/2024',94275,'M',1),
	 (58,'PISO PODOTÁTIL DE ALERTA OU DIRECIONAL, DE CONCRETO, ASSENTADO SOBRE ARGAMASSA. AF_03/2024',104658,'M2',1);
INSERT INTO db_gfc.tb_itens_produtos (id_cat,descricao,codigo,unidade,ativo) VALUES
	 (58,'EXECUÇÃO DE PASSEIO EM PISO INTERTRAVADO, COM BLOCO 16 FACES DE 22 X 11 CM, ESPESSURA 6 CM. AF_10/2022',92402,'M2',1),
	 (1,'teste',0,'ts',1);

INSERT INTO db_gfc.tb_categorias (id_cat_pai,descricao,agrupador,ativo) VALUES
	 (NULL,'Serviços Iniciais','SINAPI',1),
	 (NULL,'Serviços Gerais','SINAPI',1),
	 (NULL,'Infra-Estrutura','SINAPI',1),
	 (NULL,'Supra-Estrutura','SINAPI',1),
	 (NULL,'Alvenaria','SINAPI',1),
	 (NULL,'Esquadrias','SINAPI',1),
	 (NULL,'Revestimentos','SINAPI',1),
	 (NULL,'Pavimentação','SINAPI',1),
	 (NULL,'Peitoris/Soleiras/Rodapé/Muretas','SINAPI',1),
	 (NULL,'Pintura','SINAPI',1);
INSERT INTO db_gfc.tb_categorias (id_cat_pai,descricao,agrupador,ativo) VALUES
	 (NULL,'Cobertura','SINAPI',1),
	 (NULL,'Impermeabilização','SINAPI',1),
	 (NULL,'Instalações (no SINAPI são abertos em muito itens, em 99% dos casos são recebidos tanto do cliente quanto do fornecedor uma verba)','SINAPI',1),
	 (NULL,'Bancas/Louças/Metais/Guarnições','SINAPI',1),
	 (NULL,'Complementação da Obra','SINAPI',1),
	 (1,'Projetos e Consultorias (não possui códigos no SINAPI)','SINAPI',1),
	 (1,'Serviços Iniciais','SINAPI',1),
	 (2,'Instalação do Canteiro','SINAPI',1),
	 (2,'Tapume e Barracão','SINAPI',1),
	 (2,'Equipamentos','SINAPI',1);
INSERT INTO db_gfc.tb_categorias (id_cat_pai,descricao,agrupador,ativo) VALUES
	 (2,'Diversos (não possui códigos no SINAPI)','SINAPI',1),
	 (2,'Administração da Obra até Habite-se','SINAPI',1),
	 (2,'Proteção da Obra','SINAPI',1),
	 (2,'Administração Pós Obra (mesmos códigos da administração da obra, SINAPI não possui divisão)','SINAPI',1),
	 (2,'Serviços Técnicos (não possui códigos no SINAPI)','SINAPI',1),
	 (3,'Movimento de Terra','SINAPI',1),
	 (3,'Fundações Diretas','SINAPI',1),
	 (3,'Fundações Indiretas','SINAPI',1),
	 (4,'Concreto','SINAPI',1),
	 (4,'Forma','SINAPI',1);
INSERT INTO db_gfc.tb_categorias (id_cat_pai,descricao,agrupador,ativo) VALUES
	 (4,'Armação','SINAPI',1),
	 (5,'Alvenaria de Tijolo de Barro','SINAPI',1),
	 (5,'Alvenaria de Bloco de Concreto','SINAPI',1),
	 (5,'Serviços Gerais de Alvenaria','SINAPI',1),
	 (6,'Esquadria de Madeira','SINAPI',1),
	 (6,'Esquadria Metalica','SINAPI',1),
	 (6,'Esquadria de Ferro','SINAPI',1),
	 (6,'Ferragens','SINAPI',1),
	 (7,'Revestimento Interno','SINAPI',1),
	 (7,'Revestimento Externo','SINAPI',1);
INSERT INTO db_gfc.tb_categorias (id_cat_pai,descricao,agrupador,ativo) VALUES
	 (8,'Pavimentação Interna','SINAPI',1),
	 (9,'Rodapés','SINAPI',1),
	 (9,'Soleiras','SINAPI',1),
	 (9,'Peitoris','SINAPI',1),
	 (9,'Muretas','SINAPI',1),
	 (9,'Divisórias','SINAPI',1),
	 (10,'Pintura Interna','SINAPI',1),
	 (10,'Pintura Externa','SINAPI',1),
	 (11,'Cobertura','SINAPI',1),
	 (12,'Impermeabilização','SINAPI',1);
INSERT INTO db_gfc.tb_categorias (id_cat_pai,descricao,agrupador,ativo) VALUES
	 (13,'Instalações Especiais','SINAPI',1),
	 (13,'Instalações Mecanicas','SINAPI',1),
	 (13,'Instalações Prediais','SINAPI',1),
	 (14,'Louças e Metais','SINAPI',1),
	 (14,'Bancas e Guarnições','SINAPI',1),
	 (15,'Complementação da obra','SINAPI',1),
	 (15,'Diversos  (não possui códigos no SINAPI, itens que recebem valores informados pela construtora)','SINAPI',1),
	 (15,'Drenagem e Pavimentação Externa','SINAPI',1);
