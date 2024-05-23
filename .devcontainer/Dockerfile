FROM mcr.microsoft.com/devcontainers/base:ubuntu-22.04
# FROM mcr.microsoft.com/devcontainers/python:3.11-bullseye
# FROM mcr.microsoft.com/devcontainers/python:3.12-bullseye

# Version: prefect:2.16.4-python3.10-ubuntu22.04ip route get 1.2.3.4 | awk '{print $7}'

RUN sudo apt-get update && sudo apt-get install --no-install-recommends -y python3-pip && pip3 install pyodbc==4.0.34 awscli boto3 && pip3 install prefect==2.16.9 prefect-dask==0.2.4 prefect-dbt==0.3.1 prefect-github==0.2.2 prefect-shell==0.2.2 prefect-snowflake==0.26.1 && pip3 install azure-core==1.29.5 azure-cosmos==4.5.1 azure-identity==1.15.0 azure-storage-blob==12.19.0 && pip3 install dbt-core==1.3.0 dbt-extractor==0.4.1 dbt-semantic-interfaces==0.2.0 dbt-snowflake==1.3.0  && pip3 install snowflake-connector-python==2.7.12 prefect-snowflake==0.26.1 pandas==1.5.2&& python3 -m pip install --upgrade jsonschema && sudo apt-get clean && sudo rm -rf /var/lib/apt/lists/*
# RUN sudo apt-get update && \
#     sudo apt-get install --no-install-recommends -y python3-pip && \
#     pip3 install --upgrade pip && \
#     pip3 install prefect==2.16.9 && \
#     pip3 install dbt-core==1.7.11 dbt-snowflake==1.7.3 && \
#     pip3 install psycopg2-binary==2.9.3 s3fs==2022.8.2 cryptography==42.0.4 && \
#     # TODO: install odbc driver and mongoexport driver
#     sudo apt-get clean && sudo rm -rf /var/lib/apt/lists/*
    