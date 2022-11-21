from cron_job.utils import open_connection
import mysql.connector
class UpdateDependantTables:

    def __init__(self):
        self.cnx = open_connection()
        self.table_config = self.table_config_dict()
        pass

    def check_table_exists(self):
        cur = self.cnx.cursor()
        cur.execute('SHOW TABLES;')
        result = {}
        all_tables = cur.fetchall()
        for tablename in self.table_config:
            result[tablename] = (tablename,) in all_tables
        return result

    def recreate_table(self):
        # here we call constructor with create expression
        pass
    def update_table(self):
        # here we call constructor with create expression
        pass

    def table_config_dict(self, action="CREATE"):
        dct = {
            "CY_GROUPED_LOC": f"{action} TABLE CY_GROUPED_LOC"
                             f" SELECT locname, COUNT(howMany) AS record_count, SUM(howmany) AS record_sum "
                             f"FROM CY GROUP BY locname WITH ROLLUP;",
            "CY_GROUPED_SP": f"{action} TABLE CY_GROUPED_SP"
                             f" SELECT sciname, COUNT(howMany) as record_count, SUM(howmany) AS record_sum"
                             f"FROM CY GROUP BY sciname WITH ROLLUP;",
            "CY_GROUPED_SP_DT": f"{action} TABLE CY_GROUPED_SP_DT"
                              f" SELECT MONTH(obsdt), sciname, COUNT(sciname) AS record_count, SUM(howmany) AS record_sum"
                                f" FROM CY GROUP BY MONTH(obsdt), sciname WITH ROLLUP;",
            "CY_GROUPED_SP_LOC": f"{action} TABLE CY_GROUPED_SP_LOC"
                              f" SELECT locname, sciname, COUNT(sciname) AS record_count, SUM(howmany) AS record_sum"
                                f" FROM CY GROUP BY locname, sciname WITH ROLLUP;",
  #          "CY_GROUPED_SP_LOC_DT": f"{}", # need to implement geohash here
        }
        return dct
