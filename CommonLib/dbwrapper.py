# !/usr/bin/env python
# encoding:utf-8

# 将本工程的相关目录添加到路径内
# import sys
# sys.path.append("./")
# sys.path.append("../data/")

import pymysql
from CommonLib.config import Config


class DBWrapper:

    conn = None
    cursor = None
    is_connected = False

    def connect(self):
        is_succeed = True

        try:
            config = Config()
            self.is_connected = False
            # config_info = config.Config()

            db_add = Config.get_db_ip()
            db_port = Config.get_db_port()
            db_usr = Config.get_db_usr()
            db_pwd = Config.get_db_pwd()
            db_name = Config.get_db_name()
            db_charset = Config.get_db_charset()

            # creat the db connection
            # conn = pymysql.connect(db_add, db_port, db_usr, db_pwd, db_name, db_charset)
            conn = pymysql.connect(db=db_name, user=db_usr, passwd=db_pwd, host=db_add, port=db_port,
                                   charset=db_charset)
            conn.autocommit(True)
            self.is_connected = True
            # create the cursor
            self.cursor = conn.cursor()
            self.conn = conn
        except Exception as e:
            print(e.message)
            is_succeed = False
        else:
            pass
        finally:
            pass

        return is_succeed

    def close(self):
        is_succeed = True

        try:
            if self.is_connected:
                if self.cursor is not None:
                    self.cursor.close()
                if self.conn is not None:
                    self.conn.close()
        except Exception as e:
            print(e.message)
            is_succeed = False
        else:
            pass
        finally:
            pass

        return is_succeed

    def get_cursor(self):
        return self.cursor

    def get_connection(self):
        return self.conn
