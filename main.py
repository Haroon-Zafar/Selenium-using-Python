import time
import unittest
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Defining setup and tearDown methods in one class
# It will help us to reduce redundancy of setup and tearDown class
# MAKE SURE TO MAKE `Test` infront of the class name 
class TestMySetup(unittest.TestCase):

    # pytest allows us to execute specific set of actions
    @pytest.fixture
    def browser(self):
        chrome_driver = webdriver.Chrome()
        # yield function returns this particular function after all the test cases have stopped using it
        yield chrome_driver
        chrome_driver.quit()    

    # Test case name must start with `test` keyword
    def test_navigate_to_google(self, browser):
        pass


if __name__ == "__main__":
    unittest.main()