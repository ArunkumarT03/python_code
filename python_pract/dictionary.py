'''sentence='hello  world welcome to python programming hi there'
res={}
for ch in sentence.split():
    if ch[0] not in res:
        res[ch[0]]=[ch]
    else:
        res[ch[0]]+=[ch]

print(res)

dic={'a':'hello','b':100,'c':10.9,'d':'world'}
d={}
for c in dic.items():
    if type(c[1])==str:
        d[c[0]]=c[1][::-1]
    else:
        d[c[0]]=c[1]
print(d)

#with method     
s1='hello welcome'
d1={}
for ch in s1:
    d1[ch]=s1.count(ch)
print(d1)
#with out method
s2='hello welcome'
d2={}
for ch2 in s2:
    if ch2 not in d2:
        d2[ch2]=1
    else:
        d2[ch2]+=1
print(d2)


numbers=(1,2,3,4,5,6,7,8,9,10)
d3={}
odd_n=1
even_n=0
for cha in numbers:
    if cha%2==0:
        if even_n  not in d3:
            d3[0]=[cha]
        else:
            d3[0]+=[cha]
    else:
        if odd_n not in d3:
            d3[1]=[cha]
        else:
            d3[1]+=[cha]
print(d3)'''


items=['lotus-flower','lilly-flower','cat-animal','sunflower-flower','dog-animal']

group_item={'flowers':[],'animals':[]}
for ch in items:
    if ch.endswith('-flower'):
        group_item['flowers'].append(ch)
    elif ch.endswith('-animal'):
        group_item['animals'].append(ch)
print(group_item)      

s1='hello welcome'
d4={}
count=0
for ch in s1:
    if s1.count(ch)>1:
        d4[ch]=s1.count(ch)
print(d4)


'''items=['lotus-flower','lilly-flower','cat-animal','sunflower-flower','dog-animal']
d={}
for ch in items:
    res='''

files=('apple.txt','yahoo.pdf','gmail.pdf','amazon.pdf','google.txt','facebook.pdf','flipkart.txt')
d5={}
for ch in files:
    res=ch.split('.')

    if res[1] not in d5:
        d5[res[1]]=[res[0]]
    else:
        d5[res[1]]+=[res[0]]
print(d5)





'''apps=['apple','google','apple','yahoo','google','yahoo','gmail','amazon','apple']
d6={}

for i,ch in enumerate(apps):
    if ch not in d6:
        d6[ch]=[i]
    else:
        d6[ch]+=[i]
print(d6)'''


dic_={'a':1,'b':3,'c':4.5,'d':False}
d7={}

for c in dic_.items():
    d7[c[1]]=c[0]
print(d7)
