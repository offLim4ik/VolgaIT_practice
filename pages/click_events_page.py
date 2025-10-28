from selenium.webdriver.common.by import By
from .base_page import BasePage

class ClickEventsPage(BasePage):
    URL = "https://practice-automation.com/click-events/"
    CLICK_ME_BUTTON = (By.ID, "click-button")
    OUTPUT_MESSAGE = (By.ID, "output")

    def open(self):
        self.driver.get(self.URL)

    def click_button(self):
        self.click(self.CLICK_ME_BUTTON)

    def get_output_text(self):
        return self.find_element(self.OUTPUT_MESSAGE).text