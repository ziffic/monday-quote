import smtplib
import connect

my_email = connect.account_email
password = connect.account_password

with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email,
                        to_addrs="dave@dryweb.com",
                        msg="Subject: Hello\n\nThis is a test.")
connection.close()
