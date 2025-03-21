#model

class nota:

    def __init__(self):
        pass

    #private members
    __idEmpreend = -1
    __mesVigencia = ""
    __anoVigencia = ""
    __dtCarga = ""
    __produto = ""
    __vlNotaFiscal = -1
    __vlEstoque = -1
    
    #Getters

    def getIdEmpreend(self):
        return self.__idEmpreend
    def getMesVigencia(self):
        return self.__mesVigencia
    def getAnoVigencia(self):
        return self.__anoVigencia
    def getDtCarga(self):
        return self.__dtCarga
    def getProduto(self):
        return self.__produto
    def getVlNotaFiscal(self):
        return self.__vlNotaFiscal
    def getVlEstoque(self):
        return self.__vlEstoque
     
    #Setters

    def setIdEmpreend(self, param):
        self.__idEmpreend = param
    def setMesVigencia(self, param):
        self.__mesVigencia = param
    def setAnoVigencia(self, param):
        self.__anoVigencia = param
    def setDtCarga(self, param):
        self.__dtCarga = param
    def setProduto(self, param):
        self.__produto = param
    def setVlNotaFiscal(self, param):
        self.__vlNotaFiscal = param
    def setVlEstoque(self, param):
        self.__vlEstoque = param
