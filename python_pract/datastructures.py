'''#lineaar searching
L=[10,9,2,0,7,2,3,4]
target=2
for ind in range(0,len(L)):
    if L[ind]==target:
        print(f'{target}available in {ind}')
        break
        
else:
    print(-1)
#using function
def linear(L,target):
    for ind in range(0,len(L)):
        if L[ind]==target:
            return ind
    return -1
print(linear(L,target))


#binary search

L=[-10,0,2,4,5,45,100,420]
low=0
high=len(L)-1
target=100

while low<=high:
    mid=(low+high)//2
    if L[mid]>target:
        high=mid-1
    elif L[mid]<target:
        low=mid+1
    elif L[mid]==target:
        print(mid)
        break
else:
    print(-1)
        
#using function
def binary(L,low,high,target):
    while low<=high:
        mid=(low+high)//2
        if L[mid]>target:
            high=mid-1
        elif L[mid]<target:
            low=mid+1
        elif L[mid]==target:
            return mid
    return -1
print(binary(L,low=0,high=len(L)-1,target=100))'''


#interpolaition
#ind=low+(high-low)/L[high]+L[low]*(target-L(low))
L=[-100,-30,0,6,12,44,58,420]
target=44
low=0
high=len(L)-1
while low<=high and L[low]<=target<=L[high]:
    mid=int(low+((high-low)/(L[high]-L[low])*(target-L[low])))
    if L[mid]>target:
        high=mid-1
    elif L[mid]<target:
        low=mid+1
    elif L[mid]==target:
        print(mid)
        break
else:
    print(-1)

'''#bubble sort
L1=[220,100,10,24,45,67]
for ind1 in range(len(L1)-1,0,-1):
    for ind2 in range(ind1):
        if L1[ind2]>L1[ind2+1]:
            L1[ind2],L1[ind2+1]=L1[ind2+1],L1[ind2]
print(L1)

#selectuon sort
L2=[12,-3,18,7,2]
for ind1 in range(4):
    imag=ind1
    for ind2 in range(ind1+1,5):
        if L2[imag]>L2[ind2]:
            imag=ind2
    L2[ind1],L2[imag]=L2[imag],L2[ind1]
print(L2)'''
                   
'''##quick sort
L3=[420,56,26,76,-3,0,-42]
#asc
def quick(L3):
    if len(L3)<=1:
        return L3
    pivot=L3[0]
    left=[val for val in L3[1:] if pivot>val]
    right=[val for val in L3[1:] if pivot<=val]
    return quick(left)+[pivot]+quick(right)
print(quick(L3))
#dese
def quick(L3):
    if len(L3)<=1:
        return L3
    pivot=L3[0]
    left=[val for val in L3[1:] if pivot>val]
    right=[val for val in L3[1:] if pivot<=val]
    return quick(right)+[pivot]+quick(left)
print(quick(L3))

#last element as pivot
def quick(L3):
    if len(L3)<=1:
        return L3
    pivot=L3[-1]
    left=[val for val in L3[:-1] if pivot>val]
    right=[val for val in L3[:-1] if pivot<=val]
    return quick(left)+[pivot]+quick(right)
print(quick(L3))

#mid
def quick(L3):
    if len(L3)<=1:
        return L3
    pivot=L3[len(L3)//2]
    left=[val for val in L3[len(L3)//2:] if pivot>val]
    right=[val for val in L3[:len(L3)//2] if pivot<=val]
    return quick(left)+[pivot]+quick(right)
print(quick(L3))'''
