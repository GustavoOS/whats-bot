from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class Browser:
    def __init__(self):
        self.driver = webdriver.Chrome(
            service=ChromeService(ChromeDriverManager().install()))
        self.driver.implicitly_wait(10)

    def go_to(self, url):
        self.driver.get(url)

    def click_selector(self, selector):
        self.driver.find_element(By.CSS_SELECTOR, selector).click()
