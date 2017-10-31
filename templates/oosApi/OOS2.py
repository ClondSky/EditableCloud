import os
import boto

from boto.s3.key import Key
from boto.s3.connection import S3Connection
from boto.s3.connection import Location
from boto.exception import S3CreateError

conn = boto.connect_s3(aws_access_key_id="622ff0aad8c78a306eaa",
                       aws_secret_access_key="c4a84bcc4ce1ad09805def0284a07452dd7a7519", host='oos.ctyunapi.cn')
bucket = conn.get_bucket("surevil")
print(conn.create_key())
