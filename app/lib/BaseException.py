# -*- coding: utf-8 -*-
# @Author : yanpengfei
# @time   : 2018/9/11 下午4:28
# @File   : BaseException.py

class HttpConnectException(Exception):

    def __init__(self,err='request请求连接异常'):
        Exception.__init__(self,err)

class ParamsException(Exception):

    def __init__(self,err='参数异常'):
        Exception.__init__(self,err)