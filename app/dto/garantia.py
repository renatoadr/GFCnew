#model

class garantia:
  @property
  def Id(self):
    return self.__id

  @Id.setter
  def Id(self, param):
    self.__id = param

  @property
  def documento(self):
    return self.__documento

  @documento.setter
  def documento(self, param):
    self.__documento = param

  @property
  def observacao(self):
    return self.__observacao

  @observacao.setter
  def observacao(self, param):
    self.__observacao = param

  @property
  def status(self):
    return self.__status

  @status.setter
  def status(self, param):
    self.__status = param

  @property
  def tipo(self):
    return self.__tipo

  @tipo.setter
  def tipo(self, param):
    self.__tipo = param
