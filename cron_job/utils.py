import mysql.connector
import psycopg2
import os

DB_PASSW = os.getenv("BIRD_DB_PASSW")


def open_connection_mysql():
    cnx = mysql.connector.connect(user='root', password=DB_PASSW,
                                  host='localhost',
                                  database='bird_info')
    return cnx


def open_connection():
    cnx = psycopg2.connect(dbname="bird_info",
                           host="localhost",
                           user="root",
                           port=5432,
                           password=DB_PASSW)
    return cnx


def format_insert_values(values_list, fix_null=False):
    if fix_null:
        values_list = [val if val != "None" else "NULL" for val in values_list]
    return "'" + "', '".join([str(val).replace("'", "`") for val in values_list]) + "'"


def format_insert_keys(keys_list):
    return ', '.join([k.lower() for k in keys_list]) # key names formating should be more explicit