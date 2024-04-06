from prefect import flow, task
from prefect.concurrency.sync import concurrency
import time 


@task
def process_data(x, y):
    
    return x + y


@flow(log_prints=True)
def my_flow():
    for x, y in [(1, 2), (2, 3), (3, 4), (4, 5)]:
        print("testing:", x, " : ",y)
        time.sleep(4)
        process_data.submit(x, y)


if __name__ == "__main__":
    my_flow()