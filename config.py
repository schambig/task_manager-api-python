#!/usr/bin/python3
''' Configuration module '''


class Config:
    pass


class DevelopmentConfig(Config):
    ''' Development environment configuration class '''
    DEBUG = True


config = {
    'development': DevelopmentConfig
}
