'''#create class&object

class A3:
    sub='python full stack'
    location= 'Marathahalli'

obj1=A3()
obj2=A3()
obj3=A3()
#by using obj reference
print(obj1.sub, obj2.location)
print(obj2.sub, obj2.location)

#by using class ref
print(A3.sub,A3.location)


#modify by using obj ref
obj1.location='kkdi'
obj2.sub='SQL'
print(obj1.sub,obj1.location)
print(obj2.sub, obj2.location)
#by using class ref
A3.location='chennai'
print(obj1.sub,obj1.location)
print(obj2.sub, obj2.location)'''


'''#uncommon  property
#constructor(self)

class mrngclass:
    sub='html'
    location='marathahalli'
    def __init__(self):
        print(self)

stu1=mrngclass()
print(f'cus1:{cus1}')
stu2=mrngclass()'''

# main accessing
class SBI:
    IFSC='SBI0042'
    branch='marathahalli'
    ROI=0.08
    def __init__(self,name,mno,Aadhar,PAN,gender):
        self.name  =name
        self.mno   =mno
        self.Aadhar=Aadhar
        self.PAN   =PAN
        self.gender=gender
    def details(self):
        print(f'name:{self.name}')
        print(f'mno:{self.mno}')
        print(f'Aadhar:{self.Aadhar}')
        print(f'PAN:{self.PAN}')
        print(f'gender:{self.gender}')

obj4=SBI('ram',98364761726,33252181,'ABC5266','male')
obj5=SBI('raj',81871262677,37752112,'ABI1729','male')
obj6=SBI('Abi',9271816253,18282982,'ABD8728','female')
obj5.details()
