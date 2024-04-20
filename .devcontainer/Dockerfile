FROM mcr.microsoft.com/devcontainers/base:ubuntu-22.04
# FROM mcr.microsoft.com/devcontainers/python:3.11-bullseye
# FROM mcr.microsoft.com/devcontainers/python:3.12-bullseye

# Version: prefect:2.16.4-python3.10-ubuntu22.04
RUN sudo apt-get update && \
    sudo apt-get install --no-install-recommends -y python3-pip && \
    pip3 install --upgrade pip && \
    pip3 install prefect==2.16.9 && \
    pip3 install dbt-core==1.7.13 dbt-snowflake==1.7.3 pydantic==1.10.6 && \
    pip3 install psycopg2-binary==2.9.3 s3fs==2022.8.2 cryptography==42.0.4 && \
    # TODO: install odbc driver and mongoexport driver (pyodbc)
    sudo apt-get clean && sudo rm -rf /var/lib/apt/lists/*
    