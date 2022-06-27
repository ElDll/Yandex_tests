import pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from .Variables.data import YANDEX_BasePage_URL


@pytest.fixture()
def driver():
    chrome_options = Options()
    _driver = webdriver.Chrome(options=chrome_options)
    _driver.implicitly_wait(3)
    _driver.get(YANDEX_BasePage_URL)
    yield _driver
    _driver.quit()
