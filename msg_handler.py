# coding:utf-8
import itchat
import requests

import setting

ROBOT_API = 'http://www.tuling123.com/openapi/api'


@itchat.msg_register(itchat.content.TEXT)
def text_reply(msg):
    """
    reply text msg
    """
    data = {
        'key': setting.API_KEY,
        'info': msg['Content'],
        'loc': setting.DEFAULT_CITY,
        'userid': ''
    }
    ret = requests.post(ROBOT_API, json=data)
    text = ret.json()['text']
    return text

def server():
    """
    server
    """
    itchat.auto_login(enableCmdQR=2)
    itchat.run()
