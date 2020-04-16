import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
	Debug = False
	Testing = False
	SECRET_KEY = 'whatev rn'


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
