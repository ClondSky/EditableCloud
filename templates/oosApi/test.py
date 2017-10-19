# -*- coding: utf-8 -*-
from templates.oosApi.OOS import CloudService

cloudService = CloudService("surevil", "80", "622ff0aad8c78a306eaa",
                            "c4a84bcc4ce1ad09805def0284a07452dd7a7519")

print(cloudService.createBucket())
