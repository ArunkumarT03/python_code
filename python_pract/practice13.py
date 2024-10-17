def flatten(L):
    L1=[]
    for ele in L:
        if type(ele)==list:
            sub=flatten(ele)
            for item in sub:
                L1=L1+[item]
        else:
            L1=L1+[ele]
    return L1
L=[1,2,[3,4],5,[6,7],8]
print(tuple((flatten(L))))


a=10

def fun():
    a=20
fun()
print(a)
