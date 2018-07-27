# -*- coding: utf-8 -*-

from flask import Flask
from config import config

app = Flask(__name__)
app.config.from_object(config['default'])



@app.route('/')
def index():
    return '<h1>Hello world !</h1>'


if __name__ == '__main__':
    app.run()
