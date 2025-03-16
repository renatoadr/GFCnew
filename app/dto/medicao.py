#model

class medicao:

    def __init__(self):
        pass
 
    #private members
    __idEmpreend = -1
    __mesVigencia = ""
    __anoVigencia = ""
    __nrMedicao = -1
    __percPrevistoAcumulado = -1
    __percRealizadoAcumulado = -1
    __percPrevistoPeriodo = -1
    
    #Getters

    def getIdEmpreend(self):
        return self.__idEmpreend
    def getMesVigencia(self):
        return self.__mesVigencia
    def getAnoVigencia(self):
        return self.__anoVigencia
    def getNrMedicao(self):
        return self.__nrMedicao
    def getPercPrevistoAcumulado(self):
        return self.__percPrevistoAcumulado
    def getPercRealizadoAcumulado(self):
        return self.__percRealizadoAcumulado
    def getPercPrevistoPeriodo(self):
        return self.__percPrevistoPeriodo
     
    #Setters

    def setIdEmpreend(self, param):
        self.__idEmpreend = param
    def setMesVigencia(self, param):
        self.__mesVigencia = param
    def setAnoVigencia(self, param):
        self.__anoVigencia = param
    def setNrMedicao(self, param):
        self.__nrMedicao = param
    def setPercPrevistoAcumulado(self, param):
        self.__percPrevistoAcumulado = param
    def setPercRealizadoAcumulado(self, param):
        self.__percRealizadoAcumulado = param
    def setPercPrevistoPeriodo(self, param):
        self.__percPrevistoPeriodo = param
