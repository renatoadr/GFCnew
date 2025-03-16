#model

class inadimpencia:

    def __init__(self):
        pass

    #private members
    __idEmpreend = -1
    __mesVigencia = ""
    __anoVigencia = ""
    __ordem = -1
    __periodo = ""
    __qtUnidades = -1
    
    #Getters

    def getIdEmpreend(self):
        return self.__idEmpreend
    def getMesVigencia(self):
        return self.__mesVigencia
    def getAnoVigencia(self):
        return self.__anoVigencia
    def getOrdem(self):
        return self.__ordem
    def getPeriodo(self):
        return self.__periodo
    def getQtUnidades(self):
        return self.__qtUnidades
     
    #Setters

    def setIdEmpreend(self, param):
        self.__idEmpreend = param
    def setMesVigencia(self, param):
        self.__mesVigencia = param
    def setAnoVigencia(self, param):
        self.__anoVigencia = param
    def setOrdem(self, param):
        self.__ordem = param
    def setPeriodo(self, param):
        self.__periodo = param
    def setQtUnidades(self, param):
        self.__qtUnidades = param
