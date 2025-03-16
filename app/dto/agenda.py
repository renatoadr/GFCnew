#model

class agenda:

    def __init__(self):
        pass

    #private members
    __idEmpreend = -1
    __mesVigencia = ""
    __anoVigencia = ""
    __idAtividade = ""
    __descrAtividade = ""
    __status = ""
    __dtAtividade = ""
    __nmRespAtividade = ""
    __dtBaixa = ""
    __nmRespBaixa = ""
    
    #Getters
	
    def getIdEmpreend(self):
        return self.__idEmpreend
    def getMesVigencia(self):   
        return self.__mesVigencia
    def getAnoVigencia(self):
        return self.__anoVigencia
    def getIdAtividade(self):
        return self.__idAtividade
    def getDescrAtividade(self):
        return self.__descrAtividade
    def getStatus(self):
        return self.__status
    def getDtAtividade(self):
        return self.__dtAtividade
    def getNmRespAtividade(self):
        return self.__nmRespAtividade
    def getDtBaixa(self):
        return self.__dtBaixa
    def getNmRespBaixa(self):
        return self.__nmRespBaixa
 
    #Setters

    def setIdEmpreend(self, param):
        self.__idEmpreend = param
    def setMesVigencia(self, param):
        self.__mesVigencia = param
    def setAnoVigencia(self, param):
        self.__anoVigencia = param
    def setIdAtividade(self, param):
        self.__idAtividade = param
    def setDescrAtividade(self, param):
        self.__descrAtividade = param
    def setStatus(self, param):
        self.__status = param
    def setDtAtividade(self, param):
        self.__dtAtividade = param
    def setNmRespAtividade(self, param):
        self.__nmRespAtividade = param
    def setDtBaixa(self, param):
        self.__dtBaixa = param
    def setNmRespBaixa(self, param):
        self.__nmRespBaixa = param