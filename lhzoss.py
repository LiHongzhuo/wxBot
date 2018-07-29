# -*- coding: utf-8 -*-
import os
import ConfigParser
import oss2
import sys
from itertools import islice
reload(sys)
sys.setdefaultencoding('utf-8')

# 获取配置
config = ConfigParser.ConfigParser()
path = os.path.split(os.path.realpath(__file__))[0] + '/config.conf'
config.read(path)
ossAccessKeyId = config.get('makelove', 'ossAccessKeyId')
ossAccessKeySecret = config.get('makelove', 'ossAccessKeySecret')
ossEndpoint = config.get('makelove', 'ossEndpoint')
ossBUCKET = 'artfire-file'
auth = oss2.Auth(ossAccessKeyId, ossAccessKeySecret)
bucket = oss2.Bucket(auth, ossEndpoint, ossBUCKET)
# service = oss2.Service(auth, ossEndpoint)
# print([b.name for b in oss2.BucketIterator(service)]) #输出所有bucketname
# for b in islice(oss2.ObjectIterator(bucket), 10):#列举文件
#     print(b.key)
filepath = 'img/group_chat_backend.jpg'
filename = 'makelove.jpg'
# with open(filepath, 'rb') as fileobj:
#     result = bucket.put_object(filename, fileobj)
# print('http status: {0}'.format(result.status))
# print('request_id: {0}'.format(result.request_id))
# print('ETag: {0}'.format(result.etag))
# print('date: {0}'.format(result.headers['date']))


def upload(filepath, filename):
    filename = filename.replace('\\', '/')
    with open(filepath, 'rb') as fileobj:
        bucket.put_object(filename, fileobj)
        return 'http://' + ossBUCKET + ".oss-cn-beijing.aliyuncs.com/" + filename
