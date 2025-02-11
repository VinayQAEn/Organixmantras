import openpyxl
from selenium.webdriver.common.by import By
from Utilities import XLutils


class Search_bar:
    txt_searchbar_btn_Xpath = "//p[normalize-space()='Search']"
    txt_searchbar_box_Xpath = "//li[@class='hidden md:block']//input[@placeholder='Search for a product or a broader category']"
    search_btn_xpath = "//button[normalize-space()='Search']"
    msg_alertmsg_xpath = "/html/body/app-root/app-header/div/header/div/div/div[3]/div/ul/li[1]/div/div[2]"

    def __init__(self,driver):
        self.driver = driver
    def searchbar_ddt(self):
        self.driver.find_element(By.XPATH,self.txt_searchbar_btn_Xpath).click()
        self.file = "/Users/riyabakoria/Desktop/SearchDDT.xlsx"
        self.workbook = openpyxl.load_workbook(self.file)
        self.sheet = self.workbook["Sheet1"]
        self.rows = XLutils.get_rowcount(self.file,"Sheet1") 
        self.expected = XLutils.readdata(self.file,"Sheet1",r,2)

        for r in range(2,self.rows+1):
            self.Data = XLutils.readdata(self.file,"Sheet1",r,1)
            self.driver.find_element(By.XPATH,self.txt_searchbar_box_Xpath).send_keys(self.Data)
            self.driver.find_element(By.XPATH,self.search_btn_xpath).click()
            self.msg = self.driver.find_element(By.XPATH,self.msg_alertmsg_xpath)
            self.MSG = self.msg.text
            if self.MSG == self.expected:
                XLutils.writedata(self.file,"Sheet1",r,3,"Passed")
                XLutils.green_fill(self.file,"Sheet1",r,3)
                print("Test Passed")
            else:
                XLutils.writedata(self.file,"Sheet1",r,3,"Failed")
                XLutils.red_fill(self.file,"Sheet1",r,3)
            self.driver.find_element(By.XPATH,self.txt_searchbar_box_Xpath).clear()
            






