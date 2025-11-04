import os
import requests
from dotenv import load_dotenv
from twilio.rest import Client

load_dotenv()

STOCK = "TSLA"
THRESHOLD_CHANGE = 1.0 # Minimum % change required to trigger news message
ALPHA_KEY = os.getenv("STOCK_API_KEY")
NEWS_KEY = os.getenv("NEWS_API_KEY")
ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
MY_NUMBER = os.getenv("MY_PHONE_NUMBER")
TWILIO_NUMBER = os.getenv("TWILIO_NUMBER")

stock_url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={STOCK}&apikey={ALPHA_KEY}"
news_url = f"https://newsapi.org/v2/everything?q=TSLA&apiKey={NEWS_KEY}"

required_vars = {
    "STOCK_API_KEY": ALPHA_KEY,
    "NEWS_API_KEY": NEWS_KEY,
    "TWILIO_ACCOUNT_SID": ACCOUNT_SID,
    "TWILIO_AUTH_TOKEN": AUTH_TOKEN,
    "MY_PHONE_NUMBER": MY_NUMBER,
    "TWILIO_NUMBER": TWILIO_NUMBER,
}

missing = [item for (item, value) in required_vars.items() if not value]
if missing:
    raise ValueError(f"Missing environment variables: {', '.join(missing)}. Check your .env file for the mising information!")

stock_response = requests.get(stock_url)
stock_response.raise_for_status()
stock_data = stock_response.json()

if "Note" in stock_data:
    raise RuntimeError(f"AlphaVantage API Notice: {stock_data['Note']}")
if "Information" in stock_data:
    raise RuntimeError(f"AlphaVantage API Info: {stock_data['Information']}")
if "Error Message" in stock_data:
    raise RuntimeError(f"AlphaVantage API Error: {stock_data['Error Message']}")

time_series = stock_data["Time Series (Daily)"]
historical_dates = sorted(stock_data.keys(), reverse=True)
latest_date = historical_dates[0]
previous_date = historical_dates[1]

latest_close = float(time_series[latest_date]["4. close"])
previous_close = float(time_series[previous_date]["4. close"])

price_change = round((latest_close - previous_close) / previous_close * 100, 2)
moved_enough = abs(price_change) >= THRESHOLD_CHANGE

direction = "🔺+" if price_change > 0 else "🔻-"

if moved_enough:
    news_response = requests.get(news_url)
    news_response.raise_for_status()
    news_data = news_response.json()
    articles = news_data["articles"]
    latest_news_pieces = articles[:3]

    header = f"{STOCK}: {direction}{price_change}"
    formatted_articles = [f"{header}\nHeadline: {article['title']}\n{article['description']}" for article in latest_news_pieces]

    client = Client(ACCOUNT_SID, AUTH_TOKEN)
    for msg_to_be_sent in formatted_articles:
        message = client.messages.create(
        body=msg_to_be_sent,
        from_=TWILIO_NUMBER,
        to=MY_NUMBER,
        )
        print(message.status)
else:
    print(f"No significant changes over selected threshold of {THRESHOLD_CHANGE}%.")