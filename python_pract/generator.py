'''L=[0,10,19,67]

print(list(val for  val in L))'''

'''def  factorial(num):
    fact=1
    for val in range(1,num+1):
        fact*=val
        yield fact
num=6
genobj=factorial(num)
print(next(genobj))
print(next(genobj))
print(next(genobj))
print(next(genobj))
print(next(genobj))
print(next(genobj))'''

def fibino(num):
    first=0
    second=1
    for val in range(num):
        yield first
        t=first+second
        first=second
        second=t
genobj=fibino(10)
print(next(genobj))
print(next(genobj))
print(next(genobj))
print(next(genobj))
print(next(genobj))

#num=5
#genobj=fibino(num)
#print(next(genobj))
#print(next(genobj))
#print(next(genobj))

#print(next(genobj))
#print(next(genobj))

'''def fibino(num,pos=2):
    first=0
    second=1
    if pos==1 or pos==2:
        print(pos-1)
    else:
        for num in range(pos-2):
            t=first+second
            first=second
            second=first
for i in range(1,11):
    if fibino(i)==i:
        print(i)'''
        
