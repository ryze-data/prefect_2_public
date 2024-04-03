import time
from prefect import flow, serve, deploy, task

@task(name="Print Hello")
def print_hello(name):
    msg = f"Hello {name}!"
    time.sleep(5)
    print(msg)

    return msg

@flow
def concurrent_flow_1(sleep: int = 60, name: str ="world"):
    "Sleepy flow - sleeps the provided amount of time (in seconds)."
    time.sleep(sleep)
    message = print_hello.submit(name="Task 1 concurrent")
    message_2 = print_hello.submit(name="Task 2 concurrent")
    fast_flow()
    message_3 = print_hello(name="Task 3 concurrent", wait_for=[message, message_2])


@flow
def fast_flow(name:str ="world"):
    "Fastest flow this side of the Mississippi."
    message_2 = print_hello.submit(name="Task 3 concurrent")
    return


if __name__ == "__main__":
    concurrent_flow_1.from_source(
        "https://github.com/ryze-data/prefect_2_public.git",
        entrypoint="flows/patterns/serving_flows/single_deployment/main_2.py:slow_flow",
    ).serve(
        name="concurrent-deployment-1",
        # cron="0/5 * * * *",
        tags=["testing", "tutorial","deployment2"],
        description="This is an example deployment flow of a parrallel task execution flow.",
        version="tutorial/deployments",
        parameters={"sleep": 5,"name": "world"}
    ).deploy(
        name="no-image-deployment",
        work_pool_name="wp-local-subprocess",
        build=True
    )