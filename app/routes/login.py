# Login API
# Lantern
# Created by Abdelrahmam Salem.
# Copyright (c) 2017 Abdelrahmam Salem. All rights reserved.
# login.py

import os
import sys

sys.path.insert(0, os.path.abspath(os.path.dirname(os.path.realpath(__file__)) + '/../../'))

from . import api
from flask import (jsonify, request, render_template, redirect, session, url_for)
from app.handlers import (Context)

@api.route('/login')
def login():
	context = Context()
	context.action = 'loginAction'

	return render_template('pages/login.html', this = context)

@api.route('/loginAction')
def loginAction():
	return redirect(url_for('routes.dashboard'))