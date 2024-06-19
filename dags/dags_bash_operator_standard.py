from airflow import DAG
import pendulum
# operators.bash : BashOperator를 가져오기 위함 
# BashOperator : 명령어나 shell을 실행 시키기 위함
from airflow.operators.bash import BashOperator

dag = DAG(
    dag_id="dags_bash_operator_standard",
    schedule="0 13 * * 5#2",
    start_date=pendulum.datetime(2024, 5, 1, tz="Asia/Seoul"),
    catchup=False,
    tags=['homework']
)

bash_t1 = BashOperator(
    task_id="bash_t1",
    bash_command="echo whoami",
    dag=dag
)

bash_t2 = BashOperator(
    task_id="bash_t2",
    bash_command="echo $HOSTNAME",
    dag=dag
)

bash_t1 >> bash_t2