'''
d1={'a':20,'b':78,}
d2={'a':40,'c':48}
d3={}

for ch in d1.items():
    if ch[0] not in d3:
        d3[ch[0]]=[ch[1]]
    else:
        d3[ch[0]]+=[ch[1]]
for ch in d2.items():
    if ch[0] not in d3:
        d3[ch[0]]=[ch[1]]
    else:
        d3[ch[0]]+=[ch[1]]
print(d3)'''


'''#special
def sumofdigits(num):
    if num==0:
        return 0
    return (num%10)+sumofdigits(num//10)
def special(num):
    digits=sumofdigits(num)
    return digits in(1,3,6)
def numberange(n1,n2):
    specialnum=[]
    for number in range(n1,n2+1):
        if special(number):
            specialnum.append(number)
    return specialnum
n1=1
n2=200
specialnum=numberange(n1,n2)
print(f'special number between {n1}and {n2}:{specialnum}')'''




'''num=1234
digits=0
while num!=0:
    rem=num%10
    digits=digits*10+rem
    num//=10
print(digits)'''

'''def reverse(num,power,res=0):
    while num!=0:
        rem=num%10
        res=res+rem*power
        power//=10
        num//=10
    return res
num=1234
print(reverse(num,10**(len(str(num))-1)))'''

'''
def revrs(num,power):
    if num==0:
        return 0
    return (num%10)*power+revrs(num//10,power//10)
num=1234567
print(revrs(num,10**(len(str(num))-1)))'''

'''

#happy
num=19
while num>9:
    ans=0
    while num!=0:
        rem=num%10
        ans+=rem**2
        num//=10
    num=ans
if num==1 or num==7:
    print('happy')
else:
    print('not happy')
    
'''    
'''
def special(num,res=0):
    for fa in range(1,num//2+1):
        if num%fa==0:
            res+=fa
    return res
for i in range(1,100):
    if special(i)==i:
        print(i)
'''

'''def factor(num,fa=1):
    if fa==num//2+1:
        return 0
    if fa<=num//2:
        if num%fa==0:
            return fa + factor(num,fa+1)
        else:
            return factor(num,fa+1)
if factor(6)==6:
    print('special')
else:
    print('not special')'''

'''
def Sumfac(num,fa = 1):
    if fa == num // 2 + 1 :
        return 0
    if num % fa == 0:
        return fa + Sumfac(num,fa + 1)
    else:
        return Sumfac(num,fa + 1)
print(Sumfac(6))
'''



'''def b2n(num,pos=1):
    if num==0:
        return 0
    return (num%2)*pos+b2n(num//2,pos*10)
num=25
print(b2n(num))

def i2b(num,power=1):
    if num==0:
        return 0
    return (num%10)*power+i2b(num//10,power*2)
num=11001
print(i2b(num))'''

'''def arm(num,res=0):
    if num==0:
        return 0
    return (num%10)**digits+arm(num//10,digits)
num=34
digits=len(str(num))
print('armstrong' if arm(num,digits)==num else 'not arm')'''

'''def fact(num):
    if num==0:
        return 1
    return num*fact(num-1)
def strong(num):
    if num==0:
        return 0
    return fact(num%10)+strong(num//10)
num=0
i=0
while num<15:
    if strong(i)==i:
        print(i)
        num+=1
    i+=1'''

'''#fact,
num=5
fact=1
for fa in range(1,num+1):
    fact*=fa
print(fact)

def fact(num,fa=1):
    for num1 in range(1,num+1):
        fa*=num1
    return fa
print(list(filter(fact,range(1,10))))

#prime
num=11
for i in range(2,num//2+1):
    if num%i==0:
        print('not prime')
        break
else:
    print('prime')

num=9
fa=0
for i in range(1,num+1):
    if num%i==0:
        fa+=1
if fa==2:
    print('prime')
else:
    print('not prime')

    
num=11
sq=int(num**(1/2))
for i in range(2,sq+1):
    if num%i==0:
        print('not prime')
        break
else:
    print('prime')

def prime(num):
    for i in range(2,num//2+1):
        if num%i==0:
            return 'not prime'
    return 'prime'
num=11
print(prime(num))

def prime1(num,fa=2):
    if fa==num//2+1:
        return 'prime'
    if num%fa==0:
        return 'not prime'
    return prime1(num,fa+1)
num=9
print(prime1(num))

def prime(num):
    for i in range(2,num//2+1):
        if num%i==0:
            return 'not prime'
    return 'prime'''


'''for n in range(51):
    if n==1:
        continue
    for p in range(2,n//2+1):
        if n%p==0:
            break    
    else:
        print(n)

#palindrome
num=121
res=0
dup=num
while num!=0:
    rem=num%10
    res=res*10+rem
    num//=10
if dup==res:
    print('palindrome')
else:
    print('not palindrome')

def rev(num,power):
    if num==0:
        return 0
    return (num%10)*power+rev(num//10,power//10)
num=1234
print(rev(num,10**(len(str(num))-1)))

def palin(num,power):
    if num==0:
        return 0
    return (num%10)*power+palin(num//10,power//10)
num=121
print('palindr' if palin(num,10**(len(str(num))-1))==num else 'not palind')





def prime(num):
    for i in range(2,num//2+1):
        if num%i==0:
            return False
    return True
print(list(filter(prime,range(1,10))))

#happy
def sq(num,res=0):
    while num!=0:
        rem=num%10
        res+=rem**2
        num//=10
    return res
def happy(num):
    while num>9:
        num=sq(num)
    return num==1 
print(list(filter(happy,range(1,100))))

def sq(num):
    if num==0:
        return 0
    return (num%10)**2+sq(num//10)
def happy(num):
    if num<10:
        return num==1
    return happy(sq(num))
num=13
print('happy' if happy(num) else 'not happy')





#in2bin
num=25
pos=1
res=0
while num!=0:
    rem=num%2
    res+=rem*pos
    pos*=10
    num//=2
print(res)

#b2in
num=11001
power=1
res=0
while num!=0:
    rem=num%10
    res+=rem*power
    power*=2
    num//=10
print(res)


def in2b(num,pos=1,res=0):
    while num!=0:
        rem=num%2
        res+=rem*pos
        pos*=10
        num//=2
    return res
num=25
print(in2b(num))'''








#special

def special(num,fa=1):
    if fa==num//2+1:
        return 0
    if num%fa==0:
        return fa+special(num,fa+1)
    else:
        return special(num,fa+1)
'''for i in range(1,100):
    if special(i)==i:
        print(i)'''
num=0
i=0
while num<15:
    if special(i)==i:
        print(i)
        num+=1
    i+=1

    
