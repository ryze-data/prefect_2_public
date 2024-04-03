from prefect import flow, task
from prefect.deployments import run_deployment


@flow
def flow_of_deployments():
    deployment_run_1 = run_deployment_task.submit(
        flow_name="parallel-work",
        deployment_name="process-user",
        parameters={"user_id": 1},
    )
    deployment_run_2 = run_deployment_task.submit(
        flow_name="parallel-work",
        deployment_name="process-user",
        parameters={"user_id": 2},
    )
    downstream_task(wait_for=[deployment_run_1, deployment_run_2])


@task(task_run_name="Run deployment {flow_name}/{deployment_name}")
def run_deployment_task(
    flow_name: str,
    deployment_name: str,
    parameters: dict
):
    run_deployment(
        name=f"{flow_name}/{deployment_name}",
        parameters=parameters
    )


@task
def downstream_task():
    print("I'm downstream!")