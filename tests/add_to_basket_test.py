import allure
import pytest
from base.base_test import BaseTest
import time


@allure.feature("Adding a product to basket")
class TestAddToBasket(BaseTest):

    @allure.title("Add to Basket")
    @allure.severity("Critical")
    @pytest.mark.smoke
    def test_add_to_basket(self):
        self.add_to_basket_page.open()
        self.add_to_basket_page.enter_menu()
        self.add_to_basket_page.enter_catalog()
        self.add_to_basket_page.enter_coffee_machine_menu()
        self.add_to_basket_page.enter_type()
        self.add_to_basket_page.new_page()
        self.add_to_basket_page.busket_button()
        self.add_to_basket_page.choose_a_coffee_maker()
        self.add_to_basket_page.product()
        self.add_to_basket_page.product_in_busket()
