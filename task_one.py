# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest

class UntitledTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_untitled_test_case(self):
        driver = self.driver
        driver.get("https://demoqa.com/")
        driver.find_element_by_xpath("//div[h5='Forms']").click()
        driver.find_element_by_xpath("(//*[normalize-space(text()) and normalize-space(.)='Forms'])[1]/following::span[1]").click()
        driver.find_element_by_id("firstName").click()
        driver.find_element_by_id("firstName").clear()
        driver.find_element_by_id("firstName").send_keys(u"Тест")
        driver.find_element_by_xpath("//div[@id='genterWrapper']/div[2]/div/label").click()
        driver.find_element_by_id("submit").click()

    def is_element_present(self, how, what):
        try: self.driver.find_element(how, what)
        except NoSuchElementException as e: return False
        return True

    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

