
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os

driver = webdriver.Chrome(executable_path="D:\\learning\\chromedriver.exe")


class wikipediaSearch:


    def __init__(self):
        driver.get("https://www.wikipedia.com")
        driver.set_window_size(1000, 600)
        print(driver.title)
        self.context = input("Enter the context you want to each on Wikipedia : ")
        driver.maximize_window()

    def searchwiki(self):
        searchbox = driver.find_element_by_name("search")
        print ("search box displayed :",driver.find_element_by_name("search").is_displayed())
        searchbox.send_keys(self.context)
        searchbutton= driver.find_element_by_xpath("/html/body/div[2]/form/fieldset/button/i")
        searchbutton.click()
        print(driver.title)

    def __del__(self):
        print( id(abc))



for i in ['1','2'] :
    abc = wikipediaSearch()
    abc.searchwiki()

driver.close()


