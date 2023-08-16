"""
lab4

- Create a deployment via cli

"""

import httpx
from prefect import flow, task
from prefect.tasks import task_input_hash
from datetime import timedelta

@task(retries=2)
def fetch_weather(lat: float, lon: float):
    base_url = "https://api.open-meteo.com/v1/forecast/"
    weather = httpx.get(
        base_url,
        params = dict(latitude=lat, longitude=lon, hourly="temperature_2m"),
    )
    most_recent_temp = float(weather.json()["hourly"]["temperature_2m"][0])
    print(f"Most recent temp C: {most_recent_temp} degrees")
    return most_recent_temp
@task(cache_key_fn=task_input_hash, cache_expiration=timedelta(minutes=5))
def save_weather(temp: float):
    with open("weather.csv", "w+") as w:
        w.write(str(temp))
    return "Succefully wrote temp"
@task(retries=2, retry_delay_seconds=2)
def windspeed(lat: float, lon: float):
    base_url = "https://api.open-meteo.com/v1/forecast/"
    wind = httpx.get(
        base_url,
        params = dict(latitude=lat, longitude=lon, hourly="temperature_2m"),
    )
    wind_speed = float(wind.json()["hourly"]["windspeed_10m"][0])
    print(f"Current wind speed C: {wind_speed}")
    return wind_speed
    
@flow(retries=3)
def pipeline(lat: float, lon: float):
    temp = fetch_weather(lat, lon)
    result = save_weather(temp)
    curr_wind = windspeed(lat, lon)
    print(f"Current temp C: {temp} degrees and windspeed is {curr_wind}")
if __name__ == "__main__":
    fetch_weather(38.9, -77.0)