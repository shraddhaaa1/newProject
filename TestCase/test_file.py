import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import allure
from selenium.webdriver.common.service import Service
# healeess_op=webdriver.ChromeOptions()
# healeess_op.add_argument('headless')

class Test_Pytest:

    def test_add(self):
        a=1
        b=2
        sum=a+b
        print(sum)
        if sum==3:
            assert True
        else:
            assert False
    def test_addition(self):
        a=10
        b=20
        sum=a+b
        print(sum)
        if sum==30:
            assert True
        else:
            assert False
    def test_mult(self):
        a=2
        b=3
        mul=a*b
        print(mul)
        if mul==6:
            assert True
        else:
            assert False
    def test_cred(self):
        driver=webdriver.Chrome()
        driver.get("https://credence.in/")
        if driver.title=='Credence':
            print('u r at right place')
        else:
            print('u r at wrong place')

