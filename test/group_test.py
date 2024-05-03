# -*- coding: utf-8 -*-
import pytest
from model.group import Group
from fixture.application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_group(app):
    app.open_home_page()
    app.session.login("admin", "secret")
    app.group.open_group_page()
    app.group.create(Group("test_name", "test_header", "test_footer"))
    app.group.return_to_groups_page()
    app.session.logout()


def test_add_empty_group(app):
    app.open_home_page()
    app.session.login("admin", "secret")
    app.group.open_group_page()
    app.group.create(Group("", "", ""))
    app.group.return_to_groups_page()
    app.session.logout()
