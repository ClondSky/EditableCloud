# -*- coding: utf-8 -*-
from templates.Model import Base
from sqlalchemy import Column, Integer, CHAR


class User(Base):
    __tablename__ = "User"
    userName = Column(CHAR(20), primary_key=True)
    passWord = Column(CHAR(20))
    email = Column(CHAR(30))
