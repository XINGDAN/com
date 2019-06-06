#! /usr/bin/env python
#coding=utf-8
import requests

token = 'a-cGTq9ek_zd4dtbTKXyIGkerP0fjUB44Yz-y0hOPut5bYHiyNIiq-_pNr5qeuQwYZZ_r7-mDxHcJhOaziMuUWyCaXLgELZD5P2LJbDEmNoWALondJ8d7Pke8Z_uq1KYncMRAvuOrVo9J2jDBM1N2lCLUuoRQiUJcjen4laNmzWOeZhXf0h6XQpwN68ILZFZwjdgBLanAhMCvz9532TT-Q'
url_dep = 'https://qyapi.weixin.qq.com/cgi-bin/department/create?access_token=' + token
'''
test_json = {
                "name": "wd",
                "parentid": 1,
                "order": 1,
                "id":3
}
res = requests.post(url_dep,json=test_json)
print(res.json())
'''
update_url = 'https://qyapi.weixin.qq.com/cgi-bin/department/update?access_token=' + token

update_json = {
   "id": 3,
   "name": "wd2019060601",
}

res_update = requests.post(update_url,json=update_json)

print(res_update.json())
assert res_update.json().get("errmsg") == 'updated'