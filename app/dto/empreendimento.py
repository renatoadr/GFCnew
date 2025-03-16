#model

class empreendimento:

    def __init__(self):
        pass

    #private members
    __idEmpreend = -1
    __nmEmpreend = ""
    __apelido = ""
    __nmBanco = ""
    __nmIncorp = ""
    __nmConstrutor = ""
    __logradouro = ""
    __bairro = ""
    __cidade = ""
    __estado = ""
    __cep = ""
    __nmEngenheiro = ""
    __vlPlanoEmp = 0
    __indiceGarantia = 0
    __previsaoEntrega  = ""

    #Getters

    def getIdEmpreend(self):
        return self.__idEmpreend
    def getNmBanco(self):
        return self.__nmBanco
    def getNmEmpreend(self):
        return self.__nmEmpreend
    def getApelido(self):
        return self.__apelido
    def getNmIncorp(self):
        return self.__nmIncorp
    def getNmConstrutor(self):
        return self.__nmConstrutor
    def getLogradouro(self):
        return self.__logradouro
    def getBairro(self):
        return self.__bairro
    def getCidade(self):
        return self.__cidade
    def getEstado(self):
        return self.__estado
    def getCep(self):
        return self.__cep
    def getNmEngenheiro(self):
        return self.__nmEngenheiro
    def getVlPlanoEmp(self):
        return self.__vlPlanoEmp
    def getIndiceGarantia(self):
        return self.__indiceGarantia
    def getPrevisaoEntrega(self):
        return self.__previsaoEntrega
    def getEnderecoCompleto(self):
        return f"{self.__logradouro}, {self.__bairro} - {self.__cidade}/{self.__estado} - {self.__cep}"

    #Setters

    def setIdEmpreend(self, param):
        self.__idEmpreend = param
    def setNmBanco(self, param):
        self.__nmBanco = param
    def setNmEmpreend(self, param):
        self.__nmEmpreend = param
    def setApelido(self, param):
        self.__apelido = param
    def setNmIncorp(self, param):
        self.__nmIncorp = param
    def setNmConstrutor(self, param):
        self.__nmConstrutor = param
    def setLogradouro(self, param):
        self.__logradouro = param
    def setBairro(self, param):
        self.__bairro = param
    def setCidade(self, param):
        self.__cidade = param
    def setEstado(self, param):
        self.__estado = param
    def setCep(self, param):
        self.__cep = param
    def setNmEngenheiro(self, param):
        self.__nmEngenheiro = param
    def setVlPlanoEmp(self, param):
       self.__vlPlanoEmp = param
    def setIndiceGarantia(self, param):
       self.__indiceGarantia = param
    def setPrevisaoEntrega(self, param):
        self.__previsaoEntrega = param

