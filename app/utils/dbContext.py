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
      self.__cursor = self.__conn.cursor()
      return self.__cursor

  def commitAndClose(self):
    self.__conn.commit()
    self.__cursor.close()
    self.__conn.close()
    self.__cursor = None
    self.__conn = None

  @staticmethod
  def connect ():
    try:
      connection = m.connect(
        host=os.getenv('DB_HOST'),
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASS')
      )

      if connection.is_connected():
        return connection

    except Exception as e:
      MySql.message = e

  @staticmethod
  def close(connection):
      connection.close()

  @staticmethod
  def getOne(query: str, args: tuple):
    conn = MySql()
    cursor = conn.getCursor()
    cursor.execute(query, args)
    ret = cursor.fetchone()
    conn.commitAndClose()
    return ret

  @staticmethod
  def getAll(query: str, args: tuple):
    conn = MySql()
    cursor = conn.getCursor()
    cursor.execute(query, args)
    ret = cursor.fetchall()
    conn.commitAndClose()
    return ret

  @staticmethod
  def exec(query: str, args: tuple):
    conn = MySql()
    cursor = conn.getCursor()
    cursor.execute(query, args)
    conn.commitAndClose()
