import datetime as dt
import pandas
from random import randint
import smtplib

# Setting up your email and password
MY_EMAIL = "test@mail.com"
MY_PASSWORD = "test7475"

# Getting Today's Date
today = (dt.datetime.now().month, dt.datetime.now().day)
# Using Pandas to read csv file
data = pandas.read_csv("birthdays.csv")
data_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}

# Checking if someone from dict has Birthday
if today in data_dict:
    # In case it's True we are getting random letter template and person name
    bday_person = data_dict[today]["name"]
    file_path = f"letter_templates/letter_{randint(1,3)}.txt"
    with open(file_path) as letter_file:
        # Replacing placeholder with real name
        contents = letter_file.read()
        new_mail = contents.replace("[NAME]", bday_person)

    # Using smtplib to send Birthday wishes to the bday Person
    # Each mail provider has different smtp address
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=data_dict[today]["email"],
            msg=f"Subject:Happy Birthday!\n\n{new_mail}"
        )

print(new_mail)
