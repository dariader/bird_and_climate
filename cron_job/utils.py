import mysql.connector
import os

DB_PASSW = os.getenv("BIRD_DB_PASSW")


def open_connection():
    cnx = mysql.connector.connect(user='root', password=DB_PASSW,
                                  host='localhost',
                                  database='bird_info')
    return cnx