__author__ = 'dev25'
#!/usr/bin/python
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


class filter (loginclassUsers.Auto):
    def test_sort(self):

        self.claslog = myclasstoextend.test_login(self)
        driver = self.driver

        driver.find_element_by_link_text("Admin Pannel").click()
        driver.find_element_by_link_text("Users").click()
        time.sleep(1)

        driver.find_element_by_id("UserDepartament_numeClient").send_keys("intel")
        time.sleep(1)
        driver.find_element_by_id("UserDepartament_numeClient").send_keys(Keys.RETURN)
        time.sleep(1)
        driver.find_element_by_id("UserDepartament_numeClient").clear()
        time.sleep(1)


        driver.find_element_by_id("UserDepartament_numeDept").send_keys("Yocto")
        time.sleep(1)
        driver.find_element_by_id("UserDepartament_numeDept").send_keys(Keys.RETURN)
        time.sleep(1)
        driver.find_element_by_id("UserDepartament_numeDept").clear()
        time.sleep(1)
        driver.find_element_by_id("UserDepartament_numeDept").send_keys(Keys.RETURN)
        time.sleep(1)
        driver.find_element_by_id("UserDepartament_firstName").send_keys("irina")
        time.sleep(1)
        driver.find_element_by_id("UserDepartament_firstName").send_keys(Keys.RETURN)
        time.sleep(1)
        driver.find_element_by_id("UserDepartament_firstName").clear()
        time.sleep(1)
        driver.find_element_by_id("UserDepartament_firstName").send_keys(Keys.RETURN)
        time.sleep(1)
        driver.find_element_by_id("UserDepartament_lastName").send_keys("manole")
        time.sleep(1)
        driver.find_element_by_id("UserDepartament_lastName").send_keys(Keys.RETURN)
        time.sleep(1)
        driver.find_element_by_id("UserDepartament_lastName").clear()
        time.sleep(1)
        driver.find_element_by_id("UserDepartament_lastName").send_keys(Keys.RETURN)
        time.sleep(1)

        driver.find_element_by_id("UserDepartament_numeRol").send_keys("manager")
        time.sleep(1)
        driver.find_element_by_id("UserDepartament_numeRol").send_keys(Keys.RETURN)
        time.sleep(1)
        driver.find_element_by_id("UserDepartament_numeRol").clear()
        time.sleep(1)
        driver.find_element_by_id("UserDepartament_numeRol").send_keys(Keys.RETURN)
        time.sleep(1)
        Select(driver.find_element_by_id("UserDepartament_numeStatus")).select_by_visible_text("Inactive")
        time.sleep(1)
        driver.find_element_by_id("User_status").click()
        time.sleep(1)
        Select(driver.find_element_by_id("User_status")).select_by_visible_text("Active")
        time.sleep(1)
        driver.find_element_by_css_selector("#User_status > option[value=\"active\"]").click()
        time.sleep(1)
        Select(driver.find_element_by_id("UserDepartament_numeStatus")).select_by_visible_text("Active")
        time.sleep(1)
        Select(driver.find_element_by_id("UserDepartament_numeStatus")).select_by_visible_text("Fired")
        time.sleep(1)
        Select(driver.find_element_by_id("UserDepartament_numeStatus")).select_by_visible_text("Resigned")
        time.sleep(1)
        Select(driver.find_element_by_id("UserDepartament_numeStatus")).select_by_visible_text("Internalized")
        time.sleep(1)
        Select(driver.find_element_by_id("UserDepartament_numeStatus")).select_by_visible_text("Active")
        time.sleep(1)
        Select(driver.find_element_by_id("UserDepartament_numeStatus")).select_by_visible_text("- select -")
        time.sleep(1)

        driver.find_element_by_id("UserDepartament_numePoz").send_keys("qa")
        time.sleep(1)
        driver.find_element_by_id("UserDepartament_numePoz").send_keys(Keys.RETURN)
        time.sleep(1)
        driver.find_element_by_id("UserDepartament_numePoz").clear()
        time.sleep(1)
        driver.find_element_by_id("UserDepartament_numePoz").send_keys(Keys.RETURN)
        time.sleep(1)

        driver.find_element_by_id("UserDepartament_seniorityLevel").send_keys("senior")
        time.sleep(1)
        driver.find_element_by_id("UserDepartament_seniorityLevel").send_keys(Keys.RETURN)
        time.sleep(1)
        driver.find_element_by_id("UserDepartament_seniorityLevel").clear()
        time.sleep(1)
        driver.find_element_by_id("UserDepartament_seniorityLevel").send_keys(Keys.RETURN)
        time.sleep(1)

        driver.find_element_by_id("UserDepartament_numeManager").send_keys("sorin")
        time.sleep(1)
        driver.find_element_by_id("UserDepartament_numeManager").send_keys(Keys.RETURN)
        time.sleep(1)
        driver.find_element_by_id("UserDepartament_numeManager").clear()
        time.sleep(1)
        driver.find_element_by_id("UserDepartament_numeManager").send_keys(Keys.RETURN)
        time.sleep(1)

        driver.find_element_by_id("UserDepartament_idRol").click()
        driver.find_element_by_css_selector("#UserDepartament_idRol > option[value=\"4\"]").click()
        time.sleep(1)

        driver.find_element_by_xpath("(//option[@value='9'])[16]").click()
        driver.find_element_by_xpath("(//select[@id='UserDepartament_idNivelSenioritate'])[2]").click()
        time.sleep(1)
        Select(driver.find_element_by_xpath("(//select[@id='UserDepartament_idNivelSenioritate'])[2]")).select_by_visible_text("Middle")
        driver.find_element_by_xpath("(//option[@value='7'])[7]").click()
        time.sleep(1)
        driver.find_element_by_xpath("(//select[@id='UserDepartament_idNivelSenioritate'])[4]").click()
        Select(driver.find_element_by_xpath("(//select[@id='UserDepartament_idNivelSenioritate'])[4]")).select_by_visible_text("Senior")
        time.sleep(1)
        driver.find_element_by_xpath("(//option[@value='9'])[17]").click()
        driver.find_element_by_xpath("(//select[@id='UserDepartament_idManager'])[4]").click()
        Select(driver.find_element_by_xpath("(//select[@id='UserDepartament_idManager'])[4]")).select_by_visible_text("Sorin Jucovschi")
        time.sleep(1)
        driver.find_element_by_xpath("(//option[@value='4'])[9]").click()
        driver.find_element_by_xpath("(//select[@id='UserDepartament_idPozitie'])[4]").click()
        Select(driver.find_element_by_xpath("(//select[@id='UserDepartament_idPozitie'])[4]")).select_by_visible_text("QA")
        time.sleep(1)
        driver.find_element_by_xpath("(//option[@value='9'])[16]").click()


    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException, e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.driver.switch_to.alert()
        except NoAlertPresentException, e:
            return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to.alert()
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