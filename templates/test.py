# -*- coding: utf-8 -*-

from templates.oosApi.OOS import CloudService

cloudService = CloudService("c4582dec5d0809103126",
                            "47c783687d4c452c5d71b817b8c481915fb0094a")

#print(cloudService.create_bucket("surevil"))
# print(cloudService.modifyBucketACL("public-read-write", "fafaaaa"))
# print(cloudService.uploadLocalFile("fafaaaa", "index.txt", "C:\\Users\\zz\\Desktop\\index.html"))
# print(cloudService.dowmloadFile("fafaaaa", "index.txt", "C:\\Users\\zz\\Desktop\\index.txt"))
# print(cloudService.shareFile("fafaaaa", "index.txt", 7))
# print(cloudService.deleteFile("fafaaaa", "index.txt"))
# print(cloudService.create_ak_sk())
# print(cloudService.updateAkSk("5267b10a021b9fbac2ba"))
# print(cloudService.deleteBucket("lalaa"))
print(cloudService.upload_multipart_file("surevil", "index.txt", "C:\\Users\\zz\\Desktop\\index.html"))

# from templates.UserData.UserDao import UserDao
# from templates.Model.User import User

# user = User(userName="456", passWord="zlz")
# userService = UserDao()
# userService.insertUser(user)
# print(userService.getUserByUserName("456").userName)
