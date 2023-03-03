#!/usr/bin/python3
''' Main executable '''
from app import create_app
from config import config


environment = config['development']
app = create_app(environment)

# Check whether the current script is being run as the main program
# or if it is being imported as a module by another script
if __name__ == '__main__':
    app.run()
