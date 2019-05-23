#! /usr/bin/env python
#coding=utf-8
from apis.baseapi import BaseAPI
import logging
import requests

class DeptManagment():

    def __init__(self):
        logging.info("init department management API")

    def create_dept(self):
        new_part={
            "name":"myrequeststest",
            "parentid":1,
            "order":1,
            "id":1,
        }

