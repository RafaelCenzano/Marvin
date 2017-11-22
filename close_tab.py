from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome('/usr/local/lib/python3.5/site-packages/selenium/webdriver/chrome')
driver.get("https://google.com")
elem = driver.find_element_by_tag_name("body")
time.sleep(5)
elem.send_keys(Keys.COMMAND+"T")
time.sleep(5)
elem.send_keys(Keys.COMMAND+"W")
