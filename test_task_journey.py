import os
import sys
from firefox_driver import driver
import test_app

def test_task_journey(driver, test_app):
    driver.get('http://localhost:5000/')
    assert driver.title == 'To-Do App'