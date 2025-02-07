import pytest
import time
import random
import string
from Utilities.customlogger import customlogger
from Locators.Register_customerpage import Register_customer  

@pytest.mark.usefixtures("setup")
class Test_Register:
    def test_registeruser(self):
        print("Register User Test")
        self.log = customlogger()
        self.log = self.log.get_logger()
        self.log.info("******************Test_register_user_001****************")
        self.ru = Register_customer(self.driver)
        time.sleep(10)
        self.ru.clickLogin()
        self.ru.clickRegister()
        self.ru.enterName("Riya")
        self.random_email = generate_random_email(domain="gmail.com")

        self.ru.enterEmail(self.random_email)
        self.ru.enterPassword("Riya@123")   
        self.ru.enterConfirmPassword("Riya@123")
        self.ru.enterPhone("1234567890")
        self.ru.enterAddress("Hyderabad")
        self.ru.clickLocality()
        self.ru.enterPincode("500081")
        self.ru.clickRegisterButton()
        time.sleep(10)

def generate_random_email(domain="example.com", length=10):
        """Generate a random email address."""
        random_string = ''.join(random.choices(string.ascii_lowercase + string.digits, k=length))
        return f"{random_string}@{domain}"


     

    