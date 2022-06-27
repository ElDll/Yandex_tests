from .common_methods import CommonMethods
from .locators import MainPageLocators


class MainPage(CommonMethods):
    def __init__(self, driver):
        super().__init__(driver)

    def go_to_login_page(self):
        self.button_click(MainPageLocators.LOGIN_BUTTON)

    def go_to_disk_page(self):
        self.button_click(MainPageLocators.DISK_BUTTON)

