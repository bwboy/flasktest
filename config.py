import os
basedir = os.path.abspath(os.path.dirname(__file__))

class config:
    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(config):
    DEBUG = True

config = {
    'development':DevelopmentConfig,
    'default':DevelopmentConfig
}