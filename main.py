import time
from selenium import webdriver
from selenium.webdriver.common.by import By

def selenium_textbox():
    chrome_driver = webdriver.Chrome()
    chrome_driver.get("https://demoqa.com/buttons")
    chrome_driver.maximize_window()
    click_button = chrome_driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div/div[2]/div[2]/div[3]/button")
    click_button.click()
    dynamic_message = chrome_driver.find_element(By.ID, 'dynamicClickMessage')
    if dynamic_message.is_displayed():
        print("The Element is displayed")
    else: 
        print("The Element is NOT displayed")
    expected_result = "You have done a dynamic click"
    # .text() is used to get the text of an element.
    actual_result = dynamic_message.text()
    # assert statement is a built-in construct that allows you to test assumptions about your code
    assert expected_result == actual_result
    time.sleep(5)
    

if __name__ == "__main__":
    selenium_textbox()