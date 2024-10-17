num=25
b=0
pos=1
while num!=0:
    rem=num%2
    b+=rem*pos
    pos*=10
    num//=2
print(b)
num=25
count=0
while num!=0:
    rem=num%2
    if rem==1:
        count+=1
    num//=2
if count%2==0:
    print('evil')
else:
    print('odeous')

num=11001
power=0
ans=0
while num!=0:
    rem=num%10
    ans+=rem*(2**power)
    power+=1
    num//=10
print(ans)

def b2i(num,power=0):
    if num==0:
        return 0
    return (num%10)*(2**power)+b2i(num//10,power+1)
num=11001
print(b2i(num))

def i2b(num,pos=1):
    if num==0:
        return 0
    return(num%2)*(pos)+i2b(num//2,pos*10)
num=25
print(i2b(num))



#happy
num=19
while num>9:
    ans=0
    while num!=0:
        rem=num%10
        ans+=rem**2
        num//=10
num=ans
print('happy' if num==1 or num==7 else 'not happy')

def sq(num,ans=0):
    while num!=0:
        rem=num%10
        ans+=rem**2
        num//=10
    return ans
def happy(num):
    while num>9:
        num=sq(num)
    return num==1 or num==7
num=19
print('happy' if happy(num) else 'not happy')

def sq(num):
    if num==0:
        return 0
    return (num%10)**2+sq(num//10)
def happy(num):
    if num<10:
        return num==1
    return happy(sq(num))
num=19
print('happy' if happy(num) else 'not happy')
