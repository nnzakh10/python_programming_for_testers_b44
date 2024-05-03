# -*- coding: utf-8 -*-
import pytest

from group import Group
from application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_group(app):
    app.open_home_page()
    app.login("admin", "secret")
    app.open_group_page()
    app.create_group(Group("test_name", "test_header", "test_footer"))
    app.return_to_groups_page()
    app.logout()


def test_add_empty_group(app):
    app.open_home_page()
    app.login("admin", "secret")
    app.open_group_page()
    app.create_group(Group("", "", ""))
    app.return_to_groups_page()
    app.logout()
