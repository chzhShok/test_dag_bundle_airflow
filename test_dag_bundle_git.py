from airflow import DAG
from airflow.operators.python import PythonOperator

with DAG(
    'test_dag_bundle_git',
) as dag:
    
    test_task = PythonOperator(
        task_id='show_message',
        python_callable=lambda: print("Dag bundle works!")
    )
