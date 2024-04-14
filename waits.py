#Implicit Wait
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
obj =  Service("browser_drivers\chromedriver-win64\chromedriver.exe")
driver=webdriver.Chrome(service=obj)

driver.get('https://www.google.com/')
driver.maximize_window()
driver.implicitly_wait(10)
search_box = driver.find_element(By.NAME,'q')
search_box.send_keys('Selenium')
search_box.submit()

driver.find_element(By.XPATH,"//h3[text()='Selenium']").click()





#Explicit Wait
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
obj =  Service("browser_drivers\chromedriver-win64\chromedriver.exe")
driver=webdriver.Chrome(service=obj)

my_wait = WebDriverWait(driver,10,ignored_exceptions=[])   #Explicit wait declaration
driver.get('https://www.google.com/')
driver.maximize_window()
search_box = driver.find_element(By.NAME,'q')
search_box.send_keys('Selenium')
search_box.submit()

search_link = my_wait.until(EC.presence_of_element_located,(By.XPATH,"//h3[text()='Selenium']"))

driver.quit()
