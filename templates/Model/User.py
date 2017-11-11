# -*- coding: utf-8 -*-
from templates.Model import Base
from sqlalchemy import Column, Integer, CHAR,TEXT


class User(Base):
    __tablename__ = "USER"
    ID=Column(Integer,primary_key=True)
    NAME = Column(TEXT,nullable=False)
    EMAIL = Column(TEXT,nullable=False)
    PASSWORD = Column(TEXT,nullable=False)
    PHONE=Column(TEXT)
    ADDRESS=Column(TEXT)
    COMPANYNAME=Column(TEXT)
    LINKMAN=Column(TEXT)

