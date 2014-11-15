class C(object):
    def __init__(self): self._x = 1
    def getx(self): return self._x
    def setx(self, value): self._x = value
    def delx(self): del self._x
    x = property(getx, setx, delx, "I'm the 'x' property.")

a = C()

print a.x
a.x=2
print a.x
del a.x
print a.x

