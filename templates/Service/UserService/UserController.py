# -*- coding: utf-8 -*-

from templates.Factory.DataFactory import userDao
from templates.ResultMessage import ResultMessage


class UserController(object):
    def __init__(self):
        pass

    def login(self, user):
        password = userDao.get_password_by_email(user.EMAIL)
        if (password == user.PASSWORD):
            return ResultMessage.Success
        else:
            return ResultMessage.Wrong

    def register(self,user):
        message=userDao.insert_user(user)
        return message

