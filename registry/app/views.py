# -*- coding: utf-8 -*-
# @Author: fangzt <295157914@qq.com>
# @Date:   2018-07-29 16:55:42
# @Last Modified by:   fzt
# @Last Modified time: 2018-08-10 17:33:39

from app import app 
from flask import render_template, request
from registry_images import getImageName

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/settings/', methods=['GET', 'POST'])
def settings():
    if request.method == 'GET':
        return render_template('settings.html')
    else :
        pass

@app.route('/registry/', methods=['GET', 'POST'])
def registry():
    if request.method == 'GET':
        registries = getImageName('10.13.0.63', 5000)
        return render_template('registry.html', registries=registries)
    else :
        pass





