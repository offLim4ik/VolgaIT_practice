from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage

class PopupsPage(BasePage):
    URL = "https://practice-automation.com/popups/"
    ALERT_BUTTON = (By.ID, "alert-button")
    CONFIRM_BUTTON = (By.ID, "confirm-button")
    PROMPT_BUTTON = (By.ID, "prompt-button")

    def open(self):
        self.driver.get(self.URL)

    def trigger_alert(self):
        self.click(self.ALERT_BUTTON)
        alert = self.driver.switch_to.alert
        text = alert.text
        alert.accept()
        return text

    def trigger_confirm(self, accept=True):
        self.click(self.CONFIRM_BUTTON)
        alert = self.driver.switch_to.alert
        if accept:
            alert.accept()
        else:
            alert.dismiss()
        return self.driver.find_element(By.ID, "confirm-result").text

    def trigger_prompt(self, text="test"):
        self.click(self.PROMPT_BUTTON)
        alert = self.driver.switch_to.alert
        alert.send_keys(text)
        alert.accept()
        return self.driver.find_element(By.ID, "prompt-result").text