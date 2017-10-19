# -*- coding: utf-8 -*-
import requests
import datetime
import base64, hmac, hashlib


class CloudService(object):
    __timeFormat__ = "%a, %d %b %G %T %z +0800"
    __endPoint__ = "oos.ctyunapi.cn"

    def __init__(self, bucket, port, ak, sk):
        self.__bucket__ = bucket
        self.__port__ = port
        self.__ak__ = ak
        self.__sk__ = sk

    def set_bucket(self, bucket):
        self.__bucket__ = bucket

    def get_bucket(self):
        return self.__bucket__

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

    def createBucket(self):
        url = "http://" + self.__endPoint__
        myHeader = {
            "Host": self.__bucket__ + "." + self.__endPoint__,
            "Content-Length": "0",
            "Expires": "1241251512412",
            "Date": self.getDate(),
            "Authorization": self.authorize("PUT", self.getDate(), "")
        }
        request = requests.put(url, headers=myHeader)
        return request.headers

    def getDate(self):
        now = datetime.datetime.now()
        time = now.strftime(self.__timeFormat__)
        return time

    def authorize(self, httpVerb, date, objectName):
        CanonicalizedAmzHeaders = ""
        CanonicalizedResource = "/" + self.__bucket__ + "/" + objectName
        StringToSign = httpVerb + "\n\n\n" + date + "\n" + CanonicalizedAmzHeaders + CanonicalizedResource
        print(StringToSign)
        signature = base64.b64encode(
            hmac.new(bytes(self.__sk__, encoding="utf-8"), bytes(StringToSign, encoding="utf-8"), "SHA1").digest())
        authorization = "AWS " + self.__ak__ + ":" + str(signature).split('\'')[1]
        print(authorization)
        return authorization
