#-*-coding:UTF-8 -*-
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
import requests
import time


driver = webdriver.Firefox()
driver.get("https://campus.nutn.edu.tw/ActReg/userLogin")



elem = driver.find_element_by_id("ctl00_ContentPlaceHolder1_txt_account_sch")
elem.send_keys("S10559022")
elem = driver.find_element_by_id("ctl00_ContentPlaceHolder1_txt_password_sch")
elem.send_keys("thomas3198")

time.sleep(6)


driver.get("https://campus.nutn.edu.tw/ActReg/ActInfo/20407/10905115814")

while (True):

    time.sleep(5)
    driver.refresh()

    localtime = time.localtime(time.time())
    if( (localtime.tm_hour>=7) and (localtime.tm_min>=55) ):
        break

while (True):


    localtime = time.localtime(time.time())
    if ((localtime.tm_hour == 8) and (localtime.tm_min >= 0)):
        driver.refresh()
        flag = driver.findElement(By.id("ctl00_ContentPlaceHolder1_btnReg")).getAttribute("value")

        if (flag == '我要報名'):
            driver.findElement(By.id("ctl00_ContentPlaceHolder1_btnReg")).click()
            print("我要報名 Complete at " + time.asctime(time.localtime(time.time())))

            elem = driver.find_element_by_id("ctl00_ContentPlaceHolder1_CheckBox1")
            elem.click()
            elem = driver.find_element_by_id("ctl00_ContentPlaceHolder1_btnSubmit")
            elem.click()

            print("Sign up successfully at " + time.asctime(time.localtime(time.time())))
            driver.close()

        else:
            break
