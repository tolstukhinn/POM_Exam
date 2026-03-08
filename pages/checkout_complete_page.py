from data.urls import Urls
from base.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC


class CheckoutComplete(BasePage):

    _PAGE_URL = Urls.CHECKOUT_COMPLETE_PAGE

    _BACK_HOME_BUTTON = "//button[@id='back-to-products']"

    def return_to_home_page(self):

        self.wait.until(EC.element_to_be_clickable(self._BACK_HOME_BUTTON)).click()


