# coding:utf-8
import itchat
import requests

ROBOT_API = 'http://www.tuling123.com/openapi/api'
API_KEY = '****'
DEFAULT_CITY = '成都市'


itchat.update_config(itchat.WechatConfig(
    token='', appId='', appSecret=''
))


@itchat.msg_register(itchat.content.TEXT)
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
    itchat.run()
