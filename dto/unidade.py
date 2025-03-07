#model

class unidade:

    def __init__(self):
        pass

    #private members
    __idUnidade = -1
    __idTorre = -1
    __nmTorre = ""       # esse campo não exite na tabela Unidades
    __idEmpreend = -1
    __unidade = "" 
    __mesVigencia = "" 
    __anoVigencia = ""
    __vlUnidade = ""
    __status = ""
    __cpfComprador = ""
    __vlPago = 0
    __dtOcorrencia = "" 
    __financiado = ""
    __vlChaves = 0
    __vlPreChaves = 0
    __vlPosChaves = 0
    __qtUnidade = -1
    __ttChaves = -1
    __ttPreChaves = -1
    __ttPosChaves = -1
    __ttStatus = -1
    __ttEstoque = -1
    __ttVenda = -1
    
    #Getters

    def getIdUnidade(self):
        return self.__idUnidade
    def getIdTorre(self):
        return self.__idTorre
    def getNmTorre(self):
        return self.__nmTorre          # esse campo não exite na tabela Unidades
    def getIdEmpreend(self):
        return self.__idEmpreend
    def getUnidade(self):
        return self.__unidade
    def getMesVigencia(self):
        return self.__mesVigencia
    def getAnoVigencia(self):
        return self.__anoVigencia
    def getVlUnidade(self):
        return self.__vlUnidade
    def getStatus(self):
        return self.__status
    def getCpfComprador(self):
        return self.__cpfComprador
    def getVlPago(self):
        return self.__vlPago
    def getDtOcorrencia(self):
        return self.__dtOcorrencia
    def getFinanciado(self):
        return self.__financiado
    def getVlChaves(self):
        return self.__vlChaves
    def getVlPreChaves(self):
        return self.__vlPreChaves
    def getVlPosChaves(self):
        return self.__vlPosChaves
    def getQtUnidade(self):
        return self.__qtUnidade
    def getTtChaves(self):
        return self.__ttChaves
    def getTtPreChaves(self):
        return self.__ttPreChaves
    def getTtPosChaves(self):
        return self.__ttPosChaves
    def getTtStatus(self):
        return self.__ttStatus
    def getTtEstoque(self):
        return self.__ttEstoque
    def getTtVenda(self):
        return self.__ttVenda

    #Setters

    def setIdUnidade(self, param):
        self.__idUnidade = param
    def setIdTorre(self, param):
        self.__idTorre = param
    def setNmTorre(self, param):
        self.__nmTorre = param
    def setIdEmpreend(self, param):
        self.__idEmpreend = param
    def setUnidade(self, param):
        self.__unidade = param
    def setMesVigencia(self, param):
        self.__mesVigencia = param
    def setAnoVigencia(self, param):
        self.__anoVigencia = param
    def setVlUnidade(self, param):
        self.__vlUnidade = param
    def setStatus(self, param):
        self.__status = param
    def setCpfComprador(self, param):
        self.__cpfComprador = param
    def setVlPago(self, param):
        self.__vlPago = param
    def setDtOcorrencia(self, param):
        self.__dtOcorrencia = param
    def setFinanciado(self, param):
        self.__financiado = param
    def setVlChaves(self, param):
        self.__vlChaves = param
    def setVlPreChaves(self, param):
        self.__vlPreChaves = param
    def setVlPosChaves(self, param):
        self.__vlPosChaves = param
    def setQtUnidade(self, param):
        self.__qtUnidade = param
    def setTtChaves(self, param):
        self.__ttChaves = param
    def setTtPreChaves(self, param):
        self.__ttPreChaves = param
    def setTtPosChaves(self, param):
        self.__ttPosChaves = param
    def setTtStatus(self, param):
        self.__ttStatus = param
    def setTtEstoque(self, param):
        self.__ttEstoque = param
    def setTtVenda(self, param):
        self.__ttVenda = param
