from selenium import webdriver
from time import sleep

selenium_webdrivers = webdriver.Chrome()
selenium_webdrivers.get('https://forms.gle/DQHaH3XSLUaXW6BV7')

sleep(0.5)

Email_Address = 'yash.gurukul12@gmail.com'
Filling_Email_Address_Input_Box = selenium_webdrivers.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div[1]/div[2]/div[1]/div/div[1]/input')
Filling_Email_Address_Input_Box.send_keys(Email_Address)

sleep(0.5)

Name = 'Yash Varshney'
Filing_Name_Input_Box = selenium_webdrivers.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
Filing_Name_Input_Box.send_keys(Name)

sleep(0.5)

Software_Rating = selenium_webdrivers.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div[1]/span/div/label[5]/div[2]/div/div/div[3]/div')
Software_Rating.click()

sleep(0.5)

FeedBack = "The Software of Automating Google Form was great and I liked it much."
Long_FeedBack_Input_Box = selenium_webdrivers.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div[2]/textarea')
Long_FeedBack_Input_Box.send_keys(FeedBack)

sleep(0.5)

Submit_Button = selenium_webdrivers.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[3]/div/div/span/span')
Submit_Button.click()