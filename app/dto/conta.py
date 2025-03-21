#model

class conta:

    def __init__(self):
        pass

    #private members
    __idconta = -1
    __idEmpreend = -1
    __mesVigencia = ""
    __anoVigencia = ""
    __dtCarga = ""
    __vlLiberacao = -1
    __vlAporteConstrutora = -1
    __vlReceitaRecebiveis = -1
    __vlPagtoObra = -1
    __vlPagtoRh = -1
    __vlDiferenca = -1
    __vlSaldo = -1

    #Getters

    def getIdConta(self):
        return self.__idConta
    def getIdEmpreend(self):
        return self.__idEmpreend
    def getMesVigencia(self):
        return self.__mesVigencia
    def getAnoVigencia(self):
        return self.__anoVigencia
    def getDtCarga(self):
        return self.__dtCarga
    def getVlLiberacao(self):
        return self.__vlLiberacao
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

    def setIdConta(self, param):
        self.__idConta = param
    def setIdEmpreend(self, param):
        self.__idEmpreend = param
    def setMesVigencia(self, param):
        self.__mesVigencia = param
    def setAnoVigencia(self, param):
        self.__anoVigencia = param
    def setDtCarga(self, param):
        self.__dtCarga = param
    def setVlLiberacao(self, param):
        self.__vlLiberacao = param
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