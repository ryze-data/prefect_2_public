from prefect import flow, task
from prefect.concurrency.sync import rate_limit


@task
def my_task(i):
    return i


@flow
def rate_limit_flow():
    for _ in range(10):
        rate_limit("slow-my-flow", occupy=3)
        my_task.submit(1)


if __name__ == "__main__":
        rate_limit_flow()