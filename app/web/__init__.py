# -*- coding: utf-8 -*-
# @Author : yanpengfei
# @time   : 2018/9/26 下午2:21
# @File   : __init__.py.py

from flask import Blueprint

web = Blueprint('web',__name__)

from app.web import user