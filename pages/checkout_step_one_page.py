from data.urls import Urls
from base.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC


class CheckoutStepOne(BasePage):

    _PAGE_URL = Urls.CHECKOUT_STEP_ONE_PAGE

    _FIRST_NAME_FIELD = "//input[@id='first-name']"
    _LAST_NAME_FIELD = "//input[@id='last-name']"
    _ZIP_FIELD = "//input[@id='postal-code']"
    _CONTINUE_BUTTON = "//input[@id='continue']"

    def data_entry(self,first_name,last_name,zip_code):
        self.wait.until(EC.element_to_be_clickable(self._FIRST_NAME_FIELD)).send_keys(first_name)
        self.wait.until(EC.element_to_be_clickable(self._LAST_NAME_FIELD)).send_keys(last_name)
        self.wait.until(EC.element_to_be_clickable(self._ZIP_FIELD)).send_keys(zip_code)
        self.wait.until(EC.element_to_be_clickable(self._CONTINUE_BUTTON)).click()