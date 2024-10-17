'''#linear
L=[10,30,-3,9,420,12]
target=420
for ind in range(0,len(L)):
    if L[ind]==target:
        print(f'{target}available in{ind}')
        break
else:
    print(-1)'''

'''#binary
L1=[-30,-10,11,23,78,97]
low=0
high=len(L1)-1
target=11
while low<=high:
    mid=(low+high)//2
    if L1[mid]>target:
        high=mid-1
    elif L1[mid]<target:
        low=mid+1
    elif L1[mid]==target:
        print(mid)
        break
else:
    print(-1)'''

#inter
L1=[0,10,11,23,78,97]
low=0
high=len(L1)-1
target=11

while low<=high and L1[low]<=target<=L1[high]:
    mid=int(low+((high-low)/(L1[high]-L1[low])*(target-L1[low])))
    if L1[mid]>target:
        high=mid-1
    elif L1[mid]<target:
        low=mid+1
    elif L1[mid]==target:
        print(mid)
else:
    print(-1)

