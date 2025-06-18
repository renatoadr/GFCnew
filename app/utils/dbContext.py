from utils.logger import logger
import mysql.connector as m
import os


class MySql:
    message = ""
    DB_NAME = os.getenv('DB_NAME')
    __conn = None
    __cursor = None

    def getCursor(self):
        if self.__cursor is None:
            self.__conn = MySql.connect()
            self.__cursor = self.__conn.cursor(dictionary=True)
            return self.__cursor

    def commitAndClose(self, useCommit=False):
        try:
            if useCommit:
                self.__conn.commit()
            self.__cursor.close()
            self.__conn.close()
            self.__cursor = None
            self.__conn = None
        except:
            pass

    @staticmethod
    def getSenha():
        try:
            filePass = open('/run/secrets/db-password', 'r')
            return filePass.read()
        except:
            return os.getenv('DB_PASS')

    @staticmethod
    def connect():
        try:
            connection = m.connect(
                host=os.getenv('DB_HOST'),
                user=os.getenv('DB_USER'),
                password=MySql.getSenha()
            )

            if connection.is_connected():
                return connection

        except Exception as e:
            logger.error('Erro ao conectar com o banco: ', e)

    @staticmethod
    def close(connection):
        connection.close()

    @staticmethod
    def getOne(query: str, args: tuple = None):
        conn = MySql()
        cursor = conn.getCursor()
        cursor.execute(query, args)
        ret = cursor.fetchone()
        conn.commitAndClose()
        return ret

    @staticmethod
    def getAll(query: str, args: tuple = None):
        conn = MySql()
        cursor = conn.getCursor()
        cursor.execute(query, args)
        ret = cursor.fetchall()
        conn.commitAndClose()
        return ret

    @staticmethod
    def exec(query: str, args: tuple = None):
        conn = MySql()
        cursor = conn.getCursor()
        cursor.execute(query, args)
        conn.commitAndClose(useCommit=True)

    @staticmethod
    def execMany(query: str, args: tuple = None):
        conn = MySql()
        cursor = conn.getCursor()
        cursor.executemany(query, args)
        conn.commitAndClose(useCommit=True)
