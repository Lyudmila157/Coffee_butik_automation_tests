import pytest
from config.data import Data
from pages.authorization_page import AuthorizationPage
from pages.personal_register_page import PersonalRegisterPage
from pages.incorrect_authorization_page import IncorrectPage
from pages.add_to_basket_page import AddToBasketPage
from pages.delete_an_item_page import DeleteAnItem
from pages.changing_the_date_page import ChangingDate


class BaseTest:
    data = Data

    authorization_page: AuthorizationPage
    personal_register_page: PersonalRegisterPage
    incorrect_authorization_page: IncorrectPage
    add_to_basket_page: AddToBasketPage
    delete_an_item_page: DeleteAnItem
    changing_the_date_page: ChangingDate

    @pytest.fixture(autouse=True)
    def setup(self, request, driver):
        request.cls.driver = driver
        request.cls.data = Data()
        request.cls.authorization_page = AuthorizationPage(driver)
        request.cls.personal_register_page = PersonalRegisterPage(driver)
        request.cls.incorrect_authorization_page = IncorrectPage(driver)
        request.cls.add_to_basket_page = AddToBasketPage(driver)
        request.cls.delete_an_item_page = DeleteAnItem(driver)
        request.cls.changing_the_date_page = ChangingDate(driver)
