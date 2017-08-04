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


class Form (loginclassUsers.Auto):
    def test_sort(self):

        self.claslog = myclasstoextend.test_login(self)
        driver = self.driver
        time.sleep(1)

        driver.find_element_by_class_name("dropdown-toggle").click()
        time.sleep(3)
        driver.find_element_by_link_text("Forms").click()
        time.sleep(3)

        driver.find_element_by_id("Form_nume").send_keys("Form_Test")
        time.sleep(3)
        driver.find_element_by_xpath("/html/body/div/form/div[3]/div[1]/div[2]/div[1]").click()
        time.sleep(3)
        driver.find_element_by_xpath("/html/body/div/form/div[3]/div[1]/div[2]/select/option[2]").click()
        time.sleep(3)
        driver.find_element_by_xpath("/html/body/div[1]/form/div[3]/div[1]/div[3]/div[1]").click()
        time.sleep(3)
        driver.find_element_by_xpath("/html/body/div[1]/form/div[3]/div[1]/div[3]/select/option[2]").click()
        time.sleep(3)
        driver.find_element_by_xpath("/html/body/div[1]/form/div[3]/div[1]/div[4]/div[1]").click()
        time.sleep(3)
        driver.find_element_by_xpath("/html/body/div[1]/form/div[3]/div[1]/div[4]/div[1]/select/option[4]").click()
        time.sleep(3)
        driver.find_element_by_xpath("/html/body/div[1]/form/div[3]/div[1]/div[5]/label").click()
        time.sleep(3)

        driver.find_element_by_xpath("/html/body/div[1]/form/div[3]/div[1]/div[5]/div[1]").click()
        time.sleep(3)
        driver.find_element_by_xpath("/html/body/div[1]/form/div[3]/div[1]/div[5]/div[1]/select/option[2]").click()
        time.sleep(3)

        driver.find_element_by_xpath("/html/body/div[1]/form/div[3]/div[2]/div[4]/label/input").click()
        time.sleep(3)
        driver.find_element_by_xpath("/html/body/div[1]/form/input").click()
        time.sleep(3)


        Select(driver.find_element_by_css_selector("div.filter-container > #Form_tip")).select_by_visible_text(
            "Self Evaluation")
        time.sleep(3)
        Select(driver.find_element_by_css_selector("div.filter-container > #Form_tip")).select_by_visible_text(
            "- select -")
        time.sleep(3)
        Select(driver.find_element_by_css_selector("div.filter-container > #Form_idSeniority")).select_by_visible_text(
            "Junior")
        time.sleep(3)
        Select(driver.find_element_by_css_selector("div.filter-container > #Form_idSeniority")).select_by_visible_text(
            "- select -")
        time.sleep(3)


        driver.find_element_by_xpath("/html/body/div/div[2]/table/thead/tr[2]/td[1]/div/input").send_keys("Form_Test")
        time.sleep(3)
        driver.find_element_by_xpath("/html/body/div/div[2]/table/thead/tr[2]/td[1]/div/input").send_keys(Keys.RETURN)
        time.sleep(3)


        #driver.find_element_by_xpath("/html/body/div/div[2]/table/tbody/tr/td[7]/a[3]").click()
        driver.find_element_by_css_selector("html body div.container div#formsGrid.grid-view table.items.table.table-striped.table-bordered.table-condensed.table-hover tbody tr.odd td a#yt1.text-danger i.glyphicon.glyphicon-trash").click()

        time.sleep(4)
        #self.assertRegexpMatches(self.close_alert_and_get_its_text(), r"^Are you sure you want to delete this form [\s\S]$")
        time.sleep(3)

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