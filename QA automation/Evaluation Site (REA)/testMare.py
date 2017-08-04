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


class fulltest(loginclassUsers.Auto):
    def test_sort(self):

        self.claslog = myclasstoextend.test_login(self)
        driver = self.driver
        time.sleep(1)


        driver.find_element_by_class_name("dropdown-toggle").click()
        time.sleep(3)
        driver.find_element_by_link_text("Evaluation Periods").click()
        driver.find_element_by_id("EvaluationPeriod_nume").clear()
        driver.find_element_by_id("EvaluationPeriod_nume").send_keys("formularnou")
        driver.find_element_by_id("EvaluationPeriod_status").click()
        Select(driver.find_element_by_id("EvaluationPeriod_status")).select_by_visible_text("Started")
        driver.find_element_by_css_selector("td.active.day").click()
        driver.find_element_by_xpath("//div[@id='sizzle-1422620064707']/div/table/tbody/tr[5]/td[6]").click()

        driver.find_element_by_class_name("dropdown-toggle").click()
        driver.find_element_by_link_text("Evaluation Periods").click()
        driver.find_element_by_id("EvaluationPeriod_nume").clear()
        driver.find_element_by_id("EvaluationPeriod_nume").send_keys("formular nou")
        driver.find_element_by_id("EvaluationPeriod_status").click()
        Select(driver.find_element_by_id("EvaluationPeriod_status")).select_by_visible_text("Started")
        driver.find_element_by_css_selector("td.active.day").click()
        driver.find_element_by_xpath("//div[@id='sizzle-1422620103530']/div/table/tbody/tr[5]/td[6]").click()

        driver.find_element_by_name("yt0").click()
        driver.find_element_by_name("yt0").click()
        driver.find_element_by_link_text("Team scores").click()
        driver.find_element_by_link_text("Completed Tasks").click()
        driver.find_element_by_link_text("Wiki").click()

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