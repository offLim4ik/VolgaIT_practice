from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.screenshot import take_screenshot

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def find_element(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def click(self, locator):
        elem = self.find_element(locator)
        elem.click()

    def enter_text(self, locator, text):
        elem = self.find_element(locator)
        elem.clear()
        elem.send_keys(text)

    def is_element_visible(self, locator):
        try:
            return self.find_element(locator).is_displayed()
        except:
            take_screenshot(self.driver, "element_not_visible")
            return False