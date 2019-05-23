#! /usr/bin/env python
#coding=utf-8

import logging
import requests

class BaseAPI:

    def __init__(self):
        logging.info("init base api interface")
        self.cop_id = ''
        self.token_url = 'https://qyapi.weixin.qq.com/cgi-bin/gettoken'

    def get_token(self,secret):
        params = {'corpid':self.cop_id,'corpsecret':SECRET}
        res = requests.get(self.token_url,params=params)
        return res.json().get("access_token")

    def extend_post(self,url,params=None):
        requests.post()

