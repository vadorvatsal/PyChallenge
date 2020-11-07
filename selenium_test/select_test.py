from selenium import webdriver
browser = webdriver.Firefox()
browser.get('www.dev.to/hello_vatsal/')
# % xattr -r -d com.apple.quarantine geckodriver to bypass the security warning in MacOS
# https://firefox-source-docs.mozilla.org/testing/geckodriver/Notarization.html
