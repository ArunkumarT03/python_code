'''num=int(input('enter a number:'))
for val in range(2,num//2+1):
    if num%val==0:
        print('not prime')
        break
else:
    print('prime')'''


'''num=int(input('enter a number:'))
fact=1
for val in range(1,num+1):
    fact*=val
print(fact)'''

'''num=1234
ans=0
while num!=0:
    rem=num%10
    ans+=rem
    num//=10
print(ans)'''

'''num=20
while num>9:
    ans=0
    while num!=0:
        rem=num%10
        ans+=rem**2
        num//=10
    num=ans
if(num==1 or num==7):
    print('is happy number')
else:
    print('is not happy number')'''

'''def rec(num):
    if num==0:
        return
    print(num)
    rec(num-1)
num=-10
rec(num)'''


'''L=[4,8,9,0,7,3,9,0]
target=4
for ind in range(0,len(L)-1):
    if L[ind]==target:
        print(f'{target} available in {ind}')
        break
else:
    print(-1)'''

'''#binary search
L=[2,5,7,12,14]
lind=0
hind=len(L)-1
target=7
while lind<=hind:
    mid=(lind+hind)//2
    if L[mid]<target:
        lind=mid+1
    elif L[mid]>target:
        hind=mid-1
    elif L[mid]==target:
        print(mid)
        break
else:
    print(-1)'''

'''#interpolaition
L=[2,3,6,7,9,10]
target=6
low=0
high=len(l)-1
while low<=high and L[low]<=target<=L[high]:
    mid=int(low+((high-low)/L[low]-L[low]-L[high]))*(target-L[low])
    if L[mid]<target:
        lind=mid+1
    elif L[mid]>target:
        hind=mid-1
    elif L[mid]==target:
        print(mid)
        break
else:
    print(-1)'''

'''#bubble sort
L=[10,-2,10,1,8,-10]
for ind1 in range(len(L)-1,0,-1):
    for ind2 in range(ind1):
        if L[ind2]>L[ind2+1]:
            L[ind2],L[ind2+1]=L[ind2+1],L[ind2]
print(L)'''

'''#selection sort
L1=[20,-10,2,3,-25,7]
for ind1 in range(4):
    imag=ind1
    for ind2 in range(ind1+1,5):
        if L1[imag]>L1[ind2]:
            imag=ind2
    L1[ind1],L1[imag]=L1[imag],L1[ind1]
print(L1)'''

#quick sort
'''L=[2,4,0,-2,10]
def quick(L):
    if len(L)<=1:
        return L
    pivot=L[0]
    left=[val for val in L[1:] if pivot>val]
    right=[val for val in L[1:] if pivot<=val]
    return quick(left)+[pivot]+quick(right)
print(quick(L))'''

#merge sort
def conq(L,left,right):
    lind,rind,mind=0,0,0
    while lind<len(left) and rind<len(right):
        if left[lind]>right[rind]:
            L[mind]=right[rind]
            rind+=1
            mind+=1
        else:
            L[mind]=left[lind]
            lind+=1
            mind+=1
    while lind<len(left):
        L[mind]=left[lind]
        mind+=1
        lind+=1
    while rind<len(right):
        L[mind]=right[rind]
        mind+=1
        rind+=1
def  divide(L):
    if len(L)>1:
        mid=len(L)//2
        left=L[:mid]
        right=L[mid:]
        divide(left)
        divide(right)
        conq(L,left,right)
L=[12,9,3,-10,-3,1]
divide(L)
print(L)


n1=2
n2=100
for num in range(n1,n2+1):
    if num>1:
        for i in range(2,num):
            if num%i==0:
                print(num)
            else:
                print(num)
    

