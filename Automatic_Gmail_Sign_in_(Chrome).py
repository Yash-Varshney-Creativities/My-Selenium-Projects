from selenium.webdriver import *
import time
WebDriver = Chrome()
WebDriver.get('https://mail.google.com/')
Filling_Email_Address_Input_Box = WebDriver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input').send_keys('yash.gurukul12@gmail.com')
Filling_Email_Address_Next_Button = WebDriver.find_element_by_css_selector('#identifierNext > div > button > div.VfPpkd-RLmnJb').click()
time.sleep(1)
Filling_Email_Address_Passcode_Input_Box = WebDriver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input').send_keys(open('password.txt').read())
Filling_Email_Address_Passcode_Next_Button = WebDriver.find_element_by_xpath('//*[@id="passwordNext"]/div/button/div[2]').click()