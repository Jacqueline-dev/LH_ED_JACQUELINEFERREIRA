from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.utils.dates import days_ago

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': days_ago(1),
    'retries': 1,
}

dag = DAG(
    'data',
    default_args=default_args,
    description='Indicium Tech Code Challenge',
    schedule_interval='@daily',
)

extract_postgres = BashOperator(
    task_id='extract_postgres',
    bash_command='python /path/to/scripts/extract_postgres.py',
    dag=dag,
)

process_csv = BashOperator(
    task_id='process_csv',
    bash_command='python /path/to/scripts/process_csv.py',
    dag=dag,
)

load_data = BashOperator(
    task_id='load_data',
    bash_command='python /path/to/scripts/load_data.py',
    dag=dag,
)

extract_postgres >> process_csv >> load_data
