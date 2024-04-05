# prefect_2_public
Testing prefect functionality


## Setup

```
sudo prefect server start
-- once running kill server (TODO: figure out how to give user permisssion to that directory to create files.)
prefect server start
-- open new terminal in the same folder as prefect.yaml
prefect work-pool create "wp-local-process2" --type process

prefect --no-prompt deploy --name flow_of_deployments
prefect --no-prompt deploy --name concurrent_flow_1_deployment
prefect --no-prompt deploy --name concurrent_flow_2_deployment

```