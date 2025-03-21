#model

class medicao:

    def __init__(self):
        pass
 
    #private members
    __idMedicao = -1
    __idEmpreend = -1
    __mesVigencia = ""
    __anoVigencia = ""
    __dtCarga= ""
    __nrMedicao = -1
    __percPrevistoAcumulado = -1
    __percRealizadoAcumulado = -1
    __percDiferenca = -1
    __percPrevistoPeriodo = -1
    
    #Getters

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
     
    #Setters

    def setIdMedicao(self, param):
        self.__idMedicao = param
    def setIdEmpreend(self, param):
        self.__idEmpreend = param
    def setMesVigencia(self, param):
        self.__mesVigencia = param
    def setAnoVigencia(self, param):
        self.__anoVigencia = param
    def setDtCarga(self, param):
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
