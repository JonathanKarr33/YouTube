# xattr -d com.apple.quarantine /Users/jonathankarr/Downloads/chromedriver
# https://chromedriver.chromium.org/home
#/Users/jonathankarr/Downloads/chromedriver
# pip install selenium
from selenium import webdriver
url = "https://www.stealmylogin.com/demo.html"
username = "user"
password = "pass123"
driver = webdriver.Chrome("/Users/jonathankarr/Downloads/chromedriver")
driver.get(url)
driver.find_element_by_name("username").send_keys(username)
driver.find_element_by_name("password").send_keys(password)
driver.find_element_by_css_selector("input[type=\"submit\" i]").click()