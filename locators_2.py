from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome("browser_drivers\chromedriver-win64\chromedriver.exe")  
print('Driver Loaded')

driver.get('https://www.facebook.com/login/')
driver.maximize_window()

#CSS Selectors
#tag and id combination - tag#id whereas tag is optional
driver.find_element(By.CSS_SELECTOR,'input#email').send_keys('abc')
driver.find_element(By.CSS_SELECTOR,'#email').send_keys('abc')

#tag and class combination - tag.class whereas tag is optional
driver.find_element(By.CSS_SELECTOR,'input.inputtext').send_keys('abc')
driver.find_element(By.CSS_SELECTOR,'.inputtext').send_keys('abc')

#tag and attribute combination - tag[attribute=value] whereas tag is optional
driver.find_element(By.CSS_SELECTOR,'input[name=email]').send_keys('abc')
driver.find_element(By.CSS_SELECTOR,'[name=email]').send_keys('abc')

#tag class and attribute combination - tag.class[attribute=value] whereas tag is optional
driver.find_element(By.CSS_SELECTOR,'input.inputtext[name=email]').send_keys('abc')
driver.find_element(By.CSS_SELECTOR,'.inputtext[name=email]').send_keys('abc')

drive.close()