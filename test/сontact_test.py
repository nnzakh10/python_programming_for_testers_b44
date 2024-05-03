# -*- coding: utf-8 -*-
from model.contact import Contact


def test_create_new_contact(app):
    app.open_home_page()
    app.session.login("admin", "secret")

    app.contact.create(Contact(
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

    app.session.logout()
