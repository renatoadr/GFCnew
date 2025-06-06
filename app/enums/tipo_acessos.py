from enum import Enum


class TipoAcessos(Enum):
    ADM = 'Administrador'
    VST = 'Visitante'
    EDT = 'Editor'
    RT = 'Root'

    def to_name(acesso: str):
        return TipoAcessos[acesso].value

    def to_list():
        return [
            (TipoAcessos.ADM.name, TipoAcessos.ADM.value),
            (TipoAcessos.EDT.name, TipoAcessos.EDT.value),
            (TipoAcessos.VST.name, TipoAcessos.VST.value),
        ]
