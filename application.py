from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


class Application:

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(60)

    def login(self, group):
    self.driver.get("https://platform.today/en/casino/list/all-providers/all-games")
    self.driver.set_window_size(1920, 988)
    self.driver.execute_script("window.scrollTo(0,0)")
    self.driver.find_element(By.CSS_SELECTOR, ".btn-signin .auth-controls__title").click()
    self.driver.find_element(By.CSS_SELECTOR, ".user-credentials-form__item:nth-child(1) .ng-untouched").click()
    self.driver.find_element(By.CSS_SELECTOR, ".ng-valid").send_keys(username)
    self.driver.find_element(By.CSS_SELECTOR, ".sign-in__with-footer").click()
    self.driver.find_element(By.CSS_SELECTOR, ".ng-untouched").click()
    self.driver.find_element(By.CSS_SELECTOR, ".ng-untouched").send_keys(password)
    self.driver.find_element(By.CSS_SELECTOR, ".sign-in__with-footer").click()
    self.driver.find_element(By.CSS_SELECTOR, ".ng-star-inserted > .btn__title").click()

    def destroy (self):
        self.driver.quit()
