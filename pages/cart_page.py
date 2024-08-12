from selenium.webdriver.common.by import By


class CartPage:
    def __init__(self, driver):
        self.driver = driver

    def go_to_cart(self):
        self.driver.find_element(By.ID, "sw-gtc").click()

    def verify_cart_page(self):
        assert self.driver.find_element(By.ID, "sc-buy-box-ptc-button"), "Sepet sayfasına gidilemedi!"
