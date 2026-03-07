from data.urls import Urls
from base.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC



class LoginPage(BasePage):

    _PAGE_URL = Urls.LOGIN_PAGE

    _USERNAME_FIELD = "//input[@id='user-name']"
    _PASSWORD_FIELD = "//input[@id='password']"
    _LOGIN_BUTTON = "//input[@id='login-button']"

    def login(self,login,password):

        self.wait.until(EC.element_to_be_clickable(self._USERNAME_FIELD)).send_keys(login)
        self.wait.until(EC.element_to_be_clickable(self._PASSWORD_FIELD)).send_keys(password)
        self.wait.until(EC.element_to_be_clickable(self._LOGIN_BUTTON)).click()

