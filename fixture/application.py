from selenium.webdriver.firefox.webdriver import WebDriver
from fixture.session import SessionHelper
from fixture.group import GroupHelper


class Application:
    def __init__(self):
        self.wd = WebDriver(capabilities={"marionette": False})
        self.wd.implicitly_wait(60)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)

    def open_home_page(self):
        # открытие главной станицы
        wd = self.wd
        wd.get("http://localhost/addressbook/")

    def open_add_new(self):
        wd = self.wd
        wd.find_element_by_link_text("add new").click()

    def create_address(self, address):
        wd = self.wd
        self.open_add_new()
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(address.firstname)
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(address.lastname)
        wd.find_element_by_name("nickname").click()
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys(address.nickname)
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()

    def destroy(self):
        self.wd.quit()
