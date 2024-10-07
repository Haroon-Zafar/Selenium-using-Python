import time
from selenium import webdriver
from selenium.webdriver.common.by import By

import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class TestLoginFunctionality(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Setup the Chrome driver for all tests
        cls.chrome_driver = webdriver.Chrome()
        cls.chrome_driver.maximize_window()

    @classmethod
    def tearDownClass(cls):
        # Close the driver after all tests
        cls.chrome_driver.quit()

    def setUp(self):
        # Go to the login page for each test case
        self.chrome_driver.get("https://practicetestautomation.com/practice-test-login/")
    
    def test_valid_login(self):
        """Test Case 01: Valid Login"""
        self.perform_login("student", "Password123")
        self.assert_login_successful()

    
    def test_invalid_username(self):
        """Test Case 02: Invalid Username"""
        self.perform_login("invalid_user", "Password123")
        self.assert_login_failed()

    def test_invalid_password(self):
        """Test Case 03: Invalid Password"""
        self.perform_login("student", "wrongpassword")
        self.assert_login_failed()

    def test_empty_fields(self):
        """Test Case 04: Empty Input Fields"""
        self.perform_login("", "")
        self.assert_login_failed()

    def perform_login(self, username_input, password_input):
        """Perform the login with provided credentials"""
        username = self.chrome_driver.find_element(By.ID, 'username')
        username.send_keys(username_input)

        password = self.chrome_driver.find_element(By.ID, 'password')
        password.send_keys(password_input)

        click_button = self.chrome_driver.find_element(By.ID, 'submit')
        click_button.click()
        time.sleep(2)

    def assert_login_successful(self):
        """Check if login was successful by checking the page title or URL"""
        self.assertIn("Logged In Successfully", self.chrome_driver.page_source, "Login failed for valid credentials.")

    def assert_login_failed(self):
        """Check if login failed by looking for an error message"""
        error_message = self.chrome_driver.find_element(By.ID, "error").text
        self.assertTrue("Your username is invalid!" in error_message or "Your password is invalid!" in error_message,
                        f"Expected login failure, but login succeeded or incorrect error message. Error: {error_message}")

if __name__ == "__main__":
    unittest.main()
    

# if __name__ == "__main__":
#     selenium_textbox()