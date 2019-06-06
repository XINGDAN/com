#! /usr/bin/env python
#coding=utf-8

import random
'''
def Unicode():
    val = random.randint(0x4e00,0x9fbf)
    return chr(val)
print(Unicode())
'''
# 随机生成三个字符 0x4e00,0x9fbf这个是unicode编码值，如果需要简体中文的编码值百度一下
def get_random_char(number):
    val_list = []
    for nu in range(0,number):
        val_list.append(chr(random.randint(0x4e00,0x9fbf)))
    return "".join(val_list)
print(get_random_char(3))