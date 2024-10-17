'''def prime(num):
    f_count=0
    for fa in range(1,num+1):
        if num%fa==0:
            f_count+=1
    return f_count==2
num=11
print('p' if prime(num) else 'not')'''

def prime(num,fa=1):
    if fa==num+1:
        return False
    return(True if num%fa==0 else False)+prime(num,fa+1)
num=11
print('p' if prime(num)==2 else 'not')

def prime(num, fa=2):
    if fa==num//2+1:
        return 'prime'
    elif num%fa==0:
        return 'not prime'
    return prime(num, fa+1)
num=2
print(prime(num))

#fact
num=5
fact=1
for val in range(1,num+1):
    fact*=val
print(fact)

def fact(num,fact=1):
    for val in range(1,num+1):
        fact*=val
    return fact
num=5
print(fact(num))

def fact(num):
    if num==1:
        return 1
    return num*fact(num-1)
num=5
print(fact(num))

def fact(num,val):
    if val==num:
        return num
    return val*fact(num,val+1)
num=5
val=1
print(fact(num,val))

#add of all digits
num=1234
res=0
while num!=0:
    rem=num%10
    res+=rem
    num//=10
print(res)

def add(num,res=0):
    while num!=0:
        rem=num%10
        res+=rem
        num//=10
    return res
num=1234
print(add(num))

def add(num):
    if num==0:
        return 0
    return(num%10)+add(num//10)
num=12345
print(add(num))

#armstrong
num=153
dup=num
total=0
digits=len(str(num))
while num!=0:
    rem=num%10
    total+=rem**digits
    num//=10
print('arm' if total==dup else 'not')

def arm(num,power,res=0):
    while num!=0:
        rem=num%10
        res+=rem**power
        num//=10
    return res
num=153
power=len(str(num))
print('arm' if arm(num,power) else 'not')

def arm(num,nod):
    if num==0:
        return 0
    return(num%10)**nod+arm(num//10,nod)
num=135
print('arm' if arm(num,nod=len(str(num))) else 'not')

#disarum
#facinating
num=193
total=str(num*1)+str(num*2)+str(num*3)
for fact in range(1,10):
    if str(val) not in total:
        print('not')
    break
else:
    print('facinating')

#tech
num=2025
var=str(num)
val1=int(var[:len(var)//2])
val2=int(var[len(var)//2:])
if num==(val1+val2)**2:
    print('tech')
else:
    print('not')

#special
num=6
res=0
for fact in range(1,num//2+1):
    if num%fact==0:
        res+=fact
if num==res:
    print('special')
else:
    print('not')

def special(num,res=0):
    for fact in range(1,num//2+1):
        if num%fact==0:
            res+=fact
    return res
num=6
print('special' if special(num) else 'not')

#strong
num=145
res=0
dup=num

while num!=0:
    rem=num%10
    fact=1
    for val in range(1,rem+1):
        fact*=val
    res=res+fact
    num//=10
print('strong' if res==dup else 'not strong')

def fact(num):
    if num==0:
        return 1
    return num*fact(num-1)
def strong(num):
    if num==0:
        return 0
    return fact(num%10)+strong(num//10)
num=145
print('strong' if strong(num)==num else 'not')

def fact(num,fact=1):
    for val in range(1,num+1):
        fact*=val
    return fact
def strong(num,res=0):
    while num!=0:
        rem=num%10
        res+=fact(rem)
        num//=10
    return res
num=145
print('strong' if strong(num)==num else 'not')
#pronic
def pronic(var,i=0):
    while i*(i+1)<=var:
        if i*(i+1)==var:
            return 't'
        i+=1
    else:
        return 'n'
var=20
print(pronic(var))

#happy
num=19
while num>9:
    ans=0
    while num!=0:
        rem=num%10
        ans+=rem**2
        num//=10
ans=num
print('happy' if num==1 or num==7 else 'not happy')
        
