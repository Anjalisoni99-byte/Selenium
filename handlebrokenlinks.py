import requests
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
obj =  Service("browser_drivers\chromedriver-win64\chromedriver.exe")
driver=webdriver.Chrome(service=obj)

driver.get('http://www.deadlinkcity.com/')
driver.maximize_window()

#Find number of links in a page
links= driver.find_elements(By.TAG_NAME,'a')

count = 0
for link in links:
    url = link.get_attribute('href')
    try:
        response = requests.head(url)
    except:
        None
    if response.status_code >= 400:
        print('Broken link:',url)
        count+=1
    else:
        print('Valid link:',url)
print('Total number of broken links:',count)