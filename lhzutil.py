# -*- coding: utf-8 -*-


# 获取字符串中匹配子串的最后一个位置
def find_last(string, str):
    last_position = -1
    while True:
        position = string.find(str, last_position+1)
        if position == -1:
            return last_position
        last_position = position


# 将文件名改写成小文件名
def thumbFilePath(filepath):
    lastindexofdot = find_last(filepath, '.')
    filepath = filepath[:lastindexofdot]+'_thumb'+filepath[lastindexofdot:]
    return filepath
