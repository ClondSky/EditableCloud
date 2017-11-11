# -*- coding: utf-8 -*-

#from templates.oosApi.OOS import CloudService

#cloudService = CloudService("c4582dec5d0809103126",
#                            "47c783687d4c452c5d71b817b8c481915fb0094a")

#print(cloudService.create_bucket("surevil"))
# print(cloudService.modifyBucketACL("public-read-write", "fafaaaa"))
# print(cloudService.uploadLocalFile("fafaaaa", "index.txt", "C:\\Users\\zz\\Desktop\\index.html"))
# print(cloudService.dowmloadFile("fafaaaa", "index.txt", "C:\\Users\\zz\\Desktop\\index.txt"))
# print(cloudService.shareFile("fafaaaa", "index.txt", 7))
# print(cloudService.deleteFile("fafaaaa", "index.txt"))
#print(cloudService.create_ak_sk())
# print(cloudService.updateAkSk("5267b10a021b9fbac2ba"))
# print(cloudService.deleteBucket("lalaa"))
#print(cloudService.upload_multipart_file("surevil", "index.txt", "C:\\Users\\zz\\Desktop\\index.html"))

#from templates.Factory.ServiceFactory import userService
#from templates.Model.User import User

#user = User(EMAIL="123456789@qq.com", PASSWORD="123456")
# userDao.insert_user(user)
#print(userService.login(user))

import sqlite3
conn=sqlite3.connect('TYCloud.db')
c=conn.cursor()

'''c.execute(''CREATE TABLE USER(
     ID integer PRIMARY KEY AUTOINCREMENT,
     NAME TEXT,
     EMAIL TEXT NOT NULL UNIQUE,
     PASSWORD TEXT NOT NULL,
     PHONE TEXT,
     ADDRESS TEXT,
     COMPANYNAME TEXT,
     LINKMAN TEXT);'')
'''
         

#curson=c.execute("DROP TABLE USER")
cursor=c.execute("SELECT ID,NAME,EMAIL,PASSWORD from USER")
for row in cursor:
   print("ID = ", row[0])
   print("NAME = ", row[1])
   print ("EMAIL = ", row[2])
   print ("PASSWORD = ", row[3], "\n")

conn.close()