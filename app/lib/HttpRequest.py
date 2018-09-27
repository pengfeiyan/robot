# -*- coding: utf-8 -*-
# @Author : yanpengfei
# @time   : 2018/9/7 下午6:21
# @File   : HttpRequest.py

from app.lib.BaseRequest import BaseRequest


class HttpRequest(BaseRequest):

    def __init__(self,url):
        super().__init__(url)

    def get(self,params,**kwargs):
        return super().get(params=params,**kwargs)

    def post(self,params=None,data=None,**kwargs):
        return super().post(params,data,**kwargs)


h = HttpRequest('http://127.0.0.1:5000').get(params=None,headers={},cookies={})
print(h)

