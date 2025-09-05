from datetime import datetime
from flask import session


class CtrlSessao:
    def __init__(self, name):
        self._name = name

    def set(self, value):
        session[self._name] = value
        session.modified = True

    def get(self):
        try:
            return session.get(self._name)
        except:
            return None

    def has(self):
        try:
            data = session.get(self._name)
            return data != None
        except:
            return False

    def clear(self):
        session.pop(self._name, default=None)
        self.set(None)


class IdEmpreend(CtrlSessao):
    def __init__(self):
        super().__init__('idEmpreend')


class NmEmpreend(CtrlSessao):
    def __init__(self):
        super().__init__('nmEmpreend')


class DtCarga(CtrlSessao):
    def __init__(self):
        super().__init__('dtCarga')


class IdOrca(CtrlSessao):
    def __init__(self):
        super().__init__('idOrca')


class IdMedicao(CtrlSessao):
    def __init__(self):
        super().__init__('idMedicao')


class MesVigencia(CtrlSessao):
    def __init__(self):
        super().__init__('mesVigencia')


class AnoVigencia(CtrlSessao):
    def __init__(self):
        super().__init__('anoVigencia')


class CodBanco(CtrlSessao):
    def __init__(self):
        super().__init__('codBanco')


class Vigencia(CtrlSessao):
    def __init__(self):
        super().__init__('vigencia')

    def init(self):
        Vigencia().save(datetime.now().strftime('%Y-%m'))

    def getMonth(self):
        vig = Vigencia().get()
        return vig[1]

    def getYear(self):
        vig = Vigencia().get()
        return vig[0]

    def save(self, vigencia: str):
        vig = vigencia.split('-')
        Vigencia().set(vig)
