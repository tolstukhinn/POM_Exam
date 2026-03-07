import time
from base.base_test import BaseTest
from pages.login_page.login_page import LoginPage
from pages.home_page.home_page import HomePage




class TestFlow(BaseTest):

    def test_flow(self):
        self.login_page.open()
        self.login_page.login(
            login=self.credentials.LOGIN,
            password=self.credentials.PASSWORD,
        )
        self.home_page.sort()
        self.home_page.add_item()
        time.sleep(5)
