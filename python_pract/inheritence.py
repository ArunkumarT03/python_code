'''class parent:
    var1=20
    var2=40
    def dance(self):
        print('we do dance')
class child(parent):
    var3=50
    var4=80
obj1=parent()
obj2=child()
print(obj1.var1)
print(obj2.var2)
print(obj2.var1)
obj2.dance()'''

#multi-level
class c1:
    var1=20
    var3=60
class c2(c1):
    var4=50
    var2=70
class c3(c2):
    var5=90
    var7=10
obj1=c3()
print(obj1.var3)
