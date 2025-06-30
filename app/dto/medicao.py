# model
from datetime import datetime


class medicao:

    def __init__(self):
        pass

    # private members
    __idMedicao = -1
    __idEmpreend = -1
    __mesVigencia = ""
    __anoVigencia = ""
    __dtCarga = ""
    __nrMedicao = -1
    __percPrevistoAcumulado = -1
    __percRealizadoAcumulado = -1
    __percDiferenca = -1
    __percPrevistoPeriodo = -1
    __percRealizadoPeriodo = -1
    __dtMedicao = ""

    # Getters

    def getIdMedicao(self):
        return self.__idMedicao

    def getIdEmpreend(self):
        return self.__idEmpreend

    def getMesVigencia(self):
        return self.__mesVigencia

    def getAnoVigencia(self):
        return self.__anoVigencia

    def getDtCarga(self):
        return self.__dtCarga

    def getNrMedicao(self):
        return self.__nrMedicao

    def getPercPrevistoAcumulado(self):
        return self.__percPrevistoAcumulado

    def getPercRealizadoAcumulado(self):
        return self.__percRealizadoAcumulado

    def getPercDiferenca(self):
        return self.__percDiferenca

    def getPercPrevistoPeriodo(self):
        return self.__percPrevistoPeriodo

    def getPercRealizadoPeriodo(self):
        return self.__percRealizadoPeriodo

    def getDataMedicao(self):
        return self.__dtMedicao

    # Setters

    def setIdMedicao(self, param):
        self.__idMedicao = param

    def setIdEmpreend(self, param):
        self.__idEmpreend = param

    def setMesVigencia(self, param):
        self.__mesVigencia = param

    def setAnoVigencia(self, param):
        self.__anoVigencia = param

    def setDtCarga(self, param):
        if param is not None and isinstance(param, str):
            self.__dtCarga = datetime.strptime(param, '%Y-%m-%d %H:%M:%S')
        self.__dtCarga = param

    def setNrMedicao(self, param):
        self.__nrMedicao = param

    def setPercPrevistoAcumulado(self, param):
        self.__percPrevistoAcumulado = param

    def setPercRealizadoAcumulado(self, param):
        self.__percRealizadoAcumulado = param

    def setPercDiferenca(self, param):
        self.__percDiferenca = param

    def setPercPrevistoPeriodo(self, param):
        self.__percPrevistoPeriodo = param

    def setPercRealizadoPeriodo(self, param):
        self.__percRealizadoPeriodo = param

    def setDataMedicao(self, param):
        if param is not None and isinstance(param, str):
            self.__dtMedicao = datetime.strptime(param, '%Y-%m-%d')
        self.__dtMedicao = param
