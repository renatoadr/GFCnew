#model

class certidao:

    def __init__(self):
        pass

    #private members
    __idEmpreend            = -1  
    __estadualStatus        = ""
    __estadualValidade      = ""
    __fgtsStatus            = ""
    __fgtsValidade          = ""
    __municipalStatus       = ""
    __municipalValidade     = ""
    __srfInssStatus         = ""
    __srfInssValidade       = ""
    __trabalhistaStatus     = ""
    __trabalhistaValidade   = "" 

    #Getters

    def getIdEmpreend(self):
        return self.__idEmpreend
    def getEstadualStatus(self):
        return self.__estadualStatus
    def getEstadualValidade(self):
        return self.__estadualValidade          
    def getFgtsStatus(self):
        return self.__fgtsStatus
    def getFgtsValidade(self):
        return self.__fgtsValidade 
    def getMunicipalStatus(self):
        return self.__municipalStatus
    def getMunicipalValidade(self):
        return self.__municipalValidade 
    def getSrfInssStatus(self):
        return self.__srfInssStatus
    def getSrfInssValidade(self):
        return self.__srfInssValidade
    def getTrabalhistaStatus(self):
        return self.__trabalhistaStatus
    def getTrabalhistaValidade(self):
        return self.__trabalhistaValidade
             
    #Setters

    def setIdEmpreend(self, param):
        self.__idEmpreend = param
    def setEstadualStatus(self, param):
        self.__estadualStatus = param   
    def setEstadualValidade(self, param):
        self.__estadualValidade = param
    def setFgtsStatus(self, param):
        self.__fgtsStatus = param
    def setFgtsValidade(self, param):
        self.__fgtsValidade = param
    def setMunicipalStatus(self, param):
        self.__municipalStatus = param
    def setMunicipalValidade(self, param):
        self.__municipalValidade = param
    def setSrfInssStatus(self, param):
        self.__srfInssStatus = param
    def setSrfInssValidade(self, param):
        self.__srfInssValidade = param
    def setTrabalhistaStatus(self, param):
        self.__trabalhistaStatus = param
    def setTrabalhistaValidade(self, param):
        self.__trabalhistaValidade = param

