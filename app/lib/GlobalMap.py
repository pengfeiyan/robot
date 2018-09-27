# -*- coding: utf-8 -*-
# @Author : yanpengfei
# @time   : 2018/9/26 下午4:51
# @File   : GlobalMap.py


class GlobalMap():

    __global_map = {}

    @classmethod
    def get(cls,key):

        if not key:
            return None

        if key in cls.__global_map.keys():
            return cls.__global_map.get(key)
        else:
            return None

    @classmethod
    def set(cls,key,value=None):

        if not key:
            print('key不能为空')

        cls.__global_map[key] = value



