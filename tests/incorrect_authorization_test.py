import allure
import pytest
from base.base_test import BaseTest


@allure.feature("Personal incorrect authorization page")
class TestIncorrectProfile(BaseTest):

    @allure.title("Incorrect authorization")
    @allure.severity("Critical")
    @pytest.mark.smoke
    def test_incorrect_authorization_page(self):
        self.incorrect_authorization_page.open()
        self.incorrect_authorization_page.enter_valid_email(self.data.LOGIN)
        self.incorrect_authorization_page.enter_incorrect_password(self.data.PASSWORD_TWO)
        self.incorrect_authorization_page.click_enter_button()
        self.incorrect_authorization_page.the_inscription_incorrect_password()

