#!/usr/bin/python
# import webdriver
import unittest
import time
from xml.dom import minidom
import logging
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, NoAlertPresentException


max_depth = 5

# add lib directory into PATH soon


import loginclass


class ReaAuto(loginclass.logcl):
    # lodfile is implemented
    logger = logging.getLogger("REA_Application")
    logger.setLevel(logging.INFO)
    # create a file handler
    handler = logging.FileHandler('login.log')
    #handler.setLevel(logging.INFO)
    logging.basicConfig(level=logging.INFO)
    # create a logging format
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    # add the handlers to the logger
    logger.addHandler(handler)


    def test_login(self):
        self.driver.maximize_window()
        self.driver.get(self.base_url)
        driver = self.driver
        driver.get(self.base_url + "/user/login")
        #driver.find_element_by_link_text("Guest").click()
        #driver.find_element_by_link_text("Login").click()
        self.logger.info('Start testing: Login testcase')

        #----------------------XML Data Parsing------------------------
        def parse_xml():
            xmldoc = minidom.parse("file.xml")
            data = xmldoc.getElementsByTagName("data")
            user = xmldoc.getElementsByTagName("user")

            list = ["mail", "pass"]

            for user in user:
                list[0] = user.getElementsByTagName("mail")[0].firstChild.data
                list[1] = user.getElementsByTagName("pass")[0].firstChild.data

            return list

        data = parse_xml()
        email = driver.find_element_by_id("MLoginForm_email")
        email.send_keys(data[0])
        time.sleep(1)

        pas = driver.find_element_by_id("MLoginForm_password")
        pas.send_keys(data[1])
        time.sleep(1)
        driver.find_element_by_name("yt0").click()
        time.sleep(1)
        try:
            user = driver.find_element_by_tag_name('p')

            self.logger.info('Success Login - email and password are correct')

        except NoAlertPresentException, e:
            self.logger.error('Login Unsuccessefull,"Welcome to dashboard" is not finde on the page', exc_info=False)

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

    @property
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
