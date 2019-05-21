import requests
import pytest


#def test_weixin_pic_msg_success():
#上传临时图片获取mediaid
token = '8Hn8zm90JB0Zgo37RVN7aaEdgpLlZuHLHAZnG6FXqyOlvciZx4nQ59Q4j117l7uuE8VSIZ0qaZHbp_BH-Qf0uWJ3X7Xqgkc1WKx8juGcSmGqmZGpISZY84GBu2dVqx-jZaSaSh-FJKjmKb_w5gftsm_e_jfBQFak9rt9LQXqoELF-vXVZrWHa9k8p-0APw4gujHjntbo-B-xWTI5W-IczQ'
url_media_id = 'https://qyapi.weixin.qq.com/cgi-bin/media/upload?access_token='+token+'&type=image'
files = {'media': ('huizhen.jpg', open('huizhen.jpg', 'rb'), 'image/jpg')}
res_url_media_id = requests.post(url_media_id,files=files)
media_id = res_url_media_id.json().get('media_id')
'''   
print(media_id)
print(res_url_media_id.status_code)
print(res_url_media_id.json())

'''
#推送图片消息
url_send_image = 'https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token=' + token

test_json = {
            "touser" : "tester",
            "toparty" : "PartyID1|PartyID2",
            "totag" : "TagID1 | TagID2",
            "msgtype" : "image",
            "agentid" : 1000002,
            "image" : {
                    "media_id" : media_id
            },
            "safe":0
            }


res_send_image = requests.post(url_send_image,json=test_json)
print(res_send_image.json())

