from selenium import webdriver
import pytest
import time
from selenium.webdriver import ActionChains
class TestOrangeHRM :

    @pytest.fixture()
    def setup(self):
        self.driver=webdriver.Chrome(executable_path="D:\\learning\\chromedriver.exe")
        self.driver.maximize_window()
        yield
        self.driver.close()

    def test_homePageTitle(self,setup):
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        assert self.driver.title == "OrangeHRM"

    def test_login(self,setup):
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        self.driver.find_element_by_name("txtUsername").send_keys("Admin")
        self.driver.find_element_by_name("txtPassword").send_keys("admin123")
        self.driver.find_element_by_id("btnLogin").click()
        assert self.driver.title == "OrangeHRM"
        time.sleep(5)
        admin= self.driver.find_element_by_xpath("//*[@id='menu_admin_viewAdminModule']/b")
        user_management = self.driver.find_element_by_xpath("//*[@id='menu_admin_UserManagement']")
        user = self.driver.find_element_by_xpath("//*[@id='menu_admin_viewSystemUsers']")




