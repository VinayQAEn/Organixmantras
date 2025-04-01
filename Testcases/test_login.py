import time
import pytest
from selenium.webdriver.common.by import By
from selenium import webdriver
#from PageObject.loginpage import LoginPage
from Locators.loginpage import LoginPage
from Utilities.readproperties import ReadConfig
import sys
import os
from Utilities.customlogger import customlogger

# Print sys.path to check if the project root is included
print("sys.path before modification:")
for path in sys.path:
    print(path)

# Add the full absolute path to the PageObject directory
sys.path.append(os.path.abspath('/Users/riyabakoria/OrganixmantraAPP/PageObject'))

# Print sys.path after modification
print("sys.path after modification:")
for path in sys.path:
    print(path)



@pytest.mark.usefixtures("setup")
class Test_login_001:
   useremail = ReadConfig.get_useremail()
   password = ReadConfig.get_password()
   
   def test_homepage_title(self):
      actual_title = self.driver.title
      print(actual_title)
      if actual_title == "Organic Online Store|Grocery |Vegetables|Dairy Products|Fruits|Hyderabad|Organics Mantra(OM)":
         assert True
      else:
         assert False
   
   def test_login1(self):
      print("Login Test")
      self.log = customlogger()
      self.log = self.log.get_logger()
      self.log.info("******************Test_login_001****************")
      self.lp = LoginPage(self.driver)
      self.lp.clickLogin()
      self.lp.enterUseremail(self.useremail)
      self.log.info("Entered email")
      self.lp.enterPassword(self.password)
      self.log.info("Entered password")
      self.lp.clickLoginButton()
      self.actual_title = self.driver.title
      if self.actual_title == "Organic Online Store|Grocery |Veghhhhetables|Dairy Products|Fruits|Hyderabad|Organics Mantra(OM)":
         assert True
         self.log.info("Login test passed")
      else:
         self.driver.save_screenshot("/Users/riyabakoria/OrganixmantraAPP/Screen Shots/test_login.png")
         self.log.error("Login test failed")

   def test_browser_name(self, pytestconfig):
      browser_name = pytestconfig.getoption("browser_name")
      print(f"Browser selected: {browser_name}")
      assert browser_name in ["chrome", "firefox", "safari"]

      

