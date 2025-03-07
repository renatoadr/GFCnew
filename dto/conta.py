#model

class conta:

    def __init__(self):
        pass

    #private members
    __idEmpreend = -1
    __mesVigencia = ""
    __anoVigencia = ""
    __vlLiberacao = -1
    __vlMaterialEstoque = -1
    __vlAporteConstrutora = -1
    __vlReceitaRecebiveis = -1
    __vlPagtoObra = -1
    __vlPagtoRh = -1
    __vlDiferenca = -1
    __vlSaldo = -1

    #Getters

    def getIdEmpreend(self):
        return self.__idEmpreend
    def getMesVigencia(self):
        return self.__mesVigencia
    def getAnoVigencia(self):
        return self.__anoVigencia
    def getVlLiberacao(self):
        return self.__vlLiberacao
    def getVlMaterialEstoque(self):
        return self.__vlMaterialEstoque
    def getVlAporteConstrutora(self):
        return self.__vlAporteConstrutora
    def getVlReceitaRecebiveis(self):
        return self.__vlReceitaRecebiveis
    def getVlPagtoObra(self):
        return self.__vlPagtoObra
    def getVlPagtoRh(self):
        return self.__vlPagtoRh
    def getVlDiferenca(self):
        return self.__vlDiferenca
    def getVlSaldo(self):
        return self.__vlSaldo
     
    #Setters

    def setIdEmpreend(self, param):
        self.__idEmpreend = param
    def setMesVigencia(self, param):
        self.__mesVigencia = param
    def setAnoVigencia(self, param):
        self.__anoVigencia = param
    def setVlLiberacao(self, param):
        self.__vlLiberacao = param
    def setVlMaterialEstoque(self, param):
        self.__vlMaterialEstoque = param
    def setVlAporteConstrutora(self, param):
        self.__vlAporteConstrutora = param
    def setVlReceitaRecebiveis(self, param):
        self.__vlReceitaRecebiveis = param
    def setVlPagtoObra(self, param):
        self.__vlPagtoObra = param
    def setVlPagtoRh(self, param):
        self.__vlPagtoRh = param
    def setVlDiferenca(self, param):
        self.__vlDiferenca = param
    def setVlSaldo(self, param):
        self.__vlSaldo = param