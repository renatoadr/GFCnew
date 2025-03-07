
class gasto:

    def __init__(self):
        pass

    #private members
    __idGasto = 0
    __idEmpreend = -1
    __dtEvento = ""
    __vlMedicao = 0
    __vlCompras = 0
    __vlRhAdm = 0

    #Getters
    def getIdGasto(self):
        return self.__idGasto
    def getIdEmpreend(self):
        return self.__idEmpreend
    def getDtEvento(self):
        return self.__dtEvento
    def getVlMedicao(self):
        return self.__vlMedicao
    def getVlCompras(self):
        return self.__vlCompras
    def getVlRhAdm(self):
        return self.__vlRhAdm

    #Setters
    def setIdGasto(self, param):
        self.__idGasto = param
    def setIdEmpreend(self, param):
        self.__idEmpreend = param
    def setDtEvento(self, param):
        self.__dtEvento = param
    def setVlMedicao(self, param):
        self.__vlMedicao = param
    def setVlCompras(self, param):
        self.__vlCompras = param
    def setVlRhAdm(self, param):
        self.__vlRhAdm = param