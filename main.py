import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Defining setup and tearDown methods in one class
# It will help us to reduce redundancy of setup and tearDown class
class MySetup(unittest.TestCase):

    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://demoqa.com/buttons")
        self.driver.maximize_window()

    def tearDown(self):
        return super().tearDown()
        

# Defining Test Cases in another 
class MyTestCases(MySetup):
    # without `self` keyword we cannot define methods in our classes
    @unittest.skip("Need to be updated after sprint 2")
    # Above line will skip this particular test case and rest of the test cases will run
    def test_unit_test(self):
        
        # click_button = self.driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div/div[2]/div[2]/div[3]/button")
        click_button = self.driver.find_element(By.ID, "C1SRU")
        click_button.click()

        try:
            element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(By.ID, 'dynamicClickMessage'))
        
        finally:
            print("The element has been found")
            expected_result = "You have done a dynamic"
            actual_result = element.text
            assert expected_result == actual_result
        # time.sleep(10) pauses code execution exactly 10 seconds. It also stops the execution of the current thread
        # time.sleep(3)

        # driver_name.implicitly_wait(10) waits maximum 10 seconds for element's presence. If it is found after 2 seconds then code execution will be continued without wait for more 8 seconds.
        # chrome_driver.implicitly_wait(3)
        self.driver.implicitly_wait(3)
    


if __name__ == "__main__":
    unittest.main()