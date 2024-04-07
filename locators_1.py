from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome("browser_drivers\chromedriver-win64\chromedriver.exe")  
print('Driver Laoded')

driver.get('https://demo.nopcommerce.com//')
driver.maximize_window()

#id and name locators
driver.find_element(By.ID,'small-searchterms').send_keys('Lenovo ThinkPad X1 Carbon Laptop')
driver.find_element(By.NAME,'q').send_keys('Lenovo ThinkPad X1 Carbon Laptop')

#link and partial link text locators
driver.find_element(By.LINK_TEXT,'Register').click()
driver.find_element(By.PARTIAL_LINK_TEXT,'Reg').click()

driver.find_element(By.CLASS_NAME,'ico-cart').click()

driver.close()