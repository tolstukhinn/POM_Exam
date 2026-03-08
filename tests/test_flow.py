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
        with allure.step("02. Успешная авторизация."):
            self.login_page.login(
                login=self.credentials.LOGIN,
                password=self.credentials.PASSWORD,
            )
            allure.attach(
                body=self.driver.get_screenshot_as_png(),
                name="Авторизация",
                attachment_type=allure.attachment_type.PNG,
            )
        self.home_page.is_opened()

        with allure.step("03. Сортировка товаров."):
            self.home_page.sort()
            allure.attach(
                body=self.driver.get_screenshot_as_png(),
                name="Сортировка товаров",
                attachment_type=allure.attachment_type.PNG,
            )

        with allure.step("04. Товары добавлены в корзину."):
            self.home_page.add_item()
            allure.attach(
                body=self.driver.get_screenshot_as_png(),
                name="Товары добавлены в корзину",
                attachment_type=allure.attachment_type.PNG,
            )

        with allure.step("05. Переход в корзину."):
            self.home_page.go_to_cart()
            allure.attach(
                body=self.driver.get_screenshot_as_png(),
                name="Корзина",
                attachment_type=allure.attachment_type.PNG,
            )
        self.cart_page.is_opened()

        with allure.step("06. Удаление товара из корзины."):
            self.cart_page.remove_item()
            allure.attach(
                body=self.driver.get_screenshot_as_png(),
                name="Товар удален из корзины",
                attachment_type=allure.attachment_type.PNG,
            )
        self.cart_page.go_to_checkout()
        self.checkout_step_one.is_opened()

        with allure.step("07. Заполнение полей чекаута."):
            self.checkout_step_one.data_entry(
                first_name=self.user_data.FIRST_NAME,
                last_name=self.user_data.LAST_NAME,
                zip_code=self.user_data.ZIP_CODE
        )
            allure.attach(
                body=self.driver.get_screenshot_as_png(),
                name="Переход на второй чекаут",
                attachment_type=allure.attachment_type.PNG,
            )
        self.checkout_step_two.is_opened()

        with allure.step("08. Оформление заказа"):
            self.checkout_step_two.placing_order()
            allure.attach(
                body=self.driver.get_screenshot_as_png(),
                name="Заказ успешно оформлен",
                attachment_type=allure.attachment_type.PNG,
            )

        with allure.step("09. Возврат на домашнюю страницу"):
            self.checkout_complete.return_to_home_page()
            allure.attach(
                body=self.driver.get_screenshot_as_png(),
                name="Домашняя страница",
                attachment_type=allure.attachment_type.PNG,
            )
        self.home_page.is_opened()

        with allure.step("10. Выход из системы"):
            self.home_page.logout()
            allure.attach(
                body=self.driver.get_screenshot_as_png(),
                name="Страница авторизации",
                attachment_type=allure.attachment_type.PNG,
            )
