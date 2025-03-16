import mysql.connector as m

class MySql:
    message = ""
    DB_NAME = 'db_gfc'

    try:

        @staticmethod
        def connect ():
            connection = m.connect(
                host="localhost",
                user="root",
                #password="BIM@db2024"
                password=""
            )

            if connection.is_connected():
                return connection

    except Exception as e:
        MySql.message = e

    @staticmethod
    def close(connection):
        connection.close()

