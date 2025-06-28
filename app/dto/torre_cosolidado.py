# model

class torre_consolidado:

    def __init__(self, blocos: int, pavimentos: int, unidades: int):
        self.__blocos__ = blocos
        self.__unidades__ = unidades
        self.__pavimentos__ = pavimentos

    def getBlocos(self):
        return self.__blocos__

    def getUnidades(self):
        return self.__unidades__

    def getPavimentos(self):
        return self.__pavimentos__
