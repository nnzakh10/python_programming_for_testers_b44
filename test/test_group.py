# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app):
    app.open_home_page()
    app.session.login("admin", "secret")
    app.group.create(baseGroup)
    app.session.logout()


def test_add_empty_group(app):
    app.open_home_page()
    app.session.login("admin", "secret")
    app.group.create(Group("", "", ""))
    app.session.logout()


def test_edit_first_group(app):
    app.open_home_page()
    app.session.login("admin", "secret")
    app.group.create(baseGroup)

    app.group.edit_first(Group("edit_name", "edit_header", "edit_footer"))
    app.session.logout()


def test_delete_first_group(app):
    app.session.login("admin", "secret")
    app.group.create(baseGroup)

    app.group.delete_first()
    app.session.logout()


baseGroup = Group("test_name", "test_header", "test_footer")
