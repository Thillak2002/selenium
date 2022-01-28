from selenium import webdriver
from selenium.webdriver.common.by import By as by
import time
from selenium.webdriver.common.keys import Keys as keys
driver = webdriver.Chrome(r'C:\Users\LAP\PycharmProjects\selenium proj\Drivers\chromedriver.exe')
driver.maximize_window()
driver.implicitly_wait(15)
n=input("Please Provide the twitter account link here : ")
driver.get(n)
Bio=driver.find_element(by.CSS_SELECTOR,"div[class='css-1dbjc4n r-1adg3ll r-6gpygo']>div>div>span").text
name=driver.find_element_by_css_selector("div[class='css-1dbjc4n r-6gpygo r-14gqq1x']>div>div>div>div>span>span").text
following=driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div/div[1]/div/div[5]/div[1]/a/span[1]/span').text
followers=driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div/div[1]/div/div[5]/div[2]/a/span[1]/span').text
Tweets=driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[1]/div[1]/div/div/div/div/div[2]/div/div').text
print("Biography : ",Bio)
print("Name of the Person : ",name)
print("Following_count : ",following)
print("followers_count : ",followers)
print("Tweets_count : ",Tweets)




