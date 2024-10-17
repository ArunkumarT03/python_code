'''def check_pal(s, low, high):
    while low < high:
        if s[low] != s[high]:
            return False
        low += 1
        high -= 1
    return True
def longest_pal_substr(s):
    n = len(s)
    max_len = 1
    start = 0
    for i in range(n):
        for j in range(i, n):
            if check_pal(s, i, j) and (j - i + 1) > max_len:
                start = i
                max_len = j - i + 1
    return s[start:start + max_len]
s = input('enter a str:')
print(longest_pal_substr(s))'''




def pal(s,low,high):
    while low<high:
        if s[low]!=s[high]:
            return False
        low+=1
        high-=1
    return True
def longest_pal(s):
    n=len(s)
    max_len=1
    start=0
    for i in range(n):
        for j in range(i,n):
            if pal(s,i,j)and (j-i+1)>max_len:
                start=i
                max_len=j-i+1
    return s[start:start+max_len]
s=['aaaa','bgshaj','ahjsk']
print(longest_pal(s))







'''num=5
for r in range(1,num+1):
    for c in range(1,num+1):
        if r==1 or c==1:
            print('*',end=' ')
    print()




num=5
space=num-1
for r in range(1,num*2,2):
    for sp in range(space):
        print(' ',end=' ')
    for c in range(1,r+1):
        if r==1 or r==num*2-1:
            print('*',end=' ')
        else:
            if c==1 or c==r:
                print('*',end=' ')
            else:
                print(' ',end=' ')
    print()
    space-=1'''
   
