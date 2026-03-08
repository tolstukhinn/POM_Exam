import allure
from selenium.webdriver.remote.webdriver import WebDriver
from metaclasses.meta_locator import MetaLocator
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage(metaclass=MetaLocator):

    def __init__(self, driver):

        self.driver: WebDriver = driver

        self.wait = WebDriverWait(self.driver, 10, poll_frequency=1)


    def open(self):

        with allure.step(f"01. Открытие страницы авторизации."):

            self.driver.get(self._PAGE_URL)
            allure.attach(
                body=self.driver.get_screenshot_as_png(),
                name="Открытие login page",
                attachment_type=allure.attachment_type.PNG,
            )

    def is_opened(self):

        self.wait.until(EC.url_to_be(self._PAGE_URL))