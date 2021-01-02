import os
import time
from selenium import webdriver

IG_USERNAME = str(os.getenv("IG_USERNAME", ""))
IG_PASSWORD = str(os.getenv("IG_PASSWORD", ""))

options = webdriver.FirefoxOptions()
options.headless = True
driver = webdriver.Firefox(options=options)
driver.get('https://www.instagram.com/accounts/login/')
time.sleep(2) # wait until everything loads
dom = driver.find_element_by_xpath('//*')

username = dom.find_element_by_name('username')
password = dom.find_element_by_name('password')
login_button = dom.find_element_by_xpath('//*[@class="sqdOP  L3NKy   y3zKF     "]')

username.clear()
password.clear()
username.send_keys(IG_USERNAME)
password.send_keys(IG_PASSWORD)

login_button.click()

time.sleep(2) # wait until everything loads

if 'not-logged-in' not in driver.page_source and 'logged-in' in driver.page_source:
    print('Logged in')
else:
    print('Login failed')