import time

import pytest
from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


class CommonMethods:
    '''В этом классе собраны обертки и методы для работы с поиском элементов. Обертки на ассерты'''
    def __init__(self, driver):
        self.driver = driver

    def button_click(self,  element: tuple) -> None:
        self.find_element(*element).click()

    def input_value(self, element: tuple, text: str) -> None:
        self.find_element(*element).send_keys(text)

    def get_webelement(self, by: By, value: str, timeout=10) -> WebElement:
        """
        Получить веб элемент

        Args:
            by (By): Список поиска элемента, например By.CSS
            value (str): Значение элемента
            timeout (int, optional): Ожидание. Defaults to 10.
        """
        return self.find_element(by, value, timeout)

    def find_element(self, by: By, value: str, timeout=10) -> WebElement:
        """
        Обертка над WebDriverWait и expected_condition. Поиск элемента,
        который отобразился не только
        в DOM дереве, но и имеет высоту/ширину - явно отобразился на странице.
        """
        return WebDriverWait(self.driver, timeout).until(
            ec.visibility_of_element_located((by, value)), message=f'No such element {value}')

    def invisibility_of_element(self, by: By, value: str, timeout: int = 10) -> bool:
        return WebDriverWait(self.driver, timeout).until(ec.invisibility_of_element((by, value)),
                                                         message=f'Элемент не исчез {(by,value)}.')

    def find_elements(self, by: By, value: str, timeout=10) -> WebElement:
        """
        Используется для получения элементов, например, в выпадающих списках
        """
        return WebDriverWait(self.driver, timeout).until(
            ec.visibility_of_all_elements_located((by, value)), message=f'No such element {value}')

    def find_element_by_text(self, text) -> WebElement:
        return self.find_element(By.XPATH, f'//*[text()="{text}"]')

    def take_screenshot(self, by: By, value: str) -> None:
        """
        Сделать скриншот, если элемент отобразился на странице. Иначе ошибка.

        Returns:
            В случае, если отобразился элемент - делает его скриншот и кладет в корень проекта.
            Если элемент не найден возвращает ошибку.
        """
        element = self.get_webelement(by, value)
        if element:
            return element.screenshot(f'Screenshots/Screen{time.strftime("%Y%m%d-%H%M%S")}.png')
        else:
            return f'No element {element}'

    def get_element_color(self, by: By, value: str) -> None:
        element = self.find_element(by, value)
        return element.value_of_css_property('border-color')

    def clear_field(self, element: WebElement) -> None:
        ActionChains(self.driver).double_click(element).send_keys(Keys.DELETE).perform()

    def select_drop_down_option(self, option: str) -> None:
        """
        Выбираем элемент в дропдауне
        """
        element = self.find_element_by_text(option)
        element.click()

    def assert_element_visible(self, by: By, value: str, timeout: int = 10) -> bool:
        try:
            self.get_webelement(by, value, timeout)
            return True
        except TimeoutException:
            return False

    def assert_element_is_not_visible(self, by: By, value: str, timeout: int = 10) -> bool:
        try:
            WebDriverWait(self.driver, timeout).until(ec.invisibility_of_element_located((by, value)))
            return True
        except TimeoutException:
            return False

    def assert_text_equal(self, by: By, value: str, text: str) -> None:
        text_element = self.find_element(by, value).text.strip()
        assert text_element == text, f'{text_element} не равен {text}'

    def assert_url(self, url: str, timeout: int = 10) -> None:
        time.sleep(2)
        current_url = self.driver.current_url
        assert current_url == url, f"Ожидался {url}, открыт {current_url}"

    def assert_validation_text(self, element: WebElement, text_message: str) -> None:
        message = self.driver.execute_script('return arguments[0].validationMessage;', element)
        assert message == text_message, f"{message} , не равен {text_message}"

    def assert_validation_message(self, element: WebElement) -> None:
        self.driver.execute_script('arguments[0].checkValidity();', element)
