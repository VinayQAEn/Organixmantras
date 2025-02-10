from selenium.webdriver.common.by import By
from selenium import webdriver
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoAlertPresentException

class Om_phone:
    lnk_OM_phone_Xpath = "//p[normalize-space()='+91 81064 41105']"

    def __init__(self, driver):
        self.driver = driver

    def click_om_phonelink(self):
        try:
            # Click the phone link
            self.driver.find_element(By.XPATH, self.lnk_OM_phone_Xpath).click()

            # Wait for the alert to be present
            WebDriverWait(self.driver, 10).until(EC.alert_is_present())

            # Switch to the alert
            alert = self.driver.switch_to.alert

            # Accept the alert
            alert.accept()

            # Optional: Wait for a few seconds after accepting the alert
            time.sleep(2)

        except TimeoutException:
            print("Timed out waiting for alert to appear.")
        except NoAlertPresentException:
            print("No alert present after clicking the phone link.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

        
    
