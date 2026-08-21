from airflow import DAG
from airflow.operators.python import PythonOperator

from python.transform.transform_pipeline import run_transform_pipeline
from python.load.load_to_mysql import load_to_mysql

from datetime import datetime

with DAG(
    dag_id="ecommerce_etl",
    start_date=datetime(2026, 8, 18),
    schedule=None,
    catchup=False,
) as dag:
    
    transform_task = PythonOperator(
        task_id="transform",
        python_callable=run_transform_pipeline,
    )

    load_task = PythonOperator(
        task_id="load",
        python_callable=load_to_mysql,
    )

    transform_task >> load_task