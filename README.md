# Prefect 2 Public

This was repo was created to create a sandbox environment separate from production where prefect concepts can be tested in a fully isolated environment. It has been useful to test upgrades as well.

## Prerequisites

- Docker installed on Mac or Windows (wsl)
- VSCode and Dev Containers extension installed
- VSCode workspace save to repo directory
- Create .env file inside the repo directory and the .devcontainer folder based on env variables in the docker-compose.yml file  

## Docker Compose Instructions

```
docker compose up
```

## Dev Container Instructions

```
ctrl + shift + p or cmd + shift + p

Dev Container: Rebuild Container Without Cache
```

## Setup

```
sudo prefect server start
-- once running kill server (TODO: figure out how to give user permisssion to that directory to create files.)
prefect server start
-- open new terminal in the same folder as prefect.yaml
prefect work-pool create "wp-local-process" --type process;
prefect worker start --pool wp-local-process;
-- open up new terminal

prefect --no-prompt deploy --name flow_of_deployments
prefect --no-prompt deploy --name concurrent_flow_1_deployment
prefect --no-prompt deploy --name concurrent_flow_2_deployment

```

## Future Enhancements

Add to docker compose to create separate containers for
- cli
- workers
- docker within docker capability

## Other great repos to reference:

https://github.com/rpeden/prefect-docker-compose