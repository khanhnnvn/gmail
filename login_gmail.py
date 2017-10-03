from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Your login details.
email = "abc@abc"
passwd = "hehehe"
print ("Mo trinh duyet vao gmail")
# Browser : Firefox.
driver = webdriver.Firefox()
driver.get("http://www.gmail.com")
time.sleep(2)

# GMAIL login.
print ("Thuc hien viec dang nhap")
username=driver.find_element_by_css_selector("#identifierId")
username.send_keys(email)
time.sleep(2)
next=driver.find_element_by_css_selector("#identifierNext")
next.click()
time.sleep(2)
password=driver.find_element_by_css_selector("#password")
password.send_keys(passwd)
time.sleep(2)
login=driver.find_element_by_css_selector("#passwordNext")
login.click()

# GMAIL logout.
#
time.sleep(5)
print ("Thuc hien logout")
driver.get("https://accounts.google.com/Logout?hl=en&continue=https://mail.google.com/mail&service=mail")
time.sleep(10)

# Closing Browser.
driver.quit()
