import allure
from pages.popups_page import PopupsPage

@allure.title("Confirm popup — отмена")
def test_confirm_dismiss(driver):
    page = PopupsPage(driver)
    page.open()
    result = page.trigger_confirm(accept=False)
    assert "cancelled" in result.lower()

@allure.title("Prompt popup — пустой ввод")
def test_prompt_empty_input(driver):
    page = PopupsPage(driver)
    page.open()
    result = page.trigger_prompt("")
    assert "empty" in result.lower() or result == ""