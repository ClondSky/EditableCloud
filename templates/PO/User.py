# -*- coding: utf-8 -*-
from templates.PO import Base
from sqlalchemy import Column, Integer, CHAR


class User(Base):
    __tablename__ = "User"
    userName = Column(CHAR(20), primary_key=True)
    passWord = Column(CHAR(20))
