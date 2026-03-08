import time
import allure
import pytest
from base.base_test import BaseTest
from allure_commons.types import Severity

@allure.epic("FullFlow")
class TestFlow(BaseTest):

    @pytest.mark.full_flow
    @allure.title("Full E-commerce Flow Test")
    @allure.severity(Severity.CRITICAL)
    @allure.link(url="https://confluence.com", name="Documentation")

    def test_flow(self):
        self.login_page.open()
        self.login_page.is_opened()
        self.login_page.login(
            login=self.credentials.LOGIN,
            password=self.credentials.PASSWORD,
        )
        self.home_page.is_opened()
        self.home_page.sort()
        self.home_page.add_item()
        self.home_page.go_to_cart()
        self.cart_page.is_opened()
        self.cart_page.remove_item()
        self.cart_page.go_to_checkout()
        self.checkout_step_one.is_opened()
        self.checkout_step_one.data_entry(
            first_name=self.user_data.FIRST_NAME,
            last_name=self.user_data.LAST_NAME,
            zip_code=self.user_data.ZIP_CODE
        )
        self.checkout_step_two.is_opened()
        self.checkout_step_two.placing_order()
        self.checkout_complete.return_to_home_page()
        self.home_page.is_opened()
        self.home_page.logout()


