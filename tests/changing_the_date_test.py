import allure
import pytest
from base.base_test import BaseTest


@allure.feature("Checking the date test")
class TestCheckingDate(BaseTest):

    @allure.title("Checking the date test")
    @allure.severity("Critical")
    @pytest.mark.smoke
    def test_authorization_page(self):
        self.changing_the_date_page.open()
        self.changing_the_date_page.enter_email(self.data.LOGIN)
        self.changing_the_date_page.enter_password(self.data.PASSWORD)
        self.changing_the_date_page.click_enter_button()
        self.changing_the_date_page.page_authorisation_open()
        self.changing_the_date_page.clear_last_name()
        self.changing_the_date_page.changing_last_name()
        self.changing_the_date_page.click_radio_button()
        self.changing_the_date_page.checkbox()
        self.changing_the_date_page.save_button()
        self.changing_the_date_page.info()

