from selenium import webdriver
url = "https://www.facebook.com"
username = input("Enter username: ")
password = input("Enter password: ")
driver = webdriver.Chrome("/Users/jonathankarr/Downloads/chromedriver")
driver.get(url)
driver.find_element_by_id("email").send_keys(username)
driver.find_element_by_id("pass").send_keys(password)
driver.find_element_by_name("login").click()