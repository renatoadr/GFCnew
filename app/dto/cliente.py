#model

class cliente:

    def __init__(self):
        pass

    #private members
    __cpfCnpj = ""
    __tpCpfCnpj = ""
    __nmCliente = ""
    __ddd = ""
    __tel = ""
    __email = ""
    
    #Getters

    def getCpfCnpj(self):
        return self.__cpfCnpj
    def getTpCpfCnpj(self):
        return self.__tpCpfCnpj
    def getNmCliente(self):
        return self.__nmCliente
    def getDdd(self):
        return self.__ddd
    def getTel(self):
        return self.__tel
    def getEmail(self):
        return self.__email
     
    #Setters

    def setCpfCnpj(self, param):
        self.__cpfCnpj = param
    def setTpCpfCnpj(self, param):
        self.__tpCpfCnpj = param
    def setNmCliente(self, param):
        self.__nmCliente = param
    def setDdd(self, param):
        self.__ddd = param
    def setTel(self, param):
        self.__tel = param
    def setEmail(self, param):
        self.__email = param
