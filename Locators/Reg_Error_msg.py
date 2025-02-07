from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random
import string
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException

class Reg_error_msg:
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
    #erros_Xpaths
    er_namemsg_Xpath = "//div[contains(text(),'Name is required.')]"
    er_emailmsg_Xpath = "//div[contains(text(),'Email is required.')]"
    er_password_msg_xpath = "//div[@class='error-msg ng-star-inserted'][normalize-space()='Password is required.']"
    er_confirm_passmsg_xpath = "//div[contains(text(),'Confirm Password is required.')]"
    er_phone_err_msg_Xpath = "//div[normalize-space()='Phone Number is required.']"
    er_address_ermsg_xpath = "//div[contains(text(),'Address is required.')]"
    er_locality_err_msg_Xpath = "//div[normalize-space()='Locality is required.']"
    er_pincode_errmsg_Xpath = "//div[contains(text(),'Pincode is required.')]"



    

    def clickLogin(self):
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH,self.lnk_Login_Xpath)))
        self.driver.find_element(By.XPATH,self.lnk_Login_Xpath).click()
    def clickRegister(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH,self.lnk_Register_Xpath)))
        self.driver.find_element(By.XPATH,self.lnk_Register_Xpath).click()
    
    def clickRegisterButton(self):
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH,self.btn_Register_Xpath)))
        self.driver.find_element(By.XPATH,self.btn_Register_Xpath).click()
        print(self.driver.find_element(By.XPATH,self.btn_Register_Xpath).is_enabled())

    def enterName(self):
        self.driver.find_element(By.XPATH,self.Txt_name_Xpath).clear()
        # self.driver.find_element(By.XPATH,self.Txt_name_Xpath).send_keys(name)
    def enterEmail(self): 
        self.driver.find_element(By.XPATH,self.Txt_email_Xpath).clear()
        # self.driver.find_element(By.XPATH,self.Txt_email_Xpath).send_keys(email)
    def enterPassword(self):
        self.driver.find_element(By.XPATH,self.Txt_password_Xpath).clear()
        # self.driver.find_element(By.XPATH,self.Txt_password_Xpath).send_keys(password)
    def enterConfirmPassword(self):    
        self.driver.find_element(By.XPATH,self.Txt_confirm_pasword_Xpath).clear()
        # self.driver.find_element(By.XPATH,self.Txt_confirm_pasword_Xpath).send_keys(confirm_password)
    def enterPhone(self):
        self.driver.find_element(By.XPATH,self.Txt_Phone_Xpath).clear()
        # self.driver.find_element(By.XPATH,self.Txt_Phone_Xpath).send_keys(phone)
    def enterAddress(self):
        self.driver.find_element(By.XPATH,self.Txt_Address_Xpath).clear()
        # self.driver.find_element(By.XPATH,self.Txt_Address_Xpath).send_keys(address)
    def clickLocality(self):
        self.locality = self.driver.find_element(By.XPATH, "//label[normalize-space()='Locality...']")
        self.locality.click()
        # self.city = self.driver.find_element(By.XPATH,"//option[@value='aYIoNkoneFfmAv3Azk1t']")
        # self.act = ActionChains(self.driver)
        # self.act.move_to_element(self.city).click().perform()
    def enterPincode(self):
        self.driver.find_element(By.XPATH,self.txt_pincode_Xpath).clear()
        # self.driver.find_element(By.XPATH,self.txt_pincode_Xpath).send_keys(pincode)
    def errorsmsg_name(self):
        try:
            name_errormsg = self.driver.find_element(By.XPATH,self.er_namemsg_Xpath)
            nameerrormsg = name_errormsg.text
            assert "Name is required." in nameerrormsg
            print(f"✅ Success message displayed: {nameerrormsg}")
            return True
        except Exception:
            print("❌ Error name_message not found!")
            return False
    def errorsmsg_email(self):
        try:
            email_errormsg = self.driver.find_element(By.XPATH,self.er_emailmsg_Xpath)
            emailerrormsg = email_errormsg.text
            assert "Email is required." in emailerrormsg
            print(f"✅ Success message displayed: {emailerrormsg}")
            return True
        except Exception:
            print("❌ Error_email message not found!")
            return False
    def errorsmsg_password(self):
        try:
            password_errormsg = self.driver.find_element(By.XPATH,self.er_password_msg_xpath)
            passworderrormsg = password_errormsg.text
            assert "Password is required." in passworderrormsg
            print(f"✅ Success message displayed: {passworderrormsg}")
            return True
        except Exception:
            print("❌ Error_Password message not found!")
            return False
    def errorsmsg_confirmpassword(self):
        try:
            confirmpassword_errormsg = self.driver.find_element(By.XPATH,self.er_confirm_passmsg_xpath)
            confirmpassworderrormsg = confirmpassword_errormsg.text
            assert "Confirm Password is required." in confirmpassworderrormsg
            print(f"✅ Success message displayed: {confirmpassworderrormsg}")
            return True
        except Exception:
            print("❌ Error_confirmpassword message not found!")
            return False
    def phonemsg_errormsg(self):
        try:
            phone_errormsg = self.driver.find_element(By.XPATH,self.er_phone_err_msg_Xpath)
            phoneerrormsg = phone_errormsg.text
            assert "Phone Number is required." in phoneerrormsg
            print(f"✅ Success message displayed: {phoneerrormsg}")
            return True
        except Exception:
            print("❌ Error_phone message not found!")
            return False
    def address_errormsg(self):
        try:
            address_errormsg = self.driver.find_element(By.XPATH,self.er_address_ermsg_xpath)
            address = address_errormsg.text
            assert "Address is required." in address
            print(f"✅ Success message displayed: {address}")
            return True
        except Exception:
            print("❌ Error_address message not found!")
            return False
    def locality_errormsg(self):
        try:
            locality_errormsg = self.driver.find_element(By.XPATH,self.er_locality_err_msg_Xpath)
            locality = locality_errormsg.text
            assert "Locality is required." in locality
            print(f"✅ Success message displayed: {locality}")
            return True
        except Exception:
            print("❌ Error_locality message not found!")
            return False
    def pincode_errormsg(self):
        try:
            pincode_errormsg = self.driver.find_element(By.XPATH,self.er_pincode_errmsg_Xpath)
            pincode = pincode_errormsg.text
            assert "Pincode is required." in pincode
            print(f"✅ Success message displayed: {pincode}")
            return True
        except Exception:
            print("❌ Error_pincode message not found!")
            return False
    def clickRegisterButton(self):
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH,self.btn_Register_Xpath)))
        self.driver.find_element(By.XPATH,self.btn_Register_Xpath).click()
    


       