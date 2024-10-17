'''s1='hello'
rev=' '
for ind in range(-1,-(len(s1)+1),-1):
    rev+=s1[ind]
print(rev)

var='welcome'
rev=' '

for ind in range(len(var)-1,-1,-1):
    rev+=var[ind]
print(rev)'''

#without using range
s='think'
rev=' '
for ch in s:
    rev=ch+rev
print(rev)


var='mom'
rever=' '
for ch in var:
    rever=ch+rever
print('palin' if rever==var else 'not palin')
