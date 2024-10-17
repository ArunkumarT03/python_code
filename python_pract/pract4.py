'''st='postive'
rev=' '
#print(str1[::-1])

for ind in range(-1,-(len(st)+1),-1):
    rev+=st[ind]
print(rev)


var='strig'
rev=' '

for ch in var:
    rev=ch+rev
print(rev)'''


var='malayala'
rev=' '
for ind in range(0,len(var)//2+1):
    if var[ind]==var[-ind-1]:
        print(' palindrome')
        break
else:
    print('not palindrome')


st='malayalam'
sind=0
eind=-1
while sind!=len(st)//2:
    if st[sind]!=st[eind]:
        print('not palin')
        break
    sind+=1
    eind-=1
else:
    print('palindrome')
