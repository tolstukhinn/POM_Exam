from data.credentials import Credentials
from pages.login_page.login_page import LoginPage
from pages.home_page.home_page import HomePage


class BaseTest:

    def setup_method(self):
        self.credentials = Credentials()
        self.login_page = LoginPage(self.driver)
        self.home_page = HomePage(self.driver)