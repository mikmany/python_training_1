# -*- coding: utf-8 -*-
import pytest
from address import Address
from group import Group
from application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_group(app):
    app.login(user="admin", password="secret")
    app.create_group(Group(name="anak", header="vbcjd", footer="djvnm"))
    app.retern_to_groups_page()


def test_add_new(app):
    app.login(user="admin", password="secret")
    app.create_address(Address(firstname='mik', lastname='mikh', nickname='mukmany'))
    app.logout()
