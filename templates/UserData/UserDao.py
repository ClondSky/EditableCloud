# -*- coding: utf-8 -*-

from templates.UserDataService.UserDaoService import UserDaoService
from templates.PO import DB_session
from templates.PO.User import User
from templates.ResultMessage import ResultMessage

class UserDao(UserDaoService):
    def __init__(self):
        pass

    def insertUser(self, user):
        try:
            session = DB_session()
            session.add(user)
            session.commit()
        except:
            print("insertUser wrong")
            return ResultMessage.InsertUserWrong
        finally:
            session.close()

    def getUserByUserName(self, userName):
        try:
            session = DB_session()
            user = session.query(User).filter(User.userName == userName).one()
            return user
        except:
            print("getUserByUserName wrong")
            return ResultMessage.GetUserWrong
        finally:
            session.close()
