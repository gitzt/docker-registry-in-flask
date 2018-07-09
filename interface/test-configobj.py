#-*- coding:utf-8 -*-

import requests
import base64
import os
from configobj import ConfigObj 


def set_config(section, key, value):
    path = os.path.split(os.path.realpath(__file__))[0] + '/config.ini'
    config = ConfigObj(path, encoding='UTF8')
    config[section][key] = value
    config.write()


def get_config(section, key):
    path = os.path.split(os.path.realpath(__file__))[0] + '/config.ini'
    config = ConfigObj(path, encoding='UTF8') 
    return config[section][key]

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

'测试测试'
