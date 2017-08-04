# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class Toastertest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://localhost:8000/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_toaster(self):
        driver = self.driver
        driver.get(self.base_url + "/toastergui/landing/")
        driver.find_element_by_id("new-project-button").click()
        driver.find_element_by_link_text("Toaster").click()
        driver.find_element_by_id("new-project-button").click()
        driver.find_element_by_id("new-project-button").click()
        driver.find_element_by_link_text("Log in to the Django administration interface").click()
        driver.find_element_by_link_text("documentation about configuring releases").click()
        driver.find_element_by_xpath("//input[@value='Create project']").click()
        driver.find_element_by_xpath("(//input[@type='text'])[3]").clear()
        driver.find_element_by_xpath("(//input[@type='text'])[3]").send_keys("core-image")
        driver.find_element_by_link_text("core-image-minimal [openembedded-core | master]").click()
        driver.find_element_by_css_selector("div.input-append.controls > #build-button").click()
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException, e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException, e: return False
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

if __name__ == "__main__":
    unittest.main()
