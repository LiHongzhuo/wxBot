#!/usr/bin/env python
# coding: utf-8
import json
import re
import MySQLdb
import ConfigParser
import os
import sys

#�����ļ�����
reload(sys)
sys.setdefaultencoding('utf-8')

# �����ݿ�����
db = MySQLdb.connect("123.57.24.142", "root", "lhz#root@123", "wxbot")

# ʹ��cursor()������ȡ�����α�
cursor = db.cursor()
cursor.execute('SET NAMES UTF8')


def execute(sql):
    try:
        # ִ��sql���
        cursor.execute(sql)
        # �ύ�����ݿ�ִ��
        db.commit()
    except Exception,e:
        # Rollback in case there is any error
        db.rollback()
        print 'error and rollback'
        # print e.message

def executeNotCommit(sql):
    try:
        # ִ��sql���
        cursor.execute(sql)
    except:
        # Rollback in case there is any error
        db.rollback()
        print 'error and rollback'

def query(sql):
    # SQL ��ѯ���
    try:
        # ִ��sql���
        cursor.execute(sql)
        # ��ȡ���м�¼�б�
        results = cursor.fetchall()
        return results
        # for row in results:
        #     fname = row[0]
    except:
        print "Error: unable to fecth data"

# �ر����ݿ�����
# db.close()
