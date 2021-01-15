## Import dependent modules
from selenium import webdriver
import time


## Settings
googleEmail = "LASTNAME.FIRSTNAME@vtex.com.br"
googlePassword = "INSERTYOURPASSWORD"


## Initiate chromium and open the link
''' Use sleep function to wait for the website to load, otherwise,
    you might get into errors.
    Update the browser link with the path of your Chromium
'''
browser = webdriver.Chrome(
    "/Users/Vtex/Documents/Projects/Python/DeleteSKUs/chromedriver")
browser.get("https://vandall.myvtex.com/admin/Site/Produto.aspx")
time.sleep(6)


# Login using Google Account // Insert your Google Password in line *
loginButton = browser.find_element_by_xpath(
    "/html/body/div[2]/div/div/div/div[1]/div[2]/div[1]/div[2]/div[2]/div[2]/div")
loginButton.click()

time.sleep(5)


## Automatically complete with your email address and password
emailField = browser.find_element_by_xpath(
    "/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input")
emailField.send_keys(googleEmail)
emailField.submit()

emailFieldButton = browser.find_element_by_xpath(
    "/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button/div[2]")
emailFieldButton.click()

time.sleep(5)

passField = browser.find_element_by_xpath(
    "/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input")
passField.send_keys(googlePassword)
passField.submit()
emailFieldButton = browser.find_element_by_xpath(
    "/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button/div[2]")
emailFieldButton.click()


## Manually insert the code received on your phone
time.sleep(30)

