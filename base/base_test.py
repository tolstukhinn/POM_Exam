from data.credentials import Credentials
from data.user_data import UserData
from pages.login_page import LoginPage
from pages.home_page import HomePage
from pages.cart_page import CartPage
from pages.checkout_step_one_page import CheckoutStepOne
from pages.checkout_step_two_page import CheckoutStepTwo
from pages.checkout_complete_page import CheckoutComplete


class BaseTest:

    def setup_method(self):
        self.credentials = Credentials()
        self.user_data = UserData()
        self.login_page = LoginPage(self.driver)
        self.home_page = HomePage(self.driver)
        self.cart_page = CartPage(self.driver)
        self.checkout_step_one = CheckoutStepOne(self.driver)
        self.checkout_step_two = CheckoutStepTwo(self.driver)
        self.checkout_complete = CheckoutComplete(self.driver)
