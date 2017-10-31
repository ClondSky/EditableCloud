# -*- coding: utf-8 -*-
import requests
import datetime
import time
import urllib
import base64
import hmac

from templates.ResultMessage import ResultMessage


class CloudService(object):
    __contentType__ = {
        'html': 'text/html',
        'htm': 'text/html',
        'shtml': 'text/html',
        'css': 'text/css',
        'xml': 'text/xml',
        'gif': 'image/gif',
        'jpeg': 'image/jpeg',
        'jpg': 'image/jpeg',
        'js': 'application/x-javascript',
        'atom': 'application/atom+xml',
        'rss': 'application/rss+xml',
        'mml': 'text/mathml',
        'txt': 'text/plain',
        'jad': 'text/vnd.sun.j2me.app-descriptor',
        'wml': 'text/vnd.wap.wml',
        'htc': 'text/x-component',
        'png': 'image/png',
        'tif': 'image/tiff',
        'tiff': 'image/tiff',
        'wbmp': 'image/vnd.wap.wbmp',
        'ico': 'image/x-icon',
        'jng': 'image/x-jng',
        'bmp': 'image/x-ms-bmp',
        'svg': 'image/svg+xml',
        'svgz': 'image/svg+xml',
        'webp': 'image/webp',
        'jar': 'application/java-archive',
        'war': 'application/java-archive',
        'ear': 'application/java-archive',
        'hqx': 'application/mac-binhex40',
        'doc': 'application/msword',
        'pdf': 'application/pdf',
        'ps': 'application/postscript',
        'eps': 'application/postscript',
        'ai': 'application/postscript',
        'rtf': 'application/rtf',
        'xls': 'application/vnd.ms-excel',
        'ppt': 'application/vnd.ms-powerpoint',
        'wmlc': 'application/vnd.wap.wmlc',
        'kml': 'application/vnd.google-earth.kml+xml',
        'kmz': 'application/vnd.google-earth.kmz',
        '7z': 'application/x-7z-compressed',
        'cco': 'application/x-cocoa',
        'jardiff': 'application/x-java-archive-diff',
        'jnlp': 'application/x-java-jnlp-file',
        'run': 'application/x-makeself',
        'pl': 'application/x-perl',
        'pm': 'application/x-perl',
        'prc': 'application/x-pilot',
        'pdb': 'application/x-pilot',
        'rar': 'application/x-rar-compressed',
        'rpm': 'application/x-redhat-package-manager',
        'sea': 'application/x-sea',
        'swf': 'application/x-shockwave-flash',
        'sit': 'application/x-stuffit',
        'tcl': 'application/x-tcl',
        'tk': 'application/x-tcl',
        'der': 'application/x-x509-ca-cert',
        'pem': 'application/x-x509-ca-cert',
        'crt': 'application/x-x509-ca-cert',
        'xpi': 'application/x-xpinstall',
        'xhtml': 'application/xhtml+xml',
        'zip': 'application/zip',
        'bin': 'application/octet-stream',
        'exe': 'application/octet-stream',
        'dll': 'application/octet-stream',
        'deb': 'application/octet-stream',
        'dmg': 'application/octet-stream',
        'eot': 'application/octet-stream',
        'iso': 'application/octet-stream',
        'img': 'application/octet-stream',
        'msi': 'application/octet-stream',
        'msp': 'application/octet-stream',
        'msm': 'application/octet-stream',
        'mid': 'audio/midi',
        'midi': 'audio/midi',
        'kar': 'audio/midi',
        'mp3': 'audio/mpeg',
        'ogg': 'audio/ogg',
        'm4a': 'audio/x-m4a',
        'ra': 'audio/x-realaudio',
        '3gpp': 'video/3gpp',
        '3gp': 'video/3gpp',
        'mp4': 'video/mp4',
        'mpeg': 'video/mpeg',
        'mpg': 'video/mpeg',
        'mov': 'video/quicktime',
        'webm': 'video/webm',
        'flv': 'video/x-flv',
        'm4v': 'video/x-m4v',
        'mng': 'video/x-mng',
        'asx': 'video/x-ms-asf',
        'asf': 'video/x-ms-asf',
        'wmv': 'video/x-ms-wmv',
        'avi': 'video/x-msvideo'
    }
    __timeFormat__ = "%a, %d %b %G %T %z +0800"
    __endPoint__ = "oos-bj2.ctyunapi.cn"
    __keyEndPoint__ = "oos-bj2-iam.ctyunapi.cn"  # 所有AK/SK相关的操作，用此地址
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
    def create_bucket(self, bucket):
        url = "http://" + self.__endPoint__
        my_header = {
            "Host": bucket + "." + self.__endPoint__,
            "Content-Length": "0",
            "Date": self.get_date(),
            "Authorization": self.authorize("PUT", bucket, self.get_date())
        }
        request = requests.put(url, headers=my_header)
        print(request.content)
        if request.status_code == 200:
            return ResultMessage.Success
        else:
            return ResultMessage.Wrong

    # 修改Bucket的权限，即ACL
    def modify_bucket_acl(self, acl, bucket):
        url = "http://" + self.__endPoint__
        my_header = {
            "Host": bucket + "." + self.__endPoint__,
            "Content-Length": "0",
            "Date": self.get_date(),
            "x-amz-acl": acl,
            "Authorization": self.authorize("PUT", bucket, self.get_date(), "", "x-amz-acl:" + acl)
        }
        request = requests.put(url, headers=my_header)
        if request.status_code == 200:
            return ResultMessage.Success
        else:
            return ResultMessage.Wrong

    # 通过Put方式上传本地文件
    def upload_local_file(self, bucket, object_name, file_path):
        # 读取文件
        try:
            file = open(file_path, "rb")
            content = file.read()
        except:
            print("wrong file path")
            return ResultMessage.FilePathWrong
        finally:
            file.close()

        url = "http://" + self.__endPoint__ + "/" + object_name
        my_header = {
            "Host": bucket + "." + self.__endPoint__,
            "Date": self.get_date(),
            "Content-length": str(len(content)),
            "Content-Type": self.__contentType__[object_name.split(".")[1]],
            "Authorization": self.authorize("PUT", bucket, self.get_date(), object_name, "",
                                            self.__contentType__[object_name.split(".")[1]])
        }
        request = requests.put(url, headers=my_header, data=content)
        if request.status_code == 200:
            return ResultMessage.Success
        else:
            return ResultMessage.Wrong

    # 下载已上传的Object到本地
    def dowmload_file(self, bucket, object_name, file_path):
        url = "http://" + self.__endPoint__ + "/" + object_name
        my_header = {
            "Host": bucket + "." + self.__endPoint__,
            "Date": self.get_date(),
            "Authorization": self.authorize("GET", bucket, self.get_date(), object_name)
        }
        request = requests.get(url, headers=my_header)

        # 写入文件
        try:
            file = open(file_path, "wb")
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
    def share_file(self, bucket, object_name, expiration):
        expire_time = str(int(time.time()) + expiration * 24 * 60 * 60)
        params = urllib.parse.urlencode({
            "AWSAccessKeyId": self.__ak__,
            "Expires": expire_time,
            "Signature": self.authorize("GET", bucket, expire_time, object_name).split(":")[1]
        })
        return "http://oos.ctyunapi.cn/" \
               + bucket \
               + "/" + object_name \
               + "?" + params

    # 删除已上传的Object
    def delete_file(self, bucket, object_name):
        url = "http://" + self.__endPoint__ + "/" + object_name
        my_header = {
            "Host": bucket + "." + self.__endPoint__,
            "Date": self.get_date(),
            "Authorization": self.authorize("DELETE", bucket, self.get_date(), object_name)
        }
        request = requests.delete(url, headers=my_header)
        if request.status_code == 200 or request.status_code == 204:
            return ResultMessage.Success
        else:
            return ResultMessage.Wrong

    # 创建一组AK/SK
    def create_ak_sk(self):
        url = "http://" + self.__keyEndPoint__
        params = {
            "Action": "CreateAccessKey",
        }
        my_header = {
            "Host": self.__keyEndPoint__,
            "Date": self.get_date(),
            "Authorization": self.authorize("POST", "", self.get_date())
        }
        request = requests.post(url, headers=my_header, data=params)
        print(request.status_code)
        print(request.content)
        if request.status_code == 200:
            return ResultMessage.Success
        else:
            return ResultMessage.Wrong

    # 更改AK/SK属性（主秘钥/普通秘钥）
    def update_ak_sk(self, key_id):
        url = "http://" + self.__keyEndPoint__
        params = {
            "Action": "UpdateAccessKey",
            "AccessKeyId": key_id,
            "Status": "active",
            "isPrimary": "false"
        }
        my_header = {
            "Host": self.__keyEndPoint__,
            "Date": self.get_date(),
            "Authorization": self.authorize("POST", "", self.get_date())
        }
        request = requests.post(url, headers=my_header, data=params)
        print(request.status_code)
        print(request.content)
        if request.status_code == 200:
            return ResultMessage.Success
        else:
            return ResultMessage.Wrong

    # 删除已创建的Bucket
    def delete_bucket(self, bucket):
        url = "http://" + self.__endPoint__
        my_header = {
            "Host": bucket + "." + self.__endPoint__,
            "Date": self.get_date(),
            "Authorization": self.authorize("DELETE", bucket, self.get_date())
        }
        request = requests.delete(url, headers=my_header)
        if request.status_code == 200 or request.status_code == 204:
            return ResultMessage.Success
        else:
            return ResultMessage.Wrong

    # 分段上传一个本地文件
    def upload_multipart_file(self, bucket, object_name, file_path):
        # 初始化文件上传
        url = "http://" + self.__endPoint__ + "/" + object_name
        my_header = {
            "Host": bucket + "." + self.__endPoint__,
            "Date": self.get_date(),
            "Authorization": self.authorize("POST"+ "/" + object_name + "?uploads", bucket, self.get_date(), object_name, "",
                                             uri_resource="?uploads")
        }
        request = requests.post(url, headers=my_header, data="uploads")
        print(request.content)
        if request.status_code == 200:
            return ResultMessage.Success
        else:
            return ResultMessage.Wrong

    # 获得需要格式的日期
    def get_date(self):
        now = datetime.datetime.now()
        time = now.strftime(self.__timeFormat__)
        return time

    # 计算授权字符串
    def authorize(self, http_verb="GET", bucket="", date="", object_name="", amz="", content_type="", uri_resource=""):
        canonicalized_amz_headers = ""
        if bucket == "":
            canonicalized_resource = ""
        else:
            canonicalized_resource = "/" + bucket + "/" + object_name + uri_resource

        # amzHeaders
        if amz != "":
            canonicalized_amz_headers += amz + "\n"

        string_to_sign = http_verb + "\n" \
                         + "" + "\n" \
                         + content_type + "\n" \
                         + date + "\n" \
                         + canonicalized_amz_headers + canonicalized_resource

        print(string_to_sign)
        signature = base64.b64encode(
            hmac.new(bytes(self.__sk__, encoding="utf-8"), bytes(string_to_sign, encoding="utf-8"), "SHA1").digest())
        authorization = "AWS " + self.__ak__ + ":" + str(signature).split('\'')[1]
        print(authorization)
        return authorization
