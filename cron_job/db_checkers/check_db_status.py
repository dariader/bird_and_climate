import mysql.connector
import os

DB_PASSW = os.getenv("BIRD_DB_PASSW")
TABLENAME = 'CY'
cnx = mysql.connector.connect(user='root', password=DB_PASSW,
                              host='localhost',
                              database='bird_info')


def _table_in_db_exists():
    cur = cnx.cursor()
    cur.execute('SHOW TABLES;')
    return (TABLENAME,) in cur.fetchall()


def _table_not_empty():
    cur = cnx.cursor()
    nrows = None
    try:
        cur.execute(f'SELECT COUNT(*) FROM {TABLENAME}')
        nrows = cur.fetchall()
    except mysql.connector.errors.ProgrammingError:
        raise ValueError('CHECK DATABASE')
    finally:
        return nrows > 0


def run_checks():
    db_ok = [_table_in_db_exists(), _table_not_empty()]
    cnx.close()
    return db_ok

