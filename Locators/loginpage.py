from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    
    def __init__(self,driver):
        self.driver = driver
    
    Login_Xpath_btn = "//a[normalize-space()='Login']"
    Useremail_Xpath_textbox = "//input[@placeholder='Eg. example@email.com']"
    Password_Xpath_textbox =  "//input[@placeholder='Enter your password']"
    LoginButton_Xpath = "//button[normalize-space()='Login']"



    def clickLogin(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH,self.Login_Xpath_btn)))
        self.driver.find_element(By.XPATH,self.Login_Xpath_btn).click()

    def enterUseremail(self,email):
        self.driver.find_element(By.XPATH,self.Useremail_Xpath_textbox).clear()
        self.driver.find_element(By.XPATH,self.Useremail_Xpath_textbox).send_keys(email)

    def enterPassword(self,password):
        self.driver.find_element(By.XPATH,self.Password_Xpath_textbox).clear()
        self.driver.find_element(By.XPATH,self.Password_Xpath_textbox).send_keys(password)

    def clickLoginButton(self): 
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH,self.LoginButton_Xpath)))
        self.driver.find_element(By.XPATH,self.LoginButton_Xpath).click()
        

    

        

   
