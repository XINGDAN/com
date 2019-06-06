import requests
# 获取access_token
def test_get_accesstoken():
    url = 'https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=ww7c99ed700f77f99c&corpsecret=yi-lxOLTNkgwnuoO8xZZNdeL5y8-Df0wUAxW8yRTOEE'
    res = requests.get(url)
    print(res.json().get('access_token'))

    #token = res.json().get('access_token')

test_get_accesstoken()
