import time
from selenium import webdriver
from selenium.webdriver.common.by import By

def selenium_textbox():
    chrome_driver = webdriver.Chrome()
    chrome_driver.get("https://demoqa.com/text-box")
    first_name = chrome_driver.find_element(By.ID, "userName")
    first_name.send_keys("John")
    time.sleep(5)
    first_name.clear()
    time.sleep(5)
    # print("Chrome Initiated")


if __name__ == "__main__":
    selenium_textbox()