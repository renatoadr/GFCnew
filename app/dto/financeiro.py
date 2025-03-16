#model

class financeiro:

    def __init__(self):
        pass

    #private members
    __idEmpreend = -1
    __mesVigencia = ""
    __anoVigencia = ""
    __historico = ""
    __percFinanceiro = -1
    __vlFinanceiro = -1
    
    #Getters

    def getIdEmpreend(self):
        return self.__idEmpreend
    def getMesVigencia(self):
        return self.__mesVigencia
    def getAnoVigencia(self):
        return self.__anoVigencia
    def getHistorico(self):
        return self.__historico
    def getPercFinanceiro(self):
        return self.__percFinanceiro
    def getVlFinanceiro(self):
        return self.__vlFinanceiro
     
    #Setters

    def setIdEmpreend(self, param):
        self.__idEmpreend = param
    def setMesVigencia(self, param):
        self.__mesVigencia = param
    def setAnoVigencia(self, param):
        self.__anoVigencia = param
    def setHistorico(self, param):
        self.__historico = param
    def setPercFinanceiro(self, param):
        self.__percFinanceiro = param
    def setVlFinanceiro(self, param):
        self.__vlFinanceiro = param
