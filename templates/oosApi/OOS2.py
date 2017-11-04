import boto3
from boto import iam

client=boto3.client("iam")
#conn=iam.connect_to_region(region_name="cn-north-1", aws_access_key_id="c4582dec5d0809103126",
#                           aws_secret_access_key="47c783687d4c452c5d71b817b8c481915fb0094a",
#                           )
response=client.create_access_key(
    region_name="cn-north-1",
    aws_access_key_id="c4582dec5d0809103126",
    aws_secret_access_key="47c783687d4c452c5d71b817b8c481915fb0094a",
    host='oos-bj2-iam.ctyunapi.cn',
    UserName="Bob"
)
print(response)

