import time
from selenium import webdriver
from selenium.webdriver.common.by import By

def selenium_textbox():
    chrome_driver = webdriver.Chrome()
    chrome_driver.get("https://demoqa.com/buttons")
    chrome_driver.maximize_window()
    click_button = chrome_driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div/div[2]/div[2]/div[3]/button")
    click_button.click()
    time.sleep(5)

if __name__ == "__main__":
    selenium_textbox()