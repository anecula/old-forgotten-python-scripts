#!/usr/bin/python
# import webdriver
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException, NoAlertPresentException
import unittest, time, re

from xml.dom import minidom
from lxml import etree
import xml.etree.ElementTree as ET

import os, sys
import logging


max_depth = 5

# add lib directory into PATH soon

import loginclassUsers

from loginclassUsers import Auto as myclasstoextend


class new_app(loginclassUsers.Auto):
    def test_sort(self):

        self.claslog = myclasstoextend.test_login(self)
        driver = self.driver

        driver.find_element_by_class_name("dropdown-toggle").click()
        driver.find_element_by_link_text("Users").click()
        driver.find_element_by_link_text("Client").click()

        driver.find_element_by_id("usersGrid_c0").click()
        time.sleep(5)
        driver.find_element_by_id("usersGrid_c1").click()
        time.sleep(5)
        driver.find_element_by_id("usersGrid_c2").click()
        time.sleep(5)
        driver.find_element_by_id("usersGrid_c3").click()
        time.sleep(5)
        driver.find_element_by_id("usersGrid_c4").click()
        time.sleep(5)
        driver.find_element_by_id("usersGrid_c5").click()
        time.sleep(5)
        driver.find_element_by_id("usersGrid_c6").click()
        time.sleep(5)
        driver.find_element_by_id("usersGrid_c7").click()
        time.sleep(5)
        driver.find_element_by_id("usersGrid_c8").click()
        time.sleep(5)

        # driver.find_element_by_id("usersGrid_c9").click()


    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException, e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.driver.switch_to_alert()
        except NoAlertPresentException, e:
            return False
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
        finally:
            self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()