class produto:

    __id__ = -1
    __id_cat__ = -1
    __codigo__ = -1
    __unidade__ = ""
    __ativo__ = False
    __descricao__ = ""
    __agrupador__ = ""
    __categoria__ = ""

    def getId(self):
        return self.__id__

    def setId(self, id):
        self.__id__ = id

    def getIdCategoria(self):
        return self.__id_cat__

    def setIdCategoria(self, id_cat):
        self.__id_cat__ = id_cat

    def getCategoria(self):
        return self.__categoria__

    def setCategoria(self, categoria):
        self.__categoria__ = categoria

    def getCodigo(self):
        return self.__codigo__

    def setCodigo(self, codigo):
        self.__codigo__ = codigo

    def getUnidade(self):
        return self.__unidade__

    def setUnidade(self, unidade):
        self.__unidade__ = unidade

    def getAtivo(self):
        return self.__ativo__

    def setAtivo(self, ativo):
        self.__ativo__ = ativo

    def getDescricao(self):
        return self.__descricao__

    def setDescricao(self, descricao):
        self.__descricao__ = descricao

    def getAgrupador(self):
        return self.__agrupador__

    def setAgrupador(self, agrupador):
        self.__agrupador__ = agrupador
