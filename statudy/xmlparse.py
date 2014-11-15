#!/usr/bin/python 
# -*- coding: utf-8 -*- 

from xml.etree import ElementTree

with open('c:\\test.xml', 'rt') as f:
    tree = ElementTree.parse(f)

for node in tree.iter('hhh2'):
    print node.tag
    print node.attrib.get('myname')
    print node.text.strip()
    print node.tail.strip()
