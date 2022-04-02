import smtplib
import datetime as dt
import random
import pandas

my_email = "ashwin.shv21@gmail.com"
password = "Python@21"

now = dt.datetime.now()
week = now.weekday()

if week == 0:
    with open("quotes.txt") as data:
         data_1 = data.readlines()
         randm = random.choice(data_1)
    data_2 = pandas.read_csv("mail.csv")
    da = data_2["mail_id"].to_list()


    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs=da,
                            msg=f"Subject:Monday Motivation\n\n {randm}")



