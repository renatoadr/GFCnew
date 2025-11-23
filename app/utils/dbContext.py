from utils.logger import logger
import mysql.connector as m
import os


class MySql:
    message = ""
    DB_NAME = os.getenv('DB_NAME')
    __conn__ = None
    __cursor__ = None

    def dbConnect(self):
        try:
            connection = m.connect(
                host=os.getenv('DB_HOST'),
                user=os.getenv('DB_USER'),
                password=MySql.getSenha(),
                database=MySql.DB_NAME
            )

            if connection.is_connected():
                return connection
        except Exception as e:
            logger.error('Erro ao conectar com o banco: ', e)
            return None

    def getConn(self):
        if self.__conn__ is None:
            self.__conn__ = self.dbConnect()
        return self.__conn__

    def getCursor(self):
        if self.__cursor__ is None:
            conn = self.getConn()
            self.__cursor__ = conn.cursor(dictionary=True)
            return self.__cursor__

    def dbClose(self):
        try:
            if self.__conn__.is_connected():
                self.__cursor__.close()
                self.__conn__.close()
                self.__cursor__ = None
                self.__conn__ = None
        except Exception as error:
            logger.error("Error in close connection ", error)

    @staticmethod
    def getSenha():
        try:
            filePass = open('/run/secrets/db-password', 'r')
            return filePass.read()
        except:
            return os.getenv('DB_PASS')

    @staticmethod
    def connect():
        db = MySql()
        return db.dbConnect()

    @staticmethod
    def close(connection):
        connection.close()

    @staticmethod
    def getOne(query: str, args: tuple = None) -> dict:
        db = MySql()
        ret = None
        try:
            cursor = db.getCursor()
            cursor.execute(query, args)
            ret = cursor.fetchone()
        except Exception as error:
            logger.error("Erro ao realizar o fetchone", error)
        finally:
            db.dbClose()
        return ret

    @staticmethod
    def getAll(query: str, args: tuple = None) -> list[dict]:
        conn = MySql()
        ret = []
        try:
            cursor = conn.getCursor()
            cursor.execute(query, args)
            ret = cursor.fetchall()
        except Exception as error:
            logger.error("Erro ao realizar o fetchall", error)
        finally:
            conn.dbClose()
        return ret

    @staticmethod
    def exec(query: str, args: tuple = None) -> bool:
        conn = MySql()
        try:
            conn.getCursor().execute(query, args)
            conn.getConn().commit()
            return True
        except Exception as error:
            logger.error("Erro ao realizar o execute", error)
        finally:
            conn.dbClose()
        return False

    @staticmethod
    def execMany(query: str, args: tuple = None) -> bool:
        conn = MySql()
        try:
            conn.getCursor().executemany(query, args)
            conn.getConn().commit()
            return True
        except Exception as error:
            logger.error("Erro ao realizar o executemany", error)
        finally:
            conn.dbClose()
        return False
