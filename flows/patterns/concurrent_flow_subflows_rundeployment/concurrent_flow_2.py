from datetime import timedelta
import time
from prefect import flow, task
from prefect.tasks import task_input_hash

@task(name="Print Hello")
def print_hello(name):
    msg = f"Hello {name}!"
    time.sleep(5)
    print(msg)

    return msg


@flow()
def concurrent_flow_2(name="world"):
    
    message = print_hello.submit(name="Task 1 concurrent")
    message_2 = print_hello.submit(name="Task 2 concurrent")
    message_3 = print_hello(name="Task 3 concurrent", wait_for=[message, message_2])

if __name__ == "__main__":
    concurrent_flow_2.from_source(
        "https://github.com/ryze-data/prefect_2_public.git",
        entrypoint="flows/patterns/serving_flows/single_deployment/main.py:concurrent_flow_2",
    ).serve(
        name="concurrent-deployment-2",
        # cron="0/5 * * * *",
        tags=["testing", "tutorial","deployment2"],
        description="This is an example deployment flow",
        version="tutorial/deployments",
        parameters={"name": "world"}
    ).deploy(
        name="no-image-deployment",
        work_pool_name="wp-local-subprocess",
        build=True
    )