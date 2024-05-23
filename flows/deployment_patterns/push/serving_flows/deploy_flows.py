from prefect import flow, task

if __name__ == "__main__":
    flow.from_source(
        source="https://github.com/ryze-data/prefect_2_public.git",
        entrypoint="./flows/simple_flows/flow.py:simple_flow",
        
    ).deploy(name="deployment-with-github-storage",
    work_pool_name="wp-local-process",)