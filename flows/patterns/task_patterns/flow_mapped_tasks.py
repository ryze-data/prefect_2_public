from prefect import flow, task

import time

@flow(log_prints=True)
def flow_of_tasks():
    upstream_result = upstream.submit()
    downstream_1_result = downstream_1.submit(wait_for=[upstream_result])
    downstream_2_result = downstream_2.submit(wait_for=[upstream_result])
    mapped_task_results = mapped_task.map(upstream_result, wait_for=[downstream_1_result, downstream_2_result])
    final_task(wait_for=mapped_task_results)


@task
def upstream():

    print("get secret")
    print('Building command')
    command_list = [f'bcp select * from table_{i} queryout table_{i}.json' for i in range(1,4)] # list[1,2,3]

    return command_list

@task
def downstream_1():
    time.sleep(3)
    pass

@task
def downstream_2():
    time.sleep(3)
    pass

@task
def mapped_task(input):
    print('Command: ',input)
    time.sleep(2)
    pass


@task
def final_task():
    time.sleep(3)
    pass

if __name__ == "__main__":
    flow_of_tasks()