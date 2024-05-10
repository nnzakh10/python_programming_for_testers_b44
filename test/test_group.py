# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app):
    app.group.create(baseGroup)


def test_add_empty_group(app):
    app.group.create(Group("", "", ""))


def test_edit_first_group(app):
    app.group.create(baseGroup)
    app.group.edit_first(Group("edit_name", "edit_header", "edit_footer"))


def test_delete_first_group(app):
    app.group.create(baseGroup)
    app.group.delete_first()


baseGroup = Group("test_name", "test_header", "test_footer")
