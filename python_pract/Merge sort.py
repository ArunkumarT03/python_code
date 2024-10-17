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
L=[560,-20,-45,3,7,10]
divide(L)
print(L)
