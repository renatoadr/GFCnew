from datetime import datetime
from sqlalchemy import and_

from core.sync_elonet.domainEnum import DomainElonetEnum
from core.model.empreendimento import Empreendimento
from core.model.sync_elonet import SyncElonet
from core.model.unidade import Unidade
from core.model.cliente import Cliente
from core.model.torre import Torre
from core.model.conta import Conta
from core.db_connect import Model
from utils.logger import logger
from core.db_connect import db
import re


class SyncDataElonet:

    def __processarDados__(
        self,
        data: dict,
        velhoEntity: Model,
        novoEntity: Model,
        dominio: DomainElonetEnum,
        campos_ignorados: list[str] = []
    ):
        for key, value in data.items():
            if key in campos_ignorados:
                logger.info(
                    f'Campo {key} está na lista de ignorados. Pulando comparação.')
                continue

            if velhoEntity is not None and hasattr(velhoEntity, key):

                oldValue = getattr(velhoEntity, key)
                if oldValue != value:
                    logger.info(
                        f'Alteração detectada no campo {key}: de {oldValue} para {value}')
                    setattr(novoEntity, key, value)
                    syncElonet = SyncElonet(
                        chave_dominio=dominio.value,
                        nm_campo=key,
                        valor_antigo=str(oldValue),
                        novo_valor=str(value)
                    )
                    syncElonet.save()
                    logger.info(
                        f'Registro salvo na tabela de sincronização campo {key}')
                else:
                    setattr(novoEntity, key, oldValue)
                    logger.info(f'Nenhuma alteração no campo {key}')
            else:
                setattr(novoEntity, key, value)
                logger.info(f'Campo {key} definido com valor {value}')
        try:
            novoEntity.save()
        except Exception as e:
            logger.exception(f'Erro ao salvar entidade: {e}')
            db.session.rollback()

    def processarClientes(self, data):
        logger.info('Processando dados de Clientes...')
        doc = re.sub(r'\D', '', data['cpf_cnpj'])
        cliente = Cliente.query.filter(
            Cliente.cpf_cnpj == doc
        ).first()

        novoCliente = Cliente()
        if not cliente:
            novoCliente.cpf_cnpj = doc
            logger.info(f'Cliente com CPF/CNPJ {doc} não encontrado.')
        else:
            novoCliente.cpf_cnpj = cliente.cpf_cnpj
            logger.info(f'Cliente com CPF/CNPJ {doc} encontrado.')

        data['cpf_cnpj'] = doc
        data['tel'] = re.sub(r'\D', '', data.get(
            'tel')) if data.get('tel') else None

        self.__processarDados__(
            data,
            cliente,
            novoCliente,
            DomainElonetEnum.CLIENTE,
            campos_ignorados=['cpf_cnpj']
        )

        if not cliente:
            logger.info(f'Novo cliente criado: {novoCliente.cpf_cnpj}')
        else:
            logger.info(
                f'Cliente atualizado com sucesso: {novoCliente.cpf_cnpj}')

    def processarEmpreendimentos(self, data):
        logger.info(f'Processando dados de Empreendimentos...')
        empreendimento = Empreendimento.query.filter(
            Empreendimento.id_empreed_elonet == data['id_empreed_elonet']
        ).first()

        novoEmpreendimento = Empreendimento()
        if not empreendimento:
            novoEmpreendimento.id_empreed_elonet = data['id_empreed_elonet']
            logger.info(
                f'Empreendimento com ID Elonet {data["id_empreed_elonet"]} não encontrado.')
        else:
            novoEmpreendimento.id_empreed_elonet = empreendimento.id_empreed_elonet
            novoEmpreendimento.id_empreendimento = empreendimento.id_empreendimento
            logger.info(
                f'Empreendimento encontrado: {empreendimento.nm_empreendimento}')

        novoEmpreendimento.indice_garantia = data.get(
            'indice_garantia') or 0.01
        nomes = data.get('nm_empreendimento').strip().split(' ')
        apelido = ''.join([palavra[0] for palavra in nomes if palavra])
        novoEmpreendimento.apelido = apelido.upper()

        data['cep'] = re.sub(r'\D', '', data.get(
            'cep')) if data.get('cep') else None
        data['previsao_entrega'] = datetime.strptime(data.get(
            'previsao_entrega'), '%Y-%m-%d').date() if data.get('previsao_entrega') else None

        self.__processarDados__(
            data,
            empreendimento,
            novoEmpreendimento,
            DomainElonetEnum.EMPREENDIMENTO,
            campos_ignorados=['id_empreed_elonet']
        )

        if not empreendimento:
            logger.info(
                f'Novo empreendimento criado: {novoEmpreendimento.nm_empreendimento}')
        else:
            logger.info(
                f'Empreendimento atualizado com sucesso: {novoEmpreendimento.nm_empreendimento}')

    def processarTorres(self, data):
        logger.info('Processando dados de Torres...')
        torre = Torre.query.filter(
            and_(
                Torre.id_empreed_elonet == data['id_empreed_elonet'],
                Torre.id_torre_elonet == data['id_torre_elonet']
            )
        ).first()

        novaTorre = Torre()
        if not torre:
            emp = Empreendimento.query.filter(
                Empreendimento.id_empreed_elonet == data['id_empreed_elonet']
            ).first()
            if not emp:
                logger.info(
                    f'Empreendimento com ID Elonet {data["id_empreed_elonet"]} não encontrado.')
                return
            novaTorre.id_empreendimento = emp.id_empreendimento
            novaTorre.id_empreed_elonet = data['id_empreed_elonet']
            novaTorre.id_torre_elonet = data['id_torre_elonet']

            logger.info(
                f'Torre com ID Elonet {data["id_torre_elonet"]} não encontrada.')
        else:
            novaTorre.id_empreed_elonet = torre.id_empreed_elonet
            novaTorre.id_empreendimento = torre.id_empreendimento
            novaTorre.id_torre_elonet = torre.id_torre_elonet
            novaTorre.id_torre = torre.id_torre
            logger.info(f'Torre encontrada: {torre.nm_torre}')

        self.__processarDados__(
            data,
            torre,
            novaTorre,
            DomainElonetEnum.TORRES,
            campos_ignorados=['id_empreed_elonet', 'id_torre_elonet']
        )

        if not torre:
            logger.info(f'Nova torre criada: {novaTorre.nm_torre}')
        else:
            logger.info(f'Torre atualizada com sucesso: {novaTorre.nm_torre}')

    def processarUnidades(self, data):
        logger.info('Processando dados de Unidades...')

        torre = Torre.query.filter(
            and_(
                Torre.id_empreed_elonet == data['id_empreed_elonet'],
                Torre.id_torre_elonet == data['id_torre_elonet']
            )
        ).first()

        if not torre:
            logger.info(
                f'Torre com ID Elonet {data["id_torre_elonet"]} para empreendimento {data['id_empreed_elonet']} não encontrado.')
            return

        unidade = Unidade.query.filter(
            and_(
                Unidade.id_empreed_elonet == data['id_empreed_elonet'],
                Unidade.id_torre_elonet == data['id_torre_elonet'],
                Unidade.unidade == data['unidade'],
                Unidade.ac_historico == None
            )).first()

        novaUnidade = Unidade()

        chaves = data.get('vl_chaves') or 0.0
        preChaves = data.get('vl_pre_chaves') or 0.0
        posChaves = data.get('vl_pos_chaves') or 0.0

        novaUnidade.vl_receber = chaves + preChaves + posChaves

        if not unidade:
            now = datetime.now()
            novaUnidade.id_empreed_elonet = data['id_empreed_elonet']
            novaUnidade.id_empreendimento = torre.id_empreendimento
            novaUnidade.id_torre_elonet = data['id_torre_elonet']
            novaUnidade.id_torre = torre.id_torre
            novaUnidade.unidade = data['unidade']
            novaUnidade.mes_vigencia = str(now.month).zfill(2)
            novaUnidade.ano_vigencia = str(now.year)

            logger.info(
                f'Unidade com ID Elonet {data["id_registro"]} não encontrada.')
        else:
            novaUnidade.id_empreed_elonet = unidade.id_empreed_elonet
            novaUnidade.id_empreendimento = unidade.id_empreendimento
            novaUnidade.id_torre_elonet = unidade.id_torre_elonet
            novaUnidade.id_torre = unidade.id_torre
            novaUnidade.mes_vigencia = unidade.mes_vigencia
            novaUnidade.ano_vigencia = unidade.ano_vigencia
            unidade.ac_historico = 'EDITADO_SINC'
            unidade.save()
            logger.info(f'Unidade encontrada: {unidade.id_unidade}')

        data['cpf_cnpj_comprador'] = re.sub(r'\D', '', data.get(
            'cpf_cnpj_comprador')) if data.get('cpf_cnpj_comprador') else None

        data['status'] = data.get(
            'status_financeiro').capitalize() if data.get('status_financeiro') else None

        self.__processarDados__(
            data,
            unidade,
            novaUnidade,
            DomainElonetEnum.UNIDADES,
            campos_ignorados=[
                'id_empreed_elonet',
                'id_unidade_elonet',
                'id_registro',
                'unidade'
            ]
        )

        numUnidade = int(data.get('unidade')) if data.get(
            'unidade') and data.get('unidade').isdigit() else None
        if torre.num_apt_um_andar_um is None or torre.num_apt_um_andar_um > numUnidade:
            torre.num_apt_um_andar_um = numUnidade
        if torre.vl_unidade is None or torre.vl_unidade > novaUnidade.vl_unidade:
            torre.vl_unidade = novaUnidade.vl_unidade
        torre.save()

        if not unidade:
            logger.info(f'Nova unidade criada: {novaUnidade.id_unidade}')
        else:
            logger.info(
                f'Unidade atualizada com sucesso: {novaUnidade.id_unidade}')

    def processarContas(self, data):
        logger.info('Processando dados de Contas...')

        conta = Conta.query.filter(
            Conta.id_empreed_elonet == data['id_empreed_elonet'],
            Conta.id_conta_elonet == data['id_registro']
        ).first()

        novaConta = Conta()
        if not conta:
            emp = Empreendimento.query.filter(
                Empreendimento.id_empreed_elonet == data['id_empreed_elonet']
            ).first()
            if not emp:
                logger.info(
                    f'Empreendimento com ID Elonet {data["id_empreed_elonet"]} não encontrado.')
                return
            novaConta.id_empreendimento = emp.id_empreendimento
            novaConta.id_empreed_elonet = data['id_empreed_elonet']
            novaConta.id_conta_elonet = data['id_registro']
            novaConta.vl_aporte_construtora = 0
            novaConta.vl_pagto_obra = 0
            novaConta.vl_pagto_rh = 0
            novaConta.vl_saldo = 0
            logger.info(
                f'Conta com ID Elonet {data["id_empreed_elonet"]} não encontrada.')
        else:
            novaConta.id_empreed_elonet = conta.id_empreed_elonet
            novaConta.id_empreendimento = conta.id_empreendimento
            novaConta.id_conta_elonet = conta.id_conta_elonet
            novaConta.id_conta = conta.id_conta
            novaConta.vl_aporte_construtora = conta.vl_aporte_construtora
            novaConta.vl_pagto_obra = conta.vl_pagto_obra
            novaConta.vl_pagto_rh = conta.vl_pagto_rh
            novaConta.vl_saldo = conta.vl_saldo
            logger.info(f'Conta encontrada: {conta.id_empreed_elonet}')

        if data.get('mes_referencia') is not None:
            ref = data['mes_referencia'].split('-')
            data['ano_vigencia'] = ref[0]
            data['mes_vigencia'] = ref[1]

        data['dt_carga'] = datetime.strptime(data.get(
            'data_registro'), '%Y-%m-%d') if data.get('data_registro') else None

        self.__processarDados__(
            data,
            conta,
            novaConta,
            DomainElonetEnum.CONTAS,
            campos_ignorados=[
                'id_empreed_elonet',
                'id_conta_elonet',
                'id_registro'
            ]
        )

        aportes = novaConta.vl_liberacao + \
            novaConta.vl_aporte_construtora + novaConta.vl_receita_recebiveis
        pagamentos = novaConta.vl_pagto_obra + novaConta.vl_pagto_rh
        novaConta.vl_diferenca = aportes - pagamentos - novaConta.vl_saldo
        novaConta.save()

        if not conta:
            logger.info(f'Nova conta criada: {novaConta}')
        else:
            logger.info(f'Conta atualizada com sucesso: {novaConta}')
