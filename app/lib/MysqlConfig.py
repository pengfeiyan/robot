# -*- coding: utf-8 -*-
# @Author : yanpengfei
# @time   : 2018/9/27 下午4:56
# @File   : MysqlConfig.py

from app.config.system import MYSQL_HOST,MYSQL_PORT,MYSQL_USER,MYSQL_PASSWORD,MYSQL_DB
import pymysql

class MysqlConfig(object):

    __curser_obj = None

    def __init__(self):

        self.__host = MYSQL_HOST
        self.__port = MYSQL_PORT
        self.__user = MYSQL_USER
        self.__password = MYSQL_PASSWORD
        self.__db = MYSQL_DB

        try:
            self.__curser_obj = self.db_connect().cursor()
        except Exception:
            pass


    def db_connect(self):

        conn = pymysql.connect(
                    host = self.__host,
                    port = self.__port,
                    user = self.__user,
                    password = self.__password,
                    db = self.__db
                )

        return conn

    @property
    def cursor(self):
        return self.__curser_obj




