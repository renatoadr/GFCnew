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
  'dt_medicao' DATE NOT NULL,
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
  `nm_torre` VARCHAR(20) NOT NULL,
  `qt_unidade` INT NOT NULL,
  `qt_andar` INT NOT NULL,
  `qt_coberturas` INT NULL,
  `prefix_cobertura` VARCHAR(20) NULL,
  `num_apt_um_andar_um` INT NOT NULL,
  `vl_unidade` DECIMAL(15,2) NULL,
  `vl_cobertura` DECIMAL(15,2) NULL,
   PRIMARY KEY (`id_torre`)
)
ENGINE = InnoDB;
CREATE TABLE  IF NOT EXISTS `tb_unidades` (
  `id_unidade` INT AUTO_INCREMENT NOT NULL,
  `id_empreendimento` INT NOT NULL,
  `id_torre` INT NOT NULL,
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
