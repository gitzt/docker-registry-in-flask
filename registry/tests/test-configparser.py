# -*- coding: utf-8 -*-
# @Author: fangzt <295157914@qq.com>
# @Date:   2018-07-27 21:45:02
# @Last Modified by:   lenovo
# @Last Modified time: 2018-07-27 23:49:51

import requests
import base64
import ConfigParser
import os

def get_config(section, key):
    config = ConfigParser.ConfigParser()
    path = os.path.split(os.path.realpath(__file__))[0] + '/config.ini'
    config.read(path)
    return config.get(section, key)


ip = get_config('HOST_INFO', 'IP')
port = get_config('HOST_INFO', 'PORT')
user = get_config('USER_INFO', 'USER')
password = get_config('USER_INFO', 'PASSWORD')

url = 'http://%s:%s/v2/_catalog' % (ip, port)

account = 'Basic ' + base64.b64encode('%s:%s' % (user,password))
headers = {
    'Authorization': account
}

resp = requests.get(url, headers=headers)

print resp.text


