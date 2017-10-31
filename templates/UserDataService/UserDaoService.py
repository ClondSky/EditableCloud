# -*- coding: utf-8 -*-
from abc import ABCMeta, abstractmethod


class UserDaoService(object):
    __metaclass__ = ABCMeta  # 指定抽象类

    @abstractmethod
    def insert_user(self, user):
        pass

    def get_user_by_username(self, username):
        pass

    def save_user_info(self,user):
        pass

    def login(self, user):
        pass