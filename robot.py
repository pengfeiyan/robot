# -*- coding: utf-8 -*-
# @Author : yanpengfei
# @time   : 2018/9/27 下午2:39
# @File   : robot.py

from app import create_app

app = create_app()

if __name__ == '__main__':

    app.run(host='localhost',debug=True)