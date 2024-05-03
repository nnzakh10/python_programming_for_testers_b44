# -*- coding: utf-8 -*-
import pytest

from contact import Contact
from application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_create_new_contact(app):
    app.open_home_page()
    app.login("admin", "secret")

    app.open_add_new_page()

    app.create_new_contact(Contact(
        "Иван",
        "Иванович",
        "Иванов",
        "Ivan",
        "Иванов ИИ",
        "test_company",
        "test_address",
        "5555-55-555",
        "+1 (555) 555 55 55",
        "5555-55-555",
        "5555-55-555",
        "test@mail.ru",
        "test1@mail.ru",
        "test2@mail.ru",
        "http://localhost/",
        "1",
        "January",
        "1990",
        "1",
        "January",
        "2020"))

    app.logout()
