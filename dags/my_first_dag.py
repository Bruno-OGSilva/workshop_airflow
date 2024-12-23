from datetime import datetime

from airflow.decorators import dag, task

from time import sleep

@dag(start_date=datetime(2024, 12, 12), 
     schedule="@daily", 
     catchup=False)
def primeira_dag_com_python_operator():
    """
    minha primeira Pipipeline
    """
    @task
    def primeira_atividade():
        print("Primeira atividade iniciada")
        sleep(1)
        print("Primeira atividade finalizada")

    @task
    def segunda_atividade():
        print("Segunda atividade iniciada")
        sleep(1)
        print("Segunda atividade finalizada")

    @task
    def terceira_atividade():
        print("Terceira atividade iniciada")
        sleep(1)
        print("Terceira atividade finalizada")

    t1 = primeira_atividade()
    t2 = segunda_atividade()
    t3 = terceira_atividade()

    t1 >> t2 >> t3

primeira_dag_com_python_operator()