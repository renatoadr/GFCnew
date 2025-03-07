#model

class orcamento:

    def __init__(self):
        pass

    #private members
    __idOrcamento = -1
    __idEmpreend  = -1
    __mesVigencia = ""
    __anoVigencia = ""
    __dtCarga = ""
    __item = ""
    __orcadoValor = -1 
    __fisicoValor = -1
    __fisicoPercentual = -1
    __fisicoSaldo = -1
    __financeiroValor = -1
    __financeiroPercentual = -1
    __financeiroSaldo = -1
    
    #Getters

    def getIdOrcamento(self):
        return self.__idOrcamento
    def getIdEmpreend(self):
        return self.__idEmpreend
    def getMesVigencia(self):
        return self.__mesVigencia
    def getAnoVigencia(self):
        return self.__anoVigencia
    def getDtCarga(self):
        return self.__dtCarga
    def getItem(self):
        return self.__item
    def getOrcadoValor(self):
        return self.__orcadoValor
    def getFisicoValor(self):
        return self.__fisicoValor
    def getFisicoPercentual(self):
        return self.__fisicoPercentual
    def getFisicoSaldo(self):
        return self.__fisicoSaldo
    def getFinanceiroValor(self):
        return self.__financeiroValor    
    def getFinanceiroPercentual(self):
        return self.__financeiroPercentual
    def getFinanceiroSaldo(self):
        return self.__financeiroSaldo
     
    #Setters

    def setIdOrcamento(self, param):
        self.__idOrcamento = param
    def setIdEmpreend(self, param):
        self.__idEmpreend = param
    def setMesVigencia(self, param):
        self.__mesVigencia = param
    def setAnoVigencia(self, param):
        self.__anoVigencia = param
    def setDtCarga(self, param):
        self.__dtCarga = param
    def setItem(self, param):
        self.__item = param
    def setOrcadoValor(self, param):
        self.__orcadoValor = param
    def setFisicoValor(self, param):
        self.__fisicoValor = param
    def setFisicoPercentual(self, param):
        self.__fisicoPercentual = param
    def setFisicoSaldo(self, param):
        self.__fisicoSaldo = param
    def setFinanceiroValor(self, param):
        self.__financeiroValor = param
    def setFinanceiroPercentual(self, param):
        self.__financeiroPercentual = param
    def setFinanceiroSaldo(self, param):
        self.__financeiroSaldo = param
