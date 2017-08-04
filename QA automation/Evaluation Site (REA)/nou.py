__author__ = 'dev25'
        #Select general staff to peer evaluation
        driver.find_element_by_xpath("/html/body/div[1]/form/div[3]/div[3]/div/select/optgroup[1]/option[1]").click()
        time.sleep(3)
        driver.find_element_by_xpath("/html/body/div[1]/form/input").click()

        driver.find_element_by_class_name("dropdown-toggle").click()
        time.sleep(3)
        driver.find_element_by_link_text("Evaluation Periods").click()

        driver.find_element_by_xpath("/html/body/div/div[2]/table/thead/tr[2]/td[1]/div/input").send_keys("Form_Test")
        time.sleep(3)
        driver.find_element_by_xpath("/html/body/div/div[2]/table/thead/tr[2]/td[1]/div/input").send_keys(Keys.RETURN)

        time.sleep(3)
        driver.find_element_by_xpath("/html/body/div/div[2]/table/tbody/tr/td[8]/a[2]/i")
        time.sleep(3)

        driver.find_element_by_class_name("dropdown-toggle").click()
        time.sleep(3)
        driver.find_element_by_link_text("Forms").click()
        time.sleep(3)
        driver.find_element_by_xpath("/html/body/div/div[2]/table/thead/tr[2]/td[1]/div/input").send_keys("Form_Test")
        driver.find_element_by_xpath("/html/body/div/div[2]/table/thead/tr[2]/td[1]/div/input").send_keys(Keys.RETURN)
        time.sleep(3)
        driver.find_element_by_xpath("/html/body/div/div[2]/table/tbody/tr/td[8]/a[2]/i")
        time.sleep(3)

        driver.find_element_by_class_name("dropdown-toggle").click()
        time.sleep(3)
        driver.find_element_by_link_text("Forms").click()
        time.sleep(3)
        #driver.find_element_by_xpath("/html/body/div/div[2]/table/thead/tr[2]/td[1]/div/input").send_keys("Form_Test")
        driver.find_element_by_xpath("/html/body/div/div[2]/table/thead/tr[2]/td[1]/div/input").send_keys(Keys.RETURN)
        time.sleep(3)
        driver.find_element_by_xpath("/html/body/div/div[2]/table/tbody/tr/td[8]/a[2]/i").click()
        time.sleep(3)