# Application Configuration
# Lantern
# Created by Abdelrahmam Salem.
# Copyright (c) 2017 Abdelrahmam Salem. All rights reserved.
# config.py

import os
import logging

class Config():
    """Application configuration class"""
    def __init__(self):
        try:
            if os.environ['COD_ENV'] == 'prod':
                self.ACTIVE = self.Production
            elif os.environ['COD_ENV'] == 'dev':
                self.ACTIVE = self.Development
            elif os.environ['COD_ENV'] == 'test':
                self.ACTIVE = self.Testing
        except KeyError:
            self.ACTIVE = self.Production
			
    class Production:
        ROOT = 'https://lantern.com'
        HOST = 'localhost'
        PORT = 8885
        DEBUG = False
        STATIC = 'static'
        MYSQL_CONNSTR = 'mysql://root:root@ah@localhost/Lantern'

    class Testing(Production):
        ROOT = 'http://localhost:8888'
        PORT = 8886
        DEBUG = True

    class Development(Testing):
        PORT = 8887