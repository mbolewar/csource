from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re

class Ipfilterweb(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://10.82.0.235/"
        self.verificationErrors = []
#        self.accept_next_alert = true
    
    def test_ipfilterweb(self):
        driver = self.driver
        driver.get(self.base_url)
        driver.find_element_by_id("username").clear()
        driver.find_element_by_id("username").send_keys("admin")
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys("admin")
        driver.find_element_by_id("login_button").click()
        driver.find_element_by_id("menu_mv_network").click()
        driver.find_element_by_link_text("IP Filters").click()
        driver.find_element_by_css_selector("#mv_add_icon > span").click()
        driver.find_element_by_id("ip_address").clear()
        driver.find_element_by_id("ip_address").send_keys("10.82.0.4")
        driver.find_element_by_css_selector("#ip_submit > span").click()
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException, e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert.text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
