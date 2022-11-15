import mysql.connector
from mysql.connector import errorcode
from cron_job.data_loaders.new_ebird_data import retrieve_data
import os
"""
This is a sheduled job on a server, that:
1. Connects to the database
2. Downloads data from ebird
3. Inserts data
    - How to insert data for a specific period?
    - How to receive an error if data is not correct? 
4. Generates statistics
"""
DB_PASSW = os.getenv("BIRD_DB_PASSW")

cnx = mysql.connector.connect(user='root', password=DB_PASSW,
                              host='localhost',
                              database='bird_info')
cur = cnx.cursor()
cur.execute("USE bird_info;")
tablename = "CY"

data = retrieve_data("CY")
for i in data:
    i_keys = ', '.join([k for k in i.keys()])
    i_values ='"' + '", "'.join([str(j) for j in i.values()]) + '"' # rewrite
    cur.execute(f"INSERT INTO CY ({i_keys}) VALUES ({i_values});")

cnx.commit()
cur.close()
cnx.close()