#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'wuyuxi'

"""
f = open('xx.txt', 'r')
# 一次读取文件的全部内容，Python把内容读到内存，用一个str对象表示
content = f.read()
print(content)
f.close()
"""

"""
try:
    f = open('/path/to/file', 'r')
    print f.read()
finally:
    if f:
        f.close()
"""

"""
调用read()会一次性读取文件的全部内容，如果文件有10G，内存就爆了，所以，要保险起见，
可以反复调用read(size)方法，每次最多读取size个字节的内容。
另外，调用readline()可以每次读取一行内容，
调用readlines()一次读取所有内容并按行返回list。因此，要根据需要决定怎么调用。

如果文件很小，read()一次性读取最方便；
如果不能确定文件大小，反复调用read(size)比较保险；
如果是配置文件，调用readlines()最方便：
for line in f.readlines():
    print(line.strip()) # 把末尾的'\n'删掉
"""
with open('xx.txt', 'r') as f:
    print f.read()
