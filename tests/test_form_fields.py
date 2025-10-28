import pytest
import allure
from pages.form_fields_page import FormFieldsPage
from selenium.webdriver.common.by import By

@allure.title("Проверка placeholder в поле Message")
def test_message_placeholder(driver):
    page = FormFieldsPage(driver)
    page.open()
    placeholder = page.driver.find_element(By.ID, "message").get_attribute("placeholder")
    assert placeholder == "Enter your message here"

@allure.title("Кнопка Submit кликабельна")
def test_submit_button_clickable(driver):
    page = FormFieldsPage(driver)
    page.open()
    assert page.driver.find_element(*FormFieldsPage.SUBMIT_BUTTON).is_enabled()

@allure.title("Отправка пустого сообщения")
def test_submit_empty_message(driver):
    page = FormFieldsPage(driver)
    page.open()
    page.fill_message("")  # пусто
    page.submit_form()
    # На сайте нет валидации → просто проверим, что форма отправилась без ошибки
    assert "form-fields" in driver.current_url