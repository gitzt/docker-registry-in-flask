# -*- coding: utf-8 -*-
# @Author: fangzt <295157914@qq.com>
# @Date:   2018-08-03 14:06:08
# @Last Modified by:   fzt
# @Last Modified time: 2018-08-03 14:18:50

from flask import Blueprint, render_template, request

registry = Blueprint('registry', __name__)


@registry.route('/registry/', methods=['GET', 'POST'])
def registry():
    if request.method == 'GET':
        return render_template('registry.html')
    else :
        pass
