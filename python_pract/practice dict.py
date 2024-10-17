dic={'a':1,'b':3,'c':4.5}
d={}
'''for c in dic.items():
    d[c[1]]=c[0]
print(d)'''
print({value:key for key,value in dic.items()})

'''apps=['apple','google','apple','yahoo','google','amazon']
d={}
for i,ch in enumerate(apps):
    if ch not in d:
        d[ch]=[i]
    else:
        d[ch]+=[i]
print(d)'''
data='good vibes'
print(list(enumerate(data)))

f=('apple.txt','yahoo.pdf','google.txt','firefox.pdf')
d={}
for ch in f:
    res=ch.split('.')
    if res[1] not in d:
        d[res[1]]=[res[0]]
    else:
        d[res[1]]+=[res[0]]
print(d)

s='helo wecme'
d={}
for ch in s:
    if s.count(ch)>1:
        d[ch]=s.count(ch)
print(d)

s='hello welcome to python programming hii  there'
res={}
for ch in s.split():
    if ch[0] not in res:
        res[ch[0]]=[ch]
    else:
        res[ch[0]]+=[ch]
print(res)



s='gfdghj445677'
res=0
for ch in s:
    if ch.isdigit():
        res+=
print(res)















s
