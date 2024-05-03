# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app):
    app.open_home_page()
    app.session.login("admin", "secret")
    app.group.create(Group("test_name", "test_header", "test_footer"))
    app.session.logout()


def test_add_empty_group(app):
    app.open_home_page()
    app.session.login("admin", "secret")
    app.group.create(Group("", "", ""))
    app.session.logout()
