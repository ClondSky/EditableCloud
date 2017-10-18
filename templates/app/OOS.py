# -*- coding: utf-8 -*-
import requests
import datetime
import base64, hmac, hashlib


class CloudService(object):
    __timeFormat__ = "%a, %d %b %G %T GMT"

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

    def createBucket(self):
        url = "oos.ctyunapi.cn"
        myHeader = {
            "Host": self.__host__,
            "Content-Length": "0",
            "Date": self.getDate(),
            "Authorization": self.authorize("PUT", self.getDate(), "", "")
        }
        request = requests.put(url, header=myHeader)
        return request.headers

    def getDate(self):
        now = datetime.datetime.now()
        time = now.strftime(self.__timeFormat__)
        return time

    def authorize(self, httpVerb, date, bucket, objectName):
        StringToSign = httpVerb + "\n"
        signature = base64.b64encode(hmac.new(self.__sk__, StringToSign).digest())
        authorization = "AWS" + self.__ak__ + ":" + signature
        return authorization
