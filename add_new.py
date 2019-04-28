# -*- coding: utf-8 -*-
import pytest
from address import Address
from application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_new(app):
    app.login(username="admin", password="secret")
    app.create_address(Address(firstname='mik', lastname='mikh', nickname='mukmany'))
    app.logout()