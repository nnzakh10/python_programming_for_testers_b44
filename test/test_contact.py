# -*- coding: utf-8 -*-
from model.contact import Contact


def test_create_new_contact(app):
    app.contact.create(baseContact)


def test_create_empty_contact(app):
    app.contact.create(Contact(
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "-",
        "-",
        "",
        "-",
        "-",
        ""))


def test_edit_first_contact(app):
    app.contact.create(baseContact)
    app.contact.edit_first(Contact(
        "Петр",
        "Петрович",
        "Петров",
        "Pert",
        "Петров ПП",
        "edit_company",
        "edit_address",
        "4444-44-444",
        "+1 (444) 444 44 44",
        "4444-44-444",
        "4444-44-444",
        "edit@mail.ru",
        "edit1@mail.ru",
        "edit2@mail.ru",
        "http://localhost/edit/",
        "2",
        "February",
        "1991",
        "2",
        "February",
        "2021"))


def test_delete_first_contact(app):
    app.contact.create(baseContact)
    app.contact.delete_first()


baseContact = Contact(
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
    "2020")
