import allure
import pytest
from base.base_test import BaseTest


@allure.feature("Personal authorization page")
class TestAuthorizationProfile(BaseTest):

    @allure.title("Authorization")
    @allure.severity("Critical")
    @pytest.mark.smoke
    def test_authorization_page(self):
        self.authorization_page.open()
        self.authorization_page.enter_email(self.data.LOGIN)
        self.authorization_page.enter_password(self.data.PASSWORD)
        self.authorization_page.click_enter_button()
        self.authorization_page.page_authorisation_open()
