from fixture.session import SessionHelper


class GroupHelper:
    def __init__(self, app):
        self.session = SessionHelper(self)
        self.app = app

    def open_group_page(self):
        wd = self.app.wd
        # открытие страницы со списком групп
        wd.find_element_by_link_text("groups").click()

    def create(self, group):
        wd = self.app.wd
        self.open_group_page()
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

    def retern_to_groups_page(self):
        wd = self.app.wd
        # возвращение на страницу со списком групп
        wd.find_element_by_link_text("group page").click()