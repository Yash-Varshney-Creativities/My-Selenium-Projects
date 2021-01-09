from selenium import webdriver
from time import sleep
selenium_webdrivers = webdriver.Chrome()
selenium_webdrivers.get('https://mail.google.com/mail')

Filling_Email_Address_Input_Box = selenium_webdrivers.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input')
Filling_Email_Address_Input_Box.send_keys('navika4371@gurukultheschool.com')
Filling_Email_Address_Next_Button = selenium_webdrivers.find_element_by_css_selector('#identifierNext > div > button > div.VfPpkd-RLmnJb')
Filling_Email_Address_Next_Button.click()
sleep(1)
Filling_Email_Address_Passcode_Input_Box = selenium_webdrivers.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input')
Password = open('password.txt').read()
Filling_Email_Address_Passcode_Input_Box.send_keys(Password)
Filling_Email_Address_Passcode_Next_Button = selenium_webdrivers.find_element_by_xpath('//*[@id="passwordNext"]/div/button/div[2]')
Filling_Email_Address_Passcode_Next_Button.click()