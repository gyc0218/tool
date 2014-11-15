#!/usr/bin/python 
# -*- coding: utf-8 -*-

class Singleton(object):
    def __new__(self, *args, **kw):
        if not hasattr(self, '_mygirl'):
            self._mygirl = super(Singleton, self).__new__(self, *args, **kw)
        return self._mygirl

class MyClass(Singleton):
    a = 1
            
class MyClass1(object):
    a = 1
            
if __name__ == '__main__':
    one = MyClass()
    two = MyClass()
    one1 = MyClass1()
    two1 = MyClass1()
    one.a = 11
    one1.a=11
    print id(one),id(two)
    print two.a
    print two1.a
     
