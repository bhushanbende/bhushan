from selenium import webdriver
import time

driver=webdriver.Chrome(executable_path="D:\\learning\\chromedriver.exe")
driver.get("https://www.countries-ofthe-world.com/flags-of-the-world.html")
driver.maximize_window()


flag = driver.find_element_by_xpath("//*[@id='content']/div[2]/div[2]/table[2]/tbody/tr[100]/td[1]")

driver.execute_script("arguments[0].scrollIntoView();",flag)
time.sleep(10)
driver.close()

