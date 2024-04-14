from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time
obj =  Service("browser_drivers\chromedriver-win64\chromedriver.exe")
driver=webdriver.Chrome(service=obj)

driver.get('https://the-internet.herokuapp.com/javascript_alerts')
driver.maximize_window()

driver.find_element(By.XPATH,"//button[normalize-space()='Click for JS Alert']").click()
time.sleep(2)

alert_window = driver.switch_to.alert
print('Alert Window Text : ',alert_window.text)
time.sleep(2)
alert_window.accept() #click on OK button

# alert_window.dismiss()





#Autherntication alert
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time
obj =  Service("browser_drivers\chromedriver-win64\chromedriver.exe")
driver=webdriver.Chrome(service=obj)

#username,password -  admin
driver.get('https://admin:admin@the-internet.herokuapp.com/basic_auth')
time.sleep(2)
driver.maximize_window()

