from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import time
import unittest

# TODO put gekodriver at the /usr/bin/

# browser = webdriver.Firefox()  # Get local session of firefox
browser = webdriver.Chrome()  # Get local session of firefox
browser.get("https://www.baidu.com")  # Load page
# assert "Yahoo!" in browser.title
elem = browser.find_element_by_id("kw")  # Find the query box
elem.send_keys("seleniumhq" + Keys.RETURN)
time.sleep(0.2)  # Let the page load, will be added to the API

'''
try:
    browser.find_element_by_xpath("//a[contains(@href,'http://seleniumhq.org')]")
except NoSuchElementException:
    assert 0, "can't find seleniumhq"
'''

browser.close()
