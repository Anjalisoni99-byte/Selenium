from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
obj =  Service("browser_drivers\chromedriver-win64\chromedriver.exe")
driver=webdriver.Chrome(service=obj)

driver.get('https://demo.nopcommerce.com//')
driver.maximize_window()


#link and partial link text locators
# driver.find_element(By.LINK_TEXT,'Digital downloads').click()
driver.find_element(By.PARTIAL_LINK_TEXT,'Digital').click()

#Find number of links in a page
links = driver.find_elements(By.TAG_NAME,'a')
print('Total number of links',len(links))

#print all the link names
for link in links:
    print(link.text)