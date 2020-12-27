import json
from wb_interactions.scraper import get_wb_driver
from datetime import date

current_month = date.today().strftime("%m")

def get_date_data(web_driver, month_num, date_num, json_calendar_data):
    is_full = True
    dateBackGroundColor = web_driver.find_element_by_xpath(
        "//*[@id=\"passHolderReservations__wrapper\"]/div/div[2]/div["
        + str(month_num)
        + "]/div[1]/div[4]/span["
        + str(date_num) +"]")\
        .value_of_css_property("background-color")
    if dateBackGroundColor == 'rgba(255, 255, 255, 1)':
        is_full = False
    month = (int(current_month) + month_num - 1) % 12
    if month == 0:
        month = 12
    json_calendar_data[month].append({date_num: is_full})

def get_all_dates():
    driver = get_wb_driver()
    json_calendar_data = {12: [], 1: [], 2: []}
    for m in range(1, 3):
        for d in range(1, 32):
            try:
                get_date_data(driver, m, d, json_calendar_data)
            except:
                print("error: no combination of month: " + str(m) + " and day: " + str(d))
                driver.quit()
                raise Exception("error: no combination of month: " + str(m) + " and day: " + str(d))
    driver.quit()
    return json_calendar_data

def get_web_form_data():
    with open('web_form_data.json') as json_file:
        json_data = json.load(json_file)
        return json_data

if __name__ == "__main__":
    web_form_dates = get_web_form_data()
    web_form_dates