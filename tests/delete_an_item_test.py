import allure
import pytest
from base.base_test import BaseTest


@allure.feature("Remove an item in basket")
class TestDeleteAnItem(BaseTest):

    @allure.title("Delete an item test")
    @allure.severity("Critical")
    @pytest.mark.smoke
    def test_delete_an_item(self):
        self.delete_an_item_page.open()
        self.delete_an_item_page.enter_menu()
        self.delete_an_item_page.enter_catalog()
        self.delete_an_item_page.new_vine_cabinet_page()
        self.delete_an_item_page.checking_the_cabinet_one()
        self.delete_an_item_page.checking_the_cabinet_two()
        self.delete_an_item_page.one_cabinet_one_in_busket()
        self.delete_an_item_page.one_cabinet_two_in_busket()
        self.delete_an_item_page.busket_button()
        self.delete_an_item_page.enter_onclick_one()
        self.delete_an_item_page.enter_onclick_two()
        self.delete_an_item_page.text()




