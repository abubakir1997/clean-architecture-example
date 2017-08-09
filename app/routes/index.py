# Index API
# Lantern
# Created by Abdelrahmam Salem.
# Copyright (c) 2017 Abdelrahmam Salem. All rights reserved.
# index.py

from . import api
from flask import (jsonify, request, render_template, redirect, session, url_for)

@api.route('/')
@api.route('/index')
def index():
	if False: # change to if logged in
		from .dashboard import dashboard
		return dashboard()
	else: 
		from .login import login
		return login()