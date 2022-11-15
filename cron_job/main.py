from db_checkers.check_db_status import run_checks

def runner():
    # check there's a non-empty table
    db_status = run_checks() # if [True, True ] -- all ok, get latest data, run update
