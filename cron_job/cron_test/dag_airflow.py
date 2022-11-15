from datetime import datetime, timedelta
# The DAG object; we'll need this to instantiate a DAG
from airflow import DAG
from airflow.decorators import task
from new_ebird_data import retrieve_data
import os

api_key = os.getenv("EBIRD_API_KEY")
# Operators; we need this to operate!
from airflow.operators.bash import BashOperator

with DAG(
    'run_birds',
    # These args will get passed on to each operator
    # You can override them on a per-task basis during operator initialization
    default_args={
        'depends_on_past': False,
        # 'email': False,
        # 'email_on_failure': False,
        # 'email_on_retry': False,
        'retries': 1,
        'retry_delay': timedelta(minutes=1),
        # 'queue': 'bash_queue',
        # 'pool': 'backfill',
        # 'priority_weight': 10,
        # 'end_date': datetime(2016, 1, 1),
        # 'wait_for_downstream': False,
        # 'sla': timedelta(hours=2),
        # 'execution_timeout': timedelta(seconds=300),
        # 'on_failure_callback': some_function,
        # 'on_success_callback': some_other_function,
        # 'on_retry_callback': another_function,
        # 'sla_miss_callback': yet_another_function,
        # 'trigger_rule': 'all_success'
    },
    description='A simple tutorial DAG',
    schedule=timedelta(days=1),
    start_date=datetime(2022, 11, 13),
    catchup=False,
    tags=['example'],
) as dag:
    @task(task_id="print_the_context_1")
    def update_ebird_data():
        print("run 1")
        return retrieve_data(1)


    @task(task_id="print_the_context_2")
    def update_ebird_data_2():
        print("run 2")
        return retrieve_data(2)

    run_1 = update_ebird_data()
    run_2 = update_ebird_data_2()