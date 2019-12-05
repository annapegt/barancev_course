from selenium.webdriver.common.by import By
from time import sleep
# Class which helps in session login


class SessionHelper:
    def __init__(self, app):
        self.app = app

    def login(self, group):
        self.driver = self.app.driver
        self.driver.get("https://platform.today/en/casino/list/all-providers/all-games")
        self.driver.set_window_size(1920, 988)
        self.driver.execute_script("window.scrollTo(0,0)")
        self.driver.find_element(By.CSS_SELECTOR, ".btn-signin .auth-controls__title").click()
        sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, ".user-credentials-form__item:nth-child(1) .ng-untouched").click()
        self.driver.find_element(By.CSS_SELECTOR, ".user-credentials-form__item:nth-child(1) .ng-untouched").send_keys(group.username)
        self.driver.find_element(By.CSS_SELECTOR, ".sign-in__with-footer").click()
        self.driver.find_element(By.CSS_SELECTOR, ".ng-untouched").click()
        self.driver.find_element(By.CSS_SELECTOR, ".ng-untouched").send_keys(group.password)
        self.driver.find_element(By.CSS_SELECTOR, ".sign-in__with-footer").click()
        self.driver.find_element(By.CSS_SELECTOR, ".ng-star-inserted > .btn__title").click()
        sleep(2)

    def logout(self):
        driver = self.driver
        driver.execute_script("window.scrollTo(0,0)")
        driver.find_element(By.CSS_SELECTOR, ".client-section-menu__caret-down-icon > .icons-font-caret-down").click()
        sleep(1)
        driver.find_element(By.CSS_SELECTOR, ".btn-signout__title").click()

    def deposit_check(self):
        driver = self.driver
        driver.execute_script("window.scrollTo(0,0)")
        sleep(1)
        balance = driver.find_element(By.CSS_SELECTOR, ".balance__amount")
        sleep(1)
        assert balance.text == "4853.93"



