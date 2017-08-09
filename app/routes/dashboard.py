# Dashboard API
# Lantern
# Created by Abdelrahmam Salem.
# Copyright (c) 2017 Abdelrahmam Salem. All rights reserved.
# dashboard.py

import os
import sys

sys.path.insert(0, os.path.abspath(os.path.dirname(os.path.realpath(__file__)) + '/../../'))

from app.adapters.mysql import MySQLAdapter
from app.handlers import (Context)

sys.path.insert(0, os.path.abspath(os.path.dirname(os.path.realpath(__file__)) + '/../../config/'))

from config import Config

CONFIG = Config()

from . import api
from flask import (jsonify, request, render_template, redirect, session, url_for)

@api.route('/dashboard')
def dashboard():
	return render_template('pages/dashboard.html')