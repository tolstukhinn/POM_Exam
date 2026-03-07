import time
from base.base_test import BaseTest



class TestAddItem(BaseTest):

    def test_add_item(self):
        self.home_page.open()
        self.home_page.add_item()