import allure
from base.base_page import Base_Page
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC
import random


def generate_last_name():
    last_name = ['Valiev', 'Korchagin', 'Dack', 'Bad', 'Петров', 'Ивановa', 'Соболевский', 'Сидоров', 'Сиротина',
                 'Лебедева', 'Гаязова']
    return random.choice(last_name)


class ChangingDate(Base_Page):
    PAGE_URL = Links.CHANGING_DATE

    EMAIL_BUTTON = ("xpath", "(//input[contains(@class,'bx-auth-input')])[1]")
    PASSWORD_BUTTON = ("xpath", "(//input[contains(@class,'bx-auth-input')])[2]")
    ENTER_BUTTON = ("xpath", "//input[@name='Login']")
    PATRONYMIC_BUTTON = ("xpath", "//input[@name='SECOND_NAME']")
    LAST_NAME_LINE = ("xpath", "//input[@name='LAST_NAME']")
    RADIO_BUTTON = ("xpath", "(//input[@type='radio'])[4]")
    RADIO_BUTTON_ANOTHER = ("xpath", "(//input[@type='radio'])[3]")
    CHECKBOX = ("xpath", "(//input[@type='checkbox'])[1]")
    SAVE_BUTTON = ("xpath", "//input[@id='user_save_all']")
    INFO = ("xpath", "//p/font[@class='notetext']")

    @allure.step("Enter email")
    def enter_email(self, login):
        self.wait.until(EC.element_to_be_clickable(self.EMAIL_BUTTON)).send_keys(login)

    @allure.step("Enter password")
    def enter_password(self, password):
        self.wait.until(EC.element_to_be_clickable(self.PASSWORD_BUTTON)).send_keys(password)

    @allure.step("Click enter button")
    def click_enter_button(self):
        self.wait.until(EC.element_to_be_clickable(self.ENTER_BUTTON)).click()

    def page_authorisation_open(self):
        self.wait.until(EC.element_to_be_clickable(self.PATRONYMIC_BUTTON))

    @allure.step("Clear last name")
    def clear_last_name(self):
        self.wait.until(EC.element_to_be_clickable(self.LAST_NAME_LINE)).clear()

    @allure.step("Changing last name")
    def changing_last_name(self):
        self.wait.until(EC.element_to_be_clickable(self.LAST_NAME_LINE)).send_keys(generate_last_name())

    @allure.step("Click radio button")
    def click_radio_button(self):
        radio_button = self.wait.until(EC.element_to_be_clickable(self.RADIO_BUTTON))
        radio_button_another = self.wait.until(EC.element_to_be_clickable(self.RADIO_BUTTON_ANOTHER))
        if radio_button.get_attribute("checked") == "true":
            radio_button_another.click()
        else:
            radio_button.click()

    @allure.step("Checkbox")
    def checkbox(self):
        checkbox = self.wait.until(EC.visibility_of_element_located(self.CHECKBOX))
        if checkbox.get_attribute("checked") == "none":
            checkbox.click()
        else:
            pass

    # @allure.step("Checkbox")
    # def checkbox(self):
    #     checkbox = self.wait.until(EC.visibility_of_element_located(self.CHECKBOX))
    #     if checkbox.is_selected():
    #         checkbox.click()
    #     else:
    #         pass

    @allure.step("Save button")
    def save_button(self):
        self.wait.until(EC.element_to_be_clickable(self.SAVE_BUTTON)).click()

    @allure.step("Info")
    def info(self):
        self.wait.until(EC.element_to_be_clickable(self.INFO))