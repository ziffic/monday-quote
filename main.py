import smtplib
import connect
import datetime as dt
import random

my_email = connect.account_email
password = connect.account_password

date_to_send = dt.date(2023, 3, 23)

with open("quotes.txt", "r") as quotes:
    lines = quotes.readlines()

daily_quote = random.choice(lines)


# Check if today matches the day to send message
if date_to_send == dt.date.today():
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs="dave@dryweb.com",
                            msg=f"Subject: Hello\n\n{daily_quote}")

connection.close()
