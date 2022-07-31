# import time
# from selenium import webdriver
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get("https://practice.automationtesting.in/")
#
#
# My_Account_Menu_btn = driver.find_element_by_id("menu-item-50").click()
#
# email = driver.find_element_by_id("reg_email")
# email.send_keys("Helen@gmail.com")
#
#
# password = driver.find_element_by_id("reg_password")
# password.send_keys("Helen\gmail.com123654")
#
# register_btn = driver.find_element_by_name("register").click()
#
#
# driver.quit()

##############################Registration_login: логин в систему

import time
from selenium import webdriver
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://practice.automationtesting.in/")


My_Account_Menu_btn = driver.find_element_by_id("menu-item-50").click()

email = driver.find_element_by_id("username")
email.send_keys("Helen@gmail.com")

password = driver.find_element_by_id("password")
password.send_keys("Helen\gmail.com123654")

login_btn = driver.find_element_by_name("login").click()

element = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div/div/div/div[1]/nav/ul/li[6]/a")
element_get_text = element.text
assert element_get_text == "Logout"

driver.quit()