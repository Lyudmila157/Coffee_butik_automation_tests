import allure
from base.base_page import Base_Page
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC

class AddToBasketPage(Base_Page):
    PAGE_URL = Links.BASKET_PAGE

    MENU = ("xpath", "//button[@class='n-header-menu-btn js-sm-menu']")
    CATALOG = ("xpath", "//li[@class='has-submenu js-sm-menu-screen']")
    COFFEE_MACHIN_MENU = ("xpath", "//li[@class='has-submenu js-has-submenu']")
    TYPE = ("xpath", "(//li/div[@class='sm-menu__collapse js-collapse'])[2]")
    CHOOSE_A_COFFEE_MAKER = ("xpath", "(//div[@class='catalogItem__name bx_catalog_item_title'])[2]")
    PRODUCT = ("xpath", "//span[@id='mobile_item_quantity']")
    PRODUCT_IN_BUSKET = ("xpath", "//h2[@class='bx_ordercart_itemtitle']")
    BUCKET_BUTTON = ("xpath", "(//*[@title=\"Френч-пресс Bialetti Signature на 8 чашек (1 л)\"])[2]")
    BUY_BUTTON = ("xpath", "//a[@id='bx_117848907_207209_add_basket_link']")
    BASKET = ("xpath", "//*[contains(@class, 'bx_medium') and contains(@class, 'bx_bt_button')])[18]")
    BASKET_ITEM = ("xpath", "//*[@class='bx_ordercart_photo']")


    @allure.step("Enter menu")
    def enter_menu(self):
        self.wait.until(EC.element_to_be_clickable(self.MENU)).click()

    @allure.step("Enter catalog")
    def enter_catalog(self):
        self.wait.until(EC.element_to_be_clickable(self.CATALOG)).click()

    @allure.step("Enter coffee machine menu")
    def enter_coffee_machine_menu(self):
        self.wait.until(EC.element_to_be_clickable(self.COFFEE_MACHIN_MENU)).click()

    @allure.step("Enter type")
    def enter_type(self):
        self.wait.until(EC.element_to_be_clickable(self.TYPE)).click()

    @allure.step("New_page")
    def new_page(self):
        self.driver.get("https://kazan.coffee-butik.ru/katalog/kofemashiny/bialetti/")

    @allure.step("Busket button")
    def busket_button(self):
        self.wait.until(EC.element_to_be_clickable(self.BUCKET_BUTTON)).click()

    @allure.step("Buy_button")
    def buy_button(self):
        self.wait.until((EC.element_to_be_clickable(self.BUY_BUTTON))).click()

    @allure.step("Choose a basket")
    def choose_a_basket(self):
        self.wait.until(EC.element_to_be_clickable(self.BASKET)).click()

    @allure.step("Product")
    def product(self):
        self.wait.until(EC.element_to_be_clickable(self.PRODUCT)).click()

    @allure.step("Product in busket")
    def product_in_basket(self):
        self.wait.until(EC.presence_of_element_located(self.BASKET_ITEM))




