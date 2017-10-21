# -*- coding: utf-8 -*-
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
basedir = os.path.abspath("templates")  # 获得根目录
sqlpath = "sqlite:///" + basedir + "\\TYCloud.db"
print(sqlpath)
sql_db = create_engine("sqlite+pysqlite:///L:/TYcloud/EditableCloud/templates/oosApi/templates/TYCloud.db", echo=True)
DB_session = sessionmaker(bind=sql_db)
