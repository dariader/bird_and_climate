import mysql.connector
from cron_job.utils import open_connection, format_insert_values, format_insert_keys
import numpy as np
from mysql.connector import errorcode
import os
import shutil
import pandas as pd
PROJ_PATH = "/home/daria/PycharmProjects/bird_and_climate" # should be set automatically, stored in env var
HIST_DATA_DIR = f"{PROJ_PATH}/db_src/bird_historical_data"
HIST_DATA_ID = "0163061-220831081235567"

def populate_with_hist_data(cnx):
    cur = cnx.cursor()
    print('preparing historical data...')
    shutil.unpack_archive(f"{HIST_DATA_DIR}/{HIST_DATA_ID}.zip", f"{HIST_DATA_DIR}")
    print('prepared historical data...')
    tablename = "CY"

    print('prepared historical data...')
    hist_data = pd.read_table(f"{HIST_DATA_DIR}/{HIST_DATA_ID}.csv")
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
    print('inserting...')
    for i in hist_data.to_dict('records'):
        i_keys = format_insert_keys(i.keys())
        i_values = format_insert_values(i.values(), fix_null=False)
        cur.execute(f'INSERT INTO CY ({i_keys}) VALUES ({i_values});')

    cnx.commit()
    cur.close()

def __main__():
    cnx = open_connection()
    populate_with_hist_data(cnx)
    cnx.close()

