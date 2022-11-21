import logging

import mysql.connector
from mysql.connector import errorcode
from cron_job.utils import open_connection
from cron_job.db_modifiers.insert_historical_data import *
import os


class CheckDBStatus:
    def __init__(self):
        self.TABLENAME = 'CY'
        self.cnx = open_connection()
        self._run_assessment()
        self.cnx.commit()
        self.cnx.close()


    def _table_in_db_exists(self):
        cur = self.cnx.cursor()
        cur.execute('SHOW TABLES;')
        return (self.TABLENAME,) in cur.fetchall()

    def _table_not_empty(self):
        cur = self.cnx.cursor()
        nrows = None
        try:
            cur.execute(f'SELECT COUNT(*) FROM {self.TABLENAME}')
            nrows = cur.fetchall()
        except mysql.connector.errors.ProgrammingError:
            raise ValueError('CHECK DATABASE')
        finally:
            return nrows[0][0] > 0 # return example [(180884,)]

    def _run_checks(self):
        if self._table_in_db_exists():
            print(self._table_in_db_exists())
            db_ok = [self._table_in_db_exists(), self._table_not_empty()]
        else:
            db_ok = [False, False]
        return db_ok

    def _create_database_schema_cy(self):
        cur = self.cnx.cursor()
        table_description = (
            "CREATE TABLE CY ("
            "`index` int(11) NOT NULL AUTO_INCREMENT,"
            "`speciescode` VARCHAR(255),"
            "`comname` VARCHAR(255),"
            "`sciname` VARCHAR(255),"
            "`locid` VARCHAR(255),"
            "`locname` VARCHAR(255),"
            "`obsdt` DATETIME,"
            "`howmany` INT(255),"
            "`lat` DOUBLE(10,7),"
            "`lng` DOUBLE(10,7),"
            "`obsvalid` VARCHAR(255),"
            "`obsreviewed` VARCHAR(255),"
            "`locationprivate` VARCHAR(255),"
            "`subid` VARCHAR(255),"
            "  PRIMARY KEY (`index`)"
            ") ENGINE=InnoDB;")

        try:
            print(f"Creating table CY: ")
            cur.execute(table_description)
            print(f"Done")
        except mysql.connector.Error as err:
            # this should be not the case
            if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                print("already exists.")
            else:
                print(err.msg)

    def _run_assessment(self):
        print('running assesment')
        db_status = self._run_checks()  # if [True, True ] -- all ok, get latest data, run update
        if db_status == [True, True]:
            print("all ok")
            # if records present in db go to next procedure
            pass
        elif db_status == [True, False]:
            # if db is present, but no records -- populate with historical data
            print("populating with hist data")
            populate_with_hist_data(self.cnx)
        else:
            # no db, create schema, populate
            print("recreating bd")
            self._create_database_schema_cy()
            populate_with_hist_data(self.cnx)
        return
