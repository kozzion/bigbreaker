import os
import sys
import json
import time

from bigbreaker.common.system_webdriver import SystemWebdriver
from bigbreaker.onionmail.tab_manager_onionmail import TabManagerOnionmail

from selenium.webdriver.support.select import Select
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class TabManagerLinkedin:

    def __init__(self, webdriver, window_handle, tab_manager_onionmail:TabManagerOnionmail):
        super(TabManagerLinkedin, self).__init__()
        self.webdriver = webdriver
        self.window_handle = window_handle
        self.tab_manager_onionmail = tab_manager_onionmail

    def make_active(self):
        if not self.webdriver.current_window_handle == self.window_handle:
            self.webdriver.switch_to.window(str(self.window_handle))
            time.sleep(0.1)

    def action_create_account(self, identity):
        self.make_active()

        if not identity["onionmail_is_created"]:
            raise Exception()

       
        
        email = identity["onionmail_address"]
        name_first_0 = identity["name_first_0"]
        name_last_0 = identity["name_last_0"]
        # username = identity["linkedin_username"]
        password = identity["linkedin_password"]

        # birthday_year = identity["birthday_year"]
        # birthday_month = identity["birthday_month"]
        # birthday_day = identity["birthday_day"]



        SystemWebdriver.open_url(self.webdriver, 'https://www.linkedin.com/signup/cold-join')

        SystemWebdriver.await_is_clickable(self.webdriver, "//input[@name='email-address']")
        self.webdriver.find_element(By.XPATH, "//input[@name='email-address']").send_keys(email)
        self.webdriver.find_element(By.XPATH, "//input[@name='password']").send_keys(password)
        self.webdriver.find_element_by_id('join-form-submit').click()

        SystemWebdriver.await_is_clickable(self.webdriver, "//input[@id='first-name']")
        self.webdriver.find_element_by_id('first-name').send_keys(name_first_0)
        self.webdriver.find_element_by_id('last-name').send_keys(name_last_0)
        self.webdriver.find_element_by_id('join-form-submit').click()
    