from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def get_wb_driver():
    PATH = "C:/bin/chromedriver.exe"
    driver = webdriver.Chrome(PATH)

    driver.get("https://www.whistlerblackcomb.com/plan-your-trip/lift-access/check-availability.aspx")
    try:
        reservation_search_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "passHolderReservationsSearchButton"))
        )
    except:
        driver.quit()

    driver.execute_script("window.scrollTo(0, 500)")
    reservation_search_button.click()

    try:
        calendar = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "capacity_calendar.reverse_styles"))
        )
    except:
        driver.quit()
    return driver





