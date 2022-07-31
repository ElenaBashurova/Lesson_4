############Shop: отображение страницы товара(Проверено)

# import time
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium import webdriver
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get("https://practice.automationtesting.in/")
# time.sleep(10)
# my_account_menu_btn = driver.find_element_by_xpath("/html/body/div[1]/div[1]/header/div[2]/nav/ul/li[2]/a").click()
#
# email = driver.find_element_by_id("username")
# email.send_keys("Helen@gmail.com")
#
# password = driver.find_element_by_id("password")
# password.send_keys("Helen\gmail.com123654")
#
# login_btn = driver.find_element_by_name("login").click()
# time.sleep(10)
# shop_btn = driver.find_element_by_id("menu-item-40").click()
# time.sleep(10)
# html_btn = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div/ul/li[3]/a[1]/img").click()
#
# header_btn_text = WebDriverWait(driver, 20).until(EC.text_to_be_present_in_element((By.XPATH, '/html/body/div[1]/div[2]/div/div/div/div[2]/h1'), "HTML5 Forms"))
#
# driver.quit()


###############Shop: количество товаров в категории(Проверено)
# import time
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium import webdriver
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get("https://practice.automationtesting.in/")
# time.sleep(10)
# My_Account_Menu_btn = driver.find_element_by_id("menu-item-50").click()
#
# email = driver.find_element_by_id("username")
# email.send_keys("Helen@gmail.com")
#
# password = driver.find_element_by_id("password")
# password.send_keys("Helen\gmail.com123654")
#
# login_btn = driver.find_element_by_name("login").click()
# time.sleep(10)
# shop_btn = driver.find_element_by_id("menu-item-40").click()
# time.sleep(10)
# html_btn = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/aside/div[3]/ul/li[2]/a").click()
#
# items_count = driver.find_elements_by_class_name("woocommerce-LoopProduct-link")
# if len(items_count) == 3:
#     print("На странице 3 товара")
# else:
#     print("Ошибка. Количество товаров на странице не 3: " + str(len(items_count)))
#
# driver.quit()

##############Shop: сортировка товаров(Проверено)
# import time
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium import webdriver
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get("https://practice.automationtesting.in/")
# time.sleep(10)
# My_Account_Menu_btn = driver.find_element_by_id("menu-item-50").click()
# time.sleep(10)
# email = driver.find_element_by_id("username")
# email.send_keys("Helen@gmail.com")
#
# password = driver.find_element_by_id("password")
# password.send_keys("Helen\gmail.com123654")
#
# login_btn = driver.find_element_by_name("login").click()
# time.sleep(10)
# shop_btn = driver.find_element_by_id("menu-item-40").click()
#
# from selenium.webdriver.support.select import Select
# sorting_selector = driver.find_element_by_name("orderby")
# select = Select(sorting_selector)
# select.select_by_value("menu_order")
# sorting_selector = sorting_selector.get_attribute("value")
# if sorting_selector == "menu_order":
#     print("Выбрана сортировка по умолчанию")
# else:
#     print("Сортировка не по умолчанию")
#
# time.sleep(10)
# sorting = driver.find_element_by_tag_name("select").click()
# sorting = driver.find_element_by_css_selector("[value='price-desc']").click()
# time.sleep(10)
# sorting = driver.find_element_by_tag_name("select").click()
# sorting_high_to_low = driver.find_element_by_css_selector("[value='menu_order']").click()
#
# from selenium.webdriver.support.select import Select
# sorting_selector = driver.find_element_by_name("orderby")
# select = Select(sorting_selector)
# select.select_by_value("price-desc")
# sorting_btn = driver.find_element_by_name("orderby")
# sorting_btn_value = sorting_btn.get_attribute("value")
# if sorting_btn_value == ('price-desc'):
#     print("Верно")
# else:
#     print("Неверно")

# driver.quit()

###################Shop: отображение, скидка товара
# import time
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium import webdriver
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get("https://practice.automationtesting.in/")
# time.sleep(10)
# My_Account_Menu_btn = driver.find_element_by_id("menu-item-50").click()
#
# email = driver.find_element_by_id("username")
# email.send_keys("Helen@gmail.com")
#
# password = driver.find_element_by_id("password")
# password.send_keys("Helen\gmail.com123654")
#
# login_btn = driver.find_element_by_name("login").click()
# time.sleep(10)
# shop_btn = driver.find_element_by_id("menu-item-40").click()
# time.sleep(10)
# book_btn = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div/ul/li[1]/a[1]/img").click()
#
# old_price = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div/div/div[2]/div[1]/p/del/span")
# old_price_text = old_price.text
# assert old_price_text == "₹600.00"
#
# new_price = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div/div/div[2]/div[1]/p/ins/span")
# new_price_text = new_price.text
# assert new_price_text == "₹450.00"
#
# img_btn = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[2]/div/div/div/div[1]/a/img"))).click()
#
# close_btn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "pp_close"))).click()
#
# driver.quit()

