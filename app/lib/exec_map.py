# -*- coding: utf-8 -*-
# @Author : yanpengfei
# @time   : 2018/9/26 下午2:42
# @File   : exec_map.py

import threading

_map_lock = threading.Lock()
_global_exec_map = set()


def check_exist_in_map(project,api,case,suite=0,task=0):
    '''
    :param project: 项目id，必传
    :param api: 接口id，必传
    :param case: 用例id，必传
    :param suite: 用例集合id，不必传，默认0，当有suite运行的时候，必传
    :param task: 任务id，不必传，默认0，当有task运行的时候，必传
    :return: 是否在运行中，是：返回True，否：返回False，为True时不能删除和修改。
    '''
    return (project,api,case,suite,task) in _global_exec_map

def add_signal_to_map(project,api,case,suite=0,task=0):
    '''
    :param project: 项目id，必传
    :param api: 接口id，必传
    :param case: 用例id，必传
    :param suite: 用例集合id，不必传，默认0，当有suite运行的时候，必传
    :param task: 任务id，不必传，默认0，当有task运行的时候，必传
    '''
    with _map_lock:
        _global_exec_map.add((project,api,case,suite,task))

def del_signal_from_map(project,api,case,suite=0,task=0):
    '''
    :param project: 项目id，必传
    :param api: 接口id，必传
    :param case: 用例id，必传
    :param suite: 用例集合id，不必传，默认0，当有suite运行的时候，必传
    :param task: 任务id，不必传，默认0，当有task运行的时候，必传
    '''
    with _map_lock:
        if (project,api,case,suite,task) in _global_exec_map:
            _global_exec_map.remove((project,api,case,suite,task))