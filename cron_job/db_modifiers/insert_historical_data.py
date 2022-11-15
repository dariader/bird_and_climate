import mysql.connector
import numpy as np
from mysql.connector import errorcode
import os
import shutil
import pandas as pd

HIST_DATA_DIR = "../../db_src/bird_historical_data/"
HIST_DATA_ID = "0163061-220831081235567"
shutil.unpack_archive(f"{HIST_DATA_DIR}{HIST_DATA_ID}.zip", f"{HIST_DATA_DIR}")

DB_PASSW = os.getenv("BIRD_DB_PASSW")

cnx = mysql.connector.connect(user='root', password=DB_PASSW,
                              host='localhost',
                              database='bird_info')

cur = cnx.cursor()
cur.execute("USE bird_info;")
tablename = "CY"

table_description = (
    "CREATE TABLE CY ("
    "`index` int(11) NOT NULL AUTO_INCREMENT,"
    "`speciesCode` VARCHAR(255),"
    "`comName` VARCHAR(255),"
    "`sciName` VARCHAR(255),"
    "`locId` VARCHAR(255),"
    "`locName` VARCHAR(255),"
    "`obsDt` VARCHAR(255),"
    "`howMany` INT(255),"
    "`lat` DOUBLE(10,7),"
    "`lng` DOUBLE(10,7),"
    "`obsValid` VARCHAR(255),"
    "`obsReviewed` VARCHAR(255),"
    "`locationPrivate` VARCHAR(255),"
    "`subId` VARCHAR(255),"
    "  PRIMARY KEY (`index`)"
    ") ENGINE=InnoDB;")

try:
    print(f"Creating table {tablename}: ")
    cur.execute(table_description)
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
        print("already exists.")
    else:
        print(err.msg)

hist_data = pd.read_table(f"{HIST_DATA_DIR}{HIST_DATA_ID}.csv")
hist_data = hist_data[
    ['species', 'stateProvince', 'individualCount', 'decimalLatitude', 'decimalLongitude', 'eventDate']]

hist_data = hist_data.rename(columns={
    "species": "sciName",
    "stateProvince": "locName",
    "individualCount": "howMany",
    "decimalLatitude": "lat",
    "decimalLongitude": "lng",
    "eventDate": "obsDt"})

hist_data.howMany = hist_data.howMany.replace(np.NAN, 0)
for i in hist_data.to_dict('records'):
    i_keys = ', '.join([k for k in i.keys()])
    i_values ='"' + '", "'.join([str(j) for j in i.values()]) + '"' # rewrite
    cur.execute(f"INSERT INTO CY ({i_keys}) VALUES ({i_values});")

cnx.commit()
cur.close()
cnx.close()

