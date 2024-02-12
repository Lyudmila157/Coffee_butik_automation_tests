import allure
from base.base_page import Base_Page
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC


class IncorrectPage(Base_Page):

    PAGE_URL = Links.AUTHORIZATION_PAGE

    EMAIL_BUTTON = ("xpath", "(//input[contains(@class,'bx-auth-input')])[1]")
    PASSWORD_BUTTON = ("xpath", "(//input[contains(@class,'bx-auth-input')])[2]")
    ENTER_BUTTON = ("xpath", "//input[@name='Login']")
    INCORRECT_ELEMENT = ("xpath", "//font[@class='errortext']")

    @allure.step("Enter email")
    def enter_valid_email(self, login):
        self.wait.until(EC.element_to_be_clickable(self.EMAIL_BUTTON)).send_keys(login)

    @allure.step("Enter password")
    def enter_incorrect_password(self, password):
        self.wait.until(EC.element_to_be_clickable(self.PASSWORD_BUTTON)).send_keys(password)

    @allure.step("Click enter button")
    def click_enter_button(self):
        self.wait.until(EC.element_to_be_clickable(self.ENTER_BUTTON)).click()

    @allure.step("There is an inscription incorrect password")
    def the_inscription_incorrect_password(self):
        self.wait.until(EC.element_to_be_clickable(self.INCORRECT_ELEMENT))


