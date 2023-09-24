import mysql.connector

__mydb = None


def get_sql_connection():
    global __mydb
    if __mydb is None:
        __mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="password",
            port="3306",
            database="pantry"
        )
    return __mydb
