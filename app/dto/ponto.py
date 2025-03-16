#model

class ponto:

    def __init__(self):
        pass

    #private members
    __idEmpreend = -1
    __mesVigencia = ""
    __anoVigencia = ""
    __tipo = ""
    __historico = ""
    __status = ""
    __observacao = ""
    
    #Getters

    def getIdEmpreend(self):
        return self.__idEmpreend
    def getMesVigencia(self):
        return self.__mesVigencia
    def getAnoVigencia(self):
        return self.__anoVigencia
    def getTipo(self):
        return self.__tipo
    def getHistorico(self):
        return self.__historico
    def getStatus(self):
        return self.__status
    def getObservacao(self):
        return self.__observacao
     
    #Setters

    def setIdEmpreend(self, param):
        self.__idEmpreend = param
    def setMesVigencia(self, param):
        self.__mesVigencia = param
    def setAnoVigencia(self, param):
        self.__anoVigencia = param
    def setTipo(self, param):
        self.__tipo = param
    def setHistorico(self, param):
        self.__historico = param
    def setStatus(self, param):
        self.__status = param
    def setObservacao(self, param):
        self.__observacao = param
