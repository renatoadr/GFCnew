CREATE DATABASE  IF NOT EXISTS `db_gfc`;
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
  `nm_banco` varchar(100) DEFAULT NULL,
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

CREATE TABLE  IF NOT EXISTS `tb_laudos` (
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

CREATE TABLE `tb_torres` (
  `id_torre` int NOT NULL AUTO_INCREMENT,
  `id_empreendimento` int NOT NULL,
  `nm_torre` varchar(20) NOT NULL,
  `qt_unidade` int NOT NULL,
  `qt_andar` int NOT NULL,
  `qt_coberturas` int DEFAULT NULL,
  `prefix_cobertura` varchar(20) DEFAULT NULL,
  `num_apt_um_andar_um` int NOT NULL,
  PRIMARY KEY (`id_torre`),
  KEY `idx_torres` (`id_empreendimento`,`id_torre`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

  CREATE TABLE `tb_unidades` (
  `id_unidade` int NOT NULL AUTO_INCREMENT,
  `id_empreendimento` int NOT NULL,
  `id_torre` int NOT NULL,
  `unidade` varchar(15) NOT NULL,
  `mes_vigencia` varchar(2) NOT NULL,
  `ano_vigencia` varchar(4) NOT NULL,
  `vl_unidade` decimal(10,2) DEFAULT NULL,
  `status` varchar(8) NOT NULL,
  `cpf_cnpj_comprador` varchar(15) DEFAULT NULL,
  `vl_pago` decimal(10,2) DEFAULT NULL,
  `dt_ocorrencia` datetime DEFAULT CURRENT_TIMESTAMP,
  `financiado` varchar(3) DEFAULT NULL,
  `vl_chaves` decimal(15,2) DEFAULT NULL,
  `vl_pre_chaves` decimal(15,2) DEFAULT NULL,
  `vl_pos_chaves` decimal(15,2) DEFAULT NULL,
  `ac_historico` varchar(15) DEFAULT NULL,
  PRIMARY KEY (`id_unidade`),
  KEY `idx_unidades` (`id_empreendimento`,`id_torre`,`unidade`,`mes_vigencia`,`ano_vigencia`)
) ENGINE=InnoDB AUTO_INCREMENT=31 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE IF NOT EXISTS `tb_usuario_empreendimento` (
  `id_usuario` int NOT NULL,
  `id_empreendimento` int NOT NULL,
  PRIMARY KEY (`id_usuario`,`id_empreendimento`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE IF NOT EXISTS `tb_usuarios` (
  `id_usuario` int NOT NULL AUTO_INCREMENT,
  `email` varchar(50) DEFAULT NULL,
  `senha` varchar(12) DEFAULT NULL,
  `tp_acesso` varchar(15) DEFAULT NULL,
  `nm_usuario` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id_usuario`),
  KEY `idx_email` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE `tb_consideracoes` (
  `id` int NOT NULL AUTO_INCREMENT,
  `campo` varchar(20) NOT NULL,
  `texto` varchar(120) NOT NULL,
  `dt_criado` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `ac_historico` varchar(45) DEFAULT NULL,
  `id_empreendimento` int NOT NULL,
  `dt_editado` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci
