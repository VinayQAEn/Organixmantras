import pytest
import time
from Utilities.customlogger import customlogger
from Locators.Register_customerpage import Register_customer  
from Locators.Reg_Error_msg import Reg_error_msg
@pytest.mark.usefixtures("setup")
class Test_varify_emailmsg:
    def test_emailsucessmsg(self):
        self.em = Reg_error_msg(self.driver)
        self.rc =  Register_customer(self.driver)
        self.logger = customlogger()
        self.log = self.logger.get_logger()
        self.log.info("*********Test Reg_error_msg started********")
        self.em.clickLogin()
        self.em.clickRegister()
        self.em.clickRegisterButton()
        self.em.clickRegisterButton()
        # self.em.enterName()
        self.em.errorsmsg_name()
        # self.em.enterEmail()
        self.em.errorsmsg_email()
        # self.em.enterPassword()
        self.em.errorsmsg_password()
        # self.em.enterConfirmPassword()
        self.em.errorsmsg_confirmpassword()
        # self.em.enterPhone()
        self.em.phonemsg_errormsg()
        # self.em.enterAddress()
        self.em.address_errormsg()
        # self.em.clickLocality()
        self.em.locality_errormsg()
        # self.em.enterPincode()
        self.em.pincode_errormsg()
        
        self.log.info("************Test Reg_error_msg Finished")


