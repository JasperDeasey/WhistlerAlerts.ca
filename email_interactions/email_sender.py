import smtplib
import json
from string import Template
import datetime

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

MY_ADDRESS = 'my_email@gmail.com'
PASSWORD = 'my_password'


def send_email(email, month, date):
    # names, emails = get_contacts('mycontacts.txt')  # read contacts

    # set up the SMTP server
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login(MY_ADDRESS, PASSWORD)
    month_string = datetime.date(1900, month, 1).strftime('%B')
    # For each contact, send the email_interactions:
    # for name, email_interactions in zip(names, emails):
    msg = MIMEMultipart()  # create a message
    message = "Whistler reservations are now available on " + month_string + " " + str(date) + "!"


    # setup the parameters of the message
    msg['From'] = MY_ADDRESS
    msg['To'] = email
    msg['Subject'] = "WHISTLER RESERVATIONS: " + month_string + " " + str(date) + " has opened! \nYou will no longer recieve updates about " + month_string + " " + str(date) + " reservations."

    # add in the message body
    msg.attach(MIMEText(message, 'plain'))

    # send the message via the server set up earlier.
    s.send_message(msg)
    print("sent message to: " + email)
    del msg

# Terminate the SMTP session and close the connection
    s.quit()
