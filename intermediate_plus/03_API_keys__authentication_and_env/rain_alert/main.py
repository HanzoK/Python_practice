import os
from dotenv import load_dotenv
import requests

load_dotenv()

parameters = {
    "lat": os.getenv("LATITUDE"),
    "lon": os.getenv("LONGITUDE"),
    "cnt": 4,
    "appid": os.getenv("API_KEY"),
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/forecast", params=parameters)
response.raise_for_status()
data = response.json()

print(data)
