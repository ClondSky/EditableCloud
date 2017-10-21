# -*- coding: utf-8 -*-
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
sql_db = create_engine("sqlite:///TYCloud.db", echo=True)
DB_session = sessionmaker(bind=sql_db)
