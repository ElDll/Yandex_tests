import time

from .common_methods import CommonMethods
from .locators import DiskPageLocators
from ..Variables.data import FOLDER_NAME, DOCUMENT_NAME


class DiskPage(CommonMethods):
    def __init__(self, driver):
        super().__init__(driver)

    def close_advertising(self):
        self.button_click(DiskPageLocators.CLOSE_ADVERTISING)

    def create_copy_folder(self):
        self.button_click(DiskPageLocators.CREATE_BUTTON)
        self.button_click(DiskPageLocators.CREATE_FOLDER_BUTTON)
        self.input_value(DiskPageLocators.CREATE_FOLDER_INPUT_NAME, FOLDER_NAME)
        self.button_click(DiskPageLocators.CREATE_FOLDER_SAVE_BUTTON)

    def create_copy_document(self):
        self.button_click(DiskPageLocators.CREATE_BUTTON)
        self.button_click(DiskPageLocators.CREATE_DOCUMENT_BUTTON)
        self.input_value(DiskPageLocators.CREATE_FOLDER_INPUT_NAME, DOCUMENT_NAME)
        self.button_click(DiskPageLocators.CREATE_FOLDER_SAVE_BUTTON)


