# -*- coding: utf-8 -*-
# @Author : yanpengfei
# @time   : 2018/9/27 下午3:26
# @File   : user.py


from app.lib.MysqlConfig import MysqlConfig

class UserModel():

    __table_name = 'r_user'
    __column_id = 'id'
    __column_username = 'username'
    __column_nickname = 'nickname'
    __column_password = 'password'
    __column_role = 'role'
    __column_is_deleted = 'is_deleted'
    __column_createtime = 'createtime'
    __column_updatetime = 'updatetime'

    def login(self,username,password):

        cursor = MysqlConfig().cursor
        sql = 'select id,nickname from r_user where username=\'{username}\' and password =\'{password}\' and is_deleted = 0;'\
            .format(
                username=username,
                password=password
            )

        try:
            with cursor:
                count_num = cursor.execute(sql)
        except Exception:
            return None
        else:
            if count_num == 1:
                user_info = cursor.fetchone()
                return user_info
            else:
                return None
        finally:
            cursor.close()


