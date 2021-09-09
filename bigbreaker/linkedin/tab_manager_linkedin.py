from bigbreaker.builtin.jobitem import Jobitem
import os
import sys
import json
import time

from bigbreaker.common.system_webdriver import SystemWebdriver
from bigbreaker.onionmail.tab_manager_onionmail import TabManagerOnionmail
from bigbreaker.common.tab_manager_base import TabManagerBase

from selenium.webdriver.support.select import Select
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class TabManagerLinkedin(TabManagerBase):

    def __init__(self, webdriver, window_handle):
        super(TabManagerLinkedin, self).__init__()
        self.webdriver = webdriver
        self.window_handle = window_handle
        # tab_manager_onionmail:TabManagerOnionmail
        # self.tab_manager_onionmail = tab_manager_onionmail



    def action_create_account(self, identity):
        print('action_create_account')
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
    
    def action_apply(self, jobitem, url_job):
        print('action_apply')
        self.make_active()
        SystemWebdriver.open_url(self.webdriver, url_job)

        is_present = SystemWebdriver.await_is_present(self.webdriver, 'post-apply-timeline__content', 5, True)
        if is_present:
            return True
        
        print('start_application')

        SystemWebdriver.await_is_present(self.webdriver, 'jobs-apply-button', 5, True)
        time.sleep(4)
        self.webdriver.find_element_by_class_name('jobs-apply-button').click()
        print('clicked apply')

        # for easy apply

        SystemWebdriver.await_is_clickable(self.webdriver, "//button[@aria-label='Continue to next step']")
        self.webdriver.find_element(By.XPATH, "//button[@aria-label='Continue to next step']").click()
        
        
        SystemWebdriver.await_is_clickable(self.webdriver, "//button[@aria-label='Continue to next step']")
        print('add cover letter')
        # todo do, generate cover letter
        self.webdriver.find_element(By.XPATH, "//button[@aria-label='Continue to next step']").click()

        SystemWebdriver.await_is_clickable(self.webdriver, "//button[@aria-label='Continue to next step']")
        print('fill drop downs')
        list_element_select = self.webdriver.find_elements_by_tag_name('select')
        for element_select in list_element_select:
            element_select_typed = Select(element_select)
            list_option = [option.text for option in element_select_typed.options]
            if 'Male' in list_option:
                element_select_typed.select_by_visible_text('Male')
            if 'American Indian or Alaskan Native' in list_option:
                element_select_typed.select_by_visible_text('Decline To Self Identify')

            prefered_option = 'I am not a protected veteran'
            if prefered_option in list_option:
                element_select_typed.select_by_visible_text(prefered_option)

            prefered_option = "No, I don't have a disability, or a history/record of having a disability"
            if prefered_option in list_option:
                element_select_typed.select_by_visible_text(prefered_option)
        self.webdriver.find_element(By.XPATH, "//button[@aria-label='Continue to next step']").click()  

        SystemWebdriver.await_is_clickable(self.webdriver, "//button[@aria-label='Review your application']")   
        self.webdriver.find_element(By.XPATH, "//button[@aria-label='Review your application']").click()

                   
        SystemWebdriver.await_is_clickable(self.webdriver, "//button[@aria-label='Submit application']")
        print('unfollow')
        self.webdriver.find_element_by_id("follow-company-checkbox").click()
        exit()
        self.webdriver.find_element(By.XPATH, "//button[@aria-label='Submit application']")
        

        # Select(self.webdriver.find_element(By.XPATH, "//select[@title='Day:']")).select_by_index(birthday_day)
        # Select(self.webdriver.find_element(By.XPATH, "//select[@title='Year:']")).select_by_visible_text(str(birthday_year))
