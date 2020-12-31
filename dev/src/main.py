from selenium import webdriver
import time

options = webdriver.FirefoxOptions()
options.headless = True
driver = webdriver.Firefox(options=options)
driver.get('https://www.instagram.com/accounts/login/')
time.sleep(5) # wait until everything loads
dom = driver.find_element_by_xpath('//*')

# pdb.set_trace()
username = dom.find_element_by_name('username')
password = dom.find_element_by_name('password')
login_button = dom.find_element_by_xpath('//*[@class="sqdOP  L3NKy   y3zKF     "]')

username.clear()
password.clear()
username.send_keys('your username')
password.send_keys('your password')

login_button.click()
# driver.get('https://www.instagram.com/accounts/login')

time.sleep(5) # wait until everything loads
print("html page after trying login:")
print(driver.page_source)

if 'logged-in' in driver.page_source:
    print('Logged in')