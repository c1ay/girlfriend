# coding:utf-8
import itchatmp
import requests

ROBOT_API = 'http://www.tuling123.com/openapi/api'
API_KEY = '****'
DEFAULT_CITY = '成都市'


itchatmp.update_config(itchatmp.WechatConfig(
    token='', appId='', appSecret=''
))


@itchatmp.msg_register(itchatmp.content.TEXT)
def text_reply(msg):
    data = {
        'key': API_KEY,
        'info': msg['Content'],
        'loc': DEFAULT_CITY,
        'userid': ''
    }
    ret = requests.post(ROBOT_API, json=data)
    text = ret.json()['text']
    return text


def server():
    itchatmp.run()
