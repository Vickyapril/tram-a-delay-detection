from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'tram_delay_team',
    'depends_on_past': False,
    'email_on_failure': False,
    'retries': 0,
    'retry_delay': timedelta(minutes=1),
}

with DAG(
    'real_time_tram_a_delay',
    default_args=default_args,
    description='Detect TRAM A delay at Peychotte using Kafka, Flink SQL, and Email alert',
    schedule="@daily",  # Manual trigger for now
    start_date=datetime(2025, 6, 17),
    catchup=False,
    tags=['tram', 'delay', 'realtime', 'pey', 'airflow'],
) as dag:

    start_kafka_producer = BashOperator(
        task_id='start_kafka_producer',
        bash_command='python3 /Users/vigneshwar.gurunatha/Desktop/realtime/airflow/gtfs_producer.py'
    )

    start_transformer = BashOperator(
        task_id='start_transformer',
        bash_command='python3 /Users/vigneshwar.gurunatha/Desktop/realtime/airflow/gtfs_transformer.py'
    )

    start_email_alert = BashOperator(
        task_id='start_email_alert',
        bash_command='python3 /Users/vigneshwar.gurunatha/Desktop/realtime/airflow/email_alert_listener.py'
    )

    # Task Flow
    start_kafka_producer >> start_transformer >> start_email_alert

