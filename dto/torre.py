#model

class torre:

    def __init__(self):
        pass

    #private members
    __idTorre = -1
    __idEmpreend = -1
    __nmTorre = ""
    __qtUnidade = 0
    
    #Getters

    def getIdTorre(self):
        return self.__idTorre
    def getIdEmpreend(self):
        return self.__idEmpreend
    def getNmTorre(self):
        return self.__nmTorre
    def getQtUnidade(self):
        return self.__qtUnidade
 
    #Setters

    def setIdTorre(self, param):
        self.__idTorre = param
    def setIdEmpreend(self, param):
        self.__idEmpreend = param
    def setNmTorre(self, param):
        self.__nmTorre = param
    def setQtUnidade(self, param):
        self.__qtUnidade = param
