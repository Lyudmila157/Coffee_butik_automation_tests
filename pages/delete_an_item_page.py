import allure
from base.base_page import Base_Page
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC


class DeleteAnItem(Base_Page):
    PAGE_URL = Links.DELETE_AN_ITEM_PAGE

    MENU = ("xpath", "//button[@class='n-header-menu-btn js-sm-menu']")
    CATALOG = ("xpath", "//li[@class='has-submenu js-sm-menu-screen']")
    VINE_CABINET_ONE = ("xpath", "(//div[@class='catalogItem__name bx_catalog_item_title'])[10]")
    VINE_CABINET_TWO = ("xpath", "(//div[@class='catalogItem__name bx_catalog_item_title'])[11]")
    VINE_CABINET_ONE_IN_BUSKET = ("xpath", "//a[@id='bx_3966226736_151803_buy_link']")
    VINE_CABINET_TWO_IN_BUSKET = ("xpath", "//a[@id='bx_3966226736_248739_buy_link']")
    BUCKET_BUTTON = ("xpath", "//span[@class='quantity']")
    ONCLICK_ONE = ("xpath", "(//a[@onclick='return deleteProductRow(this)'])[2]")
    ONCLICK_TWO = ("xpath", "(//a[@onclick='return deleteProductRow(this)'])[1]")
    TEXT = ("xpath", "//font[@class='errortext']")

    @allure.step("Enter menu")
    def enter_menu(self):
        self.wait.until(EC.element_to_be_clickable(self.MENU)).click()

    @allure.step("Enter catalog")
    def enter_catalog(self):
        self.wait.until(EC.element_to_be_clickable(self.CATALOG)).click()

    @allure.step("New_vine_cabinet_page")
    def new_vine_cabinet_page(self):
        self.driver.get("https://kazan.coffee-butik.ru/katalog/holodilnoe-oborudovanie/vinnye-shkafy/")

    @allure.step("Checking the cabinet one")
    def checking_the_cabinet_one(self):
        self.wait.until(EC.element_to_be_clickable(self.VINE_CABINET_ONE))

    @allure.step("Checking the cabinet two")
    def checking_the_cabinet_two(self):
        self.wait.until(EC.element_to_be_clickable(self.VINE_CABINET_TWO))

    @allure.step("Enter one cabinet one in busket")
    def one_cabinet_one_in_busket(self):
        self.wait.until(EC.element_to_be_clickable(self.VINE_CABINET_ONE_IN_BUSKET)).click()

    @allure.step("Enter one cabinet two in busket")
    def one_cabinet_two_in_busket(self):
        self.wait.until(EC.element_to_be_clickable(self.VINE_CABINET_TWO_IN_BUSKET)).click()

    @allure.step("Busket button")
    def busket_button(self):
        self.wait.until(EC.element_to_be_clickable(self.BUCKET_BUTTON)).click()

    @allure.step("Enter onclick one")
    def enter_onclick_one(self):
        self.wait.until(EC.element_to_be_clickable(self.ONCLICK_ONE)).click()

    @allure.step("Enter onclick two")
    def enter_onclick_two(self):
        self.wait.until(EC.element_to_be_clickable(self.ONCLICK_TWO)).click()

    @allure.step("Text")
    def text(self):
        self.wait.until(EC.element_to_be_clickable(self.TEXT))
