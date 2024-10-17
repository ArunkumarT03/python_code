'''class A3():
    place='kkdi'
    area='main street'
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
    def details(self):
        print(f'name:{self.name}')
        print(f'age:{self.age}')
        print(f'gender:{self.gender}')
obj=A3('Arun',21,'male')
obj.details()
print(obj.place)

#abstraction
from abc import ABC,abstractmethod
class Animal(ABC):
    @abstractmethod
    def color(self):
        pass
    def legs(self):
        print('4 legs')
class dog(Animal):
    def  color(self):
        print('my dog ')
class cat(Animal):
    def color(self):
        print('my cat')
obj=dog()
obj.legs()
obj.color()

#polymorphism
#overloading
class A2:
    def m1(self,val1):
        print(val1)
    def m1(self,val1,val2):
        print(val1+val2)
    def  m1(self,val1,val2,val3):
        print(val1+val2+val3)
obj=A2()
obj.m1(2,4,7)

#mro
class A():
    pass
class B(A):
    pass
class C(A):
    pass
class D(B,C):
    pass
class E(C,B):
    pass

print(E.mro())'''
    

import json
json.dumps()





















