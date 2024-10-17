'''str1=input('enter:')
st_in_l=list(str1)
print(st_in_l)
print(''.join(st_in_l))

print(','.join('hello welcome to python'))

st='hello world'
print(st)
for ch in st:
    print(ord(ch))
s='hello'
print(tuple(map(lambda ch:ord(s[ch]),range(len(s)))))

st='sony12india567pvt21td'
res=0
for ch in st:
    if ch.isdigit():
        res+=int(ch)
print(res)'''

'''m='hello welcome    '
count=0
for c in m:
    if c.isalnum():
        continue
    elif c==' ':
        count+=1
print(count)

s1='HEllo W2elcome TO PYthon'
count1=0
count2=0
for c in s1:
    if c.isupper():
        count1+=1
    elif c.islower():
        count2+=1
    
print(count1,count2)

    
list1=input('enter elements:').split()
list2=input('enter elements:').split()
print(list1+list2)







l=['abc','123','hello','23']
l1=[]
for ch in l:
    if ch.isdigit():
        l1+=ch
print(l1)'''




#check all condition
s='wE wiLL learn ALL skills 100%'
vowels=0
consonants=0
uppercase=0
lowercase=0
digits=0
special=0
for ch in s:
    if ('A'<=ch<='Z')or('a'<=ch<='z'):
        if ch in 'aeiouAEIOU':
            vowels+=1
        else:
            consonants+=1
    if('A'<=ch<='Z'):
        uppercase+=1
    elif('a'<=ch<='z'):
        lowercase+=1
    elif('0'<=ch<='9'):
        digits+=1
    else:
        special+=1
print(vowels,consonants,uppercase,lowercase,digits,special)

var='today we have a class'
res=' '
for ch in var.split():
    res+=ch[::-1]+' '
print(res)

print(' '.join(var.split()[::-1]))

s='everyone must attend js'
res=' '
print(s[:len(s)//2:1])
print(s[len(s)//2::1])

for ch in range(len(s)):
    if ch%2==0:
        res+=s[ch]
print(res)

s1='hello'
word=s[sv:ev]
for sv in range(len(s1)):
    for ev in range(sv,len(s1)+1):
        print(s1[sv:ev])


for sv in range(len(s1)):
    for ev in range(sv,len(s1)+1):
        if word==word[::-1]:
            print(word)
    
