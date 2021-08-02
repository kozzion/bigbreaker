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
        SystemWebdriver.open_url(self.driver, 'https://www.onionmail.org/account/create/')
        name = identity["name_first_0"] + " " + identity["name_last_0"]
        username = identity["onionmail_username"]
        password = identity["onionmail_password"]
        #WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//input[@class='inputlong' and @id='identificacionUsuario']"))).send_keys("your_name")
        self.driver.find_element_by_id("name").send_keys(name)
        self.driver.find_element_by_id("username").send_keys(username)
        self.driver.find_element_by_id("password").send_keys(password)
        self.driver.find_element_by_id("password2").send_keys(password)
        element = self.driver.find_element_by_name("remember")
        if not element.is_selected():
            element.click()
        self.driver.find_element_by_class_name("btn-success").click()

    def action_load_list_email_recent(self, identity):
        username = identity["onionmail_username"]
        password = identity["onionmail_password"]
        if not self.username_logged_in == username:
            self.action_logout()
            self.action_login(identity)
        list_url_message = self.load_list_url_message()
        for url_message in list_url_message:
            html_email = self.action_load_html_email(url_message)

    def action_logout(self):
        pass

    def action_login(self, identity):
        username = identity["onionmail_username"]
        password = identity["onionmail_password"]
        SystemWebdriver.open_url(self.driver, 'https://www.onionmail.org/account/login/')
        self.driver.find_element_by_id("username").send_keys(username)
        self.driver.find_element_by_id("password").send_keys(password)
        element = self.driver.find_element_by_name("remember")
        if not element.is_selected():
            element.click()            
        self.driver.find_element_by_class_name("btn-success").click()

    def action_load_html_email(self, url_message):        
        SystemWebdriver.open_url(self.driver, url_message)
        #TODO
        element = self.driver.find_element_by_name("remember")
        if not element.is_selected():
            element.click()            
        self.driver.find_element_by_class_name("btn-success").click()

    def load_list_url_message(self):
        list_element = self.driver.find_elements_by_class_name("messagerow")
        list_url_message = []
        for element in list_element:
            element_href = element.find_element_by_class_name("messagerow-link")
            list_url_message.append(element_href.get_attribute("href")) 
        print(list_url_message)
        return list_url_message
            
            
        

    # def fill_create_account(self, identity):
    #     name = identity["name_first_0"] + " " + identity["name_last_0"]
    #     username = identity["onionmail_username"]
    #     password = identity["onionmail_password"]
    #     #WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//input[@class='inputlong' and @id='identificacionUsuario']"))).send_keys("your_name")
    #     self.driver.find_element_by_id("name").send_keys(name)
    #     self.driver.find_element_by_id("username").send_keys(username)
    #     self.driver.find_element_by_id("password").send_keys(password)
    #     self.driver.find_element_by_id("password2").send_keys(password)
    #     element = self.driver.find_element_by_name("remember")
    #     if not element.is_selected():
    #         element.click()
        
    # def complete_create_account(self):
    #     self.driver.find_element_by_class_name("btn-success").click()

    # def is_loaded(self):
    #     return None != self.driver.find_element_by_id("name")

    # def await_is_loaded(self):
    #     while(not self.is_loaded()):
    #         # print('not loaded')
    #         # print(self.driver.current_url)
    #         sys.stdout.flush()
    #         time.sleep(0.1)


    # def await_is_loaded2(self):
    #     while(not SystemWebdriver.is_loaded(self.driver)):
    #         sys.stdout.flush()
    #         time.sleep(0.1)