# model

class torre:

    def __init__(self):
        pass

    # private members
    __idTorre = -1
    __idEmpreend = -1
    __nmTorre = ""
    __prefixCobertura = ""
    __qtUnidade = 0
    __qtAndar = 0
    __qtCobertura = None
    __numAptUmAndarUm = None
    __vlrUnidade = -1
    __vlrCobertura = -1

    # Getters

    def getIdTorre(self):
        return self.__idTorre

    def getIdEmpreend(self):
        return self.__idEmpreend

    def getNmTorre(self):
        return self.__nmTorre

    def getQtAndar(self):
        return self.__qtAndar

    def getQtUnidade(self):
        return self.__qtUnidade

    def getQtCobertura(self):
        return self.__qtCobertura

    def getPrefixCobertura(self):
        return self.__prefixCobertura

    def getNumAptUmAndarUm(self):
        return self.__numAptUmAndarUm

    def getVlrUnidade(self):
        return self.__vlrUnidade

    def getVlrCobertura(self):
        return self.__vlrCobertura

    # Setters

    def setIdTorre(self, param):
        self.__idTorre = param

    def setIdEmpreend(self, param):
        self.__idEmpreend = param

    def setNmTorre(self, param):
        self.__nmTorre = param

    def setQtUnidade(self, param):
        self.__qtUnidade = param

    def setQtAndar(self, param):
        self.__qtAndar = param

    def setQtCobertura(self, param):
        self.__qtCobertura = param

    def setPrefixCobertura(self, param):
        self.__prefixCobertura = param

    def setNumAptUmAndarUm(self, param):
        self.__numAptUmAndarUm = param

    def setVlrUnidade(self, param):
        self.__vlrUnidade = param  

    def setVlrCobertura(self, param):
        self.__vlrCobertura = param
