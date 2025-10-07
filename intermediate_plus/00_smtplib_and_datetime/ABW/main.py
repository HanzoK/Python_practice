import pandas as pd
import datetime as dt
import random
import os
import smtplib
from dotenv import load_dotenv

LETTER_FOLDER = "letter_templates"

time = dt.datetime.now()
date_tuple = (time.month, time.day)
df = pd.read_csv("birthdays.csv")

bd_dict = {
    (row.month, row.day): row for (index, row) in df.iterrows()
}

if date_tuple in bd_dict:
    bd_person = bd_dict[date_tuple]
    random_letter = random.choice(os.listdir(LETTER_FOLDER))

    with open(f"{LETTER_FOLDER}/{random_letter}") as letter_file:
        new_letter = letter_file.read()
        stripped_name = bd_person["name"].strip()
        replaced_letter = new_letter.replace("[NAME]", bd_person["name"])
    bd_person_email = bd_person["email"].split("@", 1)[1]

    if bd_person_email == "gmail.com":
        mail_server = "smtp.gmail.com"
    else:
        mail_server = "smtp.mail.yahoo.com"

    load_dotenv()

    my_email = os.getenv("SMTP_EMAIL")
    password = os.getenv("SMTP_PASSWORD")

    with smtplib.SMTP(f"{mail_server}") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email, 
            to_addrs=bd_person["email"], 
            msg=f"Subject:Happy Birthday!\n\n{replaced_letter}"
        )


