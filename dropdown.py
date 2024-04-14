from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time
obj =  Service("browser_drivers\chromedriver-win64\chromedriver.exe")
driver=webdriver.Chrome(service=obj)

driver.get('https://www.opencart.com/index.php?route=account/register')
driver.maximize_window()

# dropdown_country = Select(driver.find_element(By.ID,"input-country"))
dropdown_element = driver.find_element(By.NAME,"country_id")
time.sleep(2)

options = dropdown_country.options
print('Number of countries:',len(options))
for option in options:
    print(option.text)

# dropdown_country.select_by_visible_text('India')
# dropdown_country.select_by_value("99")#present in html
# dropdown_country.select_by_index(10) #index starting from 0 



#Select option from dropdown withpout using built-in methods
for opt in options:
    if opt.text == 'India':
        opt.click()
        break