# -*- coding: utf-8 -*-
# @Author : yanpengfei
# @time   : 2018/9/7 下午6:15
# @File   : BaseRequest.py

import requests
from json.decoder import JSONDecodeError
from requests.exceptions import Timeout,HTTPError,ConnectionError

from app.lib.Response import Response

class BaseRequest(object):

    __headers = None
    __cookies = None
    __trycount = 3
    __timeout = 3

    def __init__(self,url=None):

        if not url:
            print('url不能为空')
        else:
            self.__url = url

    def get(self,params=dict(),**kwargs):
        '''
        基于requests的封装类，改进了一下get和post方法。post方法改进同get方法。

        http请求正常并且返回结果为json格式的，get方法会返回json格式的返回结果。
        如果服务器连接正常，返回结果不是json格式的，get方法会返回content的内容。
        如果服务器连接正常，但请求失败比如404，则返回<response>类型的结果。
        如果服务器连接错误，比如拒绝连接，dns解析错误，则返回None类型。
        '''

        if 'headers' in kwargs.keys():
            self.__headers = kwargs['headers']
        if 'cookies' in kwargs.keys():
            self.__cookies = kwargs['cookies']

        res = None

        while(self.__trycount > 0):
            try:
                res = requests.get(url=self.__url, params=params,headers=self.__headers,cookies=self.__cookies,
                                   timeout=self.__timeout)
                res.raise_for_status()
                res = res.json()
            except JSONDecodeError:
                return Response.errorByMessage(ec=2,em='接口返回结果不是json格式')
            except Timeout:
                print('连接超时')
                self.__trycount -= 1
                continue
            except ConnectionError:
                print('连接错误，可能是DNS解析错误或者是拒绝连接')
                self.__trycount -= 1
                continue
            except HTTPError:
                print('HTTP错误')
                self.__trycount -= 1
                continue
            except Exception as e:
                print(str(e))
                self.__trycount -= 1
                continue
            else:
                break
        if self.__trycount == 0:
            print('尝试三次失败，连接异常')
            return Response.errorByMessage(ec=2, em='接口重试三次，无法请求')
        else:
            return Response.success(data=res)

    def post(self,params=None,data=None,**kwargs):

        if (params != None and data != None) or ( not params != None and not data !=None ):
            print('params和data必填一个')

        if 'headers' in kwargs.keys():
            self.__headers = kwargs['headers']
        if 'cookies' in kwargs.keys():
            self.__cookies = kwargs['cookies']

        if params != None:
            return self.__post_by_params(params=params,headers=self.__headers,cookies=self.__cookies)
        else:
            return self.__post_by_data(data=data,headers=self.__headers,cookies=self.__cookies)

    def __post_by_params(self,params,headers,cookies):

        res = None

        while(self.__trycount > 0):
            try:
                res = requests.post(url=self.__url,params=params,headers=headers,cookies=cookies,
                                        timeout=self.__timeout)
                res.raise_for_status()
                res = res.json()
            except JSONDecodeError:
                return Response.errorByMessage(ec=2, em='接口返回结果不是json格式')
            except Timeout:
                print('连接超时')
                self.__trycount -= 1
                continue
            except ConnectionError:
                print('连接错误，可能是DNS解析错误或者是拒绝连接')
                self.__trycount -= 1
                continue
            except HTTPError:
                print('HTTP错误')
                self.__trycount -= 1
                continue
            except Exception as e:
                print(str(e))
                self.__trycount -= 1
                continue
            else:
                break
        if self.__trycount == 0:
            print('尝试三次失败，连接异常')
            return Response.errorByMessage(ec=2, em='接口重试三次，无法请求')
        else:
            return Response.success(data=res)

    def __post_by_data(self,data,headers,cookies):

        res = None

        while(self.__trycount > 0):
            try:
                res = requests.post(url=self.__url,data=data,headers=headers,cookies=cookies,
                                        timeout=self.__timeout)
                res.raise_for_status()
                res = res.json()
            except JSONDecodeError:
                return Response.errorByMessage(ec=2, em='接口返回结果不是json格式')
            except Timeout:
                print('连接超时')
                self.__trycount -= 1
                continue
            except ConnectionError:
                print('连接错误，可能是DNS解析错误或者是拒绝连接')
                self.__trycount -= 1
                continue
            except HTTPError:
                print('HTTP错误')
                self.__trycount -= 1
                continue
            except Exception as e:
                print(str(e))
                self.__trycount -= 1
                continue
            else:
                break
        if self.__trycount == 0:
            print('尝试三次失败，连接异常')
            return Response.errorByMessage(ec=2, em='接口重试三次，无法请求')
        else:
            return Response.success(data=res)





