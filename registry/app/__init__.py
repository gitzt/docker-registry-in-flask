# -*- coding: utf-8 -*-
# @Author: fangzt <295157914@qq.com>
# @Date:   2018-08-02 19:54:28
# @Last Modified by:   fzt
# @Last Modified time: 2018-08-10 09:28:15

from flask import Flask

# 实例化一个flask 对象
app = Flask(__name__)

# 导入 views 模块
from app import views