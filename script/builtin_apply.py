import random
import string
import json
import sys
import os
import pathlib



sys.path.append('../')
from bigbreaker.common.tools_identity import ToolsIdentity
from bigbreaker.common.system_webdriver import SystemWebdriver
from bigbreaker.google.tab_manager_google import TabManagerGoogle
from bigbreaker.linkedin.tab_manager_linkedin import TabManagerLinkedin
from bigbreaker.builtin.jobitem import Jobitem


with open('config.cfg', 'r') as file:
    config = json.load(file)

id_identity = 'identity_0'
identity = ToolsIdentity.identity_load(config, id_identity)
webdriver = ToolsIdentity.webdriver_load(config, id_identity)
handle_google = SystemWebdriver.get_handle(webdriver, 0)
handle_linkedin = SystemWebdriver.get_handle(webdriver, 1)
tab_manager_google = TabManagerGoogle(webdriver, handle_google)
tab_manager_linkedin = TabManagerLinkedin(webdriver, handle_linkedin)

list_jobitem = Jobitem.jobitem_load_list(config)
for jobitem in list_jobitem[3:]:
    jobitem = Jobitem.jobitem_validate(jobitem)
    print(jobitem['id_jobitem'])
    print(jobitem['title'])
    if (jobitem['want_top_apply'] == "n") or  (jobitem['has_applied'] == "y"):
        continue
        

    querry ='site:www.linkedin.com/jobs'
    title = jobitem['title']
    if ',' in title:
        title = title.split(',')[0].strip()
    querry += ' ' + title
    querry += ' ' + jobitem['name_company']
    print(querry)
    url_linkedin = tab_manager_google.action_get_url_first_hit(querry)
    #tab_manager_linkedin.action_navigate(url_linkedin)'
    has_applied = tab_manager_linkedin.action_apply(jobitem, url_linkedin)
    if has_applied:
        print('has_applied')
        jobitem['has_applied'] = 'y'
        #Jobitem.jobitem_save(config, jobitem)
    else:
        print('failed')
    exit()
            # print('do')
            # if ('has_applied'in jobitem):
            #     print(jobitem['has_applied'])
            # if (not 'has_applied'in jobitem) or (jobitem['has_applied'] == '?'):
            #     print(jobitem['has_applied'])
            #     print(jobitem['name_company'])
            #     print(jobitem['title'])
            #     list_part = jobitem['description'].split('\n')
            #     for part in list_part[0:3]:
            #         print(part.encode('ascii', 'ignore').decode('ascii'))
            #     print(jobitem['url_linkedin'])
                

            #     promt = ''
            #     while not promt in ['y','n','?']:
            #         print('y/n/?')
            #         promt = input()  
            #     jobitem['has_applied'] = promt
            #     Jobitem.jobitem_save(config, jobitem['id_jobitem'], jobitem)
                
            #     # print(jobitem['description'].encode('utf-8'))
            #     # promt = input()
            
            # querry ='site:www.linkedin.com/jobs'
            # title = jobitem['title']
            # if ',' in title:
            #     title = title.split(',')[0].strip()
            # querry += ' ' + title
            # querry += ' ' + jobitem['name_company']
            # print(querry)
            # url_linkedin = tab_manager_google.action_get_url_first_hit(querry)
            # print(url_linkedin)  
            # exit()
        # jobitem['want_top_apply'] = 'yes'
        # jobitem['has_applied'] = 'yes'
        # Jobitem.jobitem_save(config, jobitem['id_jobitem'], jobitem)
        
    
