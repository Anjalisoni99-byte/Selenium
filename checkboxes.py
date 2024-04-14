from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
obj =  Service("browser_drivers\chromedriver-win64\chromedriver.exe")
driver=webdriver.Chrome(service=obj)

driver.get('https://testautomationpractice.blogspot.com/')
driver.maximize_window()

#select specific checkbox
driver.find_element(By.ID,'sunday').click()
time.sleep(2)

#select all checkboxes
checkboxes = driver.find_elements(By.XPATH,"//input[@type='checkbox' and contains(@id,'day')]") 
#//input[@type='checkbox' and contains(@id,'day')]  - Xpath for all checkboxes
print(len(checkboxes))

#approach 1
for i in range(len(checkboxes)):
    checkboxes[i].click()
    time.sleep(2)

#approach 2
for checkbox in checkboxes:
    checkbox.click()
    time.sleep(1)


#Select mulitple checkboxes
for checkbox in checkboxes:
    weekname = checkbox.get_attribute('id')
    if weekname == 'sunday' or weekname == 'friday':
        checkbox.click()
        time.sleep(2)

#select last 2 checkboxes
for checkbox in checkboxes[-2:]:
    checkbox.click()
    time.sleep(2)

#select first 2 checkboxes
for checkbox in checkboxes[:2]:
    checkbox.click()
    time.sleep(2)

#clearing all the checkboxes
for checkbox in checkboxes:
    if checkbox.is_selected():
        checkbox.click()
        time.sleep(1)

driver.quit()