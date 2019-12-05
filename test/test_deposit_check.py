from model.group import Group


def test_deposit_check(app):
    app.session.login(Group(username="annaTest50", password="annaTest50"))
    app.session.deposit_check()
    app.session.logout()
