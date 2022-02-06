from selenium import webdriver
from selenium.webdriver.common.by import By as by
import time
from selenium.webdriver.common.keys import Keys as keys
import json
driver = webdriver.Chrome(r'C:\Users\LAP\PycharmProjects\selenium proj\Drivers\chromedriver.exe')

driver.implicitly_wait(15)
n="https://www.facebook.com/vijay.mummineni/about"
driver.get(n)
study=driver.find_element_by_xpath('//*[@id="mount_0_0_uT"]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div/div[4]/div/div/div/div[1]/div/div/div/div/div[2]/div/div/div/div[2]/div/div/div[2]/div/span/a/span/span').text
print("studied at" ,study)
live=driver.find_element_by_xpath('//*[@id="mount_0_0_Ld"]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div/div[4]/div/div/div/div[1]/div/div/div/div/div[2]/div/div/div/div[3]/div/div/div[2]/div/span/a/span/span').text
print("lives at",live)
works =driver.find_element_by_xpath('//*[@id="mount_0_0_Ld"]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div/div[4]/div/div/div/div[1]/div/div/div/div/div[2]/div/div/div/div[1]/div/div/div[2]/div/span/a/span/span').text
print("works at",works)
dict={
    "study":study,
    "live":live,
    "works":works
}
json_object = json.dumps(dict , indent=4)

with open("fb_scrape.json", "w") as outfile:
    outfile.write(json_object)





/
