from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome("browser_drivers\chromedriver-win64\chromedriver.exe")  
print('Driver Loaded')

driver.get('https://www.orangehrm.com/')
driver.maximize_window()

#Relative XPath - directly jumps to element on DOM, uses attributes , starts with //
driver.find_element(By.XPATH,'//*[@id="navbarSupportedContent"]/div[2]/ul/li[2]/a').click()

#Absolute Path - starts from root HTML node, uses tags/nodes , starts with /
driver.find_element(By.XPATH,'/html/body/nav/div/div[2]/div[2]/ul/li[2]/a').click()

driver.close()