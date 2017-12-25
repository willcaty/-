# -*- coding: utf-8 -*-
import json

import requests

from BaseData import *


class Token(object):
    def __init__(self, Get_Token_Url):
        """
        初始化
        :param Get_Token_Url:获取token的地址，来自BaseData中
        :return:
        """
        self.url = Get_Token_Url

    def get_token(self):
        """
        请求获取token的url，截取token并返回
        :return:返回token值
        """
        try:
            ret = requests.get(self.url).text
            return eval(ret)['access_token']
        except Exception, e:
            print e


class Message:
    def __init__(self, content, msgtype='text', agentid=5, touser='@all'):
        """
        初始化发送信息的参数
        :param content: 消息内容
        :param msgtype: 消息类型，此时固定为：text
        :param agentid: 应用的id，整型
        :param touser: 成员ID列表（消息接收者，多个接收者用‘|’分隔）。特殊情况：指定为@all，则向关注该企业应用的全部成员发送
        :return:
        """
        self.content = content
        self.msgtype = msgtype
        self.agentid = agentid
        self.touser = touser
        self.token = Token(Get_Token_Url).get_token()
        self.param = {
            'touser': self.touser,
            'msgtype': self.msgtype,
            'agentid': self.agentid,
            'text': {"content": self.content}
        }

    def send_msg(self):
        """
        发送信息的方法
        :return:
        """
        url = Send_Message + self.token
        try:
            requests.post(url, json.dumps(self.param, ensure_ascii=False))
        except Exception, e:
            print e


if __name__ == '__main__':
    touser = "wanghao|wangting"
    content = '指定人员发送'
    Message(content, touser=touser).send_msg()
