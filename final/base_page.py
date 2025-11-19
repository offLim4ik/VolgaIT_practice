from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class BasePage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def find_element(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def enter_text(self, locator, text):
        elem = self.find_element(locator)
        elem.clear()
        elem.send_keys(text)

    def type(self, locator, text):
        self.enter_text(locator, text)

    def click(self, locator):
        elem = self.find_element(locator)
        elem.click()

    def select_by_value(self, locator, value):
        select_elem = self.find_element(locator)
        select = Select(select_elem)
        select.select_by_value(value)
