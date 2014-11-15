#!/usr/bin/python 
# -*- coding: utf-8 -*- 

import itertools
import gzip
import os

with open('c:\\gzip.txt.gz', 'wb') as f:
    f.writelines(itertools.repeat('hello word!!!\n', 100))

with open('c:\\gzip.txt.gz', 'rb') as f:
    #f.seek(0)
    f.seek(6)
    print f.read(10)
print os.stat('c:\\gzip.txt.gz').st_size
