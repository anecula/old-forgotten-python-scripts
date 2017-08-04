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

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from xml.dom import minidom
from lxml import etree
import xml.etree.ElementTree as ET

import os, sys
import logging


max_depth = 5

# add lib directory into PATH soon

import loginclassUsers

from loginclassUsers import Auto as myclasstoextend


class questions(loginclassUsers.Auto):
    def test_sort(self):

        self.claslog = myclasstoextend.test_login(self)
        driver = self.driver
        time.sleep(1)
        driver.find_element_by_class_name("dropdown-toggle").click()
        driver.find_element_by_link_text("Questions").click()

        Select(driver.find_element_by_id("Intrebare_idSeniority")).select_by_visible_text("Senior")
        time.sleep(3)
        #select2-result-label-86
        #select2-result-label-108
        Select(driver.find_element_by_id("Intrebare_idPosition")).select_by_visible_text("QA")

        time.sleep(3)

        driver.find_element_by_id("Intrebare_titlu").send_keys("IntrebareQA")
        time.sleep(3)
        driver.find_element_by_name("submit").click()
        time.sleep(3)
        driver.find_element_by_xpath("/html/body/div/form/div[3]/div[3]/div/div[1]/input").send_keys("Level 1")
        time.sleep(3)
        driver.find_element_by_xpath("/html/body/div/form/div[3]/div[3]/div/div[1]/input").send_keys(Keys.RETURN)
        time.sleep(3)
        #removeFields btn btn-danger btn-xs
        driver.find_element_by_xpath("/html/body/div/form/div[4]/input").click()
        time.sleep(6)
        driver.find_element_by_xpath("/html/body/div/div[2]/table/thead/tr[2]/td[2]/div/input").send_keys("IntrebareQA")
        time.sleep(3)
        driver.find_element_by_xpath("/html/body/div/div[2]/table/thead/tr[2]/td[2]/div/input").send_keys(Keys.RETURN)
        time.sleep(3)
        driver.find_element_by_xpath("/html/body/div/div[2]/table/tbody/tr/td[6]/a[3]/i").click()
        time.sleep(10)


        self.assertRegexpMatches(self.close_alert_and_get_its_text(),
                                 r"^Are you sure you want to delete this competence [\s\S]*$")

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException, e:
            return False
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
        finally:
            self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()
