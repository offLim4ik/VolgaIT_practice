from selenium.webdriver.common.by import By
from .base_page import BasePage

class FormFieldsPage(BasePage):
    URL = "https://practice-automation.com/form-fields/"
    MESSAGE_INPUT = (By.ID, "message")
    SUBMIT_BUTTON = (By.XPATH, "//input[@type='submit']")

    def open(self):
        self.driver.get(self.URL)

    def fill_message(self, text):
        self.enter_text(self.MESSAGE_INPUT, text)

    def submit_form(self):
        self.click(self.SUBMIT_BUTTON)