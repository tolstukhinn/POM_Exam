import time
from base.base_test import BaseTest



class TestLogin(BaseTest):

    def test_login(self):
        self.login_page.open()
        self.login_page.login(
            login=self.credentials.LOGIN,
            password=self.credentials.PASSWORD
        )
        time.sleep(10)