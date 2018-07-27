# -*- coding: utf-8 -*-

from flask import Flask
from config import config

app = Flask(__name__)
app.config.from_object(config['default'])
print app.config.get('HOST')
print app.config.get('PORT')

@app.route('/')
def index():
    return '<h1>Hello world !</h1>'


if __name__ == '__main__':
    app.run()
