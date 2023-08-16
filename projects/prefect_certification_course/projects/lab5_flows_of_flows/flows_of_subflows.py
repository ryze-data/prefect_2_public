"""
lab5

- Create a deployment via cli

"""

import httpx
from prefect import flow, task
from prefect.tasks import task_input_hash
from datetime import timedelta

import time


@task(retries=2)
def fetch_weather(lat: float, lon: float):
    base_url = "https://api.open-meteo.com/v1/forecast/"
    return 20

@task(cache_key_fn=task_input_hash, cache_expiration=timedelta(minutes=5))
def save_weather(temp: float):
    file = "Write to file weather.csv"
    time.sleep(2)
    return "Succefully wrote temp"

@flow(retries=3)
def sample_pipeline(lat: float, lon: float):
    round_1 = extract_rdbms()
    round_2 = extract_document()
    round_3 = load()
    round_4 = transform()

    # Ending tasks
    temp = fetch_weather(lat, lon)
    result = save_weather(temp)
    # curr_wind = windspeed(lat, lon)
    print(f"Current temp C: {temp} degrees ")
    # and windspeed is {curr_wind}")

@flow
def extract_rdbms():
    print("extracting tables")
    time.sleep(2)
    temp = fetch_weather(lat, lon)
    time.sleep(4)
    return "Complete"

@flow
def extract_document():
    print("document tables")
    time.sleep(4)
    return "Complete"

@flow
def load():
    print("loading data")
    fetch_weather(38.9, -77.0)
    time.sleep(7)
    return "Complete"

@flow
def transform():
    print("transforming data")
    time.sleep(3)
    return "Complete"


if __name__ == "__main__":
    sample_pipeline(38.9, -77.0)