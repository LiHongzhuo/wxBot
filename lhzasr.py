#!/usr/bin/env python
# coding: utf-8
import urllib2
import time
import os
import ConfigParser
import lhz_mysql
import lhzhttp
import sys
#设置文件编码
reload(sys)
sys.setdefaultencoding('utf-8')
# 获取配置群名
config = ConfigParser.ConfigParser()
path = os.path.split(os.path.realpath(__file__))[0] + '/config.conf'
config.read(path)
asraccesskeyid = config.get('makelove', 'asraccesskeyid')
asraccesskeysecret = config.get('makelove', 'asraccesskeysecret')


# def asrByTaskid(taskid):
#     request = urllib2.Request(
#         'https://nlsapi.aliyun.com/recognize?spm=a2c4g.11186623.2.4.73043s')
#     request.add_header('Authorization', 'Dataplus ' +
#                        asraccesskeyid + ':' + signature)
#     request.add_header('Content-type', 'fakeclient')
#     request.add_header('Accept', 'application/json')
#     request.add_header('Date', time.ctime())
#     request.add_header('Content-Length', 'fakeclient')
#     # response = urllib2.urlopen(request)
#     # print request.read()
#     body = {}  # 消息体
#     body['version'] = '2.0'
#     body['model'] = 'chat'

#读取数据库待处理的taskid，更新智能语音识别结果
def dealMysqlByTaskid():
    sql = "SELECT wid,asrtaskid FROM wechatdata WHERE MsgType=34 AND wtime<(UNIX_TIMESTAMP(NOW())-60)*1000 AND content2 IS NULL and asrtaskid is not null"
    rows = lhz_mysql.query(sql)
    for row in rows:
        wid = row[0]
        taskid = row[1]
        content2 = lhzhttp.asrByTaskid(taskid)
        sql2 = "update wechatdata set content2='%s' WHERE wid=%d" % (
            content2, wid)
        lhz_mysql.executeNotCommit(sql2)
        print '处理了wid'+str(wid)
    lhz_mysql.db.commit()
    # print '提交了'


if __name__ == '__main__':
    dealMysqlByTaskid()
