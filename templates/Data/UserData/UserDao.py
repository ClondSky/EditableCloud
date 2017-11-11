# -*- coding: utf-8 -*-

from templates.Model import DB_session
from templates.Model.User import User
from templates.ResultMessage import ResultMessage


class UserDao(object):
    def __init__(self):
        pass

    def insert_user(self, user):
        try:
            session = DB_session()
            session.add(user)
            session.commit()
            return  ResultMessage.Success
        except:
            print("insertUser wrong")
            return ResultMessage.UserExist
        finally:
            session.close()

    def get_password_by_email(self, email):
        try:
            session = DB_session()
            PASSWORD = session.query(User.PASSWORD).filter(User.EMAIL == email).one()[0]
            return PASSWORD
        except:
            print("getUserByUserName wrong")
            return ResultMessage.GetUserWrong
        finally:
            session.close()



