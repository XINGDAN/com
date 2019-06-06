#! /usr/bin/env python
#coding=utf-8
from apis.baseapi import BaseAPI
import logging
import requests
import time
from initialization.sysconfig import sys_cfg

class DeptManagment():

    def __init__(self):
        BaseAPI.__init__(self)
        logging.info("init department management API")
        self.dep_secrets = sys_cfg.get('contact_para','secrets')

    def create_dept(self):
        name = time.strftime("%y%m%d")
        new_part={
            "name":"myrequeststest",
            "parentid":1,
            "order":1,
            "id":1,
        }
        logging.debug('url')
        param = {'access_token':self.get_token()}
        logging.debug('url:'+str(self.create_dep_url))
        logging.debug('params:' + str(param))
        self.post_json(self.create_dep_url,new_part,params=param)

    def get_create_dept_res(self):
        return self.get_response()


