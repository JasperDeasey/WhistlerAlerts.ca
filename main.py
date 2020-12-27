import json
import time

from email_interactions import email_sender
from wb_interactions import scraper, parser

while True:
    try:
        # first, get the reservation dates in JSON format
        reservation_date_info = parser.get_all_dates()

        # next, get the email_interactions addresses and dates from web_form_data.json
        with open('wb_interactions/web_form_data.json') as json_file:
            web_form_data = json.load(json_file)

        # next, for each email_interactions in the web_form_data object, check if the date is open
        # first, look into each of the form data
        for form_data in web_form_data:
            email = form_data['email']
            month = form_data['month']
            date = form_data['date']
            is_full = reservation_date_info[month][date-1][date]
            if not is_full:
                email_sender.send_email(email, month, date)
                web_form_data.remove(form_data)
                web_form_data
        with open('wb_interactions/web_form_data.json', 'w') as outfile:
            json.dump(web_form_data, outfile)
    finally:
        time.sleep(60)