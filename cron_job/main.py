from db_checkers.check_db_status import CheckDBStatus
from db_modifiers.update_bird_records import UpdateBirdRecords

def runner():
    # check database status:
    CheckDBStatus()
    # update records
    UpdateBirdRecords()
    # update processed tables



def __main__():
    runner()

__main__()