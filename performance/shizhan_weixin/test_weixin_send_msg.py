import requests
import pytest

def test_weixin_send_msg_first():
    #res = requests.get("https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=ww7c99ed700f77f99c&corpsecret=Qy2llVVuDMsR6gWZVRCx6iJaEk4TLOmYwJ0u0vD8xn8")
    #print(res.json())
    access_token = 'QFTtaidOVHzWZWxX1d0jOxsz7OjHt9fBhmsIsD_aoVXuohz5xhs0n6uhT1SzvqSdUp9fqGALZdzykRkbtnREZpULFCwAI08HvGt3x_93NjBYK3AId6pma80jpCvzSW5QTUUjZD2KlrB3STivT9AJnrC9VGDBMJ1Ntqv33ThZrKOdeD6L6vkAZM1JDwTXHEbA7Rw0EuDWTzpGLe8L_c4qPA'
    url = 'https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token=' + access_token

    send_json = {
   "touser" : "WangDan",
   "toparty" : "PartyID1|PartyID2",
   "totag" : "TagID1 | TagID2",
   "msgtype" : "text",
   "agentid" : 1000002,
   "text" : {
       "content" : "人生苦短，我用python，升职加薪，前程似锦"
   },
    }
    assert res.json().get("errmsg") == 'ok'
    assert res.json().get("invaliduser") == 'WangDan'
    res = requests.post(url,json=send_json)

    print(res.json())