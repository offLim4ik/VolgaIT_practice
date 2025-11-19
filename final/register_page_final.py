from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class RegistrationPage:
    URL = "https://way2automation.com/way2auto_jquery/registration.php"
    ABOUT_YOURSELF = (By.XPATH, "//label[text()='About Yourself']/following-sibling::textarea")

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(self.URL)
        WebDriverWait(self.driver, 15).until(
            EC.visibility_of_element_located(self.ABOUT_YOURSELF)
        )

    def fill_about_yourself(self, text):
        field = self.driver.find_element(*self.ABOUT_YOURSELF)
        field.clear()
        field.send_keys(text)

    def get_about_yourself_value(self):
        return self.driver.find_element(*self.ABOUT_YOURSELF).get_attribute("value")
