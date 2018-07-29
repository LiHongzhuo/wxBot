# -*- coding: utf-8 -*-
import os
import ConfigParser
import lhz_mysql
import sys

#设置文件编码
reload(sys)
sys.setdefaultencoding('utf-8')
# 获取配置群名
config = ConfigParser.ConfigParser()
path = os.path.split(os.path.realpath(__file__))[0] + '/config.conf'
config.read(path)
wcid = config.get('makelove', 'wcid')
sql = 'select receivegroupname,send_from_groupname,send_to_groupname from wxconfig where wcid=%d' % (int(wcid))
results = lhz_mysql.query(sql)
# list = config.get('makelove', 'groupname').decode('utf-8').strip(',').split(',')
row = results[0]
groupnamelist = row[0].decode('utf-8').strip(',').split(',')
send_from_groupname = row[1]
send_to_groupname = row[2].strip(',').split(',')
# send_from_groupname = config.get('makelove', 'send_from_groupname')
# send_to_groupname = config.get('makelove', 'send_to_groupname').decode('utf-8').strip(',').split(',')
# print ('是'+sendgroupname+'是').decode('utf-8').encode('gbk')