from model.group import Group
# test_login and logout methods takes fixture as parameter


def test_login(app):
    app.session.login(Group(username="annaTest50", password="annaTest50"))
    app.session.logout()






