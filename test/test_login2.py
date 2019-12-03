# Generated by Selenium IDE
import pytest
from model.group import Group
from fixture.application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_login(app):
    app.session.login(Group (username="annaTest50", password="annaTest50"))
    app.session.logout()

def logout(app):
    app.sesssion.driver.execute_script("window.scrollTo(0,0)")
    app.session.driver.find_element(By.CSS_SELECTOR, ".client-section-menu__caret-down-icon > .icons-font-caret-down").click()
    app.session.driver.find_element(By.CSS_SELECTOR, ".btn-signout__title").click()



  
