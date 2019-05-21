import requests
# 获取access_token
def test_get_accesstoken():
    url = 'https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=ww7c99ed700f77f99c&corpsecret=Qy2llVVuDMsR6gWZVRCx6kjdaW05MouG9xa1DCVsrqU'
    res = requests.get(url)
    print(res.json().get('access_token'))

    #token = res.json().get('access_token')

test_get_accesstoken()
