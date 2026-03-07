from data.credentials import Credentials
from pages.login_page.login_page import LoginPage


class BaseTest:

    def setup_method(self):
        self.credentials = Credentials()
        self.login_page = LoginPage(self.driver)