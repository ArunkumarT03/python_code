'''#public access modifier
class public:
    def __init__(self):
        self.a=10
    def MI(self):
        print(self.a)
obj1=public()
print(obj1.a)
obj1.MI()'''


'''#protecter access
class protecter:
    def __init__(self):
        self.a=10
        self._b=20
    def m2(self):
        print(self.a)
        print(self._b)
obj2=protecter()
obj2.m2()'''

#private
class private:
    def __init__(self):
        self.a=10
        self._b=20
        self.__c=420
    def m3(self):
        print(self.a)
        print(self._b)
        print(self.__c)

obj3=private()
obj3.m3()
print(obj3.a)
print(obj3._b)
print(obj3.__c)


