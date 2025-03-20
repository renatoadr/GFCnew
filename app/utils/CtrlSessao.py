from flask import session

class CtrlSessao:
  def __init__(self, name):
    self._name = name

  def set(self, value):
    session[self._name] = value

  def get(self):
    try:
      return session.get(self._name)
    except:
      return None

  def has(self):
    try:
      data = session.get(self._name)
      return data != None
    except:
      return False

  def clear(self):
    self.set(None)


class IdEmpreend(CtrlSessao):
  def __init__(self):
    super().__init__('idEmpreend')

class NmEmpreend(CtrlSessao):
  def __init__(self):
    super().__init__('nmEmpreend')

class DtCarga(CtrlSessao):
  def __init__(self):
    super().__init__('dtCarga')

class IdOrca(CtrlSessao):
  def __init__(self):
    super().__init__('idOrca')

