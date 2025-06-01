from airflow.sdk import DAG, task
import datetime
import pendulum
from airflow.providers.standard.operators.bash import BashOperator

with DAG (
    dag_id="dags_bash_with_macro_eg1",
    schedule="10 0 * * 6#2",
    start_date=pendulum.datetime(2025, 6, 1, tz="Asia/Seoul"),
    catchup=False
) as dag :
    # START_DATE : 전월 말일, END_DATE : 1일 전
    bash_task_2 = BashOperator(
        task_id = 'bash_task2',
        env = {
            'START_DATE' : '{{ data_interval_end.in_timezone("Asia/Seoul") - macros.dateutil.relativedelta.relativedelta(days-19) }}',
            'END_DATE' : '{{ data_interval_end.in_timezone("Asia/Seoul") - macros.dateutil.relativedelta.relativedelta(days-14) }}'
        },
        
        bash_command = 'echo "START_DATE: $START_DATE" && echo "END_DATE: $END_DATE"'
    )