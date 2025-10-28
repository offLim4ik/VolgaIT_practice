import os
from datetime import datetime

def take_screenshot(driver, name="screenshot"):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{name}_{timestamp}.png"
    path = os.path.join("allure-results", filename)
    driver.save_screenshot(path)