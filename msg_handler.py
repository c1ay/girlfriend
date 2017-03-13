# coding:utf-8
import itchat
import requests
from itchat.content import *

ROBOT_API = 'http://www.tuling123.com/openapi/api'
API_KEY = '****'
DEFAULT_CITY = '成都市'


@itchat.msg_register([TEXT, MAP, CARD, NOTE, SHARING])
def text_reply(msg):
    params = {
        'key': API_KEY,
        'info': msg['Text'],
        'loc': DEFAULT_CITY,
        'userid': msg['FromUserName']
    }
    res = requests.post(ROBOT_API, json=params)
    text = res.json()['text']
    itchat.send('test: {}'.format(text))
    return 'test: {}'.format(text)


def server():
    itchat.auto_login(True)
    itchat.run()
