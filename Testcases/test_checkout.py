import pytest
from Locators.Bestsellerproducts import BestSEllerPRoduct
from Utilities.customlogger import customlogger
@pytest.mark.usefixtures("setup")
class Test_checkout:
    def test_addtocart(self):
        self.cp = BestSEllerPRoduct(self.driver)  # Ensure the class is correctly imported or defined
        self.log = customlogger()
        self.logger = self.log.get_logger()
        self.logger.info('********************Test add to cart test started*****************')
        self.cp.add_tocart()
        self.logger.info('********************Test aad to cart finished*****************')
        self.logger.info("********************Test add product quantity started***********")
        self.cp.add_product_quantity()
        self.logger.info("********************Test add product quantity finished***********")
        


