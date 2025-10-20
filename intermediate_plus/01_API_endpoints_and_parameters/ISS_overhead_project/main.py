import requests
from datetime import datetime
import os
import smtplib
from dotenv import load_dotenv
import time

MY_LATITUDE = 48.208176
MY_LONGITUDE = 16.373819

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

def is_within_my_position(current_lat, current_lng):
    if int(MY_LATITUDE) - 5  <= current_lat <= int(MY_LATITUDE) + 5 and int(MY_LONGITUDE) - 5 <= current_lng <= int(MY_LONGITUDE) + 5:
        return True
    else:
        return False

parameters = {
    "lat": MY_LATITUDE,
    "lng": MY_LONGITUDE,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
time_now = datetime.now()

while True:
    time.sleep(60)
    if is_within_my_position(iss_latitude, iss_longitude) == True:
        if time_now.hour >= sunset and time_now.hour <= sunrise:
            load_dotenv()
            my_email = os.getenv("STMP_MAIL")
            password = os.getenv("SMTP_PASSWORD")
            dest_email = os.getenv("SMTP_MAIL")
            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(user=my_email, password=password)
                connection.sendmail(
                    from_addr=my_email,
                    to_addrs=my_email,
                    msg="Subject:ISS over your head!\n\n Look up now into the starry night!")

