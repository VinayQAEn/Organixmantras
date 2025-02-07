import pytest
import random
import string
from Utilities.customlogger import customlogger
from Locators.Register_customerpage import Register_customer  
from Locators.Varifyemailsucess import Verifyemailmsg
@pytest.mark.usefixtures("setup")
class Test_varify_emailmsg:
    def test_emailsucessmsg(self):
        self.rc =  Register_customer(self.driver)
        self.ve = Verifyemailmsg(self.driver)
        self.rc01 = Verifyemailmsg(self.driver)
        self.logger = customlogger()
        self.log = self.logger.get_logger()
        self.log.info("*********Test Register_user_001 started********")
        self.rc.clickLogin()
        self.rc.clickRegister()
        self.rc.enterName("Kumar")
        self.random_email = generate_random_email(domain="gmail.com")

        self.rc.enterEmail(self.random_email)
        self.rc.enterPassword("Password@123")
        self.rc.enterConfirmPassword("Password@123")
        self.rc.enterPhone("1234567890")
        self.rc.enterAddress("Golconda")
        self.rc.clickLocality()
        self.rc.enterPincode("500032")
        self.rc.clickRegisterButton()
        self.rc01.get_email_successmsg()
        self.log.info("************Test Register_user_001 Finished")
def generate_random_email(domain="example.com", length=10):
        """Generate a random email address."""
        random_string = ''.join(random.choices(string.ascii_lowercase + string.digits, k=length))
        return f"{random_string}@{domain}"

