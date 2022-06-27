import time

from .common_methods import CommonMethods
from .locators import LoginPageLocators
from ..Variables.data import YANDEX_LOGIN, YANDEX_PASSWORD


class LoginPage(CommonMethods):
    def __init__(self, driver):
        super().__init__(driver)

    def login_in_account(self):
        if self.find_element(*LoginPageLocators.PASSWORD_FIELD):
            self.button_click(LoginPageLocators.SWITCH_EMAIL_BUTTON)
        self.find_element(*LoginPageLocators.LOGIN_FIELD).send_keys(YANDEX_LOGIN)
        self.button_click(LoginPageLocators.LOGIN_BUTTON)
        time.sleep(1)
        self.input_value(LoginPageLocators.PASSWORD_FIELD, YANDEX_PASSWORD)
        self.button_click(LoginPageLocators.LOGIN_BUTTON)
