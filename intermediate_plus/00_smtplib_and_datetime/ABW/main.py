import smtplib
import os
from dotenv import load_dotenv

load_dotenv()

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
        msg="Subject:Hello\n\nThis is the body of my email."
    )

# connection.close()