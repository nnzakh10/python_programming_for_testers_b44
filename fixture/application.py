from selenium.webdriver.chrome.webdriver import WebDriver

from fixture.contact import ContactHelper
from fixture.goup import GroupHelper
from fixture.session import SessionHelper


class Application:
    def __init__(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(5)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")

    def accept_alert(self):
        wd = self.wd

        try:
            wd.switch_to.alert.accept()
            return True
        except:
            return False

    def destroy(self):
        self.wd.quit()
