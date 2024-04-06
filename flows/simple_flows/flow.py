'''
Simple Flow
'''
from prefect import flow, task

import time
import random


@flow # concurrentTaskRunner
def simple_flow():

    # unit 1
    t1 = prestep1_task.submit()
    t2 = prestep2_task.submit()
    # unit 2
    extract_task(wait_for=[t1,t2])
    load_task()
    # unit 3
    downstream_task()

@task
def prestep1_task():
    time.sleep(random.randint(4, 8))
    print("Prestep 1!")
@task
def prestep2_task():
    time.sleep(random.randint(4, 8))
    print("Prestep 2!")

@task
def extract_task():
    time.sleep(random.randint(3, 5))
    print("Extracted Data!")

@task
def load_task():
    time.sleep(random.randint(3, 5))
    print("Loaded Data")

@task
def downstream_task():
    print("I'm downstream!")

if __name__ == "__main__":
    simple_flow()