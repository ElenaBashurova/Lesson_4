import time
from selenium import webdriver
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://practice.automationtesting.in/")

driver.execute_script("window.scrollBy(0, 600);")

Selenium_Ruby_btn = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div/div/div/div/div[2]/div/div/div/div/div[2]/div[1]/div/div/ul/li/a[1]/img").click()

REVIEWS_btn = driver.find_element_by_class_name("reviews_tab").click()

five_stars_btn = driver.find_element_by_class_name("star-5").click()

review = driver.find_element_by_id("comment")
review.send_keys("Nice book!")

name = driver.find_element_by_id("author")
name.send_keys("Helen")

email = driver.find_element_by_id("email")
email.send_keys("Helen@gmail.com")

sabmit_btn = driver.find_element_by_name("submit").click()

driver.quit()