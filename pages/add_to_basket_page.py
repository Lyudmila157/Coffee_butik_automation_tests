import allure
from base.base_page import Base_Page
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options

# options = Options()
# driver = webdriver.Chrome(options=options)

class AddToBasketPage(Base_Page):
    PAGE_URL = Links.BASKET_PAGE

    MENU = ("xpath", "//button[@class='n-header-menu-btn js-sm-menu']")
    CATALOG = ("xpath", "//li[@class='has-submenu js-sm-menu-screen']")
    COFFEE_MACHIN_MENU = ("xpath", "//li[@class='has-submenu js-has-submenu']")
    TYPE = ("xpath", "(//li/div[@class='sm-menu__collapse js-collapse'])[2]")
    BUCKET_BUTTON = ("xpath", "//a[@id='bx_3966226736_175891_buy_link']")
    CHOOSE_A_COFFEE_MAKER = ("xpath", "(//div[@class='catalogItem__name bx_catalog_item_title'])[2]")
    PRODUCT = ("xpath", "//span[@id='mobile_item_quantity']")
    PRODUCT_IN_BUSKET = ("xpath", "//h2[@class='bx_ordercart_itemtitle']")

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

    @allure.step("Choose a coffee maker")
    def choose_a_coffee_maker(self):
        self.wait.until(EC.element_to_be_clickable(self.CHOOSE_A_COFFEE_MAKER)).click()

    @allure.step("Product")
    def product(self):
        self.wait.until(EC.element_to_be_clickable(self.PRODUCT)).click()

    @allure.step("Product in busket")
    def product_in_busket(self):
        self.wait.until(EC.element_to_be_clickable(self.PRODUCT_IN_BUSKET))


