# #################### Extra Hard Starting Project ######################
import datetime as dt
import pandas
import random
import smtplib

now = dt.datetime.now()
month = now.month
day = now.day
PLACEHOLDER = "[NAME]"
MY_MAIL = "ethancarter123x@gmail.com"
MY_PASSWORD = "kyjlvbfzmdhxcbgh"

# 1. Update the birthdays.csv
df = pandas.read_csv("birthdays.csv")
data_list = [[row['name'], row['email'], row['year'], row['month'], row['day']] for index, row in df.iterrows()]
for person in data_list:
    person_month = person[3]
    person_day = person[4]
    # 2. Check if today matches a birthday in the birthdays.csv
    if person_month == month and person_day == day:
        person_name = person[0]
        person_mail = person[1]
        # 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's
        with open(f"letter_templates/letter_{random.randint(1, 3)}.txt", 'r') as mail:
            mail_body = mail.read()
            # actual name from birthdays.csv
            mail_body = mail_body.replace(PLACEHOLDER, person_name)
            # 4. Send the letter generated in step 3 to that person's email address.
            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(MY_MAIL, MY_PASSWORD)
                connection.sendmail(from_addr=MY_MAIL,
                                    to_addrs=person_mail,
                                    msg=f"subject:Happy Birthday!\n\n {mail_body}")
                print(f"Mail Sent successfully to {person_name}")
