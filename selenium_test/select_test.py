# Download drivers. For MacOS move them to /usr/local/bin
# If you are getting error of untrusted driver binary then run following command in terminal

# For Firefox
# sudo xattr -d com.apple.quarantine $(which geckodriver)


# For Chrome
# sudo xattr -d com.apple.quarantine $(which chromedriver)

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time

browser = webdriver.Firefox()
browser.get('http://python.org')

search = browser.find_element_by_name('q')
search.clear()

search.send_keys("pycon")
search.send_keys(Keys.RETURN)
time.sleep(5)

browser.get('https://www.w3schools.com/tags/tryit.asp?filename=tryhtml_select')
select = Select(browser.find_element_by_id("car"))

select.select_by_index(4)
time.sleep(5)
select.select_by_visible_text("Opel")
time.sleep(5)
select.select_by_value("saab")
time.sleep(5)

options = select.options
print(options)




browser.close()

