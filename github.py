from selenium import webdriver
import time

driver = webdriver.Chrome()

driver.get('https://github.com/login')

#in here you should put your Github Email 
user1 = driver.find_element_by_xpath('//*[@id="login_field"]')
user1.send_keys('reqiure Email')

#in here you should put your Email Password
pas = driver.find_element_by_xpath('//*[@id="password"]')
pas.send_keys('Require Password')

signbt = driver.find_element_by_xpath('//*[@id="login"]/div[4]/form/input[14]')
signbt.click()

butt = driver.find_element_by_xpath('/html/body/div[1]/header/div[7]/details/summary/span[2]')
butt.click()

time.sleep(2)

butt1 = driver.find_element_by_xpath('/html/body/div[1]/header/div[7]/details/details-menu/a[1]')
butt1.click()