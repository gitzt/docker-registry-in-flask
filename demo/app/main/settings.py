# -*- coding: utf-8 -*-
# @Author: fangzt <295157914@qq.com>
# @Date:   2018-08-03 14:06:08
# @Last Modified by:   fzt
# @Last Modified time: 2018-08-03 14:19:24

from flask import Blueprint, render_template, request

settings = Blueprint('settings', __name__)

@settings.route('/settings/', methods=['GET', 'POST'])
def settings():
    if request.method == 'GET':
        return render_template('settings.html')
    else :
        pass