from core.sync_elonet.get_data import GetData
from core.sync_elonet.sync_data import SyncDataElonet


class RunSyncElonet:
    def __send_message__(
        self,
        msg=None,
        step=None,
        totalStep=None,
        subMsg=None,
        subStep=None,
        totalSubStep=None,
        in_progress=True
    ):
        main_msg = msg
        sub_task = None

        if step and totalStep:
            main_msg = f"Etapa: {step} de {totalStep}: {msg}"

        if subStep and totalSubStep:
            sub_task = f"Processando {subStep} de {totalSubStep}: {subMsg}"

        return {
            "main_task_message": main_msg,
            "sub_task_message": sub_task,
            "error": None,
            "in_progress": in_progress
        }

    def start(self):
        yield self.__send_message__(msg="Iniciado processo de sincronização Elonet...")
        yield self.__send_message__(msg="Preparando objetos de sincronização...")

        get_data = GetData()
        syncData = SyncDataElonet()

        yield self.__send_message__(msg="Obtendo dados de clientes...", step=1, totalStep=5)
        for pessoa in get_data.getEntitys("pessoas"):
            yield self.__send_message__(
                msg="Processando dados de clientes...",
                step=1,
                totalStep=5,
                subMsg=f"Aguarde...",
                subStep=pessoa['processing'],
                totalSubStep=pessoa['total']
            )
            syncData.processarClientes(pessoa['data'])

        yield self.__send_message__(msg="Obtendo dados de empreendimentos...", step=2, totalStep=5)
        for empreend in get_data.getEntitys("empreendimentos"):
            yield self.__send_message__(
                msg="Processando dados de empreendimentos...",
                step=2,
                totalStep=5,
                subMsg=f"Aguarde...",
                subStep=empreend['processing'],
                totalSubStep=empreend['total']
            )
            syncData.processarEmpreendimentos(empreend['data'])

        yield self.__send_message__(msg="Obtendo dados de torres...", step=3, totalStep=5)
        for torre in get_data.getEntitys("torres"):
            yield self.__send_message__(
                msg="Processando dados de torres...",
                step=3,
                totalStep=5,
                subMsg=f"Aguarde...",
                subStep=torre['processing'],
                totalSubStep=torre['total']
            )
            syncData.processarTorres(torre['data'])

        yield self.__send_message__(msg="Obtendo dados de unidades...", step=4, totalStep=5)
        for unidade in get_data.getEntitys("unidades"):
            yield self.__send_message__(
                msg="Processando dados de unidades...",
                step=4,
                totalStep=5,
                subMsg=f"Aguarde...",
                subStep=unidade['processing'],
                totalSubStep=unidade['total']
            )
            syncData.processarUnidades(unidade['data'])

        yield self.__send_message__(msg="Obtendo dados de contas...", step=5, totalStep=5)
        for conta in get_data.getEntitys("contas"):
            yield self.__send_message__(
                msg="Processando dados de contas...",
                step=5,
                totalStep=5,
                subMsg=f"Aguarde...",
                subStep=conta['processing'],
                totalSubStep=conta['total']
            )
            syncData.processarContas(conta['data'])

        yield self.__send_message__(msg="Sincronização Elonet finalizada com sucesso.", in_progress=False)
