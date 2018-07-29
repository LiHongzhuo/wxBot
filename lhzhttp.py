# -*- coding: utf-8 -*-
import urllib
import urllib2
import sys
import lhzoss

# 设置文件编码
reload(sys)
sys.setdefaultencoding('utf-8')
# 输出内容:登录成功


def getTaskid(param):
    url = 'http://101.200.184.163:9090/YihuoService/services/upload/asrgettaskid'
    req = urllib2.Request(url='%s%s%s' % (url, '?s=', param))
    res = urllib2.urlopen(req)
    res = res.read()
    return res


def asrByTaskid(taskid):
    url = 'http://101.200.184.163:9090/YihuoService/services/upload/asrbytaskid'
    req = urllib2.Request(url='%s%s%s' % (url, '?s=', taskid))
    res = urllib2.urlopen(req)
    res = res.read()
    return res
# param = 'http://artfire-file.oss-cn-beijing.aliyuncs.com/wxbot/voice_7545602189880972462.mp3'
# s = 'dd559abb652043a89dd8172b442a81a8'
# print asrByTaskid(s)
