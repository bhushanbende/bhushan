from selenium import webdriver
import pytest
import time
from selenium.webdriver import ActionChains



driver=webdriver.Chrome(executable_path="D:\\learning\\chromedriver.exe")
driver.maximize_window()
driver.get("https://opensource-demo.orangehrmlive.com/")
driver.find_element_by_name("txtUsername").send_keys("Admin")
driver.find_element_by_name("txtPassword").send_keys("admin123")
driver.find_element_by_id("btnLogin").click()
time.sleep(5)
admin= driver.find_element_by_xpath("//*[@id='menu_admin_viewAdminModule']/b")
user_management = driver.find_element_by_xpath("//*[@id='menu_admin_UserManagement']")
user = driver.find_element_by_xpath("//*[@id='menu_admin_viewSystemUsers']")

actions = ActionChains(driver)

actions.move_to_element(admin).move_to_element(user_management).move_to_element(user).click().perform()

time.sleep(5)