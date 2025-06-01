from airflow.sdk import DAG, task
import datetime
import pendulum
from airflow.providers.standard.operators.bash import BashOperator

with DAG (
    dag_id="dags_bash_with_macro_eg1",
    schedule="10 0 L * *",
    start_date=pendulum.datetime(2025, 6, 1, tz="Asia/Seoul"),
    catchup=False
) as dag :
    
    bash_task_1 = BashOperator(
        task_id = 'bash_task1',
        env = {
            'START_DATE' : '{{ }}',
            'END_DATE' : '{{ }}'
        },
        
        bash_command = 'echo "START_DATE: $START_DATE" && echo "END_DATE: $END_DATE"'
    )