import os
import sys
import json
import time

from bigbreaker.common.system_webdriver import SystemWebdriver

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class PagemanagerOnionmail:

    def __init__(self, driver):
        super(PagemanagerOnionmail, self).__init__()
        self.driver = driver
        self.current_url = ''
        self.username_logged_in = None

    def action_create_account(self, identity):
        SystemWebdriver.open_url(self.driver, 'https://www.instagram.com/accounts/emailsignup/?hl=en')
        
        email = identity["onionmail_email"]
        name_full = identity["name_full"]
        username = identity["instagram_username"]
        password = identity["instagram_password"]
        self.driver.find_element(By.XPATH, "//input[@aria-label='Mobile Number or Email'").send_keys("your_name")
        

        # self.driver.find_element_by_id("name").send_keys(name)
        # self.driver.find_element_by_id("username").send_keys(username)
        # self.driver.find_element_by_id("password").send_keys(password)
        # self.driver.find_element_by_id("password2").send_keys(password)
        # element = self.driver.find_element_by_name("remember")
        # if not element.is_selected():
        #     element.click()
        # self.driver.find_element_by_class_name("btn-success").click()
