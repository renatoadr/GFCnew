# model

class banco:

    def __init__(self):
        pass

    # private members
    __ispb = ""
    __codigo = ""
    __descricao = ""
    __descricao_completa = ""

    # Getters

    def getIspb(self):
        return self.__ispb

    def getCodigo(self):
        return self.__codigo

    def getDescricao(self):
        return self.__descricao

    def getDescricaoCompleta(self):
        return self.__descricao_completa

    # Setters

    def setIspb(self, param):
        self.__ispb = param

    def setCodigo(self, param):
        self.__codigo = param

    def setDescricao(self, param):
        self.__descricao = param

    def setDescricaoCompleta(self, param):
        self.__descricao_completa = param
