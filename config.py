#!/usr/bin/python3
''' Configuration module '''


class Config:
    pass

# Inherit from Config
class DevelopmentConfig(Config):
    ''' Development environment configuration class '''
    DEBUG = True

# Dictionary to store class Development, which will store configurations for the app
config = {
    'development': DevelopmentConfig
}
