import allure
from pages.click_events_page import ClickEventsPage

@allure.title("Поле изначально пустое")
def test_initial_output_empty(driver):
    page = ClickEventsPage(driver)
    page.open()
    assert page.get_output_text() == ""

@allure.title("Повторное нажатие не дублирует текст")
def test_double_click_no_duplication(driver):
    page = ClickEventsPage(driver)
    page.open()
    page.click_button()
    page.click_button()
    assert page.get_output_text() == "Button was clicked"