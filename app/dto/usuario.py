# model

class usuario:

    def __init__(self):
        pass

    # private members
    __idUsuario = -1
    __codBanco = -1
    __email = ""
    __senha = ""
    __tpAcesso = ""
    __nmUsuario = ""

    # Getters

    def getIdUsuario(self):
        return self.__idUsuario

    def getCodBanco(self):
        return self.__codBanco

    def getEmail(self):
        return self.__email

    def getSenha(self):
        return self.__senha

    def getTpAcesso(self):
        return self.__tpAcesso

    def getNmUsuario(self):
        return self.__nmUsuario

    # Setters

    def setIdUsuario(self, param):
        self.__idUsuario = param

    def setCodBanco(self, param):
        self.__codBanco = param

    def setEmail(self, param):
        self.__email = param

    def setSenha(self, param):
        self.__senha = param

    def setTpAcesso(self, param):
        self.__tpAcesso = param

    def setNmUsuario(self, param):
        self.__nmUsuario = param
