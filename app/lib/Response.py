# -*- coding: utf-8 -*-
# @Author : yanpengfei
# @time   : 2018/9/11 下午3:56
# @File   : Response.py

from app.lib.StatusCode import StatusCode
from flask import jsonify

class Response(object):

    @classmethod
    def success(cls,data={}):

        response = {}

        response['ec'] = StatusCode.SUCCESS.value
        response['em'] = StatusCode.SUCCESS_MSG.value
        response['data'] = data

        return jsonify(response)

    @classmethod
    def successByMessage(cls,em,data={}):

        response = {}

        response['ec'] = StatusCode.SUCCESS.value
        response['em'] = em
        response['data'] = data

        return jsonify(response)

    @classmethod
    def errorByMessage(cls,ec=StatusCode.ERROR.value,em=StatusCode.ERROR_MSG.value):

        response = {}

        response['ec'] = ec
        response['em'] = em

        return jsonify(response)

    def force_type(cls, rv, environ=None):

        if isinstance(rv, dict):
            rv = jsonify(rv)
        return super(Response, cls).force_type(rv, environ)
