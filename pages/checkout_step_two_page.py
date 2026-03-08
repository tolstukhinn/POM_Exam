from data.urls import Urls
from base.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC


class CheckoutStepTwo(BasePage):

    _PAGE_URL = Urls.CHECKOUT_STEP_TWO_PAGE

    _FINISH_BUTTON = "//button[@id='finish']"

    def placing_order(self):

        self.wait.until(EC.element_to_be_clickable(self._FINISH_BUTTON)).click()

