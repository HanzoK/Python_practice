import os
import requests
from dotenv import load_dotenv

load_dotenv()

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
ALPHA_KEY = os.getenv("STOCK_API_KEY")
THRESHOLD_CHANGE = 5.0 # Minimum % change required to trigger news message

url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={STOCK}&apikey={ALPHA_KEY}"

required_vars = {
    "STOCK_API_KEY": ALPHA_KEY,
}

missing = [item for (item, value) in required_vars.items() if not value]
if missing:
    raise ValueError(f"Missing environment variables: {', '.join(missing)}. Please check your .env file.")

response = requests.get(url)
data = response.json()

time_series = data["Time Series (Daily)"]
historical_dates = sorted(time_series.keys(), reverse=True)
latest_date = historical_dates[0]
previous_date = historical_dates[1]

latest_close = float(time_series[latest_date]["4. close"])
previous_close = float(time_series[previous_date]["4. close"])

price_change = round((latest_close - previous_close) / previous_close * 100, 2)

moved_enough = price_change >= THRESHOLD_CHANGE

if moved_enough:
    print("Get News")
else:
    pass

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

