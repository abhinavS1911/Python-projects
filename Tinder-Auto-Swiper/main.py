from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time

FB_ID = "<EMAIL-ID>"
FB_PASSWORD = "<PASSWORD>"

chrome_driver_path = r"C:\Users\HP\Desktop\python\chromedriver_win32\chromedriver.exe"
ser = Service(chrome_driver_path)
op = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=op, service=ser)

driver.get("https://tinder.com/")
time.sleep(2)

driver.maximize_window()

login_button = driver.find_element_by_xpath(
    '//*[@id="q1413092675"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a')
login_button.click()

time.sleep(4)

"""Selecting facebook login options"""
try:
    login_facebook = driver.find_element_by_xpath(
        '//*[@id="q-315288401"]/div/div/div[1]/div/div[3]/span/div[2]/button')
    login_facebook.click()

except NoSuchElementException:
    more_option_button = driver.find_element_by_xpath('//*[@id="q-315288401"]/div/div/div[1]/div/div[3]/span/button')
    more_option_button.click()
    time.sleep(0.5)
    login_facebook = driver.find_element_by_xpath(
        '//*[@id="q-315288401"]/div/div/div[1]/div/div[3]/span/div[2]/button')
    login_facebook.click()

time.sleep(2)

""" Switching between different windows"""
base_window = driver.window_handles[0]
facebook_window = driver.window_handles[1]
driver.switch_to.window(facebook_window)
print(driver.title)

"""Login using your account details"""
time.sleep(0.5)
email_ID = driver.find_element_by_xpath('//*[@id="email"]')
email_ID.send_keys(f"{FB_ID}")
time.sleep(1)
email_PASSWORD = driver.find_element_by_xpath('//*[@id="pass"]')
email_PASSWORD.send_keys(f"{FB_PASSWORD}")
time.sleep(0.5)
login_button = driver.find_element_by_name("login")
login_button.click()
driver.switch_to.window(base_window)
time.sleep(4)

"""Removing all the extra permission popups"""
try:
    cookie_button = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div/div[1]/button')
    cookie_button.click()
except NoSuchElementException:
    pass

time.sleep(2)

try:
    location_allow = driver.find_element_by_xpath('//*[@id="q-315288401"]/div/div/div/div/div[3]/button[1]')
    location_allow.click()
    time.sleep(0.5)
    notification_button = driver.find_element_by_xpath('//*[@id="q-315288401"]/div/div/div/div/div[3]/button[2]')
    notification_button.click()
except NoSuchElementException:
    pass

time.sleep(10)

""" Swapping left """
n = 5
while n > 0:

    try:
        random = driver.find_element_by_xpath('//*[@id="Tinder"]/body')  # Random space in the window
        random.send_keys(Keys.ARROW_LEFT)
        time.sleep(2)
        n -= 1
    except NoSuchElementException:
        # print("skipped")
        time.sleep(2)

# driver.quit()
