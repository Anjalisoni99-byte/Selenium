#Application Commands
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
obj =  Service("browser_drivers\chromedriver-win64\chromedriver.exe")
driver=webdriver.Chrome(service=obj)

#get() method - opening application URL
driver.get('https://www.orangehrm.com/')
#title- to capture title of current page
print(driver.title)
#current_url - to capture URL of current page
print(driver.current_url)
#page_source - to capture HTML source code of current page
print(driver.page_source)





#Conditional Commands
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By

obj =  Service("browser_drivers\chromedriver-win64\chromedriver.exe")
driver=webdriver.Chrome(service=obj)

driver.get('https://demo.nopcommerce.com/register')
print(driver.title)

#is_displayed() - to check if element is displayed on page
searchbox = driver.find_element(By.ID,'small-searchterms')
print('Display Status : ',searchbox.is_displayed())

#is_enabled() - to check if element is enabled on page
searchbox = driver.find_element(By.ID,'small-searchterms')
print('Enabled Status : ',searchbox.is_enabled())

#is_selected() - to check if element is selected on page
#Radio button or checkbox
rb_male = driver.find_element(By.ID,'gender-male')
rb_female = driver.find_element(By.ID,'gender-female')
print('Defalu Selected Status')
print('Selected Status Male : ',rb_male.is_selected())
print('Selected Status Female : ',rb_female.is_selected())

rb_male.click()
print('After Selecting Male Radio Button')
print('Selected Status Male : ',rb_male.is_selected())
print('Selected Status Female : ',rb_female.is_selected())

rb_female.click()
print('After Selecting Female Radio Button')
print('Selected Status Male : ',rb_male.is_selected())
print('Selected Status Female : ',rb_female.is_selected())

driver.close()






#Browser Commands
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

obj =  Service("browser_drivers\chromedriver-win64\chromedriver.exe")
driver=webdriver.Chrome(service=obj)

driver.get('https://demo.nopcommerce.com/register')
driver.maximize_window()
driver.find_element(By.LINK_TEXT,'nopCommerce').click()
time.sleep(5)
driver.close()  #close single browser window(where driver focused)
driver.quit()  #close multiple browser windows (this will kill the process)





#Navigational Commands
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
obj =  Service("browser_drivers\chromedriver-win64\chromedriver.exe")
driver=webdriver.Chrome(service=obj)

driver.get('https://snapdeal.com/')
driver.get('https://www.amazon.com/')
driver.back()   #snapdeal
driver.forward()#amazon
driver.refresh()
driver.quit()




#txt vs get_attribute()
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

obj =  Service("browser_drivers\chromedriver-win64\chromedriver.exe")
driver=webdriver.Chrome(service=obj)

driver.get("https://admin-demo.nopcommerce.com/login")

email_box= driver.find_element(By.XPATH,'//*[@id="Email"]')
email_box.clear()

email_box.send_keys('abs@gmail.com')
time.sleep(2)

print('Text Value',email_box.text) #text returns inner text of element  <input id='123' value='abc'>Email</input>  Here Email is inner text
print('Get Attribute Value',email_box.get_attribute('value'))