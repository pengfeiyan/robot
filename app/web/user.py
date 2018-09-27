# -*- coding: utf-8 -*-
# @Author : yanpengfei
# @time   : 2018/9/27 下午2:36
# @File   : user.py

from flask import request

from . import web

from app.form.user import UserForm
from app.service.user import UserService
from app.lib.Response import Response

@web.route('/login',methods=['POST'])
def login():
    user_form = UserForm(request.form)

    if user_form.validate():
        user_service = UserService(user_form.data)
        result = user_service.login()
        return Response.successByMessage(em='登陆成功',data=result)
    else:
        return Response.errorByMessage(em='参数校验失败')



