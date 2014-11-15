#!/usr/bin/python 
# -*- coding: gb2312 -*- 

import os

#with os.popen('ping 10.68.146.251') as f:
#    outPut = f.read()
ss = r'E:\备份1\vm'
#ff = ss.decode('utf-8')
#ff1 = ff.encode('GBK')
ff1 = ss
files = os.walk(ff1)

for filename, filedir, filegroup in files:
    print 'begin---------', filename, '-----------'
    for c in filedir:
        print '\t', c
    for c in filegroup:
        print '\t', c
    print '---------------------'


