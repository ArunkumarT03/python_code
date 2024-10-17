L=[(1,2),(1,3),(2,2),(2,4)]
L1=[]
'''for num in L:
   for ind in 
    if num[0]<num[1]:
        L1+=num
    else:
        L1+=1
print(L1)

a=sorted(L,key=lambda x:x[1])
print(a)'''

S='aaabbcccc'
count=1
S=S+' '
res=' '
for ind in range(len(S)-1):
    if S[ind]==S[ind+1]:
        count+=1
    else:
        res+=str(count)+S[ind]
        count=1
print(res)
