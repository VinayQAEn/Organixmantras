import pytest
from Locators.Delivery_drp import Delivery_drp
import time
@pytest.mark.usefixtures("setup")
class Test_deliveryDRp:
    def test_delivery_drp(self):
        self.dlv = Delivery_drp(self.driver)
        time.sleep(5)
        self.dlv.delivery_Drp()
        time.sleep(5)

