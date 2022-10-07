from email.message import EmailMessage
from decouple import config
import pandas as pd
import smtplib

# your email credentials
mailid = config("EMAILID")
mailpw = config("EMAILPW")

# input from the user
sub = input("Enter Email Subject : ")
body = input("Enter Email Body : ")
file_path = input("Enter Path of Excel File: ")

# reading from excel file
df = pd.read_excel(file_path)

# email setup
for mailids in df['Emailid'].values:
    msg = EmailMessage()
    msg['Subject'] = sub
    msg['From'] = mailid
    msg['To'] = mailids
    msg.set_content(body)
    # sending email
    try:
        server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
        server.login(mailid, mailpw)
        print("Sending Mail")
        server.send_message(msg)
        server.quit()
        print("Email Sent Successfully")
    except Exception as e:
        print(e)