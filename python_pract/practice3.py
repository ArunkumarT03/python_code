#polyprime

def prime(num):
    if num<=1:
        return False
    for fa in range(2,num//2+1):
        if num%fa==0:
            return False
    return True

'''def palindrome(num):
    res=0
    while num!=0:
        rem=num%10
        res=res*10+rem
        num//=10
    return res'''
'''n=0
num=0
while num<=10:
    if prime(n) and palindrome(n)==n:
        print(n)
        num+=1
    n+=1'''
    

'''for n in range(2,50):
    fa_c=0
    for fa in range(1,n+1):
        if n%fa==0:
            fa_c+=1
    if fa_c==2:
        print(n)'''
        
'''def fact(num):
    
    fact=1
    for fa in range(1,n+1):
        fact*=fa
    return fact
for n in range(1,11):
    print(fact(n))'''
            
        

'''def sq(num):
    if num==0:
        return 0
    return (num%10)**2+sq(num//10)
def happy(num):
    if num>9:
        return sq(num)
    return num==1 or num==7
num=12
print('happy' if happy(num) else 'not happy')'''
'''
def reverse(num,power):
    if num==0:
        return 0
    return (num%10)*10**power+reverse(num//10,power-1)
for i in range(11,50):
     print(reverse(i,len(str(i))-1))'''

'''s=input('enter:')
st=0
end=-1
res=''
while(st!=len(s)):
    if s[st]==s[end]:
        res+=s[st]
    st+=1
    end-=1
print(res)  ''' 



'''var='ABCA'
ans=' '
for ch in var:
    ans+=chr(ord(ch)+32)
print(ans)'''


var1='hEllO wOrld'
res=' '
count=0
for ch1 in var1:
    if var1.count(ch1)>1:
        res+='_'
    else:
        res+=ch1
print(res)

str1='it is weekend'
res=' '
a=str1
res+=' '.join(a[::-1])
print(res)
        

    

