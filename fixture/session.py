from selenium.webdriver.common.by import By
from group import fixture
from group import Group
class SessionHelper:
    def __init__(self, app):
        self.app = app

    def login(self, group):
        self.driver = self.app.driver
        self.driver.get("https://platform.today/en/casino/list/all-providers/all-games")
        self.driver.set_window_size(1920, 988)
        self.driver.execute_script("window.scrollTo(0,0)")
        self.driver.find_element(By.CSS_SELECTOR, ".btn-signin .auth-controls__title").click()
        from time import sleep
        sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, ".user-credentials-form__item:nth-child(1) .ng-untouched").click()
        self.driver.find_element(By.CSS_SELECTOR, ".user-credentials-form__item:nth-child(1) .ng-untouched").send_keys(username)
        self.driver.find_element(By.CSS_SELECTOR, ".sign-in__with-footer").click()
        self.driver.find_element(By.CSS_SELECTOR, ".ng-untouched").click()
        self.driver.find_element(By.CSS_SELECTOR, ".ng-untouched").send_keys(password)
        self.driver.find_element(By.CSS_SELECTOR, ".sign-in__with-footer").click()
        self.driver.find_element(By.CSS_SELECTOR, ".ng-star-inserted > .btn__title").click()