from selenium import webdriver

def browser():
    chrome_driver = webdriver.Chrome()
    chrome_driver.get("https://www.selenium.dev/")
    print("Chrome Initiated")


if __name__ == "__main__":
    browser()