class perguntaAspecto:
    def __init__(self, id: int, pergunta: str, grupo: str, opcoes: str, resposta: str, descricao: str):
        self.__id__ = id
        self.__grupo__ = grupo
        self.__pergunta__ = pergunta
        self.__resposta__ = resposta
        self.__descricao__ = descricao
        self.__opcoes__ = opcoes.split(';')

    def getId(self):
        return self.__id__

    def getPergunta(self):
        return self.__pergunta__

    def getGrupo(self):
        return self.__grupo__

    def getOpcoes(self):
        return self.__opcoes__

    def getResposta(self):
        return self.__resposta__ if self.__resposta__ is not None else ''

    def getDescricao(self):
        return self.__descricao__
