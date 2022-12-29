from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
import billboard
import csv

def get_hot100_songs(date: str)-> str:
    '''
    returns Hot-100 songs for the week
    '''
    chart = billboard.ChartData("hot-100", date=date)
    with open(f"../hot-100-{date}.csv", "w") as f:
        header = ["Rank","Title","Artist","No_weeks_on_chart"]
        writer = csv.writer(f)
        writer.writerow(header)
        for rank, song in enumerate(chart):
            writer.writerow([rank+1,song.title,song.artist,song.weeks])
    return "Completed !!!"

default_args = {
    'owner': 'bijay-05',
    'retries': 5,
    'retry_delay': timedelta(minutes=2)
}

with DAG(
    dag_id="hot100_songs_dag",
    default_args=default_args,
    description="This is dag to get hot-100 songs from billboard for the week.",
    start_date=datetime(2022,12,29,11),
    schedule_interval='@weekly'
) as dag:
    task1 = BashOperator(
        task_id="first_task",
        bash_command="echo Hello World, Get ready for next task!!!"
    )

    task2 = PythonOperator(
        task_id="second_task",
        python_callable=get_hot100_songs,
        op_kwargs={"date":str(datetime.utcnow())[:13]}
    )

    task3 = BashOperator(
        task_id="third_task",
        bash_command="echo Hello world, The file is created!!!"
    )

    #Task dependency method1
    task1.set_downstream(task2)