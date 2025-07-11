from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time
import datetime

current_date = datetime.datetime.now()
current_day = current_date.day
current_hour = current_date.hour
current_minute = current_date.minute

print(f"day: {current_day}, hour: {current_hour}, minute: {current_minute} \n")
print(f"type: {type(current_day)}")

options = Options()
options.add_argument("--start-maximized")

browser = webdriver.Chrome(options = options)
browser.get('https://www.tenisalameda.com.co/m2a0n2a1/public/user/login')

user_element = browser.find_element(By.ID, "lf-email")
user_element.send_keys("este.velasquez@outlook.com")
password_element = browser.find_element(By.ID, "lf-pw")
password_element.send_keys("Evv344")
password_element.submit()

WebDriverWait(browser, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "calendar-cell"))
)

days = [day.text for day in browser.find_elements(By.CLASS_NAME, "day-label")]

while ("Friday" not in days):
    next_days_button = browser.find_element(By.CLASS_NAME, "arrow-right")
    time.sleep(2)
    next_days_button.click()
    days = [day.text for day in browser.find_elements(By.CLASS_NAME, "day-label")]
    time.sleep(2)

actual_time = time.time()
print(actual_time)

input("Presiona Enter para cerrar el navegador...")
browser.quit()


#TODO Calcular la fecha del siguiente viernes, buscar con un XPATH para oprimir justo el botón de ese día y hora deseada