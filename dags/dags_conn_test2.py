from airflow import DAG
# pendulum : datetime 모듈을 쉽게 쓰기 위해서
import pendulum
from airflow.operators.empty import EmptyOperator

with DAG(
    dag_id="dags_conn_test1",
    schedule=None,
    start_date=pendulum.datetime(2024, 6, 16, tz="Asia/Seoul"),
    catchup=False
) as dag:
    
    t1 = EmptyOperator(
        task_id="t1"
    )

    t2 = EmptyOperator(
        task_id="t2"
    )

    t3 = EmptyOperator(
        task_id="t3"
    )

    t4 = EmptyOperator(
        task_id="t4"
    )

    t5 = EmptyOperator(
        task_id="t5"
    )
    
    t6 = EmptyOperator(
        task_id="t6"
    )

    t7 = EmptyOperator(
        task_id="t7"
    )

    t8 = EmptyOperator(
        task_id="t8"
    )

