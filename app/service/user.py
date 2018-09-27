# -*- coding: utf-8 -*-
# @Author : yanpengfei
# @time   : 2018/9/27 下午3:26
# @File   : user.py

from hashlib import md5

from app.config.system import SECRET_KEY
from app.model.user import UserModel
from app.lib.Response import Response

class UserService(object):



    def __init__(self,form_data):
        self.username = form_data.get('username')
        self.password = form_data.get('password')


    def login(self):

        user_model = UserModel()

        key = SECRET_KEY
        password = self.password+key
        self.password = md5(password.encode('utf8')).hexdigest()

        model_result = user_model.login(self.username,self.password)

        if model_result:
            data = {
                'id': model_result[0],
                'nickname':model_result[1]
            }
            return data
        else:
            return None


