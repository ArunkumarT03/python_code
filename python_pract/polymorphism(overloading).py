'''class A3:
    def m1(self,val1):
        print(val1)
    def m1(self,val1,val2):
        print(val1+val2)
    def m1(self,val1,val2,val3):
        print(val1+val2+val3)
obj1=A3()
#obj1.m1(4,5)
obj1.m1(4,5,6)'''
#variable length non key word arg
class A3:
    def m1(self,*args):
        res=0
        for ele in args:
            res+=ele
        return res
obj=A3()
print(obj.m1(4,5,6))
print(obj.m1())

#reduce f/n
class A2:
    def m1(self,*args):
        from functools import reduce
        return(reduce(lambda a,b:a+b,args))
obj1=A2()
print(obj1.m1(4,6,7))

#default arg
class A1:
    def m1(self,a=0,b=0,c=0,d=0):
        return(a+b+c+d)
obj2=A1()
print(obj2.m1(23,6,4))
        
