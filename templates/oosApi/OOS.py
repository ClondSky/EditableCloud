# -*- coding: utf-8 -*-
import requests
import datetime
import base64, hmac, hashlib


class CloudService(object):
    __timeFormat__ = "%a, %d %b %G %T %z +0800"
    __endPoint__ = "oos.ctyunapi.cn"

    def __init__(self, host, port, ak, sk):
        self.__host__ = host
        self.__port__ = port
        self.__ak__ = ak
        self.__sk__ = sk

    def set_host(self, host):
        self.__host__ = host

    def get_host(self):
        return self.__host__

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

    #创建Bucket
    def createBucket(self, bucket):
        url = "http://" + self.__host__
        myHeader = {
            "Host": bucket + "." + self.__host__,
            "Content-Length": "0",
            "Date": self.getDate(),
            "Authorization": self.authorize("PUT", bucket, self.getDate(), "", "")
        }
        request = requests.put(url, headers=myHeader)
        return request.headers

    #修改Bucket的权限，即ACL
    def modifyBucketACL(self, acl, bucket):
        url = "http://" + self.__host__
        myHeader = {
            "Host": bucket + "." + self.__host__,
            "Content-Length": "0",
            "Date": self.getDate(),
            "x-amz-acl": acl,
            "Authorization": self.authorize("PUT", bucket, self.getDate(), "", "x-amz-acl:" + acl)
        }
        request = requests.put(url, headers=myHeader)
        return request.content

    def getDate(self):
        now = datetime.datetime.now()
        time = now.strftime(self.__timeFormat__)
        return time

    def authorize(self, httpVerb, bucket, date, objectName, amz):
        CanonicalizedAmzHeaders = amz+"\n"
        CanonicalizedResource = "/" + bucket + "/" + objectName
        StringToSign = httpVerb + "\n\n\n" + date + "\n" + CanonicalizedAmzHeaders + CanonicalizedResource
        signature = base64.b64encode(
            hmac.new(bytes(self.__sk__, encoding="utf-8"), bytes(StringToSign, encoding="utf-8"), "SHA1").digest())
        authorization = "AWS " + self.__ak__ + ":" + str(signature).split('\'')[1]
        print(authorization)
        return authorization
