from  selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get('https://credence.in/')
driver.find_element(By.XPATH,"//img[@src='/website/images/enquiry.png']").click()
l=driver.find_element(By.XPATH,"//div[@class='quickfinder-description gem-text-output']//p")
print(l)