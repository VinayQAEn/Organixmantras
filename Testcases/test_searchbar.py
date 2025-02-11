import pytest
from Utilities.customlogger import customlogger
from Locators.Search_bar import Search_bar
@pytest.mark.usefixtures("setup")
class Test_searchbar:
    def test_search_bar(self.driver):
        self.logger = customlogger()
        self.log = self.logger.get_logger()
        self.log.info("***********Test search_bart_001 started*************")
        self.sb = Search_bar()
        self.sb.searchbar_ddt()
        self.log.info("************Test search_barddt_finished*************8")

