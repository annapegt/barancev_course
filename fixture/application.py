from selenium import webdriver
from fixture.session import SessionHelper


class Application:

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(60)
        self.session = SessionHelper(self)  # helper receives a link to fixture

    def destroy(self):
        self.driver.quit()
