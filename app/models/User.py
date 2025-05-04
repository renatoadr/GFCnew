from datetime import datetime
from enums.tipo_acessos import TipoAcessos


class User:
    def __init__(self, id: int, name: str, email: str, profile: str, loggedIn: str = None):
        self.__id = id
        self.__name = name
        self.__email = email
        self.__profile = profile
        self.__logged_in = datetime.now(
        ) if loggedIn is None else datetime.fromisoformat(loggedIn)

    @property
    def id(self) -> int:
        return self.__id

    @id.setter
    def id(self, value: int):
        self.__id = value

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, value: str):
        self.__name = value

    @property
    def email(self) -> str:
        return self.__email

    @email.setter
    def email(self, value: str):
        self.__email = value

    @property
    def profile(self) -> TipoAcessos:
        return self.__profile

    @profile.setter
    def profile(self, value: TipoAcessos):
        self.__profile = value

    @property
    def logged_in(self) -> datetime:
        return self.__logged_in

    def to_string(self) -> str:
        return f"{self.id},{self.name},{self.email},{self.profile},{self.logged_in}"

    @staticmethod
    def from_string(value: str):
        if value is None:
            return User()
        us = value.split(',')
        return User(us[0], us[1], us[2], us[3], us[4])
