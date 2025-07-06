import requests
from dotenv import load_dotenv
import os
import datetime
import smtplib


load_dotenv()
# Variables and URLS #
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
alpha_vantage_api_key = os.getenv("AA_KEY")
aa_url = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&apikey=demo'
aa_param = {
    "function": "TIME_SERIES_INTRADAY",
    "symbol": STOCK,
    "interval": "60min",
    "extended_hours": False,
    "apikey": alpha_vantage_api_key,
}

news_url = "https://newsapi.org/v2/everything"
news_key = os.getenv("NEWS_API_KEY")
news_para = {
    "q": COMPANY_NAME,
    "apiKey": news_key,
    "pageSize": 3,
    "language": "en"
}
news_snippet = []

MY_MAIL = "ethancarter123x@gmail.com"
MY_PASSWORD = "kyjlvbfzmdhxcbgh"


# Function to Fetch Data from an API #
def fetch_data(api, par):
    try:
        response = requests.get(api, params=par)
        response.raise_for_status()
        data = response.json()
        return data
    except Exception as e:
        print(f"An error occurred: {e}")
        return None


stock_data = fetch_data(aa_url, aa_param)
time_series_data = stock_data['Time Series (60min)']
print(f"time series data {time_series_data}")
today_time_date = datetime.datetime.now()
today = today_time_date.date()
yesterday = today - datetime.timedelta(days=1)
day_before_yesterday = today - datetime.timedelta(days=2)
# print(today_time_date)
# print(today)
# print(yesterday)
# print(day_before_yesterday)
# print(JSON_DATA)

# Transforming Date variables  #
time_stamp_keys = time_series_data.keys()
time_stamp_list = list(time_stamp_keys)
# print(f"Time Stamp list: {time_stamp_list}")
time_stamp_obj = [datetime.datetime.strptime(date, "%Y-%m-%d %H:%M:%S").date() for date in time_stamp_list]
# print(f"Time stamp object: {time_stamp_obj}")

# Extracting Values from Stock Data #
yesterday_closing_value = None
day_before_yesterday_close_price = None
difference_perc = 0
price_found_yesterday = False
price_found_before_yesterday = False

for current_stamp in time_stamp_list:
    current_date = datetime.datetime.strptime(current_stamp, "%Y-%m-%d %H:%M:%S").date()
    if current_date == yesterday and not price_found_before_yesterday and not price_found_yesterday:
        yesterday_closing_value = time_series_data[current_stamp]['4. close']
        price_found_yesterday = True
    elif current_date == day_before_yesterday:
        day_before_yesterday_close_price = time_series_data[current_stamp]['4. close']
        price_found_before_yesterday = True
        break
# Calculate Percentages #
if price_found_yesterday and price_found_before_yesterday:
    difference_perc = (float(yesterday_closing_value) - float(day_before_yesterday_close_price)) / float(
        day_before_yesterday_close_price) * 100

direction_short = "increased" if difference_perc >= 0 else "decreased"

print(f"Yesterday closing value: {yesterday_closing_value}")
print(f"2 days ago closing value: {day_before_yesterday_close_price}")
print(f"Percentage = {difference_perc}")

# Getting News Data and Transforming it #
try:
    if abs(difference_perc) > 10:
        news_data = fetch_data(news_url, news_para)
        news_list = news_data['articles']
        news_title = None
        news_description = None
        for source in news_list:
            news_title = source['title']
            news_description = source['description']
            final_news = f"{news_title} | {news_description}\n"
            news_snippet.append(final_news)
        full_message_news = "".join(news_snippet)
except TypeError:
    print("No Data Available")

    # Composing the MAIL #
    message_to_send = (
        f"From: {MY_MAIL}\r\n"
        f"To: {MY_MAIL}\r\n"
        f"Subject: {COMPANY_NAME} Extraordinary change!\r\n"
        f"Content-Type: text/plain; charset=utf-8\r\n"
        f"\r\n"
        f"The stock had an extraordinary change! {direction_short} of {difference_perc:.2f}% in the value of {COMPANY_NAME}. Here are some news related to that:\n{full_message_news}"
    )

    encoded_message_bytes = message_to_send.encode("utf-8")

    # Sending an Email with News and Fluctuation amount #
    try:
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(MY_MAIL, MY_PASSWORD)
            connection.sendmail(to_addrs=MY_MAIL, from_addr=MY_MAIL,
                                msg=encoded_message_bytes)
            print(f"Mail sent to {MY_MAIL}")
    except Exception as e:
        print(f"Failed to send email: {e}")
