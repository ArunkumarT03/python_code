'''def prime(num):
    f_count=0
    for fa in range(1,num+1):
        if num%fa==0:
            f_count+=1
    return f_count==2
num=5
print('prime' if prime(num) else 'not prime')'''

for val in range(1,20):
    num=val
    f_count=0
    for fa in range(1,num+1):
        if num%fa==0:
            f_count+=1
        
    if f_count==2:
        print(num)

def prime(num):
    for fa in range(2,num//2+1):
        if num%fa==0:
            return 'False'
    return 'True'
num=1
print(prime(num))

def fact(num,fact=1):
    for fa in range(num,0,-1):
        fact*=fa
    return fact
num=4
print(fact(num))

#armstrong
def armstrong(num,power=len(str(num)),res=0):
    while num!=0:
        rem=num%10
        res+=rem**power
        num//=10
    return res
num=153
print('arm'if armstrong(num)else 'not')

#diarum
def disarum(num,power,res=0):
    while num!=0:
        rem=num%10
        res+=rem**power
        num//=10
        power-=1
    return res
num,power=135,len(str(num))
print('dis' if disarum(num,power)==num else 'not')

#strong
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
print('strong'  if strong(num)==num else 'not strong')

#polyprime
def prime(num):
    f_count=0
    for fa in range(1,num+1):
        if num%fa==0:
            f_count+=1
    return 'True'
def palindrome(num,dup=num,rev=0):
    while num!=0:
        rem=num%10
        rev=rev*10+rem
        num//=10
    return rev==dup
num=11
print('polyprime'  if prime(num) and palindrome(num) else 'not')
    
