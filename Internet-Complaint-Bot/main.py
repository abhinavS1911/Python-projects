from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time

PROMISED_DOWN = 200
PROMISED_UP = 150
TWITTER_ID = "<TWITTER_ID>"
TWITTER_PASS = "<TWITTER_PASSWORD>"

chrome_driver_path = r"C:\Users\HP\Desktop\python\chromedriver_win32\chromedriver.exe"


class InternetSpeedTwitterBot():

    def __init__(self, driver_path):
        ser = Service(driver_path)
        op = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(service=ser, options=op)
        self.down = 0
        self.up = 0

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/result/12645033238")
        time.sleep(2)

        down_speed = self.driver.find_element_by_xpath(
            '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[2]/div[1]/div[2]/div/div[2]/div/div[2]/span')
        time.sleep(0.5)
        up_speed = self.driver.find_element_by_xpath(
            '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[2]/div[1]/div[2]/div/div[3]/div/div[2]/span')

        self.down = down_speed.text
        self.up = up_speed.text

    def tweet_at_provider(self):
        time.sleep(5)
        self.driver.get("https://twitter.com/login")
        time.sleep(5)

        username = self.driver.find_element_by_name("text")
        username.send_keys(TWITTER_ID)
        username.send_keys(Keys.ENTER)
        time.sleep(2)

        password = self.driver.find_element_by_name("password")
        password.send_keys(TWITTER_PASS)
        password.send_keys(Keys.ENTER)
        time.sleep(5)

        tweet = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div/div/div/div')
        message = f"Hey Airtel, Why is my Internet speed {self.down}down/{self.up}up when I pay for 200down/100up?"
        tweet.send_keys(message)
        time.sleep(0.5)

        send_button = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]')
        send_button.click()
        time.sleep(2)
        self.driver.quit()


twitter_bot = InternetSpeedTwitterBot(chrome_driver_path)

twitter_bot.get_internet_speed()

twitter_bot.tweet_at_provider()
