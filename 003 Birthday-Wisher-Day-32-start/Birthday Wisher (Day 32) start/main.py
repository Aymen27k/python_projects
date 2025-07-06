import smtplib
import datetime as dt
import random

# -------------- Checking day of the week -----------------#
date_of_birth = dt.datetime(year=1990, month=11, day=23)

now = dt.datetime.now()
week_day = now.weekday()
print(week_day)
# -------------- Getting a random Quote -----------------#

with open("quotes.txt", 'r') as file:
    data = file.readlines()
    quotes_data = [char.strip() for char in data]
    quote = random.choice(quotes_data)

# -------------- Email setup & sending -----------------#

if week_day == 1:
    MY_MAIL = "ethancarter123x@gmail.com"
    password = "kyjlvbfzmdhxcbgh"

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_MAIL, password=password)
        connection.sendmail(from_addr=MY_MAIL,
                            to_addrs="aymen27k@hotmail.com",
                            msg=f"subject:Motivation Quote\n\n {quote}"
                            )
