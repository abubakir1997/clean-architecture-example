# Main Routes File
# Lantern
# Created by Abdelrahmam Salem.
# Copyright (c) 2017 Abdelrahmam Salem. All rights reserved.
# __init__.py

from flask import Blueprint

api = Blueprint('routes', __name__)

from .dashboard import *
from .index import *
from .login import *