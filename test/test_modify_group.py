# -*- coding: utf-8 -*-
from model.group import Group
from test.test_group import baseGroup


def test_modify_group_name(app):
    if app.group.count() == 0:
        app.group.create(baseGroup)
    app.group.modify_first(Group(name="New group"))


def test_modify_group_header(app):
    if app.group.count() == 0:
        app.group.create(baseGroup)
    app.group.modify_first(Group(header="New header"))
