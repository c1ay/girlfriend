# coding:utf-8
import itchat
import requests
from itchat.content import *

ROBOT_API = 'http://www.tuling123.com/openapi/api'
API_KEY = '***'
DEFAULT_CITY = '成都市'


@itchat.msg_register([TEXT, MAP, CARD, NOTE, SHARING])
def text_reply(msg):
    params = {
        'key': 'e5bee95b8bb04e5c9f4a1b900c19cca4',
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
