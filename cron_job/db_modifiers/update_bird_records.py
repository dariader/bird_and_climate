from cron_job.utils import open_connection
from cron_job.data_loaders.new_ebird_data import *
from datetime import datetime


class UpdateBirdRecords:
    def __init__(self):
        self.new_data = None
        self.latest_date = None
        self.dif_days = None
        self.cnx = open_connection()
        print("checking last date...")
        self.check_last_date()
        self.calculate_n_days_back()
        print("calling ebird")
        self.call_records_from_ebird()
        print("inserting")
        self.insert_into_db()
        print("done!")
        self.cnx.commit()

    def check_last_date(self):
        cur = self.cnx.cursor()
        try:
            _ = cur.execute("SELECT MAX(obsDT) FROM CY;")
            self.latest_date = cur.fetchall()[0][0]
        except TypeError:
            print("Something wrong with db! cannot update records!")
            self.latest_date = None
            raise Exception
        finally:
            return self.latest_date

    def calculate_n_days_back(self):
        difference = datetime.now() - self.latest_date
        self.dif_days = difference.days

    def call_records_from_ebird(self):
        if self.dif_days > 30:
            #todo: fix this, we either need monthly updated dataset from ebird,
            # or we need to extract data date by date, which is expencive
            self.new_data = retrieve_data(30) # 30 days back is the maximum value
        else:
            self.new_data = retrieve_data(self.dif_days)


    def insert_into_db(self):
        cur = self.cnx.cursor()
        # eh we need to insert only columns we already have in db
        # so we need to specify which keys we need to pass
        cur.execute("SHOW COLUMNS FROM CY;")
        columns_cy = {_[0] for _ in cur.fetchall()}
        for i in self.new_data:
            prepared_dict = {k.lower(): v for k, v in i.items()} # keys in db in lowercase
            keys_overlap = columns_cy.intersection(set([_ for _ in prepared_dict.keys()]))
            i_keys = ', '.join(keys_overlap)
            i_values = '"' + '", "'.join([str(prepared_dict.get(key)) if key !="None" else "NULL" for key in keys_overlap]) + '"'  # rewrite
            #todo: check that there're some values before insert
            print(i)
            cur.execute(f"INSERT INTO CY ({i_keys}) VALUES ({i_values});")

    def write_logs(self):
        pass

