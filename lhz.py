import time
import MySQLdb
import lhz_mysql
import os

s = '����,����2,����3,����4,����5'
s2 = s.strip(',').split(',')
uid = []
for a in s2:
    uid.append(a)
print uid