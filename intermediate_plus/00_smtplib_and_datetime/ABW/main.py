# import datetime as dt

# now = dt.datetime.now()
# year = now.year
# month = now.month
# day_of_week = now.weekday()
# print(year)

# date_of_birth = dt.datetime(year=1995, month=12, day=15)
# print(date_of_birth)

import smtplib
import os
from dotenv import load_dotenv
import datetime as dt
import random

load_dotenv()

with open("quotes.txt") as quote_file:
    quote_list = [quote for quote in quote_file]

now = dt.datetime.now()
current_weekday = now.weekday()

quote_to_be_sent = random.choice(quote_list)

my_email = os.getenv("SMTP_EMAIL")
password = os.getenv("SMTP_PASSWORD")
dest_email = os.getenv("SMTP_DEST_EMAIL")
# connection = smtplib.SMTP("smtp.gmail.com")

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls() #starting Transport Layer Security (makes connection secure)
    connection.login(user=my_email, password=password)
    connection.sendmail(
        from_addr=my_email, 
        to_addrs=dest_email, 
        msg=f"Subject:Motivational Quote\n\n{quote_to_be_sent}"
    )

# connection.close()
