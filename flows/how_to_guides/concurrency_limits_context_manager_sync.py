'''
Reference: https://docs.prefect.io/latest/guides/global-concurrency-limits/
'''
from prefect import flow, task
from prefect.concurrency.sync import concurrency


@task
def process_data(x, y):
    with concurrency("database", occupy=1):
        return x + y


@flow
def limit_concurrency_sync_flow():
    for x, y in [(1, 2), (2, 3), (3, 4), (4, 5)]:
        process_data.submit(x, y)


if __name__ == "__main__":
    limit_concurrency_sync_flow()