# -*- coding: utf-8 -*-

from templates.UserDataService.UserDaoService import UserDaoService
from templates.Model import DB_session
from templates.Model.User import User
from templates.ResultMessage import ResultMessage


class UserDao(UserDaoService):
    def __init__(self):
        pass

    def insert_user(self, user):
        try:
            session = DB_session()
            session.add(user)
            session.commit()
        except:
            print("insertUser wrong")
            return ResultMessage.InsertUserWrong
        finally:
            session.close()

    def get_user_by_username(self, username):
        try:
            session = DB_session()
            user = session.query(User).filter(User.userName == username).one()
            return user
        except:
            print("getUserByUserName wrong")
            return ResultMessage.GetUserWrong
        finally:
            session.close()

    # 保存用户信息
    def save_user_info(self, user):
        # 一系列数据库操作
        return user.email + " success"

    # 验证登录
    def login(self, user):
        # 一系列数据库操作
        try:
            session = DB_session()
            PASSWORD = session.query(User.PASSWORD).filter(User.EMAIL == user.EMAIL).one()
            if(PASSWORD[0]==user.PASSWORD):
                return ResultMessage.Success
            else:
                return ResultMessage.Wrong
        except:
            print("getUserByUserName wrong")
            return ResultMessage.GetUserWrong
        finally:
            session.close()
