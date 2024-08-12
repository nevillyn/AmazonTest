from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SearchResultsPage:
    def __init__(self, driver):
        self.driver = driver

    def go_to_second_page(self):
        # 2. sayfa bağlantısının yüklenmesini bekle
        second_page_link = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "a.s-pagination-item.s-pagination-button"))
        )
        second_page_link.click()

        # 2. sayfanın tam olarak yüklendiğinden emin ol
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div.s-main-slot"))
        )

    def select_product(self, index=20):
        # Ürün resimlerinin yüklenmesini bekle
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, "s-image"))
        )
        self.driver.find_elements(By.CLASS_NAME, "s-image")[index].click()
