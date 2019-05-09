import requests
import pytest

def test_weixin_send_msg_first():
    #res = requests.get("https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=id&corpsecret=Q")
    #print(res.json())
    access_token = 'QFT...-bin/message/send?access_token=' + access_token

    send_json = {
   "touser" : "xingming",
   "toparty" : "PartyID1|PartyID2",
   "totag" : "TagID1 | TagID2",
   "msgtype" : "text",
   "agentid" : 1000002,
   "text" : {
       "content" : "人生苦短，我用python，升职加薪，前程似锦"
   },
    }
    assert res.json().get("errmsg") == 'ok'
    assert res.json().get("invaliduser") == 'xingming'
    res = requests.post(url,json=send_json)

    print(res.json())
