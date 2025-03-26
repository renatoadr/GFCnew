class option:
  def __init__(self, chave, valor):
    self.__chave = chave
    self.__valor = valor

  @property
  def chave(self):
    return self.__chave

  @chave.setter
  def chave(self, param):
    self.__chave = param

  @property
  def valor(self):
    return self.__valor

  @valor.setter
  def valor(self, param):
    self.__valor = param
