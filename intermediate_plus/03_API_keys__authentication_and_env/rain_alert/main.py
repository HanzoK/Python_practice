import os
from dotenv import load_dotenv
import requests
from twilio.rest import Client

load_dotenv()
account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")
my_number = os.getenv("MY_PHONE_NUMBER")
twilio_number = os.getenv("TWILIO_NUMBER")

parameters = {
    "lat": os.getenv("LATITUDE"),
    "lon": os.getenv("LONGITUDE"),
    "cnt": 12,
    "appid": os.getenv("API_KEY"),
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/forecast", params=parameters)
response.raise_for_status()
data = response.json()

will_it_rain = False
for hour in data["list"]:
    condition_code = hour["weather"][0]["id"]
    if int(condition_code) < 700:
        will_it_rain = True
if will_it_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
    body="It's going to rain. Please take care of yourself and bring an umbrella with you. ;)",
    from_=twilio_number,
    to=my_number,
    )
    print(message.status)
