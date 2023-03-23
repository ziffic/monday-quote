# import smtplib
# import connect
import datetime as dt

# my_email = connect.account_email
# password = connect.account_password
#
# with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(from_addr=my_email,
#                         to_addrs="dave@dryweb.com",
#                         msg="Subject: Hello\n\nThis is a test.")
# connection.close()

now = dt.datetime.now()
year = now.year
month = now.month
day_of_week = now.weekday()
print(day_of_week)

date_of_birth = dt.datetime(year=2000, month=3, day=23)
print(date_of_birth)
