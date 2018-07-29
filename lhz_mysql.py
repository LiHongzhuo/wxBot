#!/usr/bin/env python
# coding: utf-8
import json
import re
import MySQLdb
import ConfigParser
import os
import sys

#设置文件编码
reload(sys)
sys.setdefaultencoding('utf-8')

# 打开数据库连接
db = MySQLdb.connect("123.57.24.142", "root", "lhz#root@123", "wxbot")

# 使用cursor()方法获取操作游标
cursor = db.cursor()
cursor.execute('SET NAMES UTF8')


def execute(sql):
    try:
        # 执行sql语句
        cursor.execute(sql)
        # 提交到数据库执行
        db.commit()
    except Exception,e:
        # Rollback in case there is any error
        db.rollback()
        print 'error and rollback'
        # print e.message

def executeNotCommit(sql):
    try:
        # 执行sql语句
        cursor.execute(sql)
    except:
        # Rollback in case there is any error
        db.rollback()
        print 'error and rollback'

def query(sql):
    # SQL 查询语句
    try:
        # 执行sql语句
        cursor.execute(sql)
        # 获取所有记录列表
        results = cursor.fetchall()
        return results
        # for row in results:
        #     fname = row[0]
    except:
        print "Error: unable to fecth data"

# 关闭数据库连接
# db.close()
