# -*- coding: utf-8 -*-

from selenium.webdriver.firefox.webdriver import WebDriver
import unittest
from model.group import Group


class test_add_group(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver(capabilities={"marionette": False})
        self.wd.implicitly_wait(60)


    def test_test_add_group(self):
        wd = self.wd
        self.login(wd, user="admin", password="secret")
        self.create_group(wd, Group(name="anak", header="vbcjd", footer="djvnm"))
        self.retern_to_groups_page(wd)
        self.logout(wd)

    def retern_to_groups_page(self, wd):
        wd = self.wd
        # возвращение на страницу со списком групп
        wd.find_element_by_link_text("group page").click()

    def logout(self, wd):
        wd = self.wd
        # выход из аккаунта
        wd.find_element_by_link_text("Logout").click()

    def create_group(self, wd, group):
        wd = self.wd
        self.open_group_page(wd)
        # создание группы
        wd.find_element_by_name("new").click()
        # открытие формы
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footer)
        # клик по созданию
        wd.find_element_by_name("submit").click()

    def open_group_page(self, wd):
        wd = self.wd
        # открытие страницы со списком групп
        wd.find_element_by_link_text("groups").click()

    def login(self, wd, user, password):
        wd = self.wd
        self.open_home_page(wd)
        # логин
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(user)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys("%s" % password)
        wd.find_element_by_css_selector("input[type=\"submit\"]").click()

    def open_home_page(self, wd):
        wd = self.wd
        # открытие главной станицы
        wd.get("http://localhost/addressbook/")

    def tearDown(self):
        self.wd.quit()


if __name__ == '__main__':
    unittest.main()