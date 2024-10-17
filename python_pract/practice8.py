'''L=[1,2,3,8,4,8]
target=8
for ind in range(0,len(L)):
    if L[ind]==target:
        print(ind)
        break
else:
    print(-1)

#binary
L1=[-1,2,6,9,12,24,45]
target=6
hind=len(L1)-1
lind=0

while lind<=hind:
    midind=(lind+hind)//2
    if L1[midind]>target:
        hind=midind-1
    elif L1[midind]<target:
        lind=midind+1
    elif L1[midind]==target:
        print(midind)
        break
    else:
        print(-1)
        

#bubble sort
L=[200,89,-10,38,1]
for ind1 in range(len(L)-1,0,-1):
    for ind2 in range(ind1):
        if L[ind2]>L[ind2+1]:
            L[ind2],L[ind2+1]=L[ind2+1],L[ind2]
print(L)'''

'''#selection
L1=[23,16,18,19,-10,-1]
for ind1 in range(len(L1)-1):
    imag=ind1
    for ind2 in range(ind1+1,len(L1)):
        if L1[imag]>L1[ind2]:
             imag=ind2
    L1[ind1],L1[imag]=L1[imag],L1[ind1]
print(L1)

#Quick sort
L=[24,7,17,9,2,10]
def Quick(L):
    if len(L)<=1:
        return L
    pivot=L[0]
    left=[val for val in L[1:] if pivot>val]
    right=[val for val in L[1:] if pivot<=val]
    return Quick(left)+[pivot]+Quick(right)
print(Quick(L))'''

#merge
def conq(L,l,r):
    lind,rind,mind=0,0,0
    while lind<len(l) and rind<len(r):
        if l[lind]>r[rind]:
            L[mind]=r[rind]
            rind+=1
        else:
            L[mind]=l[lind]
            lind+=1
        mind+=1
    while lind<len(l):
        L[mind]=l[lind]
        lind+=1
        mind+=1
    while rind<len(r):
        L[mind]=r[rind]
        rind+=1
        mind+=1
def divide(L):
    if len(L)>1:
        mid=len(L)//2
        l=L[:mid]
        r=L[mid:]
        divide(l)
        divide(r)
        conq(L,l,r)
L=[200,10,-1,2,-10]
divide(L)
print(L)
