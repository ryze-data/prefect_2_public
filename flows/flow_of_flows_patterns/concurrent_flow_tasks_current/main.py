from datetime import timedelta
import time
from prefect import flow, task
from prefect.tasks import task_input_hash
from subflow_one import my_subflow
from subflow_two import my_subflow_two

@flow(name="Hello Flow")
def hello_world(name="world"):
    message = print_hello.submit(name="Task 1 concurrent")
    message_2 = print_hello.submit(name="Task 2 concurrent")
    message_3 = print_hello.submit(name="Task 3 concurrent")
    
@task(name="Print Hello")
def print_hello(name):
    msg = f"Hello {name}!"
    time.sleep(5)
    print(msg)
    # my_task.fn()
    return msg

# @task
# def my_task():
#     time.sleep(3)
#     print("Hello, I'm a task called my_task()")

@task(cache_key_fn=task_input_hash, cache_expiration=timedelta(days=1))
def hello_task(name_input):
    # Doing some work
    print("Saying hello")
    return "hello " + name_input


@flow(log_prints=True)
def flow_of_tasks():
    # basic
    # upstream_results = upstream.submit()
    # downstream_1_result = downstream_1.submit(upstream_results)
    # downstream_2_result = downstream_2.submit(upstream_results)
    # mapped_task_results = mapped_task.map([downstream_1_result, downstream_2_result])
    # final_task(mapped_task_results)   

    # data pipeline
    list_of_tables = get_database_tables.submit()

    for table in list_of_tables.result():
        table_results = execute_query.submit(table,wait_for=[list_of_tables])
        # database_to_datalake = execute_query.submit(table,wait_for=[table_results])
        # mapped_task_results = mapped_task.map([downstream_1_result, downstream_2_result])
        #validation(database_to_datalake)

@task
def upstream():
    return "Hello from upstream!"

@task
def get_database_tables():
    return ["table1", "table2", "table3"]

@task
def execute_query(input):
    return f"select * from {input}"

@task
def execute_query(input):
    return f"{input} --> organization_datalake"

@task
def validation(input):
    return f"{input}. Data Validation has been completed."


@task
def downstream_1(input):
    return input

@task
def downstream_2(input):
    return input

@task
def mapped_task(input):
    return input

@task
def final_task(input):
    print(input)

if __name__ == "__main__":
    # hello_world("Marvin")
    flow_of_tasks()