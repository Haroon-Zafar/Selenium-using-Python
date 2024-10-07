import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

def selenium_textbox():
    chrome_driver = webdriver.Chrome()
    chrome_driver.get("https://demoqa.com/buttons")
    chrome_driver.maximize_window()
    
    click_button = chrome_driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div/div[2]/div[2]/div[3]/button")
    click_button.click()

    try:
        element = WebDriverWait(chrome_driver, 10).until(EC.presence_of_element_located(By.ID, 'dynamicClickMessage'))
    
    finally:
        print("The element has been found")
        expected_result = "You have done a dynamic"
        actual_result = element.text
        assert expected_result == actual_result
    # time.sleep(10) pauses code execution exactly 10 seconds. It also stops the execution of the current thread
    # time.sleep(3)

    # driver_name.implicitly_wait(10) waits maximum 10 seconds for element's presence. If it is found after 2 seconds then code execution will be continued without wait for more 8 seconds.
    # chrome_driver.implicitly_wait(3)
    chrome_driver.implicitly_wait(3)


if __name__ == "__main__":
    selenium_textbox()