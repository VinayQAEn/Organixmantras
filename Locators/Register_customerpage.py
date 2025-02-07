from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random
import string
from selenium.webdriver.common.action_chains import ActionChains


class Register_customer:
    def __init__(self,driver):
        self.driver = driver

    lnk_Login_Xpath = "//a[normalize-space()='Login']"
    lnk_Register_Xpath = "//a[normalize-space()='Register']"
    Txt_name_Xpath = "//input[@placeholder='Name']"
    Txt_email_Xpath = "//input[@placeholder='Email']"
    Txt_password_Xpath = "//input[@placeholder='Enter your password']"
    Txt_confirm_pasword_Xpath = "//input[@placeholder='Enter your confirm password']"
    Txt_Phone_Xpath = "/html/body/app-root/app-register/app-auth-layout/div/div/div[1]/div/div[2]/div/div/form/div/div/div[1]/div[5]/div/div/div/input"
    Txt_Address_Xpath = "/html/body/app-root/app-register/app-auth-layout/div/div/div[1]/div/div[2]/div/div/form/div/div/div[1]/div[6]/div/div/input"
    Drp_Locality_Xpath = "//label[@class='dropbtn']"
    Txt_Searchbar_Xpath = "//input[@placeholder='Search..']"
    ele_drp = "//option[@value='BysuZ5TNkxaOocaOPyDG']"
    txt_pincode_Xpath = "/html/body/app-root/app-register/app-auth-layout/div/div/div[1]/div/div[2]/div/div/form/div/div/div[1]/div[8]/div/div/input"
    btn_Register_Xpath = "//button[normalize-space()='Register']"

    

    def clickLogin(self):
        element = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH,self.lnk_Login_Xpath)))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        element.click()
        self.driver.find_element(By.XPATH,self.lnk_Login_Xpath).click()
    def clickRegister(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH,self.lnk_Register_Xpath)))
        self.driver.find_element(By.XPATH,self.lnk_Register_Xpath).click()
    def enterName(self,name):
        self.driver.find_element(By.XPATH,self.Txt_name_Xpath).clear()
        self.driver.find_element(By.XPATH,self.Txt_name_Xpath).send_keys(name)
    def enterEmail(self,email): 
        self.driver.find_element(By.XPATH,self.Txt_email_Xpath).clear()
        self.driver.find_element(By.XPATH,self.Txt_email_Xpath).send_keys(email)
    def enterPassword(self,password):
        self.driver.find_element(By.XPATH,self.Txt_password_Xpath).clear()
        self.driver.find_element(By.XPATH,self.Txt_password_Xpath).send_keys(password)
    def enterConfirmPassword(self,confirm_password):    
        self.driver.find_element(By.XPATH,self.Txt_confirm_pasword_Xpath).clear()
        self.driver.find_element(By.XPATH,self.Txt_confirm_pasword_Xpath).send_keys(confirm_password)
    def enterPhone(self,phone):
        self.driver.find_element(By.XPATH,self.Txt_Phone_Xpath).clear()
        self.driver.find_element(By.XPATH,self.Txt_Phone_Xpath).send_keys(phone)
    def enterAddress(self,address):
        self.driver.find_element(By.XPATH,self.Txt_Address_Xpath).clear()
        self.driver.find_element(By.XPATH,self.Txt_Address_Xpath).send_keys(address)
    def clickLocality(self):
        self.locality = self.driver.find_element(By.XPATH, "//label[normalize-space()='Locality...']")
        self.locality.click()
        self.city = self.driver.find_element(By.XPATH,"//option[@value='aYIoNkoneFfmAv3Azk1t']")
        self.act = ActionChains(self.driver)
        self.act.move_to_element(self.city).click().perform()
    def enterPincode(self,pincode):
        self.driver.find_element(By.XPATH,self.txt_pincode_Xpath).clear()
        self.driver.find_element(By.XPATH,self.txt_pincode_Xpath).send_keys(pincode)
    def clickRegisterButton(self):
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH,self.btn_Register_Xpath)))
        self.driver.find_element(By.XPATH,self.btn_Register_Xpath).click()
    

    

    
