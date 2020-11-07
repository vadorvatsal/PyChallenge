# % xattr -r -d com.apple.quarantine geckodriver to bypass the security warning in MacOS
# https://firefox-source-docs.mozilla.org/testing/geckodriver/Notarization.html

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Firefox()
browser.get('http://python.org')

search = browser.find_element_by_name('q')
search.clear()

search.send_keys("pycon")
search.send_keys(Keys.RETURN)
time.sleep(5)

browser.close()

