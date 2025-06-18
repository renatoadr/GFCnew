class agenda_atividade:

    def __init__(self, id, atividade):
        self.__id__ = id
        self.__atividade__ = atividade

    def getId(self):
        return self.__id__

    def getNmAtividade(self):
        return self.__atividade__
