from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
import time
from datetime import datetime, timedelta, date

def give_next_day_desired_day(today, desired_day):
    """
    Gets date of next desired day, given current date
    and desired day (String). Matches desired day to a number
    in a dictionary.
    Returns:
    nex_desired_day_string (String)
    """
    days = {"Monday": 0, "Tuesday": 1, "Wednesday": 2, 
            "Thursday": 3, "Friday": 4, "Saturday": 5, "Sunday": 6}
    
    days_until_desired = (days[desired_day] - today.weekday()) % 7
    next_desired_day = today + timedelta(days = days_until_desired)
    next_desired_day_string = next_desired_day.strftime("%Y-%m-%d")

    return days_until_desired, next_desired_day_string

def log_in():
    """
    Logs in the reservation account
    """
    user_element = browser.find_element(By.ID, "lf-email")
    user_element.send_keys("este.velasquez@outlook.com")
    password_element = browser.find_element(By.ID, "lf-pw")
    password_element.send_keys("Evv344")
    password_element.submit()

def scroll_until_desired_day(desired_day):
    """
    Checks the days showing in the screen, and moves to the 
    next days until it finds the desired one.
    """
    days = [day.text for day in browser.find_elements(By.CLASS_NAME, "day-label")]

    while (desired_day not in days):
        next_days_button = browser.find_element(By.CLASS_NAME, "arrow-right")
        time.sleep(1)
        next_days_button.click()
        days = [day.text for day in browser.find_elements(By.CLASS_NAME, "day-label")]
        time.sleep(1)

def delete_overlay():
    """
    Executes Java code in the browser, hides the overlay 
    """
    browser.execute_script("""
        let overlay = document.getElementById("squarebox-overlay");
        if (overlay) overlay.style.display = "none";
    """)

desired_hour = 18
desired_hour_string = str(desired_hour) + ":00"
desired_day = "Monday"

options = Options()
options.add_argument("--start-maximized")

browser = webdriver.Chrome(options = options)
browser.get('https://www.tenisalameda.com.co/m2a0n2a1/public/user/login')

wait = WebDriverWait(browser, 10)

log_in()

WebDriverWait(browser, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "calendar-cell"))
)

scroll_until_desired_day(desired_day)

today = datetime.now()
current_hour = today.hour
days_until_desired, next_desired_day_string = give_next_day_desired_day(today, desired_day)

WebDriverWait(browser, 10).until(
    EC.invisibility_of_element_located(
        (By.CSS_SELECTOR, ".success-message.message")
    )
)

if (days_until_desired <= 2 and current_hour >= desired_hour):
    xpath = f'//a[contains(@href, "ds={next_desired_day_string}") and contains(@href, "ts={desired_hour_string}")]'
    reservation_button = browser.find_element(By.XPATH, xpath)

    if "Free" in reservation_button.text:
        reservation_button.click()

        wait = WebDriverWait(browser, 5)

        book_button = wait.until(EC.element_to_be_clickable((By.ID, "sb-button")))
        delete_overlay()
        book_button.click()

        wait = WebDriverWait(browser, 10)

        delete_overlay()
        confirmation_button = wait.until(EC.element_to_be_clickable((By.NAME, "bf-submit")))
        confirmation_button.click()

    else:
        print("El horario ya no está disponible")
 

input("Presiona Enter para cerrar el navegador...")
browser.quit()

