'''dic={'a':1,'b':3,'c':45}
d={}
print({key:key*key for key in range(1,6)})'''

'''a=3
b=7
if a>b:
    lcm=a
else:
    lcm=b
while lcm!=0:
    if lcm%a==0 and lcm%b==0:
        print(lcm)
        break
    else:
        lcm+=1

a=6
b=9
if a<b:
    gcd=a
else:
    gcd=b
while gcd!=0:
    if a%gcd==0 and b%gcd==0:
        print(gcd)
        break
    else:
        gcd-=1'''
'''S='engineering'
res=' '
for ch in S:
    if ch not in  res:
        res+=ch
print(res)

st='string'
rev=' '
for ch in st:
    rev=ch+rev
print(rev)

var='think'
res=''
for ch in range(-1,-(len(var)+1),-1):
    res+=var[ch]
print(res)'''

L=[2,3,4,5,6,7]
res=[]
for ch in range(len(L)):
    if L[ch]%2==0:
        res.append(L[ch+1])
print(res)

L1=['h1','hello','python','bye']
rev=[]
for ch in L1:
    t=""
    for c in ch:
        t=c+t
    rev.append(t)
print(rev)

L=['apple','google','apple','yahoo','amazon','google']
ans=[]
for i in L:
    if L.count(i)>1:
        ans.append(i)
print(ans)

S='today is holiday'
rev=''
for ch in S.split():
    t=' '
    for c in ch:
       t=c+t
    rev+=t
print(rev)

N='123456785'
count=0
for ch in N:
    if '0'<=ch<='9':
        count+=1
print(count)

num=122345677
count=0
while num!=0:
    rem=num%10
    count+=rem
    num//=10
print(count)




