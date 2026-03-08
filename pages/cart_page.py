from data.urls import Urls
from base.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC


class CartPage(BasePage):

    _PAGE_URL = Urls.CART_PAGE

    _REMOVE_ITEM_BUTTON = "//button[@id='remove-test.allthethings()-t-shirt-(red)']"

    def remove_item(self):

        self.wait.until(EC.element_to_be_clickable(self._REMOVE_ITEM_BUTTON)).click()

    _CHECKOUT_BUTTON = "//button[@id='checkout']"

    def go_to_checkout(self):

        self.wait.until(EC.element_to_be_clickable(self._CHECKOUT_BUTTON)).click()
