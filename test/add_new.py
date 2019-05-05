# -*- coding: utf-8 -*-
import pytest
from model.address import Address
from model.group import Group
from fixture.application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_group(app):
    app.sesion.login(user="admin", password="secret")
    app.group.create(Group(name="anak", header="vbcjd", footer="djvnm"))
    app.retern_to_groups_page()
    app.session.logout()


def test_add_new(app):
    app.session.login(user="admin", password="secret")
    app.create_address(Address(firstname='mik', lastname='mikh', nickname='mukmany'))
    app.session.logout()
