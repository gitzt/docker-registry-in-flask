import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    pass


class DevelopmentConfig(Config):
    DEBUG = True
    HOST='0.0.0.0'
    PORT=5200
    

config = {
    'development': DevelopmentConfig,

    'default': DevelopmentConfig
}

