from selenium import webdriver
import pytest

@pytest.fixture(scope="module")
def driver():
    options = webdriver.FirefoxOptions()
    options.add_argument('-headless')
    with webdriver.Firefox(options=options) as driver:
        yield driver