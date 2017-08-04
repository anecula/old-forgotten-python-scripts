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
from selenium.webdriver.common.action_chains import ActionChains

from xml.dom import minidom
from lxml import etree
import xml.etree.ElementTree as ET

import os, sys
import logging


max_depth = 5

# add lib directory into PATH soon

import loginclassUsers

from loginclassUsers import Auto as myclasstoextend


class EvaluationPeriods (loginclassUsers.Auto):
    def test_sort(self):

        self.claslog = myclasstoextend.test_login(self)
        driver = self.driver
        time.sleep(1)

        driver.find_element_by_class_name("dropdown-toggle").click()
        time.sleep(3)
        driver.find_element_by_link_text("Forms").click()
        time.sleep(3)

        driver.find_element_by_xpath("/html/body/div/form/div[3]/div[1]/div[1]/input").send_keys("Form_Test")
        time.sleep(3)
        driver.find_element_by_xpath("/html/body/div/form/div[3]/div[1]/div[3]/select").click()
        time.sleep(3)
        driver.find_element_by_xpath("/html/body/div/form/div[3]/div[1]/div[3]/select/option[2]").click()
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

        driver.find_element_by_class_name("dropdown-toggle").click()
        time.sleep(3)
        driver.find_element_by_link_text("Evaluation Periods").click()
        time.sleep(3)
        driver.find_element_by_id("EvaluationPeriod_nume").clear()
        time.sleep(3)
        driver.find_element_by_id("EvaluationPeriod_nume").send_keys("Form_Test")
        time.sleep(3)
        driver.find_element_by_id("EvaluationPeriod_status").click()
        time.sleep(3)
        driver.find_element_by_xpath("/html/body/div/form/div[3]/div[1]/div[3]/label").click()
        time.sleep(3)
        driver.find_element_by_xpath("/html/body/div/form/div[3]/div[1]/div[3]/select/option[2]").click()
        time.sleep(3)
        driver.find_element_by_xpath("/html/body/div/form/div[3]/div[2]/div[1]/input").click()
        time.sleep(3)
        driver.find_element_by_xpath("/html/body/div[2]/div[1]/table/tbody/tr[2]/td[7]").click()
        time.sleep(3)
        driver.find_element_by_xpath("/html/body/div/form/div[3]/div[2]/div[2]/input").click()
        time.sleep(3)
        driver.find_element_by_xpath("/html/body/div[2]/div[1]/table/tbody/tr[5]/td[6]").click()
        time.sleep(3)
        driver.find_element_by_xpath("/html/body/div/form/div[3]/div[3]/div/select").click()
        time.sleep(3)

        #Choose type of Department
        driver.find_element_by_xpath("/html/body/div/form/div[3]/div[3]/div/select/optgroup").click()
        time.sleep(3)
        driver.find_element_by_xpath("/html/body/div/form/div[3]/div[3]/div/select/optgroup/option[1]").click()
        ActionChains(driver).key_down(Keys.SHIFT)
        time.sleep(3)
        driver.find_element_by_xpath("/html/body/div/form/div[3]/div[3]/div/select/optgroup/option[2]").click()
        ActionChains(driver).key_down(Keys.SHIFT)
        time.sleep(3)
        driver.find_element_by_xpath("/html/body/div/form/div[3]/div[3]/div/select/optgroup/option[3]").click()
        time.sleep(3)
        driver.find_element_by_xpath("/html/body/div/form/div[3]/div[4]/div/select").click()
        time.sleep(3)
        driver.find_element_by_xpath("/html/body/div/form/div[3]/div[4]/div/select").click()
        time.sleep(3)

        driver.find_element_by_xpath("/html/body/div/form/div[3]/div[4]/div/select/optgroup[1]").click()
        time.sleep(3)

        #Choose type of Form
        driver.find_element_by_xpath("/html/body/div/form/div[3]/div[4]/div/select/optgroup[1]/option[1]").click()
        time.sleep(3)
        ActionChains(driver).key_down(Keys.SHIFT)
        driver.find_element_by_xpath("/html/body/div/form/div[3]/div[4]/div/select/optgroup[1]/option[2]").click()
        ActionChains(driver).key_down(Keys.SHIFT)
        driver.find_element_by_xpath("/html/body/div/form/div[3]/div[4]/div/select/optgroup[1]/option[3]").click()
        ActionChains(driver).key_down(Keys.SHIFT)

        driver.find_element_by_xpath("/html/body/div/form/div[3]/div[4]/div/select/optgroup[2]/option[1]").click()
        ActionChains(driver).key_down(Keys.SHIFT)

        driver.find_element_by_xpath("/html/body/div/form/div[3]/div[4]/div/select/optgroup[2]/option[2]").click()
        ActionChains(driver).key_down(Keys.SHIFT)

        driver.find_element_by_xpath("/html/body/div/form/div[3]/div[4]/div/select/optgroup[3]/option").click()
        ActionChains(driver).key_down(Keys.SHIFT)

        driver.find_element_by_xpath("/html/body/div/form/div[3]/div[4]/div/select/optgroup[4]/option[1]").click()
        ActionChains(driver).key_down(Keys.SHIFT)
        time.sleep(3)
        driver.find_element_by_xpath("/html/body/div/form/input").click()
        time.sleep(3)
        driver.find_element_by_xpath("/html/body/div/div[2]/table/thead/tr[2]/td[1]/div/input").send_keys("Form_Test")
        time.sleep(3)
        driver.find_element_by_xpath("/html/body/div/div[2]/table/thead/tr[2]/td[1]/div/input").send_keys(Keys.RETURN)
        time.sleep(3)
        driver.find_element_by_xpath("/html/body/div/div[2]/table/tbody/tr/td[8]/a[5]").click()
        time.sleep(3)
        driver.find_element_by_xpath("/html/body/div[1]/form/div[3]/div[1]/div/div[1]/a").click()
        time.sleep(3)
        driver.find_element_by_xpath("/html/body/div[1]/form/div[3]/div[1]/div/select/option[6]").click()
        time.sleep(3)
        driver.find_element_by_xpath("/html/body/div[1]/form/div[3]/div[2]/div/div[1]/ul").click()
        time.sleep(3)
        driver.find_element_by_xpath("/html/body/div[1]/form/div[3]/div[2]/div/select/option[6]").click()
        time.sleep(3)
        driver.find_element_by_xpath("/html/body/div/form/div[3]/div[3]/div/div[1]").click()
        time.sleep(3)
        #Select general staff to peer evaluation
        driver.find_element_by_xpath("/html/body/div[1]/form/div[3]/div[3]/div/select/optgroup[1]/option[1]").click()
        time.sleep(3)
        driver.find_element_by_xpath("/html/body/div[1]/form/input").click()
        time.sleep(3)

        driver.find_element_by_class_name("dropdown-toggle").click()
        time.sleep(3)
        driver.find_element_by_link_text("Evaluation Periods").click()


        #driver.find_element_by_xpath("/html/body/div/div[2]/table/thead/tr[2]/td[1]/div/input").send_keys("Form_Test")
        time.sleep(3)
        driver.find_element_by_xpath("/html/body/div/div[2]/table/thead/tr[2]/td[1]/div/input").send_keys(Keys.RETURN)

        time.sleep(1)
        driver.find_element_by_xpath("/html/body/div/div[2]/table/tbody/tr/td[8]/a[2]/i").click()
        time.sleep(3)

        driver.find_element_by_class_name("dropdown-toggle").click()
        time.sleep(3)
        driver.find_element_by_link_text("Forms").click()
        time.sleep(3)
        driver.find_element_by_xpath("/html/body/div/div[2]/table/thead/tr[2]/td[1]/div/input").send_keys("Form_Test")
        driver.find_element_by_xpath("/html/body/div/div[2]/table/thead/tr[2]/td[1]/div/input").send_keys(Keys.RETURN)
        time.sleep(3)
        driver.find_element_by_xpath("/html/body/div/div[2]/table/tbody/tr/td[7]/a[3]/i").click()
        time.sleep(3)

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