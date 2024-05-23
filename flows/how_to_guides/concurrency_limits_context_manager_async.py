'''
Reference: https://docs.prefect.io/latest/guides/global-concurrency-limits/
'''
import asyncio
from prefect import flow, task
from prefect.concurrency.asyncio import concurrency

@task
async def process_data(x, y):
    async with concurrency("database", occupy=1):
        return x + y


@flow
async def my_flow():
    for x, y in [(1, 2), (2, 3), (3, 4), (4, 5)]:
        await process_data.submit(x, y)


if __name__ == "__main__":
    asyncio.run(my_flow())