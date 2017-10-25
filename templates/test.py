# -*- coding: utf-8 -*-

from templates.oosApi.OOS import CloudService

cloudService = CloudService("622ff0aad8c78a306eaa",
                            "c4a84bcc4ce1ad09805def0284a07452dd7a7519")

# print(cloudService.createBucket("fafaaaa"))
# print(cloudService.modifyBucketACL("public-read-write", "fafaaaa"))
# print(cloudService.uploadLocalFile("fafaaaa", "index.txt", "C:\\Users\\zz\\Desktop\\index.html"))
# print(cloudService.dowmloadFile("fafaaaa", "index.txt", "C:\\Users\\zz\\Desktop\\index.txt"))
# print(cloudService.shareFile("fafaaaa", "index.txt", 7))
# print(cloudService.deleteFile("fafaaaa", "index.txt"))
print(cloudService.createAkSk())
# print(cloudService.updateAkSk("5267b10a021b9fbac2ba"))
# print(cloudService.deleteBucket("lalaa"))

# from templates.UserData.UserDao import UserDao
# from templates.PO.User import User

# user = User(userName="456", passWord="zlz")
# userService = UserDao()
# userService.insertUser(user)
# print(userService.getUserByUserName("456").userName)
