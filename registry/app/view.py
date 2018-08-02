# -*- coding: utf-8 -*-
# @Author: fangzt <295157914@qq.com>
# @Date:   2018-07-29 16:55:42
# @Last Modified by:   fzt
# @Last Modified time: 2018-08-02 19:38:29


from flask import Flask, render_template, request
import os

path = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)


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
        return render_template('registry.html')
    else :
        pass





if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5100)