###############Shop: проверка цены в корзине(Проверено)
# import time
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium import webdriver
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get("https://practice.automationtesting.in/")
# time.sleep(10)
# shop_btn = driver.find_element_by_id("menu-item-40").click()
# time.sleep(10)
# buy_book_btn = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div/ul/li[4]/a[2]").click()
# time.sleep(10)
#
# basket_quantity = driver.find_element_by_xpath("/html/body/div[1]/div[1]/header/div[2]/nav/ul/li[6]/a/span[1]")
# basket_quantity = "1 item"
# assert basket_quantity == "1 item"
#
# basket_amount = driver.find_element_by_class_name("amount")
# basket_amount = "₹180.00"
# assert basket_amount == "₹180.00"
#
#
# time.sleep(10)
# basket_btn = driver.find_element_by_xpath("/html/body/div[1]/div[1]/header/div[2]/nav/ul/li[6]/a").click()


# subtotal_text = WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.CLASS_NAME, "cart-subtotal"), "₹180.00"))
# total_text = WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".product-subtotal>span"), "₹180.00"))


# driver.quit()

#################Shop: работа в корзине(Проверено)
# import time
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium import webdriver
# from selenium.webdriver.support import expected_conditions as EC
#
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get("https://practice.automationtesting.in/")
#
# shop_btn = driver.find_element_by_id("menu-item-40").click()
#
# driver.execute_script("window.scrollBy(0, 300);")
#
# first_book_btn =  driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div/ul/li[4]/a[2]").click()
#
# time.sleep(10)
# second_book_btn = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div/ul/li[5]/a[2]").click()
#
# time.sleep(10)
# basket_btn = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div/ul/li[4]/a[3]").click()
#
# time.sleep(10)
# delete_btn = driver.find_element_by_class_name("remove").click()
#
# time.sleep(10)
# undo_btn = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div/div/div/div[1]/div[1]/a').click()
#
# element = driver.find_element_by_name("cart[045117b0e0a11a242b9765e79cbf113f][qty]")
# element.clear()
#
# quantity = driver.find_element_by_css_selector(".quantity>input")
# quantity.send_keys("3")
#
# UPDATE_BASKET_btn = driver.find_element_by_name("update_cart").click()
#
# quantity_check_btn = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div/div/div/div[1]/form/table/tbody/tr[1]/td[5]/div/input")
# quantity_check_btn_value = quantity_check_btn.get_attribute("value")
# if quantity_check_btn_value == ('3'):
#     print("Верно")
# else:
#     print("Неверно")
#
# time.sleep(10)
# APPLY_COUPON_btn = driver.find_element_by_class_name("button").click()
#
# text = WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".woocommerce-error>li"), "Please enter a coupon code."))
#
#
# driver.quit()


##############Shop: покупка товара(Проверено)
# import time
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium import webdriver
# from selenium.webdriver.support import expected_conditions as EC
#
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get("https://practice.automationtesting.in/")
#
# shop_btn = driver.find_element_by_id("menu-item-40").click()
#
# driver.execute_script("window.scrollBy(0, 300);")
#
# buy_book_btn = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div/ul/li[4]/a[2]").click()
#
# time.sleep(10)
#
# basket_btn = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div/ul/li[4]/a[3]").click()
#
#
# PROCEED_TO_CHECKOUT_btn = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".wc-proceed-to-checkout>a"))).click()
#
#
# First_Name = driver.find_element_by_id("billing_first_name")
# First_Name.send_keys("Helen")
#
# Last_Name = driver.find_element_by_id("billing_last_name")
# Last_Name.send_keys("Helen1")
#
# Email = driver.find_element_by_id("billing_email")
# Email.send_keys("helen@gmail.com")
#
# phone = driver.find_element_by_id("billing_phone")
# phone.send_keys("89566255256")
#
# selector_btn = driver.find_element_by_class_name("select2-chosen").click()
# country = driver.find_element_by_id("s2id_autogen1_search")
# country.send_keys("Åland Islands")
# country_btn = driver.find_element_by_class_name("select2-match").click()
#
# address = driver.find_element_by_name("billing_address_1")
# address.send_keys("Åland Islands")
#
# zip = driver.find_element_by_name("billing_postcode")
# zip.send_keys("56966")
#
# city = driver.find_element_by_name("billing_city")
# city.send_keys("NY")
#
# driver.execute_script("window.scrollBy(0, 600);")
# time.sleep(10)
#
# radio_btn = driver.find_element_by_id("payment_method_cheque").click()
#
# PLACE_ORDER_btn = driver.find_element_by_name("woocommerce_checkout_place_order").click()
#
# first_text = WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".woocommerce>p "), "Thank you. Your order has been received."))
#
# second_text = WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.XPATH, "/html/body/div[1]/div[2]/div/div/div/div/div[1]/ul/li[4]/strong"), "Check Payments"))
