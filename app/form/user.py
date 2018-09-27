# -*- coding: utf-8 -*-
# @Author : yanpengfei
# @time   : 2018/9/27 下午2:48
# @File   : user.py

from wtforms import Form,StringField,PasswordField
from wtforms.validators import DataRequired,Length

class UserForm(Form):

    username = StringField(
        validators=[
            DataRequired(message='登陆用户名必填'),
            Length(4,32,message='登陆用户名长度应在4到32位之间')
        ]
    )

    password = PasswordField(
        validators=[
            DataRequired(message='登陆密码必填'),
            Length(6,20,message='登陆密码长度应在6到20位之间')
        ]
    )