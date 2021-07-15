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

time.sleep(3) # wait until everything loads

if 'not-logged-in' not in driver.page_source and 'logged-in' in driver.page_source:
    print('Logged in')
else:
    print('Login failed')

driver.get('https://www.instagram.com/' + IG_USERNAME + '/')
time.sleep(2) # wait until everything loads
driver.find_element_by_partial_link_text('followers').click()

previous_scroll_position = 0
scroll_position = 1
while(previous_scroll_position != scroll_position):
    previous_scroll_position = scroll_position
    scroll_position = driver.execute_script('var followersPanelElement = document.getElementsByClassName("isgrP")[0];followersPanelElement.scrollTop = followersPanelElement.scrollHeight; return followersPanelElement.scrollTop;')
    print("scrolling followers...")
    time.sleep(3)
# print("finished scrolling")

followers_elements = driver.find_elements_by_xpath('//*[@class="FPmhX notranslate  _0imsa "]')
followers =  list(map(lambda element: element.text, followers_elements))

driver.get('https://www.instagram.com/' + IG_USERNAME + '/')
time.sleep(2) # wait until everything loads
driver.find_element_by_partial_link_text('following').click()

previous_scroll_position = 0
scroll_position = 1
while(previous_scroll_position != scroll_position):
    previous_scroll_position = scroll_position
    scroll_position = driver.execute_script('var followersPanelElement = document.getElementsByClassName("isgrP")[0];followersPanelElement.scrollTop = followersPanelElement.scrollHeight; return followersPanelElement.scrollTop;')
    print("scrolling following...")
    time.sleep(3)
# print("finished scrolling")

followings_elements = driver.find_elements_by_xpath('//*[@class="FPmhX notranslate  _0imsa "]')
followings =  list(map(lambda element: element.text, followings_elements))

print('you follow, but they do not follow you:')
not_following_you = []
for following in followings:
    if following not in followers:
        not_following_you.append(following)
for account in not_following_you:
    print(account)

print('they follow you, but you dont follow them back:')
you_dont_follow = []
for follower in followers:
    if follower not in followings:
        you_dont_follow.append(follower)
for account in you_dont_follow:
    print(account)