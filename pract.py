from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get('https://credence.in/')
driver.find_element(By.XPATH,"//img[@src='/website/images/enquiry.png']").click()
l=len(driver.find_elements(By.XPATH,"//div[@class='quickfinder-description gem-text-output']//p//a"))
print(l)
contact_no_list=[]
for i in range(1,l+1):
    contact_no = driver.find_element(By.XPATH,"/html/body/div[5]/div/p/a[" +str(i)+ "]").text
    print(contact_no)
    contact_no_list.append(contact_no)
print(contact_no_list)
m= '+91 7391053250'
index=contact_no_list.index(m)
print(f'{m} is foundd at index {index}')

if m in contact_no_list:
    assert True
else:
    assert False