from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from .session import SessionHelper


class Application:

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(60)
        self.session = SessionHelper(self)


    def destroy (self):
        self.driver.quit()
