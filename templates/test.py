# -*- coding: utf-8 -*-

from templates.oosApi.OOS import CloudService

cloudService = CloudService("oos.ctyunapi.cn", "80", "622ff0aad8c78a306eaa",
                            "c4a84bcc4ce1ad09805def0284a07452dd7a7519")

# print(cloudService.createBucket("lal"))
# print(cloudService.modifyBucketACL("public-read-write", "lal"))
print(cloudService.uploadLocalFile("surevil", "index.txt", "C:\\Users\\zz\\Desktop\\index.html"))
#print(cloudService.shareFile("surevil", "hackathon.jpg", 30))
# print(cloudService.deleteFile("surevil", "index.html"))

# from templates.UserData.UserDao import UserDao
# from templates.PO.User import User

# user = User(userName="456", passWord="zlz")
# userService = UserDao()
# userService.insertUser(user)
# print(userService.getUserByUserName("456").userName)
