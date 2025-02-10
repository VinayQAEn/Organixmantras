import pytest
from Locators.OM_phone import Om_phone
from Utilities.customlogger import customlogger

@pytest.mark.usefixtures("setup")
class Test_OM_Phone:
    def test_om_phone(self):
        self.logger = customlogger()
        self.log =self.logger.get_logger()
        self.log.info("*********Test OM Phone started***********")
        self.op = Om_phone(self.driver)
        self.op.click_om_phonelink()
        
        
        
