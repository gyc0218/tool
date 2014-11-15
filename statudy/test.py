#!/usr/bin/python 
# -*- coding: utf-8 -*- 

from xml.etree import ElementTree
import zlib

with open('c:\\test.xml', 'rt') as f:
    tree = f.read()

print len(tree)

compressed = zlib.compress(tree)
print len(compressed), compressed


ss = zlib.decompress(compressed)
print ss
