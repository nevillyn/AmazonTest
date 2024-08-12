from selenium.webdriver.common.by import By


class HomePage:
    def __init__(self, driver):
        self.driver = driver

    def accept_cookies(self):
        self.driver.find_element(By.ID, 'sp-cc-accept').click()

    def search(self, query):
        search_box = self.driver.find_element(By.ID, 'twotabsearchtextbox')
        search_box.send_keys(query)
        search_box.submit()

    def navigate_to_home(self):
        self.driver.find_element(By.ID, 'nav-logo-sprites').click()
