
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os
import unittest
import HtmlTestRunner




class WikipediaTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
     cls.driver = webdriver.Chrome(executable_path="D:\\learning\\chromedriver.exe")
     cls.driver.maximize_window()

    def test_pageload(self):
        self.driver.get("https://www.wikipedia.com")
        self.assertEqual("Wikipedia",self.driver.title,"Web page failed to open")


    def test_searchwiki(self):
        searchbox = self.driver.find_element_by_name("search")
        print ("search box displayed :",self.driver.find_element_by_name("search").is_displayed())
        searchbox.send_keys("Google")
        searchbutton= self.driver.find_element_by_xpath("/html/body/div[2]/form/fieldset/button/i")
        searchbutton.click()
        print(self.driver.title)

    @classmethod
    def tearDownClass(cls) :
        cls.driver.quit()
        print("Test completed")

if __name__=='__main__':
    unittest.main(testRunner = HtmlTestRunner.HTMLTestRunner( output= "D:\\learning\\Report"))



