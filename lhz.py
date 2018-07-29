import time
import MySQLdb
import lhz_mysql
import os

s = '众神,众神2,众神3,众神4,众神5'
s2 = s.strip(',').split(',')
uid = []
for a in s2:
    uid.append(a)
print uid