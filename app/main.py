#!/usr/bin/python2.7

# Main Flask file
# Lantern
# Created by Abdelrahmam Salem.
# Copyright (c) 2017 Abdelrahmam Salem. All rights reserved.
# main.py

import os
import sys
from flask import (Flask, request, redirect)

sys.path.insert(0, os.path.abspath(os.path.dirname(os.path.realpath(__file__)) + '/../'))
sys.path.insert(0, os.path.abspath(os.path.dirname(os.path.realpath(__file__)) + '/../../config/'))

from app.routes import *
from config import Config

CONFIG = Config()

app = Flask(__name__, 
	static_folder = '../{}'.format(CONFIG.ACTIVE.STATIC), 
	template_folder = '../templates')

app.url_map.strict_slashes = False
app.secret_key = '*\x16\xfe\xe2W\x16F\x84\x04\x01\xa3\x0b\x9a\xc8q\xc1\x8f\x00\x0fT\x04b\xea\x97'
app.register_blueprint(api)

@app.before_request
def before_request():
	# Remove Leading Slash(es) '/'
    url = request.path 
    if url != '/' and url.endswith('/'):
        return redirect(url.strip('/'))

if __name__ == '__main__':
	app.run(host = CONFIG.ACTIVE.HOST, port = CONFIG.ACTIVE.PORT, debug = CONFIG.ACTIVE.DEBUG)
