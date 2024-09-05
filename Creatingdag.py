from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.utils.dates import days_ago
from airflow.operators.python_operator import PythonOperator # type: ignore




default_args = {
    'owner': 'airflow',
    'start_date': days_ago(1),
    'retries': 1,
}

# Creating DAG Object
dag = DAG(dag_id='DAG-1',
        default_args=default_args,
        schedule_interval='@once', 
        catchup=False
    )

hello_world_task = BashOperator(
    task_id='hello_world_task',
    bash_command='python -c "print(\'Hello, world!\')"',
    dag=dag
)
run_script = BashOperator(
    task_id='run_python_script',
    bash_command='python /opt/airflow/dags/script.py '
                 '{{ dag_run.conf["local_file"] }} '
                 '{{ dag_run.conf["s3_file"] }} '
                 '{{ dag_run.conf["bucket_name"] }}',
    dag=dag,
)


# Define the task dependencies
hello_world_task >> run_script