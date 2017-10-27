# -*- coding: utf-8 -*-
from abc import ABCMeta, abstractmethod


class UserDaoService(object):
    __metaclass__ = ABCMeta  # 指定抽象类

    @abstractmethod
    def insertUser(self, user):
        pass

    def getUserByUserName(self, userName):
        pass

    def saveUserInfo(self,user):
        pass

    def login(self, user):
        pass