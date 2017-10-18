from requests import request


class CloudService(object):
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
        pass

    def authorize(httpVerb, date, bucket, objectName):
        pass
