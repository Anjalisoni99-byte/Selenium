#Run automated tests in chrome browser  - Selenium 3
#https://chromedriver.chromium.org/downloads

#Test Case - 1
# 1.Open Web Broswer(Chrome)  2.  Open any URL   3.  Capture title of home page(Actual)  4. Verify title of page (Expected)
# 5.Close Browser

from selenium import webdriver
driver = webdriver.Chrome("browser_drivers\chromedriver-win64\chromedriver.exe")  
print('Driver Laoded')
driver.get('https://www.python.org/')
actual_title = driver.title
expected_title = "Welcome to Python.org"
print('Actual Title : ',actual_title)
#assert actual_title == expected_title

if actual_title == expected_title:
    print('Test Case Passed')
else:
    print('Test Case Failed')

driver.close()


#Test Case - 2
# 1.Open Web Broswer(Chrome)  2.  Open any URL   3. Enter username  4. Enter Passowrd  
# 5.Click on Login   6.Capture title of home page(Actual)  7. Verify title of page (Expected)
# 8.Close Browser

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome("browser_drivers\chromedriver-win64\chromedriver.exe")  
print('Driver Laoded')
driver.get("https://profile.w3schools.com/log-in?redirect_url=https%3A%2F%2Fwww.w3schools.com%2Fpython%2F")
driver.find_element(By.NAME ,'email').send_keys('anjibce123@gmail.com')
driver.find_element(By.NAME ,'current-password').send_keys('Anjali@123')
driver.find_element(By.CLASS_NAME ,'LoginModal_cta_bottom_box_button_login__5Fbwv').click()

actual_title = driver.title
expected_title = "Log in - W3Schools"
print('Actual Title : ',actual_title)
#assert actual_title == expected_title

if actual_title == expected_title:
    print('Test Case Passed')
else:
    print('Test Case Failed')

driver.close()




#Run automated tests in chrome browser  - Selenium 4

#Test Case - 1
# 1.Open Web Broswer(Chrome)  2.  Open any URL   3.  Capture title of home page(Actual)  4. Verify title of page (Expected)
# 5.Close Browser

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service_obj = Service("browser_drivers\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj) 
print('Driver Laoded')
driver.get('https://www.python.org/')
actual_title = driver.title
expected_title = "Welcome to Python.org"
print('Actual Title : ',actual_title)
#assert actual_title == expected_title

if actual_title == expected_title:
    print('Test Case Passed')
else:
    print('Test Case Failed')

driver.close()


#Test Case - 2
# 1.Open Web Broswer(Chrome)  2.  Open any URL   3. Enter username  4. Enter Passowrd  
# 5.Click on Login   6.Capture title of home page(Actual)  7. Verify title of page (Expected)
# 8.Close Browser

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
  
service_obj = Service("browser_drivers\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj) 
print('Driver Laoded')
driver.get("https://profile.w3schools.com/log-in?redirect_url=https%3A%2F%2Fwww.w3schools.com%2Fpython%2F")
driver.find_element(By.NAME ,'email').send_keys('anjibce123@gmail.com')
driver.find_element(By.NAME ,'current-password').send_keys('Anjali@123')
driver.find_element(By.CLASS_NAME ,'LoginModal_cta_bottom_box_button_login__5Fbwv').click()

actual_title = driver.title
expected_title = "Log in - W3Schools"
print('Actual Title : ',actual_title)
#assert actual_title == expected_title

if actual_title == expected_title:
    print('Test Case Passed')
else:
    print('Test Case Failed')

driver.close()