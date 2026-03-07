from data.urls import Urls
from base.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC


class HomePage(BasePage):

    _PAGE_URL = Urls.HOME_PAGE

    _DROPDOWN_ELEMENT = "//select[@class='product_sort_container']"
    _SORT_ELEMENT = "//option[@value='lohi']"

    def sort(self):

        self.wait.until(EC.element_to_be_clickable(self._DROPDOWN_ELEMENT)).click()
        self.wait.until(EC.element_to_be_clickable(self._SORT_ELEMENT)).click()

    _BACKPACK = "//button[@id='add-to-cart-sauce-labs-backpack']"
    _T_SHIRT = "//button[@id='add-to-cart-test.allthethings()-t-shirt-(red)']"

    def add_item(self):
        self.wait.until(EC.element_to_be_clickable(self._T_SHIRT)).click()
        self.wait.until(EC.element_to_be_clickable(self._BACKPACK)).click()

