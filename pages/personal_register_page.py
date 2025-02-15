import random
import string
import allure
from base.base_page import Base_Page
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC


# The function generates an email
def generate_random_email():
    domain = "@gmail.com"
    username_length = random.randint(5, 10)
    username = ''.join(random.choice(string.ascii_lowercase) for _ in range(username_length))
    return username + domain


random_email = generate_random_email()


# The function generates a name
def generate_name():
    first_name = ['Alice', 'Bob', 'Charlie', 'Мила', 'Настя', 'Сергей', 'Владимир', 'Марк', 'Leon', 'Stepa', 'Noy']
    return random.choice(first_name)


# The function generates a last name
def generate_last_name():
    last_name = ['Smith', 'Johnson', 'Williams', 'Йовович', 'Петрова', 'Иванов', 'Ноболевский', 'Varlamov', 'Сироткин',
                 'Обухов', 'Гаязов']
    return random.choice(last_name)


# In the class that registers the user, we link to the start page, we have painted locators
class PersonalRegisterPage(Base_Page):

    PAGE_URL = Links.PERSONAL_REGISTER_PAGE

    LOGIN_FIELD = ("xpath", "//input[@name='REGISTER[LOGIN]']")
    ADDRESS_EMAIL = ("xpath", "//input[@name='REGISTER[EMAIL]']")
    PASSWORD_FIELD = ("xpath", "//input[@class='bx-auth-input form-control']")
    PASSWORD_CONFIRM = ("xpath", "(//input[@class='form-control'])[3]")
    REGISTER_NAME = ("xpath", "//input[@name='REGISTER[NAME]']")
    REGISTER_LAST_NAME = ("xpath", "//input[@name='REGISTER[LAST_NAME]']")
    CHECKBOX = ("xpath", "//input[@type='checkbox']")
    REGISTER_SUBMIT_BUTTON = ("xpath", "//input[@name='register_submit_button']")


    @allure.step("Enter login field")
    def enter_login_field(self):
        login_field = self.wait.until(EC.element_to_be_clickable(self.LOGIN_FIELD))
        login_field.send_keys(f"User {random.randint(1, 100)}")

    # The user enters a random email
    @allure.step("Enter address email")
    def enter_address_email(self):
        address_email = self.wait.until(EC.element_to_be_clickable(self.ADDRESS_EMAIL))
        address_email.send_keys(random_email)

    # The user enters a random password and repeats entering the password
    @allure.step("Enter password field")
    def enter_password_field(self):
        password_field = self.wait.until(EC.element_to_be_clickable(self.PASSWORD_FIELD))
        password_field.send_keys(f"Test {random.randint(1, 100)}")
        password_field_value = password_field.get_attribute("value")
        password_confirm = self.wait.until(EC.element_to_be_clickable(self.PASSWORD_CONFIRM))
        password_confirm.send_keys(password_field_value)

    # The user enters a random name
    @allure.step("Enter register name")
    def enter_register_name(self):
        register_name = self.wait.until(EC.element_to_be_clickable(self.REGISTER_NAME))
        register_name.send_keys(generate_name())

    # The user enters a random last name
    @allure.step("Enter register last name")
    def enter_register_last_name(self):
        register_last_name = self.wait.until(EC.element_to_be_clickable(self.REGISTER_LAST_NAME))
        register_last_name.send_keys(generate_last_name())

    # Clicks the checkbox and checks that it has been entered
    @allure.step("Enter checkbox")
    def enter_checkbox(self):
        checkbox = self.wait.until(EC.visibility_of_element_located(self.CHECKBOX))
        checkbox.click()
        assert checkbox.get_attribute("checked") == "true"

    @allure.step("Enter register submit button")
    def enter_register_submit_button(self):
        register_submit_button = self.wait.until(EC.element_to_be_clickable(self.REGISTER_SUBMIT_BUTTON))
        register_submit_button.click()
