#!/usr/bin/python
import unittest, time, re, sys, getopt, os, logging
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException


# locally import from lib


class logcl (unittest.TestCase):
    def setUp(self):
        self.sequence = 1

        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(1)
        self.base_url = 'https://rea-test.rinf.ro'
        self.verificationErrors = []
        self.accept_next_alert = True


if __name__ == "__main__":
    unittest.main()
