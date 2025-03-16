import mysql.connector as m
import os

class MySql:
    message = ""
    DB_NAME = os.getenv('DB_NAME')

    try:

        @staticmethod
        def connect ():
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

