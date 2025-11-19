import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import itertools


def level1():
    massiv = [2025, 3, 11]
    full = list(itertools.permutations(massiv))
    return str(full) + f' Всего {len(full)} вариаций'


def level2():
    list = [1, 3, 6, 7, 9, 4, 10, 5, 6, 12, 2, 7, 11]
    list = sorted(list)
    count = 0
    dlina = 0
    for i in list:
        if i == 12:
            continue
        if (list[i] + 1) == list[i + 1]:
            count += 1
        else:
            if count > dlina:
                dlina = count
    return f'Максимальная длина: {dlina}'


def level3():
    s1 = "aabbdsaacc"
    s2 = "abadc"
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return f'Самая длинная последовательность: {str(dp[m][n])}'


class RegistrationPage:
    URL = "https://way2automation.com/way2auto_jquery/registration.php"
    FIRST_NAME = (By.NAME, "name")
    LAST_NAME = (By.XPATH, "//fieldset[1]/p[2]/input")
    PHONE = (By.NAME, "phone")
    USERNAME = (By.NAME, "username")
    EMAIL = (By.NAME, "email")
    PASSWORD = (By.NAME, "password")
    CONFIRM_PASSWORD = (By.NAME, "c_password")
    ABOUT_YOURSELF = (By.XPATH, "//label[text()='About Yourself']/following-sibling::textarea")

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(self.URL)
        WebDriverWait(self.driver, 15).until(
            EC.visibility_of_element_located(self.ABOUT_YOURSELF)
        )

    def fill_form(self, about_text):
        self.driver.find_element(*self.FIRST_NAME).send_keys("Kalashnikov")
        self.driver.find_element(*self.LAST_NAME).send_keys("Vyacheslav")
        self.driver.find_element(*self.PHONE).send_keys("89218293772")
        self.driver.find_element(*self.USERNAME).send_keys("slavakalashnikov")
        self.driver.find_element(*self.EMAIL).send_keys("test@example.com")
        self.driver.find_element(*self.PASSWORD).send_keys("Password123")
        self.driver.find_element(*self.CONFIRM_PASSWORD).send_keys("Password123")
        self.driver.find_element(*self.ABOUT_YOURSELF).send_keys(about_text)

    def get_about_yourself_value(self):
        return self.driver.find_element(*self.ABOUT_YOURSELF).get_attribute("value")


@pytest.fixture(scope="function")
def driver():
    options = Options()
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(options=options)
    yield driver


@allure.feature("Форма регистрации")
@allure.story("Автоматическое вычисление и ввод решений в 'About Yourself'")
def test_fill_about_yourself_with_answers(driver):
    page = RegistrationPage(driver)
    page.open()

    with allure.step("Вычисление решения задач"):
        ans1 = level1()
        ans2 = level2()
        ans3 = level3()
        full_answer = f"{ans1},{ans2},{ans3}"
        allure.attach(full_answer, name="Итоговая строка ответов", attachment_type=allure.attachment_type.TEXT)

    with allure.step("Заполнение поля 'About Yourself'"):
        page.fill_form(full_answer)

    with allure.step("Проверка корректности ввода"):
        actual = page.get_about_yourself_value()
        assert actual == full_answer, f"Ожидалось:\n{full_answer}\n\nПолучено:\n{actual}"


@allure.feature("Форма регистрации")
@allure.story("Проверка видимости всех обязательных полей")
def test_all_form_fields_are_visible(driver):
    page = RegistrationPage(driver)
    page.open()

    fields = [
        page.FIRST_NAME,
        page.LAST_NAME,
        page.PHONE,
        page.USERNAME,
        page.EMAIL,
        page.PASSWORD,
        page.CONFIRM_PASSWORD,
        page.ABOUT_YOURSELF
    ]

    for i, field in enumerate(fields, 1):
        with allure.step(f"Проверка видимости поля #{i}"):
            assert WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located(field)
            ), f"Поле {field} не отображается"
