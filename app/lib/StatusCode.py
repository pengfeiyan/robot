# -*- coding: utf-8 -*-
# @Author : yanpengfei
# @time   : 2018/9/11 下午4:01
# @File   : StatusCode.py

from enum import Enum,unique


@unique
class StatusCode(Enum):

    SUCCESS = 100
    SUCCESS_MSG = '成功'

    ERROR = 0
    ERROR_MSG = '失败'

    UNAUTHORIZED = 101
    UNAUTHORIZED_MSG = '未授权，请先登陆'

    DATABASE_ERROR = 102
    DATABASE_ERROR_MSG = '数据库操作失败'
