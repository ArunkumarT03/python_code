'''num=1234
res=0
while num!=0:
    digits=num%10
    res=res*10+digits
    num//=10
print(res)

def rev(num,res=0):
    while num!=0:
        digits=num%10
        res=res*10+digits
        num//=10
    return res
num=12345
print(rev(num))'''


'''#phno
num=7092302110
osum=0
esum=0
while num!=0:
    esum=0
    osum=0
    rem=num%10
    if rem%2==0:
        esum+=rem
    else:
        osum+=rem
    num//=10
print(esum,osum)'''
#prime
num=2
for i in range(2,num//2+1):
    if num%i==0:
        print('not prime')
        break
else:
    print('prime')

# intger to binary
def i2b(num,res=0,pos=1):
    while num!=0:
        rem=num%2
        res+=rem*pos
        pos*=10
        num//=2
    return res
num=25
print(i2b(num))

#binary to intger
def b2i(num,res=0,power=1):
   while num!=0:
       rem=num%10
       res+=rem*power
       power*=2
       num//=10
   return res
print(b2i(11001))


#armstrong
num=153
dup=num
res=0
digits=len(str(num))
while num!=0:
    rem=num%10
    res+=rem**digits
    num//=10
if res==dup:
    print('is armstrong')
else:
    print('is not armstrong')

def armstrong(num,res=0,dup=num):
    while num!=0:
        rem=num%10
        res+=rem**digits
        num//=10
    return res
num=145
digits=len(str(num))
print('strong' if armstrong(num)==res else 'not armstrong')

def armstrong(num,res=0,nod=len(str(num))):
    if num==0:
        return 0
    return (num%10)**nod+armstrong(num//10,nod)
num=156
nod=len(str(num))
print('armsrong' if armstrong(num,nod)==num else 'not armstrong')


    




#strong
num=145
res=0
dup=num
while num!=0:
    rem=num%10
    fact=1
    for val  in range(1,rem+1):
        fact*=val
    res+=fact
    num//=10
if  dup==res:
    print('is strong')
else:
    print('not srong')

def fact(num):
    if num==0:
        return 1
    return num*fact(num-1)
def strong(num,res=0,dup=num):
    if num==0:
        return 0

    return fact(num%10)+strong(num//10)
num=145
print('strong' if strong(num)==dup else 'not strong')



def rec(num):
    if num==0:
        return
    print(num)
    rec(num+1)
num=-10
rec(num)



def sq(num):
    return num**2
print(list(map(sq,[2,4,9,14,6])))

num=5
for i in  range(1,11):
    print(num,'x',i,'=',num*i)




