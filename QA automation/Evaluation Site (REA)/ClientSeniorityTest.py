__author__ = 'dev25'
# !/usr/bin/python
#import webdriver
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException, NoAlertPresentException
import unittest, time, re
from selenium.webdriver.common.keys import Keys

from xml.dom import minidom
from lxml import etree
import xml.etree.ElementTree as ET

import os, sys
import logging


max_depth = 5

# add lib directory into PATH soon

import loginclassUsers

from loginclassUsers import Auto as myclasstoextend


class ClientSeniority (loginclassUsers.Auto):
    def test_sort(self):

        self.claslog = myclasstoextend.test_login(self)
        driver = self.driver
        time.sleep(1)

        driver.find_element_by_class_name("dropdown-toggle").click()
        time.sleep(3)
        driver.find_element_by_link_text("Client Seniority").click()
        time.sleep(3)

        driver.find_element_by_id("ClientSenioritate_nume").send_keys("juniorblue")
        time.sleep(3)
        driver.find_element_by_name("submit").click()
        time.sleep(3)

        driver.find_element_by_xpath("/html/body/div/div[2]/table/thead/tr[2]/td[2]/div/input").send_keys("juniorblue")
        time.sleep(3)
        driver.find_element_by_xpath("/html/body/div/div[2]/table/thead/tr[2]/td[2]/div/input").send_keys(Keys.RETURN)

        time.sleep(3)
        driver.find_element_by_xpath("/html/body/div/div[2]/table/tbody/tr/td[3]/a[2]/i").click()
        time.sleep(3)
        self.assertRegexpMatches(self.close_alert_and_get_its_text(), r"^Are you sure you want to delete this seniority [\s\S]$")
        #driver.find_element_by_class_name("glyphicon glyphicon-trash").click()
        time.sleep(10)

    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException, e: return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return text
        finally: self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)



if __name__ == "__main__":
    unittest.main()

