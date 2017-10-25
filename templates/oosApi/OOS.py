# -*- coding: utf-8 -*-
import requests
import datetime
import time
import urllib
import base64
import hmac

from templates.ResultMessage import ResultMessage


class CloudService(object):
    __contentType__ = {"txt": "text/plain", "jpg": "image/jpeg"}
    __timeFormat__ = "%a, %d %b %G %T %z +0800"
    __endPoint__ = "oos.ctyunapi.cn"
    __keyEndPoint__ = "oos-iam.ctyunapi.cn"  # 所有AK/SK相关的操作，用此地址
    __port__ = "80"

    def __init__(self, ak, sk):
        self.__ak__ = ak
        self.__sk__ = sk

    def set_port(self, port):
        self.__port__ = port

    def get_port(self):
        return self.__port__

    def set_ak(self, ak):
        self.__ak__ = ak

    def get_ak(self):
        return self.__ak__

    def set_sk(self, sk):
        self.__sk__ = sk

    def get_sk(self):
        self.__sk__

    # 创建Bucket
    def createBucket(self, bucket):
        url = "http://" + self.__endPoint__
        myHeader = {
            "Host": bucket + "." + self.__endPoint__,
            "Content-Length": "0",
            "Date": self.getDate(),
            "Authorization": self.authorize("PUT", bucket, self.getDate())
        }
        request = requests.put(url, headers=myHeader)
        if request.status_code == 200:
            return ResultMessage.Success
        else:
            return ResultMessage.Wrong

    # 修改Bucket的权限，即ACL
    def modifyBucketACL(self, acl, bucket):
        url = "http://" + self.__endPoint__
        myHeader = {
            "Host": bucket + "." + self.__endPoint__,
            "Content-Length": "0",
            "Date": self.getDate(),
            "x-amz-acl": acl,
            "Authorization": self.authorize("PUT", bucket, self.getDate(), "", "x-amz-acl:" + acl)
        }
        request = requests.put(url, headers=myHeader)
        if request.status_code == 200:
            return ResultMessage.Success
        else:
            return ResultMessage.Wrong

    # 通过Put方式上传本地文件
    def uploadLocalFile(self, bucket, objectName, filePath):
        # 读取文件
        try:
            file = open(filePath, "rb")
            content = file.read()
        except:
            print("wrong file path")
            return ResultMessage.FilePathWrong
        finally:
            file.close()

        url = "http://" + self.__endPoint__ + "/" + objectName
        myHeader = {
            "Host": bucket + "." + self.__endPoint__,
            "Date": self.getDate(),
            "Content-length": str(len(content)),
            "Content-Type": self.__contentType__[objectName.split(".")[1]],
            "Authorization": self.authorize("PUT", bucket, self.getDate(), objectName, "",
                                            self.__contentType__[objectName.split(".")[1]])
        }
        request = requests.put(url, headers=myHeader, data=content)
        if request.status_code == 200:
            return ResultMessage.Success
        else:
            return ResultMessage.Wrong

    # 下载已上传的Object到本地
    def dowmloadFile(self, bucket, objectName, filePath):
        url = "http://" + self.__endPoint__ + "/" + objectName
        myHeader = {
            "Host": bucket + "." + self.__endPoint__,
            "Date": self.getDate(),
            "Authorization": self.authorize("GET", bucket, self.getDate(), objectName)
        }
        request = requests.get(url, headers=myHeader)

        # 写入文件
        try:
            file = open(filePath, "wb")
            content = request.content
            file.write(content)
        except:
            print("wrong file path")
            return ResultMessage.FilePathWrong
        finally:
            file.close()

        if request.status_code == 200:
            return ResultMessage.Success
        else:
            return ResultMessage.Wrong

    # 分享已上传的Object，URL有效期为一周
    def shareFile(self, bucket, objectName, expiration):
        expireTime = str(int(time.time()) + expiration * 24 * 60 * 60)
        params = urllib.parse.urlencode({
            "AWSAccessKeyId": self.__ak__,
            "Expires": expireTime,
            "Signature": self.authorize("GET", bucket, expireTime, objectName).split(":")[1]
        })
        return "http://oos.ctyunapi.cn/" \
               + bucket \
               + "/" + objectName \
               + "?" + params

    # 删除已上传的Object
    def deleteFile(self, bucket, objectName):
        url = "http://" + self.__endPoint__ + "/" + objectName
        myHeader = {
            "Host": bucket + "." + self.__endPoint__,
            "Date": self.getDate(),
            "Authorization": self.authorize("DELETE", bucket, self.getDate(), objectName)
        }
        request = requests.delete(url, headers=myHeader)
        if request.status_code == 200 or request.status_code == 204:
            return ResultMessage.Success
        else:
            return ResultMessage.Wrong

    # 创建一组AK/SK
    def createAkSk(self):
        url = "http://" + self.__keyEndPoint__
        params = {
            "Action": "CreateAccessKey"
        }
        myHeader = {
            "Host": self.__keyEndPoint__,
            "Date": self.getDate(),
            "Authorization": self.authorize("POST", "", self.getDate())
        }
        request = requests.post(url, headers=myHeader, data=params)
        print(request.status_code)
        print(request.content)
        if request.status_code == 200:
            return ResultMessage.Success
        else:
            return ResultMessage.Wrong

    # 更改AK/SK属性（主秘钥/普通秘钥）
    def updateAkSk(self, keyId):
        url = "http://" + self.__keyEndPoint__
        params = {
            "Action": "UpdateAccessKey",
            "AccessKeyId": keyId,
            "Status": "active",
            "isPrimary": "false"
        }
        myHeader = {
            "Host": self.__keyEndPoint__,
            "Date": self.getDate(),
            "Authorization": self.authorize("POST", "", self.getDate())
        }
        request = requests.post(url, headers=myHeader, data=params)
        print(request.status_code)
        print(request.content)
        if request.status_code == 200:
            return ResultMessage.Success
        else:
            return ResultMessage.Wrong

    # 删除已创建的Bucket
    def deleteBucket(self, bucket):
        url = "http://" + self.__endPoint__
        myHeader = {
            "Host": bucket + "." + self.__endPoint__,
            "Date": self.getDate(),
            "Authorization": self.authorize("DELETE", bucket, self.getDate())
        }
        request = requests.delete(url, headers=myHeader)
        if request.status_code == 200 or request.status_code == 204:
            return ResultMessage.Success
        else:
            return ResultMessage.Wrong

    # 获得需要格式的日期
    def getDate(self):
        now = datetime.datetime.now()
        time = now.strftime(self.__timeFormat__)
        return time

    # 计算授权字符串
    def authorize(self, httpVerb="GET", bucket="", date="", objectName="", amz="", contentType=""):
        CanonicalizedAmzHeaders = ""
        if bucket == "":
            CanonicalizedResource = ""
        else:
            CanonicalizedResource = "/" + bucket + "/" + objectName

        # amzHeaders
        if amz != "":
            CanonicalizedAmzHeaders += amz + "\n"

        StringToSign = httpVerb + "\n" \
                       + "" + "\n" \
                       + contentType + "\n" \
                       + date + "\n" \
                       + CanonicalizedAmzHeaders + CanonicalizedResource

        print(StringToSign)
        signature = base64.b64encode(
            hmac.new(bytes(self.__sk__, encoding="utf-8"), bytes(StringToSign, encoding="utf-8"), "SHA1").digest())
        authorization = "AWS " + self.__ak__ + ":" + str(signature).split('\'')[1]
        print(authorization)
        return authorization
