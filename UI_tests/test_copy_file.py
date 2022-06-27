import time

from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.disk_page import DiskPage


class TestCopyFile:
    def test_working_button(self, driver):
        main_page = MainPage(driver)
        main_page.go_to_login_page()
        login_page = LoginPage(driver)
        login_page.login_in_account()
        main_page.go_to_disk_page()
        disk_page = DiskPage(driver)
        disk_page.create_copy_folder()
        disk_page.create_copy_document()


