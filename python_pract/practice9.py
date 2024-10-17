'''num=153
res=0
digits=len(str(num))
total=num
while num!=0:
    rem=num%10
    res+=rem**digits
    num//=10
if total==res:
    print('arm')
else:
    print('not')

def b2i(num,pos=1,res=0):
    while num!=0:
        rem=num%10
        res+=rem*pos
        pos*=2
        num//=10
    return res
print(b2i(1110))


def i2b(num,pos=1,res=0):
    while num!=0:
        rem=num%2
        res+=rem*pos
        num//=2
        pos*=10
    return res
print(i2b(25))





num=12345
res=0
while num!=0:
    rem=num%10
    res=res*10+rem
    num//=10
print(res)

def revre(num,power,res=0):
    while num!=0:
        rem=num%10
        res=res+rem*power
        power//=10
        num//=10
    return res
num=1234
print(revre(num,10**(len(str(num))-1)))
def revr(num,power):
    if num==0:
        return 0
    return (num%10)*power+revr(num//10,power//10)
num=123456
print(revr(num,10**(len(str(num))-1)))



#strong

num=145
res=0
dup=num
while num!=0:
    rem=num%10
    fact=1
    for  val in range(1,rem+1):
        fact*=val
    res+=fact
    num//=10
if dup==res:
    print('strong')
else:
    print('not')

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
for i in range(1,200):
    if strong(i)==i:
        print(i)

n=0
num=0
while num<15:
    if strong(n)==n:
        print(n) 
        num+=1
    n+=1'''


'''#special
def special(num,res=0):
    for fa in range(1,num//2+1):
        if num%fa==0:
            res+=fa
    return res
n=0
num=0
while num<15:
    if special(n)==n:
        print(n)
        num+=1
    n+=1
for val in range(0,50):
    if special(val)==val:
        print(val)'''
'''num=0
while num<7:
    num+=3
    if num==6:
        continue
print(num)'''

s='today is hollyday'
rev=' '
'''for ch in s.split():
    rev+=ch[::-1]+' '
print(rev.strip())'''

for ch in s.split():
    t=' '
    for c in ch:
        t=c+t
    rev+=t
print(rev)


            

