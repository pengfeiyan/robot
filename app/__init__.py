# -*- coding: utf-8 -*-
# @Author : yanpengfei
# @time   : 2018/9/26 下午12:06
# @File   : __init__.py.py

from flask import Flask

def create_app():
    '''
    创建flask的核心app，加载配置文件，注册蓝图，初始化数据库db
    :return:返回flask的核心app
    '''
    app = Flask(__name__)

    load_config(app=app)
    regis_blueprint(app=app)
    load_robot_resource()

    return app

def regis_blueprint(app):
    '''
    将蓝图注册进flask的核心app中
    :param app: flask核心app
    :return: None
    '''
    from app.web import web
    app.register_blueprint(web)

def load_config(app):
    '''
    加载配置
    :param app:flask核心对象
    :return: None
    '''
    app.config.from_object('app.config.system')
    app.config.from_object('app.config.setting')

def load_robot_resource():
    '''
    加载robot平台运行时需要的数据资源，全局map
    :return: None
    '''
    pass