
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import xlrd
import os
import time

print(os.path.isfile("D://learning//facebooklog.xlsx"))
loc = ("D://learning//facebooklog.xlsx")
wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)

driver = webdriver.Chrome(executable_path ="D:\\learning\\chromedriver.exe")
driver.get("http://www.facebook.com/")

print(driver.title) #title of the page

username = driver.find_element_by_name("email")
password = driver.find_element_by_id("pass")


#is_displayed() not found in  list
if driver.find_element_by_name("email"):
    print("True")
else:
    print("False")

if driver.find_element_by_id("pass"):
    print("True")
else:
    print("False")


print(sheet.cell_value(1,1))
print(sheet.cell_value(1,2))



username.send_keys(sheet.cell_value(1,1))
password.send_keys(sheet.cell_value(1,2))

time.sleep(5)

print("closing drivers")

driver.close()


