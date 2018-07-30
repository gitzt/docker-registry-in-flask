# -*- coding: utf-8 -*-
# @Author: fangzt <295157914@qq.com>
# @Date:   2018-07-29 16:55:42
# @Last Modified by:   fzt
# @Last Modified time: 2018-07-30 13:44:08

from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/registry/', methods=['GET', 'POST'])
def registry():
    if request.method == 'GET' :
        return render_template('registry.html')
    else :
        pass

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5100)

