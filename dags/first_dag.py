from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator


default_args = {
    'owner': 'bijay-05',
    'retries': 5,
    'retry_delay': timedelta(minutes=2)
}

with DAG(
    dag_id="first_dag",
    default_args=default_args,
    description="This is our first dag.",
    start_date=datetime(2022,12,27),
    schedule_interval='@daily'
) as dag:
    task1 = BashOperator(
        task_id="first_task",
        bash_command="echo Hello World, This is first task!!!"
    )

    task2 = BashOperator(
        task_id="second_task",
        bash_command="echo Hello second time, This is second task!!!"
    )

    #Task dependency method1
    task1.set_downstream(task2)