'''
Simple Flow
'''
from prefect import flow, task
from prefect.task_runners import ConcurrentTaskRunner
from prefect.concurrency.sync import concurrency


import time
import random

@task
def stop_at_floor(floor):
    print(f"elevator moving to floor {floor}")
    time.sleep(floor)
    print(f"elevator stops on floor {floor}")

@flow(task_runner=ConcurrentTaskRunner())
def elevator():
    for floor in range(10, 0, -1):
        stop_at_floor.submit(floor)

@flow # concurrentTaskRunner
def simple_flow():

    # unit 1
    t1 = prestep1_task
    t2 = get_tables_task
    # TypeError: 'Task' object is not iterable
    for t in t2:
        extract_task(t) # loop through these tasks
    # unit 2
    # extract_task(t2,wait_for=[t1]) # loop through these tasks
    load_task()
    # # unit 3
    downstream_task()

@task
def prestep1_task():
    time.sleep(random.randint(4, 8))
    print("Prestep 1!")
    return ['db1']

@task
def get_tables_task():

    print("get secret")
    print('Building command')
    command_list = [f'bcp select * from table_{i} queryout table_{i}.json' for i in range(1,4)] # list[1,2,3]

    return command_list

@task
def extract_task(command):

    print(f'Executing {command}')


@task
def load_task():
    time.sleep(random.randint(3, 5))
    print("Loaded Data")

@task
def downstream_task():
    print("I'm downstream!")

if __name__ == "__main__":
    elevator()