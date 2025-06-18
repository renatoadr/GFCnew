from enum import Enum


class StatusAgenda(Enum):
    NAO_INICIADO = 'Não Iniciado'
    EM_ANDAMENTO = 'Em Andamento'
    FINALIZADO = 'Finalizado'
    BLOQUEADO = 'Bloqueado'
    REJEITADO = 'Rejeitado'
    PENDENTE = 'Pendente'

    def to_name(chave: str):
        return StatusAgenda[chave].value

    def to_list():
        return [
            (StatusAgenda.NAO_INICIADO.name, StatusAgenda.NAO_INICIADO.value),
            (StatusAgenda.EM_ANDAMENTO.name, StatusAgenda.EM_ANDAMENTO.value),
            (StatusAgenda.FINALIZADO.name, StatusAgenda.FINALIZADO.value),
            (StatusAgenda.PENDENTE.name, StatusAgenda.PENDENTE.value),
            (StatusAgenda.BLOQUEADO.name, StatusAgenda.BLOQUEADO.value),
            (StatusAgenda.REJEITADO.name, StatusAgenda.REJEITADO.value),
        ]
