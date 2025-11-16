class categoria:

    __id__ = -1
    __idCategoriaPai__ = -1
    __descricaoPai__ = ""
    __descricao__ = ""
    __agrupador__ = ""
    __ativo__ = False

    def getId(self):
        return self.__id__

    def setId(self, id):
        self.__id__ = id

    def getIdCategoriaPai(self):
        return self.__idCategoriaPai__

    def setIdCategoriaPai(self, idCategoriaPai):
        self.__idCategoriaPai__ = idCategoriaPai

    def getDescricao(self):
        return self.__descricao__

    def setDescricao(self, descricao):
        self.__descricao__ = descricao

    def getDescricaoPai(self):
        return self.__descricaoPai__

    def setDescricaoPai(self, descricaoPai):
        self.__descricaoPai__ = descricaoPai

    def getAgrupador(self):
        return self.__agrupador__

    def setAgrupador(self, agrupador):
        self.__agrupador__ = agrupador

    def getAtivo(self):
        return self.__ativo__

    def setAtivo(self, ativo):
        self.__ativo__ = ativo
