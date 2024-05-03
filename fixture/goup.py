from selenium.webdriver.common.by import By


class GroupHelper:

    def __init__(self, app):
        self.app = app

    def return_to_groups_page(self):
        wd = self.app.wd
        wd.find_element(By.LINK_TEXT, "group page").click()

    def create(self, group):
        wd = self.app.wd
        self.open_group_page()
        # init group creation
        wd.find_element(By.NAME, "new").click()

        # fill group form
        self.fill_form(group)

        # submit group creation
        wd.find_element(By.NAME, "submit").click()
        self.return_to_groups_page()

    def edit_first(self, group):
        wd = self.app.wd
        self.open_group_page()

        # select first group
        wd.find_element(By.NAME, "selected[]").click()

        self.open_edit_page()
        self.fill_form(group)
        wd.find_element(By.NAME, "update").click()
        self.return_to_groups_page()

    def delete_first(self):
        wd = self.app.wd
        self.open_group_page()

        # select first group
        wd.find_element(By.NAME, "selected[]").click()

        # submit deletion
        wd.find_element(By.NAME, "delete").click()
        self.return_to_groups_page()

    def open_group_page(self):
        wd = self.app.wd
        wd.find_element(By.LINK_TEXT, "groups").click()

    def open_edit_page(self):
        wd = self.app.wd
        wd.find_element(By.NAME, "edit").click()

    def fill_form(self, group):
        wd = self.app.wd

        wd.find_element(By.NAME, "group_name").click()
        wd.find_element(By.NAME, "group_name").clear()
        wd.find_element(By.NAME, "group_name").send_keys(group.name)
        wd.find_element(By.NAME, "group_header").click()
        wd.find_element(By.NAME, "group_header").clear()
        wd.find_element(By.NAME, "group_header").send_keys(group.header)
        wd.find_element(By.NAME, "group_footer").click()
        wd.find_element(By.NAME, "group_footer").clear()
        wd.find_element(By.NAME, "group_footer").send_keys(group.footer)
