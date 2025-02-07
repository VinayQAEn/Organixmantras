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
from Utilities import XLutils

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
class Test_login_002:
   path = "/Users/riyabakoria/OrganixmantraAPP/Test Data/Data.xlsx"
   def test_loginDDT(self):
      print("Login TestDDT")
      self.log = customlogger()
      self.log = self.log.get_logger()
      self.log.info("*******TestDDT*************")
      self.log.info("******************Test_login_002****************")
      self.lp = LoginPage(self.driver)
      self.rows = XLutils.get_rowcount(self.path,"Sheet")
      print("No of rows in excel",self.rows)
      for r in range(2,self.rows+1):
         self.useremail = XLutils.readdata(self.path,"Sheet",r,1)
         self.password = XLutils.readdata(self.path,"Sheet",r,2)
         self.status  = XLutils.readdata(self.path,"Sheet",r,3)
         self.lp.clickLogin()
         self.lp.enterUseremail(self.useremail)
         self.lp.enterPassword(self.password)
         self.lp.clickLoginButton()
         time.sleep(5)
         self.page_Url = self.driver.current_url
         if self.page_Url == "https://organicsmantra.in/email-verification":
            if self.status == "Pass":
               self.log.info("Test is Passed")
               XLutils.writedata(self.path,"Sheet",r,4,"Pass")
            elif self.status == "Fail":
               self.log.info("Test is Failed")
               XLutils.writedata(self.path,"Sheet",r,4,"Fail")
            elif self.page_Url == "https://organicsmantra.in/login":
                if self.status == "Pass":
                    self.log.info("Test is Failed")
                    XLutils.writedata(self.path,"Sheet",r,4,"Fail")
                elif self.status == "Fail":
                    self.log.info("Test is Passed")
                    XLutils.writedata(self.path,"Sheet",r,4,"Pass")
            else:
                self.log.info("Test is Failed")
                XLutils.writedata(self.path,"Sheet",r,4,"Fail")
         else:
             self.log.info("Test is Failed")
             XLutils.writedata(self.path,"Sheet",r,4,"Fail")
       

