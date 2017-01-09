import os
basedir = os.path.abspath(os.path.dirname(__file__))

class config:
    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(config):
    DEBUG = True
    MONGODB_DB = 'flasktest'
    MONGODB_HOST = '127.0.0.1'
    MONGODB_PORT = 127017

config = {
    'development':DevelopmentConfig,
    'default':DevelopmentConfig
}