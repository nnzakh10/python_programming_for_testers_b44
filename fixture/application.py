from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

from fixture.contact import ContactHelper
from fixture.goup import GroupHelper
from fixture.session import SessionHelper


class Application:
    def __init__(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(30)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)

    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")

    def destroy(self):
        self.wd.quit()

    def open_add_new_page(self):
        wd = self.wd
        wd.find_element(By.LINK_TEXT, "add new").click()
