from enum import Enum


class TipoAcessos(Enum):
    ADM = 'Administrador'
    EDT = 'Editor'
    ADMINISTRADOR = 'ADM'
    EDITOR = 'EDT'

    def to_list():
        return [('ADM', 'Administrador'),
                ('EDT', 'Editor'),]
