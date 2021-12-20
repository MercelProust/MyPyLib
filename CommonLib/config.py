# !/usr/bin/env python
# encoding:utf-8

# This is a module to get config info
# and this is using singleton pattern


# class ConfigSingleton(type):
#     def __init__(cls, name, bases, dict):
#         super(ConfigSingleton, cls).__init__(name, bases, dict)
#         cls._instance = None
#
#     def __call__(cls, *args, **kw):
#         if cls._instance is None:
#             cls._instance = super(ConfigSingleton, cls).__call__(*args, **kw)
#         return cls._instance
 
# public class to be called in other module


class Config(object):
    # __metaclass__ = ConfigSingleton

    @classmethod
    def get_db_ip(cls):
        return "10.10.81.142"

    @classmethod
    def get_db_port(cls):
        return 3306

    @classmethod
    def get_db_usr(cls):
        return "root"

    @classmethod
    def get_db_pwd(cls):
        return "123456"

    @classmethod
    def get_db_name(cls):
        return 'otadb'

    @classmethod
    def get_db_charset(cls):
        return "utf8"
