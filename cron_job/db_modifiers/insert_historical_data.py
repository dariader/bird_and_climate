import mysql.connector
from cron_job.utils import open_connection
import numpy as np
from mysql.connector import errorcode
import os
import shutil
import pandas as pd

HIST_DATA_DIR = "../../db_src/bird_historical_data/"
HIST_DATA_ID = "0163061-220831081235567"


def populate_with_hist_data(cnx):
    cur = cnx.cursor()
    shutil.unpack_archive(f"{HIST_DATA_DIR}{HIST_DATA_ID}.zip", f"{HIST_DATA_DIR}")

    cur.execute("USE bird_info;")
    tablename = "CY"

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
        i_keys = ', '.join([k.lower() for k in i.keys()])
        i_values ='"' + '", "'.join([str(j) for j in i.values()]) + '"' # rewrite
        cur.execute(f"INSERT INTO CY ({i_keys}) VALUES ({i_values});")

    cnx.commit()
    cur.close()

def __main__():
    cnx = open_connection()
    populate_with_hist_data(cnx)
    cnx.close()

