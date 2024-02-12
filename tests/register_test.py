import allure
import pytest
from base.base_test import BaseTest


# User registration test
@allure.feature("Personal register profile")
class TestRegisterProfile(BaseTest):

    @allure.title("Register")
    @allure.severity("Critical")
    @pytest.mark.smoke
    def test_personal_register_test(self):
        self.personal_register_page.open()
        self.personal_register_page.enter_login_field()
        self.personal_register_page.enter_address_email()
        self.personal_register_page.enter_password_field()
        self.personal_register_page.enter_register_name()
        self.personal_register_page.enter_register_last_name()
        self.personal_register_page.enter_checkbox()
        self.personal_register_page.enter_register_submit_button()
