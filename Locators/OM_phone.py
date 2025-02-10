from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
import time

class Om_phone:
    lnk_OM_phone_Xpath = "//p[normalize-space()='+91 81064 41105']"
    def __init__(self,driver):
        self.driver = driver
    def click_om_phonelink(self):
        self.act = ActionChains(self.driver)
        self.driver.find_element(By.XPATH, self.lnk_OM_phone_Xpath).click()
        self.myalert = self.driver.switch_to.alert
        self.myalert.accept()
        time.sleep(10)

        
    
