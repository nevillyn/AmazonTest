import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pages.home_page import HomePage
from pages.search_page import SearchResultsPage
from pages.product_page import ProductPage
from pages.cart_page import CartPage

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.amazon.com.tr/")
driver.maximize_window()

home_page = HomePage(driver)
time.sleep(0.5)
home_page.accept_cookies()
home_page.search('Samsung')

search_results_page = SearchResultsPage(driver)
search_results_page.go_to_second_page()
time.sleep(1)
search_results_page.select_product()

product_page = ProductPage(driver)
product_page.add_to_cart()

cart_page = CartPage(driver)
cart_page.go_to_cart()
cart_page.verify_cart_page()

home_page.navigate_to_home()
driver.quit()
