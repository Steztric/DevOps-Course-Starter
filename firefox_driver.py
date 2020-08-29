from selenium import webdriver
import pytest

@pytest.fixture(scope="module")
def driver():
    with webdriver.Firefox() as driver:
        yield driver