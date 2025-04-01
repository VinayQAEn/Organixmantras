from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import openpyxl
import time
from Utilities import XLutils


class Search_bar:
    txt_searchbar_btn_Xpath = "//p[normalize-space()='Search']"
    txt_searchbar_box_Xpath = "//li[@class='hidden md:block']//input[@placeholder='Search for a product or a broader category']"
    search_btn_xpath = "//button[normalize-space()='Search']"
    msg_alertmsg_xpath = "/html/body/app-root/app-header/div/header/div/div/div[3]/div/ul/li[1]/div/div[2]"

    def __init__(self, driver):
        self.driver = driver

    def searchbar_ddt(self):
        time.sleep(10)

        wait = WebDriverWait(self.driver, 10)  # Wait up to 10 seconds

        # Wait until the search button is clickable before clicking
        search_button = wait.until(EC.element_to_be_clickable((By.XPATH, self.txt_searchbar_btn_Xpath)))
        search_button.click()

        self.file = "/Users/riyabakoria/Desktop/SearchDDT.xlsx"
        self.workbook = openpyxl.load_workbook(self.file)
        self.sheet = self.workbook["Sheet1"]
        self.rows = XLutils.get_rowcount(self.file, "Sheet1")

        for r in range(2, self.rows + 1):
            self.expected = XLutils.readdata(self.file, "Sheet1", r, 2)
            self.Data = XLutils.readdata(self.file, "Sheet1", r, 1)

            # Wait for the search input box to be visible before typing
            search_box = wait.until(EC.visibility_of_element_located((By.XPATH, self.txt_searchbar_box_Xpath)))
            search_box.send_keys(self.Data)

            # Wait for the search button to be clickable before clicking
            search_btn = wait.until(EC.element_to_be_clickable((By.XPATH, self.search_btn_xpath)))
            search_btn.click()

            # Wait for the message alert to appear before getting text
            self.msg = wait.until(EC.presence_of_element_located((By.XPATH, self.msg_alertmsg_xpath)))
            self.MSG = self.msg.text

            if self.MSG == self.expected:
                XLutils.writedata(self.file, "Sheet1", r, 3, "Passed")
                XLutils.green_fill(self.file, "Sheet1", r, 3)
                print(f"Row {r}: Test Passed")
            else:
                XLutils.writedata(self.file, "Sheet1", r, 3, "Failed")
                XLutils.red_fill(self.file, "Sheet1", r, 3)
                print(f"Row {r}: Test Failed")

            search_box.clear()  # Clear the search box for the next input

            






